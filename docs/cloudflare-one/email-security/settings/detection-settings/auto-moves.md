---
url: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/auto-moves/
title: Auto-move events \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:36.443934+00:00
---

# Auto-move events · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/auto-moves/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)Settings

  4. /Detection settings
  5. /Auto-move events



# Auto-move events

Last updated Sep 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/auto-moves/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Auto-moves allow you to automatically move emails out of your inbox based on a [disposition](https://developers.cloudflare.com/cloudflare-one/email-security/reference/dispositions-and-attributes/) that Email security assigns to each message (for example, malicious, spam, or spoof).

Use auto-moves to enforce email security policy without relying on end users to identify and act on threats themselves. After you configure auto-moves, Email security handles flagged messages according to the action you choose for each disposition.

To configure auto-move events:

  1. Log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/).
  2. Select **Email security**.
  3. Select **Settings** > **Auto-moves** > **View**.
  4. Select **Configure**.
  5. For each disposition (malicious, spam, bulk, suspicious, spoof), choose what happens to matching emails: 
     * **Soft delete - user recoverable** : Moves the message to the user's **Recoverable Items - Deleted** folder. The user can still find and restore the message. This option is only available for Microsoft 365 customers. Refer to [Microsoft 365 Exchange data deletion ↗︎](https://learn.microsoft.com/en-us/compliance/assurance/assurance-exchange-online-data-deletion) for more information.
     * **Hard delete - admin recoverable** : Removes the message from the user's inbox entirely. Only an administrator can recover it.
     * **Move to trash** : Moves the message to the user's trash or deleted items folder. This option is only available for Google Workspace users.
     * **Move to junk** : Moves the message to the user's junk or spam folder.
     * **No action** : Leaves the message where it is. Email security still records the disposition, but does not move the message.
  6. Select **Save**.



[PreviousImpersonation registry](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/impersonation-registry/)[NextConfigure link actions](https://developers.cloudflare.com/cloudflare-one/email-security/settings/detection-settings/configure-link-actions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/email-security/settings/detection-settings/auto-moves.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
