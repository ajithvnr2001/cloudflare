---
url: https://developers.cloudflare.com/security/web-assets/manage-operations/
title: Manage operations \u00b7 Security dashboard docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:30.817433+00:00
---

# Manage operations · Security dashboard docs

> Source: https://developers.cloudflare.com/security/web-assets/manage-operations/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security dashboard](https://developers.cloudflare.com/security/)
  3. /[Web Assets](https://developers.cloudflare.com/security/web-assets/)
  4. /Manage operations



# Manage operations

Last updated Aug 19, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security/web-assets/manage-operations/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewOperation statesDiscovery requirementsDiscovered operationsStart profile learningTraffic matching behaviorAdd operations manuallyUse variables in operation patternsAdd operations from schemasRefine operationsDelete operationsUse the Cloudflare API

## Operation states

Each operation has one of the following states:

State | Meaning  
---|---  
`full` | An operation that you selected, added manually, or created from a schema. Full operations are used for matching, logging, detections, and rules.  
`candidate` | An operation that Cloudflare discovered from traffic. Candidate operations are used for matching, logging, detections, and rules before you manually review them.  
`shadow` | An operation that exists in Web Assets but is not used for matching, logging, detections, or rules.  
  
You do not need to move every discovered operation to the `full` state. Candidate operations provide operation context automatically. Profile learning starts only when you select **Learn profile**.

## Discovery requirements

If an operation does not appear in Web Assets, Cloudflare may not have observed enough valid requests over a continuous period. Discovery only processes requests that satisfy all of the following requirements:

  * The request must return a `2xx` response code from the Cloudflare edge.
  * The request must not come directly from Cloudflare Workers.
  * The operation must receive at least 500 requests within a 10-day period.



## Discovered operations

Discovery continuously identifies operations from proxied HTTP traffic. Discovery groups similar request paths together by using path normalization.

For example, discovery can group these requests:
    
    
    GET https://api.example.com/profile/238
    GET https://api.example.com/profile/392

Discovery can group them into one operation:
    
    
    GET api.example.com/profile/{var1}

Discovered operations are used for matching before you manually refine them. This provides operation context without requiring a state change first.

Discovery-backed matching is subject to plan availability and system limits. Cloudflare currently sends up to 3,000 operations per zone to the edge for matching. Operations in the `full` state are prioritized first, followed by operations in the `candidate` state.

## Start profile learning

Select **Learn profile** to start intentional profile learning. Discovery, manual creation, and editing do not start profiling.

Customers with API Security already have access to Schema Profiles through Schema Learning and Schema Validation. Cloudflare is opening a closed beta to invited Enterprise customers without API Security. Interested customers can contact their account team to express interest. Closed-beta access does not imply future plan availability or pricing.

For a candidate or shadow operation, this action also moves the operation into the `full` state. An operation already in the `full` state remains there. Cloudflare then learns expected request structure from qualifying traffic.

For API endpoints, API Shield also collects data for other context:

  * Request structures through [schema learning](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/)
  * Normal request volume through [rate limit recommendations](https://developers.cloudflare.com/api-shield/security/volumetric-abuse-detection/)
  * Authentication usage through [Authentication Posture](https://developers.cloudflare.com/api-shield/security/authentication-posture/)
  * Persisted security findings through [API endpoint risk labels](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/#risk-labels)



Each feature has separate data and timing requirements. For Schema Profiles, refer to [Schema learning](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/).

Full operations can also use protections that require a known API endpoint, including [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/), [fallthrough rules](https://developers.cloudflare.com/api-shield/security/schema-validation/#add-validation-by-adding-a-fallthrough-rule), and [sequence mitigation](https://developers.cloudflare.com/api-shield/security/sequence-mitigation/).

  1. In the Cloudflare dashboard, go to the **Web Assets** page with the **Operations** tab highlighted.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Open the row actions for the operation.

  3. Select **Learn profile**.




After the profile becomes available, select **View details**. Review the learned schema under **Security overview**.

## Traffic matching behavior

Cloudflare matches each request to one operation at the edge. When more than one operation pattern could match the same request, the more specific operation wins.

Matching priority

Operations in the `full` state always match before operations in the `candidate` state.

For example, these operations could both match `GET https://example.com/checkout/pay`:
    
    
    GET example.com/checkout/pay
    GET example.com/checkout/{var1}

Cloudflare uses `GET example.com/checkout/pay` because it is more specific.

For the same method, hostname pattern, and path pattern, Cloudflare generates the same operation UUID. This keeps operation identity stable when the same operation is found again.

## Add operations manually

Add an operation manually when traffic you want to protect has not been discovered, or when you want to define the operation structure yourself.

  1. In the Cloudflare dashboard, go to the **Web Assets** page with **Operations** tab highlighted.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Select **Add operation**.

  3. Choose **Manually add**.

  4. Select the HTTP method, enter the hostname pattern and path pattern.

  5. Confirm with **Add operation**.




Manual creation only adds the operation to inventory. Select **Learn profile** separately to start profiling.

## Use variables in operation patterns

When you add an operation manually, use variables to match similar traffic with one operation.

For path variables, enclose the variable in braces:
    
    
    /api/users/{var1}/details

For hostname variables, the variable must occupy a complete hostname label. Cloudflare supports patterns such as:
    
    
    {hostVar1}.example.com
    foo.{hostVar1}.example.com
    {hostVar2}.{hostVar1}.example.com

Do not combine a hostname variable with other characters in the same label. The following pattern is not supported:
    
    
    foo-{hostVar1}.example.com

## Add operations from schemas

If you already maintain OpenAPI schemas, you can continue uploading them to create operations.

Schema upload is also used by [API Shield](https://developers.cloudflare.com/api-shield/) for schema validation. For more information, refer to [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/) and [schema learning](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/schema-learning/).

## Refine operations

Refine operations when the current grouping does not match how the traffic should be grouped or protected.

For example, you may want separate operations for login and password reset traffic, even if both routes share part of the same path structure. You may also want to replace several narrow operations with one broader operation when they represent the same application behavior.

Review overlapping operations before making changes. Cloudflare matches a request to one operation. A broad operation can change how similar requests are grouped, while a narrow operation can isolate one flow from related traffic.

  1. In the Cloudflare dashboard, go to the **Web Assets** page with the **Operations** tab highlighted.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Open the row actions for the operation.

  3. Select **Edit operation**.

  4. Update the HTTP method, hostname pattern, or path pattern.

  5. Select **Save**.




Editing updates the operation inventory entry. It does not start profile learning.

Editing this operation will change its ID

Cloudflare computes operation IDs from the HTTP method, hostname, and path. Changing these values creates a different operation ID.

## Delete operations

You can delete operations one at a time or in bulk.

  1. In the Cloudflare dashboard, go to the **Web Assets** page with **Operations** tab highlighted.

[ Go to **Web assets** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/security/web-assets)
  2. Select the operation(s) that you want to delete.

  3. Confirm with **Delete operations**.




Note

After you delete an operation, Cloudflare no longer matches future traffic to that operation. If Cloudflare later discovers similar traffic, the traffic may appear again as a discovered operation.

## Use the Cloudflare API

You can interact with operations through the Cloudflare API. For more information, refer to [operations API documentation](https://developers.cloudflare.com/api/resources/api_gateway/subresources/discovery/subresources/operations/methods/list/).

[PreviousGet started](https://developers.cloudflare.com/security/web-assets/get-started/)[NextLabel operations](https://developers.cloudflare.com/security/web-assets/label-operations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security/web-assets/manage-operations.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
