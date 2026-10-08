---
url: https://developers.cloudflare.com/agent-lee/take-home-code/
title: Export generated code \u00b7 Agent Lee docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:05.169917+00:00
---

# Export generated code · Agent Lee docs

> Source: https://developers.cloudflare.com/agent-lee/take-home-code/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agent Lee](https://developers.cloudflare.com/agent-lee/)
  3. /Export generated code



# Export generated code

Last updated Sep 24, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agent-lee/take-home-code/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksExport and clone your codeSecurity and privacyLimitationsRelated resources

Take the source code Agent Lee generates with you by exporting it to a temporary, Git-cloneable repository.

Beta

Code export is part of the Agent Lee beta. Behaviors and limits described here may change.

When Agent Lee generates a small project for you — for example, a starter static site or a Worker — you can export the source so you can keep working on it locally. Agent Lee packages the generated files into a temporary repository and gives you a one-time command to clone it to your machine.

This is a **take-home** flow: the repository is short-lived and lives in Cloudflare-managed storage, not in your account. It is meant for getting generated code onto your own machine, after which you push it to a Git host of your choice. You do not need to connect a GitHub or GitLab account.

## How it works

  * **Temporary repository.** When you export, Agent Lee writes the generated files to a repository that expires about 36 hours after it is created. Once it expires, the export card disables the copy button and the code can no longer be cloned.
  * **On-demand clone command.** Agent Lee does not put a clone command or credential in the chat transcript. Instead, the export card shows a **Copy clone command** button that fetches a fresh command when you select it. The command embeds a read credential that is valid for about one hour.
  * **Export card.** The card shows the project name, the list of exported files, and a countdown to expiry so you know how long you have to clone.



## Export and clone your code

  1. Ask Agent Lee to build something that produces code, then ask it to export the code. For example: "Export this project so I can clone it."

  2. In the export card that appears, review the file list and the expiry countdown.

  3. Select **Copy clone command**. Agent Lee fetches a fresh command and copies it to your clipboard.

  4. Paste the command into your terminal and run it. What you copied is already a complete `git clone` invocation, so do not add anything to it. It has the following shape, where the credential is embedded in the remote URL and the final argument is the local directory to create:
         
         git clone https://<credential>@<host>/<repository>.git <project-name>

  5. Change into the new directory, point the repository at your own Git host, and push it there to keep it:
         
         cd <project-name>
         git remote set-url origin https://your-git-host.example/you/your-repo.git
         git push -u origin main




## Security and privacy

  * **No credential in chat.** The clone command and its read credential are delivered only when you select **Copy clone command** — never in the message text, conversation history, or model context. Agent Lee will not type the clone command into the chat, so do not ask it to.
  * **Short-lived access.** The read credential expires about an hour after it is issued. If the command stops working before the repository expires, return to the export card and copy a fresh one.
  * **Nothing is written to your account.** The temporary repository lives in Cloudflare-managed storage. Agent Lee does not create repositories, tokens, or other resources in your Cloudflare account to perform an export.
  * **Automatic cleanup.** The temporary repository is deleted automatically once it expires. Clone and push to your own host before then.



## Limitations

  * Exported repositories are temporary and are not backed up. Once a repository expires, it cannot be recovered.

  * The clone credential is read-only and single-purpose. You cannot push back to the temporary repository — push to your own Git host instead.

  * Code export is intended for small, self-contained projects that Agent Lee generates during a conversation. A single export can include:

    * up to 50 files
    * up to 100 KB per file
    * up to 2 MB in total

Agent Lee tells you if a project is too large to export. If that happens, ask it for a smaller subset of the project.




## Related resources

  * [Agent Lee overview](https://developers.cloudflare.com/agent-lee/)
  * [Workers](https://developers.cloudflare.com/workers/)



[PreviousOverview](https://developers.cloudflare.com/agent-lee/)[NextManage access and permissions](https://developers.cloudflare.com/agent-lee/manage-access/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agent-lee/take-home-code.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
