---
url: https://developers.cloudflare.com/r2/api/s3/api/
title: S3 API compatibility \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:42.426205+00:00
---

# S3 API compatibility · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/api/s3/api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /…

[API](https://developers.cloudflare.com/r2/api/)

  4. /S3
  5. /S3 API compatibility



# S3 API compatibility

Last updated Jul 31, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/api/s3/api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow to read this pageBucket regionChecksum TypesBucket-level operations Implemented bucket-level operations Unimplemented bucket-level operationsObject-level operations Implemented object-level operations Unimplemented object-level operations

R2 implements the S3 API to allow users and their applications to migrate with ease. When comparing to AWS S3, Cloudflare has removed some API operations' features and added others. The S3 API operations are listed below with their current implementation status. Feature implementation is currently in progress. Refer back to this page for updates. The API is available via the `https://<ACCOUNT_ID>.r2.cloudflarestorage.com` endpoint. Find your [account ID in the Cloudflare dashboard](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).

## How to read this page

This page has two sections: bucket-level operations and object-level operations.

Each section will have two tables: a table of implemented APIs and a table of unimplemented APIs.

Refer the feature column of each table to review which features of an API have been implemented and which have not.

✅ Feature Implemented   
🚧 Feature Implemented (Experimental)   
❌ Feature Not Implemented

## Bucket region

When using the S3 API, the region for an R2 bucket is `auto`. For compatibility with tools that do not allow you to specify a region, an empty value and `us-east-1` will alias to the `auto` region.

This also applies to the `LocationConstraint` for the `CreateBucket` API.

## Checksum Types

Checksums have an algorithm and a [type ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html#ChecksumTypes). Refer to the table below.

Checksum Algorithm | `FULL_OBJECT` | `COMPOSITE`  
---|---|---  
CRC-64/NVME (`CRC64NVME`) | ✅ | ❌  
CRC-32 (`CRC32`) | ❌ | ✅  
CRC-32C (`CRC32C`) | ❌ | ✅  
SHA-1 (`SHA1`) | ❌ | ✅  
SHA-256 (`SHA256`) | ❌ | ✅  
  
## Bucket-level operations

The following tables are related to bucket-level operations.

### Implemented bucket-level operations

Below is a list of implemented bucket-level operations. Refer to the Feature column to review which features have been implemented (✅) and have not been implemented (❌).

API Name | Feature  
---|---  
✅ [ListBuckets ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) |   
✅ [HeadBucket ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [CreateBucket ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) | ❌ ACL:   
❌ x-amz-acl   
❌ x-amz-grant-full-control   
❌ x-amz-grant-read   
❌ x-amz-grant-read-acp   
❌ x-amz-grant-write   
❌ x-amz-grant-write-acp   
❌ Object Locking:   
❌ x-amz-bucket-object-lock-enabled   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [DeleteBucket ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [DeleteBucketCors ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [GetBucketCors ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [GetBucketLifecycleConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [GetBucketLocation ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [GetBucketEncryption ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [PutBucketCors ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html) | ❌ Checksums:   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [PutBucketLifecycleConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycleConfiguration.html) | ❌ Checksums:   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
  
### Unimplemented bucket-level operations

Unimplemented bucket-level operations

API Name | Feature  
---|---  
❌ [GetBucketAccelerateConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketAcl ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketAnalyticsConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketIntelligentTieringConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html) | ❌ id  
❌ [GetBucketInventoryConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketLifecycle ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketLogging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketMetricsConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketNotification ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotification.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketNotificationConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketOwnershipControls ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketPolicy ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketPolicyStatus ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketReplication ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketRequestPayment ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketTagging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketVersioning ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetBucketWebsite ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetObjectLockConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [GetPublicAccessBlock ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [ListBucketAnalyticsConfigurations ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html) | ❌ Query Parameters:   
❌ continuation-token   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [ListBucketIntelligentTieringConfigurations ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html) | ❌ Query Parameters:   
❌ continuation-token   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [ListBucketInventoryConfigurations ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html) | ❌ Query Parameters:   
❌ continuation-token   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [ListBucketMetricsConfigurations ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketMetricsConfigurations.html) | ❌ Query Parameters:   
❌ continuation-token   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketAccelerateConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html) | ❌ Checksums:   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketAcl ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html) | ❌ Permissions:   
❌ x-amz-grant-full-control   
❌ x-amz-grant-read   
❌ x-amz-grant-read-acp   
❌ x-amz-grant-write   
❌ x-amz-grant-write-acp   
❌ Checksums:   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketAnalyticsConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketEncryption ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) | ❌ Checksums:   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketIntelligentTieringConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketInventoryConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketLifecycle ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html) | ❌ Checksums:   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketLogging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html) | ❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketMetricsConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html) | ❌ id   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketNotification ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotification.html) | ❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketNotificationConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html) | ❌ Validation:   
❌ x-amz-skip-destination-validation   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketOwnershipControls ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketOwnershipControls.html) | ❌ Checksums:   
❌ Content-MD5   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketPolicy ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html) | ❌ Validation:   
❌ x-amz-confirm-remove-self-bucket-access   
❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketReplication ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html) | ❌ Object Locking:   
❌ x-amz-bucket-object-lock-token   
❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketRequestPayment ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html) | ❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketTagging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html) | ❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketVersioning ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) | ❌ Multi-factor authentication:   
❌ x-amz-mfa   
❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutBucketWebsite ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html) | ❌ Checksums:   
❌ Content-MD5   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutObjectLockConfiguration ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html) | ❌ Object Locking:   
❌ x-amz-bucket-object-lock-token   
❌ Checksums:   
❌ Content-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
❌ [PutPublicAccessBlock ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html) | ❌ Checksums:   
❌ Content-MD5   
❌ x-amz-sdk-checksum-algorithm   
❌ x-amz-checksum-algorithm   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
  
## Object-level operations

The following tables are related to object-level operations.

### Implemented object-level operations

Below is a list of implemented object-level operations. Refer to the Feature column to review which features have been implemented (✅) and have not been implemented (❌).

#### Behaviors & Limitations

**UploadPart:** Uploading to the same part number replaces the previous part. If a subsequent upload to the same part fails, the original part is lost and must be re-uploaded.

API Name | Feature  
---|---  
✅ [HeadObject ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) | ✅ Conditional Operations:   
✅ If-Match   
✅ If-Modified-Since   
✅ If-None-Match   
✅ If-Unmodified-Since   
✅ Range:   
✅ Range (has no effect in HeadObject)   
✅ partNumber   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [ListObjects ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) | Query Parameters:   
✅ delimiter   
✅ encoding-type   
✅ marker   
✅ max-keys   
✅ prefix   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [ListObjectsV2 ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) | Query Parameters:   
✅ list-type   
✅ continuation-token   
✅ delimiter   
✅ encoding-type   
✅ fetch-owner   
✅ max-keys   
✅ prefix   
✅ start-after   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [GetObject ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | ✅ Conditional Operations:   
✅ If-Match   
✅ If-Modified-Since   
✅ If-None-Match   
✅ If-Unmodified-Since   
✅ Range:   
✅ Range   
✅ PartNumber   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [PutObject ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) | ✅ Conditional Operations:   
✅ If-Match   
✅ If-Modified-Since   
✅ If-None-Match   
✅ If-Unmodified-Since   
✅ System Metadata:   
✅ Content-Type   
✅ Cache-Control   
✅ Content-Disposition   
✅ Content-Encoding   
✅ Content-Language   
✅ Expires   
✅ Content-MD5   
✅ Storage Class:   
✅ x-amz-storage-class   
✅ STANDARD   
✅ STANDARD_IA   
❌ Object Lifecycle   
❌ Website:   
❌ x-amz-website-redirect-location   
❌ SSE:   
❌ x-amz-server-side-encryption-aws-kms-key-id   
❌ x-amz-server-side-encryption   
❌ x-amz-server-side-encryption-context   
❌ x-amz-server-side-encryption-bucket-key-enabled   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Tagging:   
❌ x-amz-tagging   
❌ Object Locking:   
❌ x-amz-object-lock-mode   
❌ x-amz-object-lock-retain-until-date   
❌ x-amz-object-lock-legal-hold   
❌ ACL:   
❌ x-amz-acl   
❌ x-amz-grant-full-control   
❌ x-amz-grant-read   
❌ x-amz-grant-read-acp   
❌ x-amz-grant-write-acp   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [DeleteObject ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) | ❌ Multi-factor authentication:   
❌ x-amz-mfa   
❌ Object Locking:   
❌ x-amz-bypass-governance-retention   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [DeleteObjects ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) | ❌ Multi-factor authentication:   
❌ x-amz-mfa   
❌ Object Locking:   
❌ x-amz-bypass-governance-retention   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [ListMultipartUploads ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html) | ✅ Query Parameters:   
✅ delimiter   
✅ encoding-type   
✅ key-marker   
✅️ max-uploads   
✅ prefix   
✅ upload-id-marker  
✅ [CreateMultipartUpload ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html) | ✅ System Metadata:   
✅ Content-Type   
✅ Cache-Control   
✅ Content-Disposition   
✅ Content-Encoding   
✅ Content-Language   
✅ Expires   
✅ Content-MD5   
✅ Storage Class:   
✅ x-amz-storage-class   
✅ STANDARD   
✅ STANDARD_IA   
❌ Website:   
❌ x-amz-website-redirect-location   
❌ SSE:   
❌ x-amz-server-side-encryption-aws-kms-key-id   
❌ x-amz-server-side-encryption   
❌ x-amz-server-side-encryption-context   
❌ x-amz-server-side-encryption-bucket-key-enabled   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Tagging:   
❌ x-amz-tagging   
❌ Object Locking:   
❌ x-amz-object-lock-mode   
❌ x-amz-object-lock-retain-until-date   
❌ x-amz-object-lock-legal-hold   
❌ ACL:   
❌ x-amz-acl   
❌ x-amz-grant-full-control   
❌ x-amz-grant-read   
❌ x-amz-grant-read-acp   
❌ x-amz-grant-write-acp   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [CompleteMultipartUpload ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner   
❌ Request Payer:   
❌ x-amz-request-payer  
✅ [AbortMultipartUpload ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) | ❌ Request Payer:   
❌ x-amz-request-payer  
✅ [CopyObject ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) | ✅ Operation Metadata:   
✅ x-amz-metadata-directive   
✅ System Metadata:   
✅ Content-Type   
✅ Cache-Control   
✅ Content-Disposition   
✅ Content-Encoding   
✅ Content-Language   
✅ Expires   
✅ Conditional Operations:   
✅ x-amz-copy-source   
✅ x-amz-copy-source-if-match   
✅ x-amz-copy-source-if-modified-since   
✅ x-amz-copy-source-if-none-match   
✅ x-amz-copy-source-if-unmodified-since   
✅ Storage Class:   
✅ x-amz-storage-class   
✅ STANDARD   
✅ STANDARD_IA   
❌ ACL:   
❌ x-amz-acl   
❌ x-amz-grant-full-control   
❌ x-amz-grant-read   
❌ x-amz-grant-read-acp   
❌ x-amz-grant-write-acp   
❌ Website:   
❌ x-amz-website-redirect-location   
❌ SSE:   
❌ x-amz-server-side-encryption   
❌ x-amz-server-side-encryption-aws-kms-key-id   
❌ x-amz-server-side-encryption-context   
❌ x-amz-server-side-encryption-bucket-key-enabled   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
✅ x-amz-copy-source-server-side-encryption-customer-algorithm   
✅ x-amz-copy-source-server-side-encryption-customer-key   
✅ x-amz-copy-source-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Tagging:   
❌ x-amz-tagging   
❌ x-amz-tagging-directive   
❌ Object Locking:   
❌ x-amz-object-lock-mode   
❌ x-amz-object-lock-retain-until-date   
❌ x-amz-object-lock-legal-hold   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner   
❌ x-amz-source-expected-bucket-owner   
❌ Checksums:   
❌ x-amz-checksum-algorithm  
✅ [UploadPart ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) | ✅ System Metadata:   
✅ Content-MD5   
❌ SSE:   
❌ x-amz-server-side-encryption   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
✅ [UploadPartCopy ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) | ✅ Copy Source:   
✅ x-amz-copy-source (required)   
❌ Conditional Operations:   
❌ x-amz-copy-source-if-match   
❌ x-amz-copy-source-if-modified-since   
❌ x-amz-copy-source-if-none-match   
❌ x-amz-copy-source-if-unmodified-since   
✅ Range:   
✅ x-amz-copy-source-range   
✅ SSE-C:   
✅ x-amz-server-side-encryption-customer-algorithm   
✅ x-amz-server-side-encryption-customer-key   
✅ x-amz-server-side-encryption-customer-key-MD5   
✅ x-amz-copy-source-server-side-encryption-customer-algorithm   
✅ x-amz-copy-source-server-side-encryption-customer-key   
✅ x-amz-copy-source-server-side-encryption-customer-key-MD5   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner   
❌ x-amz-source-expected-bucket-owner  
✅ [ListParts ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html) | Query Parameters:   
✅ max-parts   
✅ part-number-marker   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
  
Caution

Even though `ListObjects` is a supported operation, it is recommended that you use `ListObjectsV2` instead when developing applications. For more information, refer to [ListObjects ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html).

### Unimplemented object-level operations

Unimplemented object-level operations

API Name | Feature  
---|---  
❌ [GetObjectTagging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner   
❌ Request Payer:   
❌ x-amz-request-payer  
❌ [PutObjectTagging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner   
❌ Request Payer:   
❌ x-amz-request-payer   
❌ Checksums:   
❌ x-amz-sdk-checksum-algorithm  
❌ [DeleteObjectTagging ↗︎](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) | ❌ Bucket Owner:   
❌ x-amz-expected-bucket-owner  
  
[PreviousWorkers API reference](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)[NextExtensions](https://developers.cloudflare.com/r2/api/s3/extensions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/api/s3/api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
