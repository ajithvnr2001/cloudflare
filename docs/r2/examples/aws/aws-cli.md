---
url: https://developers.cloudflare.com/r2/examples/aws/aws-cli/
title: aws CLI \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:45.349380+00:00
---

# aws CLI · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/aws/aws-cli/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /…

[Examples](https://developers.cloudflare.com/r2/examples/)

  4. /S3 SDKs
  5. /aws CLI



# aws CLI

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/aws/aws-cli/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGenerate presigned URLs

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.

  


With the [`aws` ↗︎](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) CLI installed, you may run [`aws configure` ↗︎](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) to configure a new profile. You will be prompted with a series of questions for the new profile's details.
    
    
    aws configure
    
    
    AWS Access Key ID [None]: <ACCESS_KEY_ID>
    AWS Secret Access Key [None]: <SECRET_ACCESS_KEY>
    Default region name [None]: auto
    Default output format [None]: json

The `region` value can be set to `auto` since it is required by the SDK but not used by R2.

You may then use the `aws` CLI for any of your normal workflows.
    
    
    # Provide your Cloudflare account ID
    aws s3api list-buckets --endpoint-url https://<ACCOUNT_ID>.r2.cloudflarestorage.com
    # {
    #     "Buckets": [
    #         {
    #             "Name": "my-bucket",
    #             "CreationDate": "2022-05-18T17:19:59.645000+00:00"
    #         }
    #     ],
    #     "Owner": {
    #         "DisplayName": "134a5a2c0ba47b38eada4b9c8ead10b6",
    #         "ID": "134a5a2c0ba47b38eada4b9c8ead10b6"
    #     }
    # }
    
    aws s3api list-objects-v2 --endpoint-url https://<ACCOUNT_ID>.r2.cloudflarestorage.com --bucket my-bucket
    # {
    #     "Contents": [
    #         {
    #             "Key": "ferriswasm.png",
    #             "LastModified": "2022-05-18T17:20:21.670000+00:00",
    #             "ETag": "\"eb2b891dc67b81755d2b726d9110af16\"",
    #             "Size": 87671,
    #             "StorageClass": "STANDARD"
    #         }
    #     ]
    # }

## Generate presigned URLs

You can also generate presigned links which allow you to share public access to a file temporarily.
    
    
    # You can pass the --expires-in flag to determine how long the presigned link is valid.
    aws s3 presign --endpoint-url https://<ACCOUNT_ID>.r2.cloudflarestorage.com  s3://my-bucket/ferriswasm.png --expires-in 3600
    # https://<ACCOUNT_ID>.r2.cloudflarestorage.com/my-bucket/ferriswasm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=<credential>&X-Amz-Date=<timestamp>&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=<signature>

[PreviousRclone](https://developers.cloudflare.com/r2/examples/rclone/)[Nextaws-sdk-go](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-go/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/aws/aws-cli.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
