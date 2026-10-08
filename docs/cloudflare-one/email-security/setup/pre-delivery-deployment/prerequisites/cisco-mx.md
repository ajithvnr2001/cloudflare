---
url: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-mx/
title: Cisco - Cisco as MX Record \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:42.817487+00:00
---

# Cisco - Cisco as MX Record · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-mx/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)[Setup](https://developers.cloudflare.com/cloudflare-one/email-security/setup/)Pre-delivery deployment

  4. /Prerequisites
  5. /Cisco - Cisco as MX Record



# Cisco - Cisco as MX Record

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-mx/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Overview1\. Add a Sender Group for Email security Email Protection IPs2\. Add SMTP route for the Email security Email Protection Hosts3\. Create Incoming Content Filters Incoming Content Filter - To Email security Incoming Content Filter - From Email security4\. Add the Incoming Content Filter to the Inbound Policy table5\. Geographic locations6\. Set up MX/Inline

![A schematic showing where Email security is in the life cycle of an email received](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1116,height=476,format=webp/_astro/Cisco_to_Cisco_MX_Inline.T2fNxiw3.png)

In this tutorial, you will learn how to configure Email security with Cisco as MX record.

## 1\. Add a Sender Group for Email security Email Protection IPs

To add a new Sender Group:

  1. Go to **Mail Policies** > **HAT Overview**.

  2. Select the **Add Sender Group** button.

  3. Configure the new Sender Group as follows:

     * **Name** : `Email security`.
     * **Order** : Order above the existing **WHITELIST** sender group.
     * **Comment** : `Email security Email Protection egress IP Addresses`.
     * **Policy** : `TRUSTED` (by default, spam detection is disabled for this mail flow policy).
     * **SBRS** : Leave blank.
     * **DNS Lists** : Leave blank.
     * **Connecting Host DNS Verification** : Leave all options unchecked.
  4. Select **Submit and Add Senders** , and add the IP addresses mentioned in [Egress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/). If you need to process emails in the EU or India regions for compliance purposes, add those IP addresses as well.




## 2\. Add SMTP route for the Email security Email Protection Hosts

To add a new SMTP Route:

  1. Go to **Network** > **SMTP Routes**.

  2. Select **Add Route**.

  3. Configure the new SMTP Route as follows:

     * **Receiving Domain** : `a1s.mailstream`
     * In **Destination Hosts** , select **Add Row** , and add the Email security MX hosts. Refer to the Geographic locations table for more information on which MX hosts to use.



## 3\. Create Incoming Content Filters

To manage the mail flow between Email security and Cisco ESA, you need two filters:

  * One to direct all incoming messages to Email security.
  * One to recognize messages coming back from Email security to route for normal delivery.



### Incoming Content Filter - To Email security

To create a new Content Filter:

  1. Go to **Mail Policies** > **Incoming Content Filters**.

  2. Select **Add Filter** to create a new filter.

  3. Configure the new Incoming Content Filter as follows:

     * **Name** : `ESA_to_A1S`
     * **Description** : `Redirect messages to Email security for anti-phishing inspection`
     * **Order** : This will depend on your other filters.
     * **Condition** : No conditions.
     * **Actions** : 
       * For **Action** select **Send to Alternate Destination Host**.
       * For **Mail Host** input `a1s.mailstream` (the SMTP route configured in step 2).



### Incoming Content Filter - From Email security

To create a new Content Filter:

  1. Go to **Mail Policies** > **Incoming Content Filters**.

  2. Select the **Add Filter** button to create a new filter.

  3. Configure the new Incoming Content Filter as follows:

     * **Name** : `A1S_to_ESA`
     * **Description** : `Email security inspected messages for final delivery`
     * **Order** : This filter must come before the previously created filter.
     * **Conditions** : Add conditions of type **Remote IP/Hostname** with all the IP addresses mentioned in [Egress IPs](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/). For example:

Order | Condition | Rule  
---|---|---  
`1` | `Remote IP/Hostname` | `Remote IP/Hostname`  
`2` | `Remote IP/Hostname` | `52.89.255.11`  
`3` | `Remote IP/Hostname` | `52.0.67.109`  
`4` | `Remote IP/Hostname` | `54.173.50.115`  
`5` | `Remote IP/Hostname` | `104.30.32.0/19`  
`6` | `Remote IP/Hostname` | `158.51.64.0/26`  
`7` | `Remote IP/Hostname` | `158.51.65.0/26`  
  
     * Ensure that the _Apply rule:_ dropdown is set to **If one or more conditions match**.
     * **Actions** : Select **Add Action** , and add the following: 

Order | Action | Rule  
---|---|---  
\--1 | `Skip Remaining Content Filters (Final Action)` | `skip-filters()`  
  



## 4\. Add the Incoming Content Filter to the Inbound Policy table

Assign the Incoming Content Filters created in step 3 to your primary mail policy in the Incoming Mail Policy table. Then, commit your changes to activate the email redirection.

## 5\. Geographic locations

When configuring the Email security MX records, it is important to configure hosts with the correct MX priority. This will allow mail flows to the preferred hosts and fail over as needed.

Choose from the following Email security MX hosts, and order them by priority. For example, if you are located outside the US and want to prioritize email processing in the EU, add `mailstream-eu1.mxrecord.io` as your first host, and then the US servers.

Host | Location | Note  
---|---|---  
* `mailstream-central.mxrecord.mx`
* `mailstream-east.mxrecord.io`
* `mailstream-west.mxrecord.io`
| US | Best option to ensure all email traffic processing happens in the US.  
`mailstream-eu1.mxrecord.io` | EU | Best option to ensure all email traffic processing happens in Germany, with backup to US data centers.  
`mailstream-bom.mxrecord.mx` | India | Best option to ensure all email traffic processing happens within India.  
`mailstream-india-primary.mxrecord.mx` | India | Same as `mailstream-bom.mxrecord.mx`, with backup to US data centers.  
`mailstream-asia.mxrecord.mx` | India | Best option to ensure all email traffic processing happens in India, with Australia data centers as backup.  
`mailstream-syd.area1.cloudflare.net` | Australia / New Zealand | Best option to ensure all email traffic processing happens within Australia.  
`mailstream-australia-primary.area1.cloudflare.net` | Australia / New Zealand | Best option to ensure all email traffic processing happens in Australia, with India and US data centers as backup.  
  
## 6\. Set up MX/Inline

Now that you have completed the prerequisite steps, set up MX/Inline on the Cloudflare dashboard. Refer to [Set up MX/Inline deployment](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/) for the next steps.

[PreviousCisco - Email security as MX Record](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/)[NextMX/Inline deployment](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-mx.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
