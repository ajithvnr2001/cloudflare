---
url: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/
title: Credentials \u00b7 Cloudflare Images docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:37.734881+00:00
---

# Credentials · Cloudflare Images docs

> Source: https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Images](https://developers.cloudflare.com/images/)
  3. /…

StorageUpload images

  4. /[Import from S3](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/)
  5. /Credentials



# Credentials

Last updated Sep 10, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/credentials/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

To import images, Cloudflare Images requires access to your Amazon S3 bucket. You can use credentials for any AWS Identity and Access Management (IAM) user with the correct permissions.

Cloudflare recommends creating a user with narrowly scoped permissions.

To create the required permissions:

  1. Log in to your AWS IAM account.

  2. Create a policy with the following format (replace `<BUCKET_NAME>` with the bucket you want to grant access to):
         
         {
         	"Version": "2012-10-17",
         	"Statement": [
         		{
         			"Effect": "Allow",
         			"Action": ["s3:Get*", "s3:List*"],
         			"Resource": [
         				"arn:aws:s3:::<BUCKET_NAME>",
         				"arn:aws:s3:::<BUCKET_NAME>/*"
         			]
         		}
         	]
         }

  3. Next, create a new user and attach the created policy to that user.




You can now use both the Access Key ID and Secret Access Key to create a new source. Refer to [Import images from S3](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/enable/) for setup instructions.

[PreviousEdit sources](https://developers.cloudflare.com/images/storage/upload-images/import-from-s3/edit/)[NextUpload via a Worker](https://developers.cloudflare.com/images/storage/upload-images/upload-file-worker/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/images/storage/upload-images/import-from-s3/credentials.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
