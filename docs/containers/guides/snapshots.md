---
url: https://developers.cloudflare.com/containers/guides/snapshots/
title: Use snapshots \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:36.239454+00:00
---

# Use snapshots · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/guides/snapshots/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Guides
  4. /Use snapshots



# Use snapshots

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/guides/snapshots/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCreate a container snapshotRestore a container snapshotUnderstand retentionRelated resources

Snapshots let you save point-in-time filesystem state from a running [Container](https://developers.cloudflare.com/containers/). The examples on this page use the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/).

Scheduling policy requirement

Snapshots are only supported by Container applications that use the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy). Applications that use the `default` scheduling policy cannot create or restore snapshots.

## Create a container snapshot

Use `snapshotContainer()` to capture the full container filesystem. Snapshots are immutable. If you restore a snapshot and then change files, create a new snapshot to persist those changes.

Snapshot image compatibility

Snapshots capture the Container's complete filesystem state, but not its memory or running processes. A snapshot is tied to the Container image version it was created from and is not portable to a different image. After updating the image, create a new snapshot from a Container running that image.

The returned snapshot handle is a plain data object. You can store it and restore it later, including from another Durable Object:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async saveContainer() {
    		const containerSnapshot = await this.ctx.container.snapshotContainer({
    			name: "before-upgrade",
    		});
    
    		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async saveContainer() {
    		const containerSnapshot = await this.ctx.container.snapshotContainer({
    			name: "before-upgrade",
    		});
    
    		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
    	}
    }

## Restore a container snapshot

Load the saved snapshot handle. Then, pass it to `this.ctx.container.start()` when you start another container:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async restoreContainer() {
    		const containerSnapshot = await this.ctx.storage.get("containerSnapshot");
    
    		if (!containerSnapshot) {
    			return;
    		}
    
    		this.ctx.container.start({ containerSnapshot, enableInternet: false });
    	}
    }

src/index.tsts
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async restoreContainer() {
    		const containerSnapshot =
    			await this.ctx.storage.get<ContainerSnapshot>("containerSnapshot");
    
    		if (!containerSnapshot) {
    			return;
    		}
    
    		this.ctx.container.start({ containerSnapshot, enableInternet: false });
    	}
    }

## Understand retention

Snapshots have an implicit [30-day time-to-live](https://developers.cloudflare.com/containers/platform/limits/#snapshot-limits). Each restore refreshes that time-to-live.

You cannot set a custom time-to-live yet.

## Related resources

  * [Scheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/) \- Choose how Container instances are configured and updated
  * [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/) \- Full `ctx.container` API reference
  * [Lifecycle of a Container](https://developers.cloudflare.com/containers/concepts/architecture/) \- Understand startup, sleep, and shutdown behavior



[PreviousSSH](https://developers.cloudflare.com/containers/guides/ssh/)[NextMigrate from the Container class to the Durable Object Container API](https://developers.cloudflare.com/containers/guides/migrate-to-durable-object-container-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/guides/snapshots.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
