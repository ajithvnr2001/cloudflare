---
url: https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/
title: Save and restore a sandbox with snapshots \u00b7 Cloudflare Sandboxes docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:19.200213+00:00
---

# Save and restore a sandbox with snapshots · Cloudflare Sandboxes docs

> Source: https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Sandboxes](https://developers.cloudflare.com/sandbox/)
  3. /[Work with files](https://developers.cloudflare.com/sandbox/files/)
  4. /Save and restore a workspace



# Save and restore a sandbox with snapshots

Last updated Sep 30, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/sandbox/files/save-and-restore-a-workspace/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesSave and restore a sandboxCopy a sandboxStart a sandbox overRelated resources

A Durable Object saves the filesystem of a sandbox as a Container snapshot, stores the snapshot ID, and starts the next instance from the snapshot. In this example, the sandbox keeps a notes file in `/workspace`.

Public beta

Container snapshots are in public beta. Features and behavior may change.

## Prerequisites

  * A Worker with a Durable Object that starts a container with the [Durable Object scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy). To create one, refer to [Run a Linux command](https://developers.cloudflare.com/sandbox/get-started/).



## Save and restore a sandbox

  1. Add an inactivity timeout to your Durable Object. The constructor sets the timeout again when a restarted Durable Object finds the container running:

src/index.tsts
         
         const INACTIVITY_TIMEOUT_MS = 10 * 60 * 1000;
         
         export class MyContainer extends DurableObject<Env> {
         	constructor(ctx: DurableObjectState, env: Env) {
         		super(ctx, env);
         		const container = ctx.container;
         		if (container?.running) {
         			void ctx.blockConcurrencyWhile(() =>
         				container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS),
         			);
         		}
         	}
         }

Then start the container from the stored snapshot when there is one:

src/index.tsts
         
         export class MyContainer extends DurableObject<Env> {
         	// ...
         
         	private async startSandbox(): Promise<Container> {
         		const container = this.ctx.container;
         
         		if (!container) {
         			throw new Error("The container binding is not configured");
         		}
         
         		if (!container.running) {
         			const snapshotId = await this.ctx.storage.get<string>("snapshotId");
         
         			container.start({
         				...(snapshotId
         					? { containerSnapshot: { id: snapshotId } }
         					: { image: "cloudflare/debian-trixie" }),
         				entrypoint: ["sleep", "infinity"],
         				enableInternet: false,
         			});
         			await container.setInactivityTimeout(INACTIVITY_TIMEOUT_MS);
         		}
         
         		return container;
         	}
         }

If the stored snapshot cannot be restored, the request fails with an error such as `Snapshot "<SNAPSHOT_ID>" was not found.` Later requests fail the same way until the stored ID changes. The method does not fall back to the image, because the sandbox would then start with an empty workspace.

  2. Add a method that saves the filesystem and stops the instance:

src/index.tsts
         
         export class MyContainer extends DurableObject<Env> {
         	// ...
         
         	async save() {
         		const container = await this.startSandbox();
         		const snapshot = await container.snapshotContainer({ name: "workspace" });
         
         		await this.ctx.storage.put("snapshotId", snapshot.id);
         		await container.destroy();
         
         		return { snapshotId: snapshot.id, size: snapshot.size };
         	}
         }

A snapshot saves the writable root filesystem. It does not include mounted directories, memory, or running processes. Finish writing files before you save. For more information about what a restored instance starts with, refer to [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/#snapshots-carry-files-to-the-next-instance).

  3. Add a method that adds a line to a file and returns the file, so you can check what a restore brings back:

src/index.tsts
         
         export class MyContainer extends DurableObject<Env> {
         	// ...
         
         	async note(line?: string) {
         		const container = await this.startSandbox();
         		const script = line
         			? 'mkdir -p /workspace && printf "%s\n" "$1" >> /workspace/notes.txt && cat /workspace/notes.txt'
         			: "cat /workspace/notes.txt";
         		const process = await container.exec(["sh", "-c", script, "sh", line ?? ""]);
         		const output = await process.output();
         
         		return new TextDecoder().decode(output.stdout);
         	}
         }

  4. Add routes to your Worker that write a note, save the sandbox, and read the notes:

src/index.jsjs
         
         export default {
         	async fetch(request, env) {
         		const url = new URL(request.url);
         		const match =
         			/^\/sandboxes\/([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)\/(notes|snapshot)$/.exec(
         				url.pathname,
         			);
         
         		if (!match) {
         			return new Response("Not found", { status: 404 });
         		}
         
         		const [, name, action] = match;
         		const sandbox = env.MY_CONTAINER.getByName(name);
         
         		if (action === "snapshot" && request.method === "POST") {
         			return Response.json(await sandbox.save());
         		}
         
         		if (action === "notes" && request.method === "POST") {
         			return new Response(await sandbox.note(await request.text()));
         		}
         
         		if (action === "notes") {
         			return new Response(await sandbox.note());
         		}
         
         		return new Response("Method not allowed", { status: 405 });
         	},
         };

src/index.tsts
         
         export default {
         	async fetch(request: Request, env: Env): Promise<Response> {
         		const url = new URL(request.url);
         		const match = /^\/sandboxes\/([a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)\/(notes|snapshot)$/.exec(
         			url.pathname,
         		);
         
         		if (!match) {
         			return new Response("Not found", { status: 404 });
         		}
         
         		const [, name, action] = match;
         		const sandbox = env.MY_CONTAINER.getByName(name);
         
         		if (action === "snapshot" && request.method === "POST") {
         			return Response.json(await sandbox.save());
         		}
         
         		if (action === "notes" && request.method === "POST") {
         			return new Response(await sandbox.note(await request.text()));
         		}
         
         		if (action === "notes") {
         			return new Response(await sandbox.note());
         		}
         
         		return new Response("Method not allowed", { status: 405 });
         	},
         } satisfies ExportedHandler<Env>;

Snapshots can contain credentials or other sensitive files written in the sandbox. Authenticate callers first, so other people cannot read or restore the files of another sandbox. For more information, refer to [Sandbox security](https://developers.cloudflare.com/sandbox/concepts/security/#the-sandbox-name-decides-what-a-request-reaches).

  5. Deploy your Worker:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  6. Write a note in the sandbox named `ada`, save the sandbox, then read the notes. Replace the example hostname with the `workers.dev` URL that Wrangler prints:
         
         curl https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/sandboxes/ada/notes --data "Continue from this checkpoint."
         curl https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/sandboxes/ada/snapshot --request POST
         curl https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/sandboxes/ada/notes

The save responds with the snapshot ID and its size in bytes, such as `{"snapshotId":"<SNAPSHOT_ID>","size":123456}`. The last request starts a new instance from the snapshot, and the note is back:
         
         Continue from this checkpoint.




## Copy a sandbox

A snapshot ID restores in any Durable Object of the same class. To copy the files of one sandbox to a new sandbox, store the snapshot ID in the Durable Object of the new sandbox:

  1. Add methods to your Durable Object that return the stored snapshot ID and store another one:

src/index.tsts
         
         export class MyContainer extends DurableObject<Env> {
         	// ...
         
         	async snapshotId() {
         		return (await this.ctx.storage.get<string>("snapshotId")) ?? null;
         	}
         
         	async useSnapshot(snapshotId: string) {
         		// Replacing a running instance would discard files it has not saved.
         		if (this.ctx.container?.running) {
         			return false;
         		}
         
         		await this.ctx.storage.put("snapshotId", snapshotId);
         		return true;
         	}
         }

  2. Add a route to your Worker that copies one sandbox to another:

src/index.tsts
         
         if (action === "copy" && request.method === "POST") {
         	const from = url.searchParams.get("from") ?? "";
         	const snapshotId = await env.MY_CONTAINER.getByName(from).snapshotId();
         
         	if (!snapshotId || !(await sandbox.useSnapshot(snapshotId))) {
         		return new Response("Cannot copy", { status: 409 });
         	}
         
         	return new Response(null, { status: 204 });
         }

Add `copy` to the actions in the route pattern. A copy receives every file in the snapshot, so copy only between sandboxes that belong to the same user.

  3. Copy `ada` to `grace`, then read the notes from `grace`:
         
         curl "https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/sandboxes/grace/copy?from=ada" --request POST
         curl https://<YOUR_WORKER>.<YOUR_SUBDOMAIN>.workers.dev/sandboxes/grace/notes
         
         Continue from this checkpoint.

From this point, each sandbox changes its own files.




## Start a sandbox over

To discard the files of a sandbox, destroy its instance and delete the stored snapshot ID. The next request starts from the image:

src/index.tsts
    
    
    export class MyContainer extends DurableObject<Env> {
    	// ...
    
    	async reset() {
    		if (this.ctx.container?.running) {
    			await this.ctx.container.destroy();
    		}
    
    		await this.ctx.storage.delete("snapshotId");
    	}
    }

Deleting the stored ID does not delete the snapshot, so a sandbox that copied it can still restore it until the snapshot expires.

## Related resources

  * [Save a sandbox automatically](https://developers.cloudflare.com/sandbox/files/save-a-sandbox-automatically/): save before a sandbox stops for inactivity, and save checkpoints while it is in use.
  * [Back up a directory to R2](https://developers.cloudflare.com/sandbox/files/back-up-a-directory-to-r2/): keep one directory in your own bucket instead of the whole filesystem.
  * [Checkpoint workspace example ↗︎](https://github.com/cloudflare/sandbox-sdk/tree/main/examples/checkpoint-workspace): a deployable Worker that saves, restores, and copies sandboxes.
  * [Sandbox lifetime](https://developers.cloudflare.com/sandbox/concepts/lifetime/)
  * [Durable Object container API](https://developers.cloudflare.com/containers/api/durable-object-container/)



[PreviousMove files](https://developers.cloudflare.com/sandbox/files/manage-files/)[NextSave a sandbox automatically](https://developers.cloudflare.com/sandbox/files/save-a-sandbox-automatically/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/sandbox/files/save-and-restore-a-workspace.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
