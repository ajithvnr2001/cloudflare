---
url: https://developers.cloudflare.com/containers/configuration/scaling-and-routing/
title: Scaling and Routing \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:34.253996+00:00
---

# Scaling and Routing · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/configuration/scaling-and-routing/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Configuration
  4. /Scaling and Routing



# Scaling and Routing

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewScale container instances with explicit IDs Use the getRandom helper function

## Scale container instances with explicit IDs

Note

This section uses helpers from the [Container class](https://developers.cloudflare.com/containers/api/container-class/).

Today, Containers are scaled manually by getting containers with a unique ID, then starting the container. Note that getting a container does not automatically start it.
    
    
    // get and start two container instances
    const containerOne = getContainer(
    	env.MY_CONTAINER,
    	idOne,
    ).startAndWaitForPorts();
    
    const containerTwo = getContainer(
    	env.MY_CONTAINER,
    	idTwo,
    ).startAndWaitForPorts();

Each instance will run until its `sleepAfter` time has elapsed, or until it is manually stopped.

This behavior is very useful when you want explicit control over the lifecycle of container instances. For instance, you may want to spin up a container backend instance for a specific user, or you may briefly run a code sandbox to isolate AI-generated code, or you may want to run a short-lived batch job.

### Use the `getRandom` helper function

If you want to run multiple instances of a container and route requests between them, use the `getRandom` helper function:
    
    
    import { Container, getRandom } from "@cloudflare/containers";
    
    const INSTANCE_COUNT = 3;
    
    class Backend extends Container {
    	defaultPort = 8080;
    	sleepAfter = "2h";
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		const containerInstance = await getRandom(env.BACKEND, INSTANCE_COUNT);
    		return containerInstance.fetch(request);
    	},
    };

Use `getRandom` to route to multiple stateless container instances. It randomly selects one of N instances for each request, which means:

  * It requires that the user set a fixed number of instances to route to.
  * It will randomly select each instance, regardless of location.



We plan to fix these issues with built-in autoscaling and routing features in the near future.

[PreviousEnvironment Variables](https://developers.cloudflare.com/containers/configuration/environment-variables/)[NextRollouts](https://developers.cloudflare.com/containers/configuration/rollouts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/configuration/scaling-and-routing.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
