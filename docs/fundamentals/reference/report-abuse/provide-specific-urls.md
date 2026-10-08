---
url: https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/
title: Providing specific URLs - Report abuse \u00b7 Cloudflare Fundamentals docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:26.767849+00:00
---

# Providing specific URLs - Report abuse · Cloudflare Fundamentals docs

> Source: https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)
  3. /…

Reference

  4. /[Abuse](https://developers.cloudflare.com/fundamentals/reference/report-abuse/)
  5. /Providing specific URLs



# Providing specific URLs

Last updated Apr 20, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/fundamentals/reference/report-abuse/provide-specific-urls/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewGet the URL for specific contentSubmitting the abuse report

If you are [submitting an abuse report ↗︎](https://abuse.cloudflare.com) to Cloudflare because our IP address appears in the WHOIS and DNS records for a website, it is very likely that the website is one of millions of websites that use our pass-through security and content distribution network (CDN) services. Because assets on the same website may be hosted by different providers, it is important that you submit the URL for that specific asset to enable appropriate action. This guide will teach you how to identify URLs for specific video or images on a webpage.

## Get the URL for specific content

To get the URL for a specific piece of content on a webpage:

  1. Open your web browser (Google Chrome, Safari, Firefox, Edge).

  2. Go to the web page you want to report.

  3. Right click on the content you wish to report (often a video or image).

  4. Select **Inspect Element**.

  5. In the **DevTools** panel, look for the **src** attribute in the selected the image, video, or iFrame. ![Look for the URL in the src attribute of the video or image](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1268,height=322,format=webp/_astro/identify-url.o_PP6jZ2.png)

  6. Copy the URL.




Providing the most specific and helpful URL enables Cloudflare to correctly identify any services it may be providing with respect to that content.

## Submitting the abuse report

Once you have identified the URL for the specific asset, you can [submit an abuse report ↗︎](https://abuse.cloudflare.com) through Cloudflare's online abuse reporting process.

You can learn more about the process, and what you can expect from Cloudflare in response to such abuse reports, from [our abuse policy ↗︎](https://www.cloudflare.com/trust-hub/reporting-abuse/).

[PreviousComplaint types](https://developers.cloudflare.com/fundamentals/reference/report-abuse/complaint-types/)[NextCustomer abuse report obligations](https://developers.cloudflare.com/fundamentals/reference/report-abuse/abuse-report-obligations/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/fundamentals/reference/report-abuse/provide-specific-urls.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
