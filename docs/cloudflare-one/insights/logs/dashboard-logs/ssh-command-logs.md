---
url: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/
title: SSH command logs \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:52.047570+00:00
---

# SSH command logs · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Insights](https://developers.cloudflare.com/cloudflare-one/insights/)[Logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/)

  4. /[Dashboard logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/)
  5. /SSH command logs



# SSH command logs

Last updated May 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesView SSH logsLog fieldsExport SSH logs with Logpush

SSH command logs record the commands that users run on infrastructure targets protected by [Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/). Use these logs to audit user activity on your SSH servers and investigate specific sessions.

To view SSH command logs, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Insights** > **Logs** > **SSH command logs**.

## Prerequisites

To generate SSH command logs, you must:

  1. Set up [Access for Infrastructure](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/) for your SSH servers.
  2. [Enable SSH command logging](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#ssh-command-logs) by uploading an encryption public key. Cloudflare uses this key to encrypt your logs so that only you can read their contents.



## View SSH logs

SSH command logs displayed in the dashboard are encrypted using the public key you provided during setup. The logs are not readable in the dashboard — you must download and decrypt them locally. To view the contents of the logs:

  1. In [Cloudflare One ↗︎](https://one.dash.cloudflare.com/), go to **Insights** > **Logs** > **SSH command logs**.
  2. Filter the logs using the name of your SSH application.
  3. Select the SSH session for which you want to export command logs.
  4. In the side panel, scroll down to **SSH logs** and select **Download**.
  5. Decrypt the log using the [SSH Logging CLI ↗︎](https://github.com/cloudflare/ssh-log-cli/) and the private key that corresponds to the public key you uploaded.



## Log fields

Field | Description  
---|---  
**Session ID** | Unique identifier for the SSH session.  
**User email** | Email address of the user who initiated the SSH session.  
**Target ID** | Identifier of the infrastructure target being accessed. Corresponds to the target you configured in Access for Infrastructure.  
**Client address** | Source IP address of the SSH connection.  
**Server address** | Destination IP address of the SSH server.  
**Session start datetime** | Timestamp when the SSH session started.  
**Session finish datetime** | Timestamp when the SSH session ended.  
**Program type** | Type of SSH program: `shell` (interactive terminal), `exec` (single command execution), `x11`, `direct-tcpip`, or `forwarded-tcpip`. Note that `x11`, `direct-tcpip`, and `forwarded-tcpip` correspond to SSH features that are [not currently supported](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#known-limitations) by Access for Infrastructure.  
**Payload** | Captured request/response data in [asciicast v2 ↗︎](https://docs.asciinema.org/manual/asciicast/v2/) format, a structured terminal recording format. Includes commands for `exec` programs.  
**Error** | SSH error message, if an error occurred during the session.  
  
## Export SSH logs with Logpush

Enterprise users can export SSH command logs to external storage or analysis destinations using [Logpush](https://developers.cloudflare.com/cloudflare-one/insights/logs/logpush/). Unlike dashboard logs, Logpush payloads are not encrypted with a customer-provided public key — secure access to your storage destination accordingly.

For a list of all available fields, refer to [SSH Logs](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/account/ssh_logs/).

[PreviousManage PII](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/manage-pii/)[NextSCIM provisioning logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/insights/logs/dashboard-logs/ssh-command-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
