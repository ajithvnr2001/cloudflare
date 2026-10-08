---
url: https://developers.cloudflare.com/sandbox/1-0-preview/migrate/
title: Migrate from Sandbox SDK 0.x \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:32.821092+00:00
---

# Migrate from Sandbox SDK 0.x · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/1-0-preview/migrate/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Sandbox SDK 0.x](https://developers.cloudflare.com/sandbox/sdk/)
  4. /Migrate to 1.0



# Migrate from Sandbox SDK 0.x

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/1-0-preview/migrate/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSupport for Sandbox SDK 0.xPlan for a one-way switchFind the pages your application needsStay on 0.x until you moveRelated resources

To move an application from Sandbox SDK 0.x to 1.0, replace the `Sandbox` class with a Durable Object class that you write. Then replace each 0.x feature that your application uses. Your class starts a container that uses the [Durable Object scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy), which is in public beta. For the reasons behind these changes, refer to [Changes in Sandbox SDK 1.0](https://developers.cloudflare.com/sandbox/sdk/migrate/changes-in-1-0/).

Sandboxes on 1.0 start faster. On a prepared image, the median time from `start()` to the first command is under 600 ms, compared with about 4 s on 0.x. Each `start()` call also chooses its own image, and a deploy does not restart running sandboxes.

## Support for Sandbox SDK 0.x

Sandbox SDK 0.x receives bug and security fixes until 2026-12-31, and no new features. After that date, deployed 0.x applications keep running, and `@cloudflare/sandbox` 0.x stays on npm.

The migration pages compare 1.0 with 0.12, the last 0.x release. If your application uses an earlier release, upgrade to `@cloudflare/sandbox` 0.12.10 and the `docker.io/cloudflare/sandbox:0.12.10` image first.

## Plan for a one-way switch

Caution

You cannot undo the deploy that moves your class to `scheduling_policy: "durable_object"`. After that deploy, 0.x code cannot start containers for the class, even after `wrangler rollback`.

You can move every sandbox in one deploy, or run a 1.0 class next to the 0.x class and move sandboxes one at a time. Rehearse either way on a staging Worker first. To choose a way and prepare for the deploy, refer to [Plan the move to Sandbox SDK 1.0](https://developers.cloudflare.com/sandbox/sdk/migrate/plan-the-move/).

## Find the pages your application needs

Every application needs the first two pages in the following table. To find the others, search your source directory for 0.x calls:
    
    
    grep -rhow \
    	-e getSandbox -e sleepAfter -e keepAlive \
    	-e envVars -e onStart -e onStop \
    	-e onActivityExpired -e createSession \
    	-e readFile -e writeFile -e listFiles -e watch \
    	-e startProcess -e streamProcessLogs \
    	-e exposePort -e proxyToSandbox -e wsConnect \
    	-e tunnels -e terminal -e SandboxAddon \
    	-e outboundByHost -e setOutboundHandler \
    	-e allowedHosts -e deniedHosts -e gitCheckout \
    	-e enableInternet -e interceptHttps \
    	-e mountBucket -e createBackup -e restoreBackup \
    	-e runCode -e createCodeContext \
    	-e sandbox/opencode -e sandbox/openai \
    	-e sandbox/bridge -e WarmPool \
    	src | sort | uniq -c

The command prints each name it finds and how often it appears. Some names, such as `watch` and `terminal`, can also match code that does not use the SDK. The 0.12 `codex-app-server` template prints:
    
    
          1 enableInternet
          6 getSandbox
          1 gitCheckout
          2 interceptHttps
          1 outboundByHost
          2 proxyToSandbox
          1 readFile
          2 sleepAfter
          1 startProcess
          1 writeFile

Each name leads to one page:

0.x code | Page | Work in 1.0  
---|---|---  
`Sandbox`, `getSandbox()`, `sleepAfter`, `keepAlive`, `envVars`, `onStart()`, `onStop()`, `onActivityExpired()` | [Replace the Sandbox class](https://developers.cloudflare.com/sandbox/sdk/migrate/replace-the-sandbox-class/) | Write the class  
`exec()`, `execStream()`, `createSession()` | [Change command calls](https://developers.cloudflare.com/sandbox/sdk/migrate/commands/) | Change calls  
`readFile()`, `writeFile()`, `listFiles()`, `watch()` | [Change file calls](https://developers.cloudflare.com/sandbox/sdk/migrate/files/) | Change calls  
`startProcess()`, `streamProcessLogs()` | [Move background processes](https://developers.cloudflare.com/sandbox/sdk/migrate/background-processes/) | Add code  
`exposePort()`, `proxyToSandbox()`, `wsConnect()` | [Move preview URLs](https://developers.cloudflare.com/sandbox/sdk/migrate/preview-urls/) | Add code  
`tunnels` | [Move tunnels](https://developers.cloudflare.com/sandbox/sdk/migrate/tunnels/) | Add code  
`terminal()`, `SandboxAddon` | [Move browser terminals](https://developers.cloudflare.com/sandbox/sdk/migrate/terminals/) | Add code  
`outboundByHost`, `setOutboundHandler()`, `allowedHosts`, `deniedHosts`, `enableInternet`, `interceptHttps`, `gitCheckout()` | [Move outbound rules](https://developers.cloudflare.com/sandbox/sdk/migrate/outbound-traffic/) | Add code  
`mountBucket()` | [Move bucket mounts](https://developers.cloudflare.com/sandbox/sdk/migrate/bucket-mounts/) | Change calls  
`createBackup()`, `restoreBackup()` | [Move backups](https://developers.cloudflare.com/sandbox/sdk/migrate/backups/) | Add code  
`runCode()`, `createCodeContext()` | [Replace the code interpreter](https://developers.cloudflare.com/sandbox/sdk/migrate/code-interpreter/) | Add code  
`sandbox/opencode`, `sandbox/openai`, `sandbox/bridge`, `WarmPool` | [Move other 0.x features](https://developers.cloudflare.com/sandbox/sdk/migrate/other-features/) | Add or remove code  
`FROM docker:dind-rootless` in a `Dockerfile` | [Run Docker inside the sandbox](https://developers.cloudflare.com/sandbox/sdk/migrate/other-features/#run-docker-inside-the-sandbox) | Change the image  
  
Work through the pages on your staging Worker, test it with your own checks, and then deploy to production. For every 0.x API and its replacement, including features with no equivalent in 1.0, refer to the [API map](https://developers.cloudflare.com/sandbox/sdk/migrate/api-map/).

## Stay on 0.x until you move

Until you move, pin `@cloudflare/sandbox` to `0.12.10` and your image to `docker.io/cloudflare/sandbox:0.12.10`. The [deprecation changelog entry](https://developers.cloudflare.com/changelog/post/2026-06-09-deprecating-sandbox-sdk-features/) lists 0.x features to avoid in new work: the HTTP and WebSocket transports, `exposePort()`, default sessions, and separate streaming methods.

## Related resources

  * [Changes in Sandbox SDK 1.0](https://developers.cloudflare.com/sandbox/sdk/migrate/changes-in-1-0/)
  * [API map](https://developers.cloudflare.com/sandbox/sdk/migrate/api-map/)
  * [`@cloudflare/sandbox` reference](https://developers.cloudflare.com/sandbox/reference/)
  * [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/)



[PreviousOverview](https://developers.cloudflare.com/sandbox/sdk/)[NextChanges in 1.0](https://developers.cloudflare.com/sandbox/sdk/migrate/changes-in-1-0/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/sdk/migrate/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
