---
url: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/
title: Configure link actions \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:36.785369+00:00
---

# Configure link actions · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)Settings

  4. /Detection settings
  5. /Configure link actions



# Configure link actions

Last updated Sep 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewLink actions settingsAdd patterns for URLs

You can configure how Email security handles links in emails.

Note

You can only configure link actions if you deploy Email security via [MX/Inline](https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment/).

To configure link actions:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Select **Email security**.
  3. Select **Settings** > **Link actions** > **View**.



You can configure **Link actions settings** , or **URL rewrite ignore patterns**.

## Link actions settings

To configure link actions, select **Configure**.

The dashboard will display **Open links evaluated as suspicious in a remote browser (Recommended)**. This option is turned on by default. Email security will also allow you to select message dispositions to open all the links for dispositioned emails in a remote browser.

Select one or more disposition, then select **Save**.

If **Open links evaluated as suspicious in a remote browser (Recommended)** is turned off, you can select **URL defang** or **No action** on each disposition. Select **Save** once you have completed the configuration.

When opening links, Email security will not allow you to:

  * [Copy (from remote to client)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)
  * [Paste (from client to remote)](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)
  * Use [keyboard](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)
  * [Print](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)
  * [Download files](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)
  * [Uploads files](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/)



## Add patterns for URLs

You can add patterns for URLs that should be rewritten.

  1. Under **URL rewrite ignore patterns** , select **Add a pattern**.
  2. Enter a valid IP, URL, or regular expression. You can enter up to 512 characters.
  3. Select **Save**.



To edit a pattern, go to the pattern you want to edit, select the three dots, then **Edit**. Once you have finished modifying the URL pattern, select **Save**.

To delete a pattern, go to the pattern you want to delete, select the three dots, then **Delete**.

[PreviousAuto-move events](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/auto-moves/)[NextConfigure text add-ons](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-text-add-ons/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/settings/detection-settings/configure-link-actions.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
