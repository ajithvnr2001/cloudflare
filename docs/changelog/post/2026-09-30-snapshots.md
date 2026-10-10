---
url: https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/
title: Snapshot and restore Container filesystem \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:29.925953+00:00
---

# Snapshot and restore Container filesystem · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)September 30, 2026

## Snapshot and restore Container filesystem

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) now support snapshot APIs in public beta for saving and restoring point-in-time filesystem state. Create a snapshot first, then pass it back to `start()` to restore files after container sleep, restart, or handoff to another Durable Object.

Use `snapshotContainer()` through the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/) to capture the full container filesystem. Create a snapshot from a running Container, store its handle, and pass that handle to `start()` when you restore it later:

src/index.jsjs
    
    
    import { DurableObject } from "cloudflare:workers";
    
    export class MyDurableObject extends DurableObject {
    	async saveSnapshot() {
    		// Create a snapshot from the running Container.
    		const containerSnapshot = await this.ctx.container.snapshotContainer({});
    
    		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
    	}
    
    	async restoreSnapshot() {
    		// Restore the saved snapshot later.
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
    	async saveSnapshot() {
    		// Create a snapshot from the running Container.
    		const containerSnapshot = await this.ctx.container.snapshotContainer({});
    
    		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
    	}
    
    	async restoreSnapshot() {
    		// Restore the saved snapshot later.
    		const containerSnapshot =
    			await this.ctx.storage.get<ContainerSnapshot>("containerSnapshot");
    
    		if (!containerSnapshot) {
    			return;
    		}
    
    		this.ctx.container.start({ containerSnapshot, enableInternet: false });
    	}
    }

Snapshots are only supported for Container applications that use the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy). Snapshots are immutable, so create a new snapshot to persist filesystem changes made after a restore.

For more information, refer to [Snapshots](https://developers.cloudflare.com/containers/guides/snapshots/) and the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/).
