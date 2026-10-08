---
url: https://developers.cloudflare.com/containers/guides/ssh/
title: SSH \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:36.388543+00:00
---

# SSH · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/guides/ssh/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Guides
  4. /SSH



# SSH

Last updated Aug 28, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/guides/ssh/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewConfigure SSHConnect with WranglerUse as SSH proxyProcess visibility

Anyone with write access to a Container can SSH into it with Wrangler as long as a matching public key is listed in `authorized_keys`.

SSH does not expose a publicly accessible port on the Container. The only way to connect is through Wrangler with [`wrangler containers ssh`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-ssh), which authenticates against your Cloudflare account.

## Configure SSH

SSH can be configured in your [Container's configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) with the `ssh` and `authorized_keys` properties. Only the `ssh-ed25519` key type is supported.

The `ssh.enabled` property only controls whether you can SSH into a Container through Wrangler. It defaults to `true`. Set it to `false` to disable SSH access completely.

## Connect with Wrangler

To SSH into a Container with Wrangler, add an `ssh-ed25519` public key to `authorized_keys` in your Container configuration. The following example shows a basic configuration:
    
    
    {
    	"containers": [
    		{
    			// other options here...
    			"authorized_keys": [
    				{
    					"name": "<NAME>",
    					"public_key": "<YOUR_PUBLIC_KEY_HERE>"
    				}
    			]
    		}
    	]
    }
    
    
    [[containers]]
    [[containers.authorized_keys]]
    name = "<NAME>"
    public_key = "<YOUR_PUBLIC_KEY_HERE>"

For more information on configuring SSH, refer to [SSH configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#ssh).

Find the instance ID for your Container by running [`wrangler containers instances`](https://developers.cloudflare.com/workers/wrangler/commands/containers/#containers-instances) or in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/containers). The instance you want to SSH into must be running. SSH will not start a stopped Container, and an active SSH connection alone will not keep a Container alive.

Once SSH is configured and the Container is running, open the SSH connection with:
    
    
    wrangler containers ssh <INSTANCE_ID>

## Use as SSH proxy

You can use `wrangler containers ssh` as an OpenSSH `ProxyCommand`. This lets your local SSH client connect through Wrangler.
    
    
    ssh -o ProxyCommand="wrangler containers ssh %h" cloudchamber@<INSTANCE_ID>

When used this way, Wrangler pipes standard input and output to the SSH server in the running Container. You can also pass `--stdio` to force this mode.

## Process visibility

Without the [`containers_pid_namespace`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#use-an-isolated-pid-namespace-for-containers) compatibility flag, all processes inside the VM are visible when you connect to your Container through SSH. This flag is turned on by default for Workers with a [compatibility date](https://developers.cloudflare.com/workers/configuration/compatibility-dates/) of `2026-04-01` or later.

[PreviousImage Management](https://developers.cloudflare.com/containers/guides/image-management/)[NextUse snapshots](https://developers.cloudflare.com/containers/guides/snapshots/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/guides/ssh.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
