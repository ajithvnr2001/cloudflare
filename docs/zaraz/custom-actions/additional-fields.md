---
url: https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/
title: Additional fields \u00b7 Cloudflare Zaraz docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:17.845639+00:00
---

# Additional fields · Cloudflare Zaraz docs

> Source: https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Zaraz](https://developers.cloudflare.com/zaraz/)
  3. /[Custom actions](https://developers.cloudflare.com/zaraz/custom-actions/)
  4. /Additional fields



# Additional fields

Last updated Apr 16, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/zaraz/custom-actions/additional-fields/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAdd an additional field to a specific actionAdd an additional field to all actions in a tool

Some tools supported by Zaraz let you add fields in addition to the required field. Fields can usually be added either to a specific action, or to all the action within a tool, by adding the field as a **Default Field**.

## Add an additional field to a specific action

Adding an additional field to an action will attach it to this action only, and will not affect your other actions.

  1. In the Cloudflare dashboard, go to the **Tag setup** page.

[ Go to **Tag setup** ↗ ](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)
  2. Select **Tools Configuration** > **Third-party tools**.

  3. Locate the third-party tool with the action you want to add the additional field to, and select **Edit**.

  4. Select the action you wish to modify.

  5. Select **Add Field**.

  6. Choose the desired field from the drop-down menu and select **Add**.

  7. Enter the value you wish to pass to the action.

  8. Select **Save**.




The new field will now be used in this event.

## Add an additional field to all actions in a tool

Adding an additional field to the tool sets it as a default field for all of the tool actions. It is the same as adding it to every action in the tool.

  1. In the Cloudflare dashboard, go to the **Tag setup** page.

[ Go to **Tag setup** ↗ ](https://dash.cloudflare.com/?to=/:account/tag-management/zaraz)
  2. Select **Tools Configuration** > **Third-party tools**.

  3. Locate the third-party tool where you want to add the field, and select **Edit**.

  4. Select **Settings** > **Add Field**.

  5. Choose the desired field from the drop-down menu, and select **Add**.

  6. Enter the value you wish to pass to all the actions in the tool.

  7. Select **Save**.




The new field will now be attached to every action that belongs to the tool.

[PreviousCreate an action](https://developers.cloudflare.com/zaraz/custom-actions/create-action/)[NextEdit tools and actions](https://developers.cloudflare.com/zaraz/custom-actions/edit-tools-and-actions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/zaraz/custom-actions/additional-fields.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
