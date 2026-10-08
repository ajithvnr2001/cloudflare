---
url: https://developers.cloudflare.com/r2/examples/authenticate-r2-auth-tokens/
title: Authenticate against R2 API using auth tokens \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:44.922259+00:00
---

# Authenticate against R2 API using auth tokens · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/authenticate-r2-auth-tokens/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /[Examples](https://developers.cloudflare.com/r2/examples/)
  4. /Authenticate against R2 API using auth tokens



# Authenticate against R2 API using auth tokens

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/authenticate-r2-auth-tokens/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

The following example shows how to authenticate against R2 using the S3 API and an API token.

Note

For providing secure access to bucket objects for anonymous users, we recommend using [pre-signed URLs](https://developers.cloudflare.com/r2/api/s3/presigned-urls/) instead.

Pre-signed URLs do not require users to be a member of your organization and enable direct programmatic access to R2.

Ensure you have set the following environment variables prior to running either example. Refer to [Authentication](https://developers.cloudflare.com/r2/api/tokens/) for more information.
    
    
    export AWS_REGION=auto
    export AWS_ENDPOINT_URL=https://<account_id>.r2.cloudflarestorage.com
    export AWS_ACCESS_KEY_ID=your_access_key_id
    export AWS_SECRET_ACCESS_KEY=your_secret_access_key

Install the `@aws-sdk/client-s3` package for the S3 API:

npmyarnpnpmbun
    
    
    npm i @aws-sdk/client-s3
    
    
    yarn add @aws-sdk/client-s3
    
    
    pnpm add @aws-sdk/client-s3
    
    
    bun add @aws-sdk/client-s3

Run the following Node.js script with `node index.js`. Ensure you change `Bucket` to the name of your bucket, and `Key` to point to an existing file in your R2 bucket.

Note, tutorial below should function for TypeScript as well.

index.jsjavascript
    
    
    import { GetObjectCommand, S3Client } from "@aws-sdk/client-s3";
    
    const s3 = new S3Client();
    
    const Bucket = "<YOUR_BUCKET_NAME>";
    const Key = "pfp.jpg";
    
    const object = await s3.send(
      new GetObjectCommand({
        Bucket,
        Key,
      }),
    );
    
    console.log("Successfully fetched the object", object.$metadata);
    
    // Process the data as needed
    // For example, to get the content as a Buffer:
    // const content = data.Body;
    
    // Or to save the file (requires 'fs' module):
    // import { writeFile } from "node:fs/promises";
    // await writeFile('ingested_0001.parquet', data.Body);

Install the `boto3` S3 API client:
    
    
    pip install boto3

Run the following Python script with `python3 get_r2_object.py`. Ensure you change `bucket` to the name of your bucket, and `object_key` to point to an existing file in your R2 bucket.

get_r2_object.pypython
    
    
    import boto3
    from botocore.client import Config
    
    # Configure the S3 client for Cloudflare R2
    s3_client = boto3.client('s3',
      config=Config(signature_version='s3v4')
    )
    
    # Specify the object key
    #
    bucket = '<YOUR_BUCKET_NAME>'
    object_key = '2024/08/02/ingested_0001.parquet'
    
    try:
      # Fetch the object
      response = s3_client.get_object(Bucket=bucket, Key=object_key)
    
      print('Successfully fetched the object')
    
      # Process the response content as needed
      # For example, to read the content:
      # object_content = response['Body'].read()
    
      # Or to save the file:
      # with open('ingested_0001.parquet', 'wb') as f:
      #     f.write(response['Body'].read())
    
    except Exception as e:
      print(f'Failed to fetch the object. Error: {str(e)}')

Use `go get` to add the `aws-sdk-go-v2` packages to your Go project:
    
    
    go get github.com/aws/aws-sdk-go-v2
    go get github.com/aws/aws-sdk-go-v2/config
    go get github.com/aws/aws-sdk-go-v2/credentials
    go get github.com/aws/aws-sdk-go-v2/service/s3

Run the following Go application as a script with `go run main.go`. Ensure you change `bucket` to the name of your bucket, and `objectKey` to point to an existing file in your R2 bucket.
    
    
    package main
    
    import (
      "context"
      "fmt"
      "io"
      "log"
      "github.com/aws/aws-sdk-go-v2/aws"
      "github.com/aws/aws-sdk-go-v2/config"
      "github.com/aws/aws-sdk-go-v2/service/s3"
    )
    
    func main() {
        cfg, err := config.LoadDefaultConfig(context.TODO())
        if err != nil {
    	    log.Fatalf("Unable to load SDK config, %v", err)
        }
    
        // Create an S3 client
        client := s3.NewFromConfig(cfg)
    
        // Specify the object key
        bucket := "<YOUR_BUCKET_NAME>"
        objectKey := "pfp.jpg"
    
        // Fetch the object
        output, err := client.GetObject(context.TODO(), &s3.GetObjectInput{
    	    Bucket: aws.String(bucket),
    	    Key:    aws.String(objectKey),
        })
        if err != nil {
    	    log.Fatalf("Unable to fetch object, %v", err)
        }
        defer output.Body.Close()
    
        fmt.Println("Successfully fetched the object")
    
        // Process the object content as needed
        // For example, to save the file:
        // file, err := os.Create("ingested_0001.parquet")
        // if err != nil {
        // 	log.Fatalf("Unable to create file, %v", err)
        // }
        // defer file.Close()
        // _, err = io.Copy(file, output.Body)
        // if err != nil {
        // 	log.Fatalf("Unable to write file, %v", err)
        // }
    
        // Or to read the content:
        content, err := io.ReadAll(output.Body)
        if err != nil {
    	    log.Fatalf("Unable to read object content, %v", err)
        }
        fmt.Printf("Object content length: %d bytes\n", len(content))
    }

[PreviousMulti-cloud setup ↗︎](https://developers.cloudflare.com/reference-architecture/diagrams/storage/egress-free-storage-multi-cloud/)[NextAuthenticate against R2 with temporary credentials](https://developers.cloudflare.com/r2/examples/authenticate-r2-temp-credentials/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/authenticate-r2-auth-tokens.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
