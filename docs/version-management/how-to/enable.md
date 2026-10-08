---
url: https://developers.cloudflare.com/version-management/how-to/enable/
title: Enable version management \u00b7 Cloudflare Version Management docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:16:14.797898+00:00
---

# Enable version management · Cloudflare Version Management docs

> Source: https://developers.cloudflare.com/version-management/how-to/enable/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Version Management](https://developers.cloudflare.com/version-management/)
  3. /How to
  4. /Enable



# Enable

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/version-management/how-to/enable/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewDisable Version Management

By default, Version Management is not enabled on a zone.

To enable [Version Management ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/versioning):

  1. Log in to the Cloudflare dashboard.

[ Go to **Account home** ↗ ](https://dash.cloudflare.com/?to=/:account/home)
  2. Select your account and zone.

  3. Go to **Version Management**.

  4. Select **Enable versioning**.




Note

If you cannot enable Version Management, make sure your zone, account, and user meet the [requirements](https://developers.cloudflare.com/version-management/#requirements).

Once you [enable](https://developers.cloudflare.com/version-management/how-to/enable/) Version Management, Cloudflare will automatically create:

  * **Version Zero** , think about this as the configuration of your current zone. Once default environments are created, Version Zero is automatically deployed to them, guaranteeing no disruption in your live traffic. This Version is also permanently editable. In case you decide to disable Zone Versioning, Version Zero will become your zone again.
  * **Global Configuration** , you can find all the configurations here that are not supported by Version Management.



Important

Any changes made to the **Global Configuration** will immediately apply to your zone and all versions of your zone, affecting live traffic.

On the Environments page, you can create default environments for **Production** , **Staging** , and **Development**.

## Disable Version Management

Caution

When you disable Zone Versioning, all your zone configurations will revert to those in your **Version Zero**.

When deleting the production environment, all traffic will default to Version 0. The action of deleting an environment does not impact any versions configuration.

To disable Zone Versioning:

  1. Confirm that **Version Zero** has the correct configurations for your zone:

     1. Use the [comparison feature](https://developers.cloudflare.com/version-management/how-to/compare-versions/) to view the differences between your current **Production** version and **Version Zero**.

     2. If there are differences, make changes to **Version Zero** so it matches your current **Production** version.

     3. [Promote](https://developers.cloudflare.com/version-management/how-to/environments/#promote-a-version) **Version Zero** to your **Production** environment.

     4. Confirm that your new **Production** environment functions as expected.

  2. Send a `GET` request to the `/zones/{zone_id}/environments` endpoint.
         
         curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/environments" \
         --header "X-Auth-Email: <EMAIL>" \
         --header "X-Auth-Key: <API_KEY>"

In the response, save the following values:

     * The environment `ref` of every rule
  3. Using the `ref` of those environments, send a `DELETE` request to the `/zones/{zone_id}/environments/{ref}` endpoint for each environment.
         
         curl --request DELETE \
         "https://api.cloudflare.com/client/v4/zones/{zone_id}/environments/{ref}" \
         --header "X-Auth-Email: <EMAIL>" \
         --header "X-Auth-Key: <API_KEY>"

  4. Then, send a `GET` request to find all HTTP applications (or versions of your zone).
         
         curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/http_applications" \
         --header "X-Auth-Email: <EMAIL>" \
         --header "X-Auth-Key: <API_KEY>"

Save the `id` of each HTTP application.

  5. Using the `id` of those HTTP applications, send `DELETE` requests for every application.
         
         curl --request DELETE \
         "https://api.cloudflare.com/client/v4/zones/{zone_id}/http_applications/{http_application_id}" \
         --header "X-Auth-Email: <EMAIL>" \
         --header "X-Auth-Key: <API_KEY>"




Once all these steps are completed, Zone Versioning will go back to its original landing page.

[PreviousGet started](https://developers.cloudflare.com/version-management/get-started/)[NextManage environments](https://developers.cloudflare.com/version-management/how-to/environments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/version-management/how-to/enable.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
