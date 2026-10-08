---
url: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/
title: AWS integration \u00b7 Cloudflare SSL/TLS docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:43.164404+00:00
---

# AWS integration · Cloudflare SSL/TLS docs

> Source: https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/

  1. [Home](https://developers.cloudflare.com/)
  2. /[SSL/TLS](https://developers.cloudflare.com/ssl/)
  3. /…

Origin server

  4. /[Authenticated Origin Pulls (mTLS)](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/)
  5. /AWS integration



# AWS integration

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBefore you begin1\. Generate a custom certificate2\. Configure AWS Application Load Balancer3\. Configure CloudflareRoll back the Cloudflare configuration

This guide will walk you through how to set up [per-hostname](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/) authenticated origin pulls to securely connect to an AWS Application Load Balancer using [mutual TLS verify ↗︎](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html).

## Before you begin

  * You should already have your AWS account and [EC2 ↗︎](https://docs.aws.amazon.com/ec2/?icmpid=docs_homepage_featuredsvcs) configured.
  * Note that this tutorial uses command-line interface (CLI) to generate a custom certificate, and [API calls](https://developers.cloudflare.com/fundamentals/api/get-started/) to configure Cloudflare Authenticated Origin Pulls.
  * For the most up-to-date documentation on how to set up AWS, refer to the [AWS documentation ↗︎](https://docs.aws.amazon.com/).



## 1\. Generate a custom certificate

  1. Run the following command to generate a 4096-bit RSA private key, using AES-256 encryption. Enter a passphrase when prompted.


    
    
    openssl genrsa -aes256 -out rootca.key 4096

  2. Create the CA root certificate. When prompted, fill in the information to be included in the certificate. For the `Common Name` field, use the domain name as value, not the hostname.


    
    
    openssl req -x509 -new -nodes -key rootca.key -sha256 -days 1826 -out rootca.crt

  3. Create a Certificate Signing Request (CSR). When prompted, fill in the information to be included in the request. For the `Common Name` field, use the hostname as value.


    
    
    openssl req -new -nodes -out cert.csr -newkey rsa:4096 -keyout cert.key

  4. Sign the certificate using the `rootca.key` and `rootca.crt` created in previous steps.


    
    
    openssl x509 -req -in cert.csr -CA rootca.crt -CAkey rootca.key -CAcreateserial -out cert.crt -days 730 -sha256 -extfile ./cert.v3.ext

  5. Make sure the certificate extensions file `cert.v3.ext` specifies the following:


    
    
    basicConstraints=CA:FALSE

## 2\. Configure AWS Application Load Balancer

  1. Upload the `rootca.cert` to an [S3 bucket ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html).
  2. [Create a trust store ↗︎](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html#create-trust-store) at your EC2 console, indicating the **S3 URI** where you uploaded the certificate.
  3. Create an EC2 instance and install an HTTPD daemon. Choose an [instance type ↗︎](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) according to your needs - it can be a minimal instance eligible to [AWS Free Tier ↗︎](https://aws.amazon.com/free/). This tutorial was based on an example using t2.micro and [Amazon Linux 2023 ↗︎](https://docs.aws.amazon.com/linux/al2023/ug/what-is-amazon-linux.html).


    
    
    sudo yum install -y httpd
    sudo systemctl start httpd

  4. Create a [target group ↗︎](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html#configure-target-group) for your Application Load Balancer. 
     * Choose **Instances** as target type.
     * Specify port `HTTP/80`.
  5. After you finish configuring the target group, confirm that the target group is [healthy ↗︎](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html).
  6. [Configure a load balancer and a listener ↗︎](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html#configure-load-balancer). 
     * Choose the **Internet-facing** scheme.
     * Switch the listener to port `443` so that the **mTLS** option is available, and select the target group created in previous steps.
     * For **Default SSL/TLS server certificate** , choose **Import certificate** > **Import to ACM** , and add the certificate private key and body.
     * Under **Client certificate handling** , select **Verify with trust store**.
  7. Save your settings.
  8. (Optional) Run the following commands to confirm that the Application Load Balancing is asking for the client certificate.


    
    
    openssl s_client -verify 5 -connect <your-application-load-balancer>:443 -quiet -state

Since you have not yet uploaded the certificate to Cloudflare, the connection should fail (`read:errno=54`, for example).

You can also run `curl --verbose` and confirm `Request CERT (13)` is present within the SSL/TLS handshake:
    
    
    curl --verbose https://<your-application-load-balancer>
    ...
    * TLSv1.2 (IN), TLS handshake, Request CERT (13):
    ...

## 3\. Configure Cloudflare

  1. [Upload the certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/create/) you created in Step 1 to Cloudflare. You should use the leaf certificate, not the root CA.


    
    
    MYCERT="$(cat cert.crt|perl -pe 's/\r?\n/\\n/'|sed -e 's/..$//')"
    MYKEY="$(cat cert.key|perl -pe 's/\r?\n/\\n/'|sed -e's/..$//')"
    
    request_body=$(< <(cat <<EOF
    {
    "certificate": "$MYCERT",
    "private_key": "$MYKEY",
    "bundle_method":"ubiquitous"
    }
    EOF
    ))
    
    # Push the certificate
    
    curl --silent \
    "https://api.cloudflare.com/client/v4/zones/$ZONEID/origin_tls_client_auth/hostnames/certificates" \
    --header "Content-Type: application/json" \
    --header "X-Auth-Email: $MYAUTHEMAIL" \
    --header "X-Auth-Key: $MYAUTHKEY" \
    --data "$request_body"

  2. [Associate the certificate with the hostname](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/) that should use it.



Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

  * `SSL and Certificates Write`

Enable or Disable a Hostname for Client Authenticationbash
    
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"config": [
    				{
    						"enabled": true,
    						"cert_id": "<CERT_ID>",
    						"hostname": "<YOUR_HOSTNAME>"
    				}
    		]
    	}'

Note

Make sure your [encryption mode](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/) is set to **Full** or higher. If you only want to adjust this setting for a specific hostname, use [Configuration Rules](https://developers.cloudflare.com/rules/configuration-rules/settings/#ssl).

* * *

## Roll back the Cloudflare configuration

  1. Use a [`PUT` request](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/) to disable Authenticated Origin Pulls on the hostname.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `SSL and Certificates Write`
Enable or Disable a Hostname for Client Authenticationbash
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames" \
    	--request PUT \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"config": [
    				{
    						"enabled": false,
    						"cert_id": "<CERT_ID>",
    						"hostname": "<YOUR_HOSTNAME>"
    				}
    		]
    	}'

  2. (Optional) Use a [`GET` request](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/) to obtain a list of the client certificate IDs. You will need the ID of the certificate you want to remove for the following step.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `SSL and Certificates Write`
     * `SSL and Certificates Read`
List Certificatesbash
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames/certificates" \
    	--request GET \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

  3. Use the [Delete hostname client certificate](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/) endpoint to remove the certificate you had uploaded.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:
     * `SSL and Certificates Write`
Delete Hostname Client Certificatebash
    
    curl "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/origin_tls_client_auth/hostnames/certificates/$CERTIFICATE_ID" \
    	--request DELETE \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"




[PreviousAbout](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/explanation/)[NextGlobal](https://developers.cloudflare.com/ssl/origin-configuration/authenticated-origin-pull/set-up/global/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ssl/origin-configuration/authenticated-origin-pull/aws-alb-integration.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
