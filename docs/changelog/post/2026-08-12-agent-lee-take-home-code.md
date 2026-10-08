---
url: https://developers.cloudflare.com/changelog/post/2026-08-12-agent-lee-take-home-code/
title: Export the code Agent Lee generates \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:07:07.820635+00:00
---

# Export the code Agent Lee generates · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-08-12-agent-lee-take-home-code/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)August 12, 2026

## Export the code Agent Lee generates

[Agent Lee](https://developers.cloudflare.com/agent-lee/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-12-agent-lee-take-home-code/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

When Agent Lee generates a project for you — a starter static site, a Worker, a scaffold — you can now take the source with you. Agent Lee packages the generated files into a temporary repository and gives you a one-time command to clone it to your own machine.

Previously, generated code lived only in the conversation. You had to copy files out of the chat by hand, which is tedious for anything larger than a single snippet and easy to get wrong.

#### How it works

  * Ask Agent Lee to build something, then ask it to export the code.
  * An export card appears listing the files and a countdown to expiry.
  * Select **Copy clone command**. Agent Lee fetches a fresh command and copies it to your clipboard.
  * Run it in your terminal, then point the repository at your own Git host and push:


    
    
    git remote set-url origin https://your-git-host.example/you/your-repo.git
    git push -u origin main

#### Good to know

  * **The export is temporary.** The repository expires about 36 hours after it is created and is then deleted automatically. The clone credential expires about an hour after it is issued. Clone promptly, then push to a repository you control.
  * **No credential appears in the chat.** The clone command and its read-only credential are delivered only when you select **Copy clone command** — never in the message text or conversation history.
  * **Nothing is written to your account.** The temporary repository lives in Cloudflare-managed storage, and connecting a GitHub or GitLab account is not required.
  * **Intended for small projects.** An export can include up to 50 files, up to 100 KB per file and 2 MB in total.



Agent Lee remains in beta. Features and behaviors may change as the product evolves.

For details, see [Export generated code](https://developers.cloudflare.com/agent-lee/take-home-code/).
