---
url: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/common-policies/
title: Common DLP policies \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:31.092433+00:00
---

# Common DLP policies · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/common-policies/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Data loss prevention](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/)

  4. /[Scan HTTP traffic](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/)
  5. /Common policies



# Common policies

Last updated Apr 17, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/common-policies/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLog uploads/downloadsBlock file typesBlock uploads/downloads for specific usersExclude Android applicationsExclude specific sites

The following DLP policies are commonly used to secure sensitive data in uploaded and downloaded files. They are built as [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) using the [DLP Profile](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#dlp-profile) selector.

Before using these policies, complete the [prerequisites for scanning HTTP traffic](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/#prerequisites).

## Log uploads/downloads

When you want to monitor where sensitive data is going before enforcing blocks, use the **Allow** action. In a Gateway HTTP policy, all matches — including Allow — are recorded in your [HTTP request logs](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/#4-view-dlp-logs). This gives you visibility into sensitive data transfers without disrupting users.

The following example logs any upload or download that matches your enabled [Financial Information](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-profiles/predefined-profiles/#financial-information) DLP profile entries when users interact with file sharing applications.

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
DLP Profile | in | _Financial Information_ | And | Allow  
Content Categories | in | _File Sharing_ |  |   
  
## Block file types

Block the upload or download of files based on their type.

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
Upload File Types | in | _Microsoft Office Word Document (docx)_ | And | Block  
Download File Types | in | _PDF (pdf)_ |  |   
  
Create a Zero Trust Gateway rulebash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/gateway/rules" \
    	--request POST \
    	--header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
    	--json '{
    		"name": "Block file types",
    		"description": "Block the upload or download of files based on their type",
    		"enabled": true,
    		"action": "block",
    		"filters": [
    				"http"
    		],
    		"traffic": "any(http.upload.file.types[*] in {\"docx\"}) and any(http.download.file.types[*] in {\"pdf\"})",
    		"identity": "",
    		"device_posture": ""
    	}'

For more information on what file formats DLP can scan, refer to [Supported file types](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/#supported-file-types).

## Block uploads/downloads for specific users

You can configure access on a per-user or group basis by adding [identity-based conditions](https://developers.cloudflare.com/cloudflare-one/traffic-policies/identity-selectors/) to your policies. These selectors match against user attributes from your configured identity provider.

The following example blocks only contractors from uploading/downloading Financial Information to file sharing apps. Users who are not in the _Contractors_ group are not affected by this policy.

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
DLP Profile | in | _Financial Information_ | And | Block  
Content Categories | in | _File Sharing_ | And |   
User Group Names | in | _Contractors_ |  |   
  
## Exclude Android applications

Many Android applications (such as Google Drive) use [certificate pinning](https://developers.cloudflare.com/ssl/reference/certificate-pinning/), which is incompatible with Gateway TLS decryption. These applications verify they are connecting directly to their own servers and will reject Gateway's inspection certificate. If needed, you can create a [Do Not Inspect policy](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#do-not-inspect) so that the app can continue to function on Android:

  1. Set up an [OS version device posture check](https://developers.cloudflare.com/cloudflare-one/reusable-components/posture-checks/client-checks/os-version/) that checks for the Android operating system.

  2. Create the following HTTP policy in Gateway:

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
Application | in | _Google Drive_ | And | Do Not Inspect  
Passed Device Posture Checks | in | _OS Version Android_ |  |   
  



Android users can now use the app, but the app traffic will bypass Gateway inspection entirely — including DLP scanning, HTTP logging, and antivirus scanning.

## Exclude specific sites

In your [DLP logs](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/#4-view-dlp-logs), you may find that certain sites routinely trigger DLP detections that do not represent actual data loss (false positives). To exempt these sites from DLP scanning:

  1. [Create a list](https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/) of hostnames or URLs.

  2. Exclude the list from your DLP policy using the `not in list` operator, which references the list you created in step 1:

Selector | Operator | Value | Logic | Action  
---|---|---|---|---  
DLP Profile | in | _Financial Information_ | And | Block  
Application | in | _Google Drive_ | And |   
Domain | not in list | _Do not DLP - SSN_ |  |   
  



[PreviousCreate DLP policies](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/)[NextLogging options](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/data-loss-prevention/dlp-policies/common-policies.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
