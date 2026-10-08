---
url: https://developers.cloudflare.com/client-side-security/reference/script-statuses/
title: Script and connection statuses \u00b7 Client-side security docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:57.984981+00:00
---

# Script and connection statuses · Client-side security docs

> Source: https://developers.cloudflare.com/client-side-security/reference/script-statuses/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Client-side security](https://developers.cloudflare.com/client-side-security/)
  3. /Reference
  4. /Statuses



# Script and connection statuses

Last updated Apr 15, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/client-side-security/reference/script-statuses/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAvailable statuses

Cloudflare classifies scripts and connections (also known as resources) according to the following:

  * The number of times a script/connection was reported.
  * Whether the script/connection is considered malicious or not.



Use client-side security's dashboards to review the scripts loaded in your domain and the connections they make. For more information, refer to [Monitor resources and cookies](https://developers.cloudflare.com/client-side-security/detection/monitor-connections-scripts/).

## Available statuses

  * **Infrequent** : There are less than three reports for the script/connection. If there are no reports for a script/connection with _Infrequent_ status for five days, then Cloudflare will delete all the information about the script/connection. Scripts with _Infrequent_ status appear only in the All Reported Scripts dashboard, and connections with _Infrequent_ status appear only in the All Reported Connections dashboard.
  * **Active** : There are more than three reports for the script/connection.
  * **Inactive** : A previously active script/connection was not reported in the last seven days. If the script/connection is reported again later, its status will change back to _Active_. If the script/connection is not reported for 30 days, Cloudflare will delete all the information about it. Scripts with _Inactive_ status appear only in the All Reported Scripts dashboard, and connections with _Inactive_ status appear only in the All Reported Connections dashboard.



Note

All scripts and connections considered malicious will appear in the Monitors dashboard, regardless of their status.

Malicious script detection is only available to customers with Client-Side Security Advanced.

[PreviousConfiguration settings](https://developers.cloudflare.com/client-side-security/reference/settings/)[NextPCI DSS compliance](https://developers.cloudflare.com/client-side-security/reference/pci-dss/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/client-side-security/reference/script-statuses.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
