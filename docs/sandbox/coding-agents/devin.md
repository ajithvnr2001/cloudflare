---
url: https://developers.cloudflare.com/sandbox/coding-agents/devin/
title: Run Devin in a sandbox \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:39:26.680043+00:00
---

# Run Devin in a sandbox · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/coding-agents/devin/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Coding agents](https://developers.cloudflare.com/sandbox/coding-agents/)
  4. /Devin



# Run Devin in a sandbox

Last updated Oct 9, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites Get your Devin credentialsDeploy with one clickCustomize and deploy manuallyRun a Devin sessionHow the template runs sessionsSecurityRelated resources

[Devin ↗︎](https://docs.devin.ai/cloud/outposts/overview) runs its agent loop in its own service. Each session works on a machine where Devin runs commands, edits files, and opens a browser. A Devin Outpost moves that machine to infrastructure that you choose. The Devin Outpost template runs each session in its own Linux sandbox: a [Container](https://developers.cloudflare.com/containers/) that one Durable Object starts for that session.

## Prerequisites

You need:

  * A Devin Enterprise organization with permission to manage outposts and service users
  * A Cloudflare account on the Workers Paid plan with access to Containers
  * For manual deployment, [Node.js 24 ↗︎](https://nodejs.org/) and a running [Docker ↗︎](https://www.docker.com/) daemon



### Get your Devin credentials

  1. Open your Devin organization outpost settings. In this URL, replace both occurrences of `my-org` with your organization slug:
         
         https://my-org.devinenterprise.com/org/my-org/settings/enterprise-environment?tab=outposts

  2. Create or select an outpost, and copy its outpost ID for `DEVIN_OUTPOST_ID`.

  3. For `DEVIN_API_TOKEN`, use a Devin service-user token with the **Run outpost workers** permission.




For more information about outposts, refer to the [Devin Outposts overview ↗︎](https://docs.devin.ai/cloud/outposts/overview).

## Deploy with one click

The **Deploy to Cloudflare** button creates the Worker, the cron trigger, the Durable Object namespace, and the container application.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/sandbox-sdk/tree/main/templates/devin)

Enter these values when the deployment flow prompts for them:

Variable | Value  
---|---  
`DEVIN_OUTPOST_ID` | Your Devin Outpost ID  
`DEVIN_API_TOKEN` | A Devin service-user token with the **Run outpost workers** permission  
  
After the deployment finishes, select your outpost from the **Virtual environment** menu when you create a Devin session.

## Customize and deploy manually

Deploy manually when you need to add dependencies, tools, or environment variables to the container image.

  1. Create a project from the Devin Outpost template:

npmyarnpnpm
         
         npm create cloudflare@latest -- cloudflare-devin-outpost --template=cloudflare/sandbox-sdk/templates/devin
         
         yarn create cloudflare cloudflare-devin-outpost --template=cloudflare/sandbox-sdk/templates/devin
         
         pnpm create cloudflare@latest cloudflare-devin-outpost --template=cloudflare/sandbox-sdk/templates/devin

  2. Go to the project directory and log in to your Cloudflare account:
         
         cd cloudflare-devin-outpost
         npx wrangler login

  3. In `wrangler.jsonc`, replace the empty `DEVIN_OUTPOST_ID` value with your outpost ID.

The default `DEVIN_API_URL` is `https://api.devin.ai/opbeta`. Change this value only if your Devin environment uses another API URL.

  4. Store your Devin API token as a Worker secret:
         
         npx wrangler secret put DEVIN_API_TOKEN

Enter your service-user token when Wrangler prompts you. Do not add the token to `wrangler.jsonc`.

  5. Deploy the Worker and container:
         
         npm run deploy

Wrangler builds the container image and deploys the Worker, the container application, and the cron trigger.

  6. Check the deployment with the Worker URL from the Wrangler output:
         
         curl https://<YOUR_WORKER>.workers.dev/

The Worker returns:
         
         {
         	"service": "devin-outpost",
         	"status": "ok"
         }




## Run a Devin session

In Devin, create a session and select your outpost from the **Virtual environment** menu. The Worker checks for new sessions every 10 seconds by default, so the sandbox for the session starts shortly after you create it.

## How the template runs sessions

A cron trigger runs the Worker once a minute. During each run, the Worker asks Devin for the sessions of your outpost every 10 seconds, or every `DEVIN_RECONCILE_INTERVAL_MS` milliseconds if you set that variable. The Worker sends the status of each session to the Durable Object for that session:

Devin status | What the template does  
---|---  
`pending`, `running` | Starts the sandbox for the session if it is not running, from its snapshot if it has one.  
`suspended` | Waits for the Devin CLI to exit, saves a snapshot of the sandbox, then stops it.  
`terminated` | Stops the sandbox and forgets its snapshot.  
  
The Durable Object only starts and stops its container. Inside the sandbox, the Devin CLI (`devin worker start`) claims the session and runs it.

Your Worker connects to Devin on a cron trigger and lists sessions. It sends each session to its own Durable Object, which starts and stops a container. The Devin CLI in the container connects to Devin, claims the session, and runs it. Every connection to Devin starts on Cloudflare, so nothing connects in.

When Devin suspends a session, the Devin CLI exits. The sandbox keeps running until the Durable Object saves a snapshot of its disk. When the session continues, the sandbox starts from that snapshot and the Devin CLI claims the session again. The snapshot keeps the files and installed packages of the session. It does not keep running processes. If the Devin CLI exits while the session is still running, the template saves a snapshot and starts a new sandbox from it.

For more information, refer to [Save and restore a sandbox with snapshots](https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/).

Note

The template saves a snapshot only after the Devin CLI exits. If a sandbox stops before then, the session continues from its previous snapshot, or from the image if it has none. The Worker API cannot delete snapshots, so the snapshot of a terminated session stays in your account.

## Security

Each session runs in its own container and does not share files or processes with other sessions. Inside the container, Devin runs as root, can reach the Internet, and holds the Devin API token. Code that runs in a session can read that token. Deploy a separate outpost for each group of users that must not share access.

For more information, refer to [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/).

## Related resources

  * [Devin Outposts overview ↗︎](https://docs.devin.ai/cloud/outposts/overview)
  * [Devin Outpost template ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/templates/devin)
  * [Containers](https://developers.cloudflare.com/containers/)
  * [Save and restore a sandbox with snapshots](https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/)



[PreviousPi](https://developers.cloudflare.com/sandbox/coding-agents/pi/)[NextCursor](https://developers.cloudflare.com/sandbox/coding-agents/cursor/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/coding-agents/devin.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
