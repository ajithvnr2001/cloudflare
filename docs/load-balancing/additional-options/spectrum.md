---
url: https://developers.cloudflare.com/load-balancing/additional-options/spectrum/
title: Add load balancing to Spectrum applications \u00b7 Cloudflare Load Balancing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:04.324409+00:00
---

# Add load balancing to Spectrum applications · Cloudflare Load Balancing docs

> Source: https://developers.cloudflare.com/load-balancing/additional-options/spectrum/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Load Balancing](https://developers.cloudflare.com/load-balancing/)
  3. /[Additional configuration](https://developers.cloudflare.com/load-balancing/additional-options/)
  4. /Spectrum



# Spectrum

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/load-balancing/additional-options/spectrum/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up 1\. Configure your load balancer 2\. Configure your Spectrum applicationLimitations

You can configure [Spectrum](https://developers.cloudflare.com/spectrum/) with Load Balancing to bring resiliency to your TCP or UDP based applications.

Leverage health monitors, failover, and traffic steering by selecting a load balancer as **Origin** when creating your Spectrum application.

The exact settings will vary depending on your use case. Refer to the following steps to understand the workflow.

* * *

## Set up

### 1\. Configure your load balancer

  1. In the Cloudflare dashboard, go to the **Load Balancing** page.

[ Go to **Load Balancing** ↗ ](https://dash.cloudflare.com/?to=/:account/load-balancing)
  2. Select an account where the Load Balancing add-on is [enabled](https://developers.cloudflare.com/load-balancing/get-started/enable-load-balancing/).

  3. Go to **Load Balancing** and select **Create load balancer**.

  4. On the **Load Balancer Setup** , select **Public load balancer**

  5. Choose the website to which you want to add this load balancer.

  6. On the **Hostname** page, define the settings presented and select **Next**.

     * Enter a **Hostname** , which is the DNS name at which the load balancer is available. For more details on record priority, refer to [DNS records for load balancing](https://developers.cloudflare.com/load-balancing/load-balancers/dns-records/).

Caution

To prevent issues with DNS resolution, the load balancer hostname should be different from the hostname (or domain) you intend to define for your Spectrum application.

     * Keep the orange cloud icon enabled, meaning the load balancer is proxied. This refers to the [proxy mode](https://developers.cloudflare.com/load-balancing/understand-basics/proxy-modes/) and, with Spectrum, traffic is always proxied.

     * Keep **Session Affinity** and **Failover across pools** disabled as these features are not supported with Spectrum.

  7. On the **Add a Pool** page, define the settings presented and select **Next**.

     * Select one or more existing pools or [create a new pool](https://developers.cloudflare.com/load-balancing/pools/create-pool/#create-a-pool) 1.
     * If needed, update the [fallback pool](https://developers.cloudflare.com/load-balancing/understand-basics/health-details/#fallback-pools) 2.
  8. On the **Monitors** page, define the settings presented and select **Next**.

     * Review the monitors attached to your pools.
     * If needed, you can attach an existing monitor or [create a new monitor](https://developers.cloudflare.com/load-balancing/monitors/create-monitor/#create-a-monitor).
  9. On the **Traffic Steering** page, choose an option for [Traffic steering](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/) and select **Next**.

  10. Keep **Custom Rules** page empty as this feature is not supported with Spectrum.

  11. On the **Review** page:



  * Review your configuration and make any changes. 
    * If you set traffic steering to **Off** , re-order the pools in your load balancer to adjust the fallback order.
    * If you chose to set traffic steering to Random, you can [set weights to your pools](https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/steering-policies/standard-options/#random-steering) (via the [API](https://developers.cloudflare.com/api/resources/load_balancers/methods/create/)) to determine the percentage of traffic sent to each pool.
  * Choose whether to **Save as Draft** or **Save and Deploy**.



### 2\. Configure your Spectrum application

  1. In the Cloudflare dashboard, go to the **Spectrum** page.

[ Go to **Spectrum** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/spectrum)
  2. Select **Create an Application**. If this is your first time using Spectrum, the **Create an Application** modal appears.

  3. Select your **[Application Type](https://developers.cloudflare.com/spectrum/reference/configuration-options/#application-type)**.

  4. Under **Domain** , enter the domain that will use Spectrum.

  5. Under **Edge Port** , enter the port Cloudflare should use for your application.

  6. Under **Origin** , select **Load Balancer**.

  7. Select the load balancer you want to use from the dropdown. Disabled load balancers will not show on the **Load Balancer** menu.

  8. Select **Add**.




* * *

## Limitations

  * Load Balancing [session affinity](https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/), [failover across pools](https://developers.cloudflare.com/load-balancing/understand-basics/adaptive-routing/#failover-across-pools), and [custom rules](https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/) are not supported by Spectrum.

  * UDP health checks are only available with public monitoring. TCP can be used with both public and private monitoring.




## Footnotes

  1. Within Cloudflare, pools represent your endpoints and how they are organized. As such, a pool can be a group of several endpoints, or you could also have only one endpoint (an origin server, for example) per pool. ↩

  2. A fallback pool is the pool of last resort. When all pools are disabled or unhealthy, this is where the load balancer will send traffic. ↩




[PreviousCloudflare Tunnel (published applications)](https://developers.cloudflare.com/load-balancing/additional-options/cloudflare-tunnel/)[NextPerform planned maintenance](https://developers.cloudflare.com/load-balancing/additional-options/planned-maintenance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/load-balancing/additional-options/spectrum.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
