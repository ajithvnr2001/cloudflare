---
url: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-ruby/
title: aws-sdk-ruby \u00b7 Cloudflare R2 docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:45.896440+00:00
---

# aws-sdk-ruby · Cloudflare R2 docs

> Source: https://developers.cloudflare.com/r2/examples/aws/aws-sdk-ruby/

  1. [Home](https://developers.cloudflare.com/)
  2. /[R2](https://developers.cloudflare.com/r2/)
  3. /…

[Examples](https://developers.cloudflare.com/r2/examples/)

  4. /S3 SDKs
  5. /aws-sdk-ruby



# aws-sdk-ruby

Last updated Sep 4, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-ruby/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You must [generate an Access Key](https://developers.cloudflare.com/r2/api/tokens/) before getting started. All examples will utilize `access_key_id` and `access_key_secret` variables which represent the **Access Key ID** and **Secret Access Key** values you generated.

  


Many Ruby projects also store these credentials in environment variables instead.

Add the following dependency to your `Gemfile`:
    
    
    gem "aws-sdk-s3"

Then you can use Ruby to operate on R2 buckets:
    
    
    require "aws-sdk-s3"
    
    @r2 = Aws::S3::Client.new(
      # Retrieve your S3 API credentials for your R2 bucket via API tokens (see: https://developers.cloudflare.com/r2/api/tokens)
      access_key_id: "#{ACCESS_KEY_ID}",
      secret_access_key: "#{SECRET_ACCESS_KEY}",
      # Provide your Cloudflare account ID
      endpoint: "https://#{ACCOUNT_ID}.r2.cloudflarestorage.com",
      region: "auto", # Required by SDK but not used by R2
    )
    
    # List all buckets on your account
    puts @r2.list_buckets
    
    #=> {
    #=>   :buckets => [{
    #=>     :name => "your-bucket",
    #=>     :creation_date => "…",
    #=>   }],
    #=>   :owner => {
    #=>     :display_name => "…",
    #=>     :id => "…"
    #=>   }
    #=> }
    
    # List the first 20 items in a bucket
    puts @r2.list_objects_v2(bucket: "your-bucket", max_keys: 20)
    
    #=> {
    #=>   :is_truncated => false,
    #=>   :name => "your-bucket",
    #=>   :prefix => nil,
    #=>   :delimiter => nil,
    #=>   :max_keys => 20,
    #=>   :common_prefixes => [],
    #=>   :encoding_type => nil,
    #=>   :key_count => 3,
    #=>   :contents => [
    #=>     …,
    #=>     …,
    #=>     …,
    #=>   ]
    #=> }

[Previousaws-sdk-php](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-php/)[Nextaws-sdk-rust](https://developers.cloudflare.com/r2/examples/aws/aws-sdk-rust/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/r2/examples/aws/aws-sdk-ruby.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
