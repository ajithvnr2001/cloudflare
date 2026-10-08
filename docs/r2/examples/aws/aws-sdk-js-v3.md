---
url: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-js-v3/
title: aws-sdk-js-v3 \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:45.269240+00:00
---

# aws-sdk-js-v3 · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-js-v3/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /…

[Examples](https://developers.cloudflare.com/r2/examples/)

  4. /S3 SDKs
  5. /aws-sdk-js-v3



# aws-sdk-js-v3

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-js-v3/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGenerate presigned URLsRestrict uploads with CORS and Content-Type

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.

  


JavaScript or TypeScript users may continue to use the [`@aws-sdk/client-s3` ↗︎](https://www.npmjs.com/package/@aws-sdk/client-s3) npm package as per normal. You must pass in the R2 configuration credentials when instantiating your `S3` service client.

Note

Currently, you cannot use AWS S3-compatible API while developing locally via `wrangler dev`.
    
    
    import {
    	S3Client,
    	ListBucketsCommand,
    	ListObjectsV2Command,
    	GetObjectCommand,
    	PutObjectCommand,
    } from "@aws-sdk/client-s3";
    
    const S3 = new S3Client({
    	region: "auto", // Required by SDK but not used by R2
    	// Provide your Cloudflare account ID
    	endpoint: `https://${ACCOUNT_ID}.r2.cloudflarestorage.com`,
    	// Retrieve your S3 API credentials for your R2 bucket via API tokens (see: https://developers.cloudflare.com/r2/api/tokens)
    	credentials: {
    		accessKeyId: ACCESS_KEY_ID,
    		secretAccessKey: SECRET_ACCESS_KEY,
    	},
    });
    
    console.log(await S3.send(new ListBucketsCommand({})));
    // {
    //     '$metadata': {
    //     httpStatusCode: 200,
    //         requestId: undefined,
    //         extendedRequestId: undefined,
    //         cfId: undefined,
    //         attempts: 1,
    //         totalRetryDelay: 0
    // },
    //     Buckets: [
    //     { Name: 'user-uploads', CreationDate: 2022-04-13T21:23:47.102Z },
    //     { Name: 'my-bucket', CreationDate: 2022-05-07T02:46:49.218Z }
    //     ],
    //     Owner: {
    //         DisplayName: '...',
    //         ID: '...'
    //     }
    // }
    
    console.log(
    	await S3.send(new ListObjectsV2Command({ Bucket: "my-bucket" })),
    );
    // {
    //     '$metadata': {
    //       httpStatusCode: 200,
    //       requestId: undefined,
    //       extendedRequestId: undefined,
    //       cfId: undefined,
    //       attempts: 1,
    //       totalRetryDelay: 0
    //     },
    //     CommonPrefixes: undefined,
    //     Contents: [
    //       {
    //         Key: 'cat.png',
    //         LastModified: 2022-05-07T02:50:45.616Z,
    //         ETag: '"c4da329b38467509049e615c11b0c48a"',
    //         ChecksumAlgorithm: undefined,
    //         Size: 751832,
    //         StorageClass: 'STANDARD',
    //         Owner: undefined
    //       },
    //       {
    //         Key: 'todos.txt',
    //         LastModified: 2022-05-07T21:37:17.150Z,
    //         ETag: '"29d911f495d1ba7cb3a4d7d15e63236a"',
    //         ChecksumAlgorithm: undefined,
    //         Size: 279,
    //         StorageClass: 'STANDARD',
    //         Owner: undefined
    //       }
    //     ],
    //     ContinuationToken: undefined,
    //     Delimiter: undefined,
    //     EncodingType: undefined,
    //     IsTruncated: false,
    //     KeyCount: 8,
    //     MaxKeys: 1000,
    //     Name: 'my-bucket',
    //     NextContinuationToken: undefined,
    //     Prefix: undefined,
    //     StartAfter: undefined
    //   }

## Generate presigned URLs

You can also generate presigned links that can be used to share public read or write access to a bucket temporarily.
    
    
    import { getSignedUrl } from "@aws-sdk/s3-request-presigner";
    
    // Use the expiresIn property to determine how long the presigned link is valid.
    console.log(
    	await getSignedUrl(
    		S3,
    		new GetObjectCommand({ Bucket: "my-bucket", Key: "dog.png" }),
    		{ expiresIn: 3600 },
    	),
    );
    // You can also create links for operations such as PutObject to allow temporary write access to a specific key.
    // Specify ContentType to restrict uploads to a specific file type.
    console.log(
    	await getSignedUrl(
    		S3,
    		new PutObjectCommand({
    			Bucket: "my-bucket",
    			Key: "dog.png",
    			ContentType: "image/png",
    		}),
    		{ expiresIn: 3600 },
    	),
    );
    
    
    https://my-bucket.<ACCOUNT_ID>.r2.cloudflarestorage.com/dog.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=<credential>&X-Amz-Date=<timestamp>&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=<signature>&x-id=GetObject
    https://my-bucket.<ACCOUNT_ID>.r2.cloudflarestorage.com/dog.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=<credential>&X-Amz-Date=<timestamp>&X-Amz-Expires=3600&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Signature=<signature>&x-id=PutObject

You can use the link generated by the `PutObject` example to upload to the specified bucket and key, until the presigned link expires. When using a presigned URL with `ContentType`, the client must include a matching `Content-Type` header in the request.
    
    
    curl -X PUT "https://my-bucket.<ACCOUNT_ID>.r2.cloudflarestorage.com/dog.png?X-Amz-Algorithm=..." \
      -H "Content-Type: image/png" \
      --data-binary @dog.png

## Restrict uploads with CORS and Content-Type

When generating presigned URLs for uploads, you can limit abuse and misuse by:

  1. **Restricting Content-Type** : Specify the allowed content type in the `PutObjectCommand`. The upload will fail if the client sends a different `Content-Type` header.

  2. **Configuring CORS** : Set up [CORS rules](https://developers.cloudflare.com/r2/buckets/cors/#add-cors-policies-from-the-dashboard) on your bucket to control which origins can upload files. Configure CORS via the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/r2/overview) by adding a JSON policy to your bucket settings:



    
    
    [
      {
        "AllowedOrigins": ["https://example.com"],
        "AllowedMethods": ["PUT"],
        "AllowedHeaders": ["Content-Type"],
        "ExposeHeaders": ["ETag"],
        "MaxAgeSeconds": 3600
      }
    ]

Then generate a presigned URL with a Content-Type restriction:
    
    
    const putUrl = await getSignedUrl(
    	S3,
    	new PutObjectCommand({
    		Bucket: "my-bucket",
    		Key: "dog.png",
    		ContentType: "image/png",
    	}),
    	{ expiresIn: 3600 },
    );

When a client uses this presigned URL, they must:

  * Make the request from an allowed origin (enforced by CORS)
  * Include the `Content-Type: image/png` header (enforced by the signature)



[Previousaws-sdk-js](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-js/)[Nextaws-sdk-kotlin](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-kotlin/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/aws/aws-sdk-js-v3.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
