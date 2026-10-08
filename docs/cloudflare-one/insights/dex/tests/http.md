---
url: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/
title: HTTP test \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:50.011392+00:00
---

# HTTP test · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Digital experience](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

  4. /[Synthetic tests](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/)
  5. /HTTP test



# HTTP test

Last updated Aug 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/http/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a testTest resultsExport DEX application test logsRelated resources

Feature availability

[Client modes](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/) | [Zero Trust plans ↗︎](https://www.cloudflare.com/teams-pricing/)  
---|---  
  
  * Traffic and DNS mode 
  * Traffic only mode 

| All plans  
  
System | Availability | Minimum client version  
---|---|---  
Windows | ✅ | 2023.3.381  
macOS | ✅ | 2023.3.381  
Linux | ✅ | 2023.3.398  
iOS | ❌ |   
Android | ✅ | 1.0  
ChromeOS | ✅ | 1.0  
  
An HTTP test sends a `GET` request from an end-user device to a specific web application. You can use the response metrics to troubleshoot connectivity issues. For example, you can check whether the application is inaccessible for all users in your organization, or only certain ones.

HTTP tests run periodically from devices that have the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) installed and turned on. You can use them to verify that an internal application is reachable after a configuration change or to monitor a SaaS application for outages that affect your organization.

## Create a test

To set up an HTTP test for an application:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Insights** > **Digital experience**.
  2. Select the **Tests** tab.
  3. Select **Add a Test**.
  4. Fill in the following fields: 
     * **Name** : Enter any name for the test.
     * **Target** : Enter the URL of the website or application that you want to test (for example, `https://jira.site.com`). Both public and private hostnames are supported. If testing a private hostname, ensure that the domain is on your [local domain fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) list.
     * **Source device profiles** : (Optional) Select the [device profiles](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) that you want to run the test on. If no profiles are selected, the test will run on all supported devices connected to your Zero Trust organization.
     * **Test type** : Select _HTTP Get_.
     * **Test frequency** : Specify how often the test will run. Input a minute value between 5 and 60.
  5. Select **Add test**.
  6. After the test is created and running, you can [view the results](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/view-results/) of your test.



## Test results

An HTTP test measures the following data:

Data | Description  
---|---  
Resource fetch time | Total time of all steps of the request, measured from [`startTime` to `responseEnd` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Performance_API/Resource_timing).  
Server response time | Round-trip time for the device to receive a response from the target.  
DNS response time | Round-trip time for the DNS query to resolve.  
HTTP status codes | [Status code ↗︎](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status) returned by the target.  
  
Use these metrics together to identify where in the connection a problem occurs. For example, a high DNS response time with a normal server response time points to a DNS resolution issue rather than a problem with the target server.

## Export DEX application test logs

You can use [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/) to export [DEX application test](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/dex_application_tests/) data to [R2](https://developers.cloudflare.com/r2/) (Cloudflare's object storage), a third-party cloud storage bucket, or a Security Information and Event Management (SIEM) tool. This is useful if you need to retain test data beyond the [7-day log retention period](https://developers.cloudflare.com/cloudflare-one/insights/logs/#log-retention) or correlate DEX data with other log sources.

## Related resources

  * [DEX rules](https://developers.cloudflare.com/cloudflare-one/insights/dex/rules/) \- Define which users or groups a test applies to, using selectors such as user email, user group, operating system, or managed network.



[PreviousOverview](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/)[NextTraceroute test](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/dex/tests/http.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
