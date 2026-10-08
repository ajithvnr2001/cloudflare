---
url: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-kotlin/
title: aws-sdk-kotlin \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:45.848896+00:00
---

# aws-sdk-kotlin · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-kotlin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /…

[Examples](https://developers.cloudflare.com/r2/examples/)

  4. /S3 SDKs
  5. /aws-sdk-kotlin



# aws-sdk-kotlin

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-kotlin/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic UsageGenerate presigned URLs

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.

  


This example uses the [aws-sdk-kotlin ↗︎](https://github.com/aws/aws-sdk-kotlin). You must pass in the R2 configuration credentials when instantiating your `S3` client:

## Basic Usage
    
    
    import aws.sdk.kotlin.runtime.auth.credentials.StaticCredentialsProvider
    import aws.sdk.kotlin.services.s3.S3Client
    import aws.sdk.kotlin.services.s3.listObjects
    import aws.sdk.kotlin.services.s3.model.GetObjectRequest
    import aws.sdk.kotlin.services.s3.model.PutObjectRequest
    import aws.sdk.kotlin.services.s3.presigners.presignGetObject
    import aws.sdk.kotlin.services.s3.presigners.presignPutObject
    import aws.smithy.kotlin.runtime.auth.awscredentials.Credentials
    import aws.smithy.kotlin.runtime.net.url.Url
    import kotlinx.coroutines.runBlocking
    import kotlin.time.Duration.Companion.minutes
    
    val ACCOUNT_ID = "<ACCOUNT_ID>"
    val ACCESS_KEY = "<ACCESS_KEY>"
    val SECRET_KEY = "<SECRET_KEY>"
    
    fun main() = runBlocking {
        val r2Client = S3Client.fromEnvironment {
            region = "auto" // Required by SDK, but not used by R2
            endpointUrl = Url.parse("https://${ACCOUNT_ID}.r2.cloudflarestorage.com")
            credentialsProvider = StaticCredentialsProvider(
                Credentials(
                    accessKeyId = ACCESS_KEY,
                    secretAccessKey = SECRET_KEY
                ),
            )
        }
    
        println("Available buckets:")
        r2Client.listBuckets().buckets?.forEach { bucket ->
            println("* ${bucket.name}")
        }
    
        val bucketName = "<BUCKET_NAME>"
        println("\nObjects in bucket '${bucketName}':")
        r2Client.listObjects { bucket = bucketName }.contents?.forEach {
            println("* ${it.key} (size: ${it.size} bytes, modified: ${it.lastModified})")
        }
    
        r2Client.close()
    }
    
    
    Available buckets:
    * my-bucket-1
    * my-bucket-2
    
    Objects in bucket 'my-bucket-1':
    * image1.png (size: 253167 bytes, modified: 2026-01-17T11:30:58.896Z)
    * image2.png (size: 247027 bytes, modified: 2026-01-17T11:30:57.779Z)

## Generate presigned URLs

You can also generate presigned links that can be used to temporarily share public read or write access to a bucket.
    
    
    val uploadUrl = r2Client.presignPutObject(
        input = PutObjectRequest {
            bucket = bucketName
            key = "README.md"
        },
        duration = 15.minutes,
    ).url
    println(uploadUrl)
    
    val getUrl = r2Client.presignGetObject(
        input = GetObjectRequest {
            bucket = bucketName
            key = "README.md"
        },
        duration = 15.minutes,
    ).url
    println(getUrl)

You can use these presigned URLs with any HTTP client. For example, to upload a file using the PUT URL:
    
    
    curl -X PUT "https://<your-presigned-put-url>" -H "Content-Type: application/octet-stream" --data-binary "@local-file.txt"

To download a file using the GET URL:
    
    
    curl -X GET "https://<your-presigned-get-url>" -o downloaded-file.txt

[Previousaws-sdk-js-v3](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-js-v3/)[Nextaws-sdk-net](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-net/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/aws/aws-sdk-kotlin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
