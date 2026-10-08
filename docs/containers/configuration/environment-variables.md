---
url: https://developers.cloudflare.com/containers/configuration/environment-variables/
title: Environment Variables \u00b7 Cloudflare Containers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:33.819176+00:00
---

# Environment Variables · Cloudflare Containers docs

> Source: https://developers.cloudflare.com/containers/configuration/environment-variables/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Containers](https://developers.cloudflare.com/containers/)
  3. /Configuration
  4. /Environment Variables



# Environment Variables

Last updated Sep 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/containers/configuration/environment-variables/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRuntime environment variablesUser-defined environment variables

## Runtime environment variables

The container runtime automatically sets the following variables:

  * `CLOUDFLARE_APPLICATION_ID` \- the ID of the Containers application
  * `CLOUDFLARE_COUNTRY_A2` \- the [ISO 3166-1 Alpha 2 code ↗︎](https://www.iso.org/obp/ui/#search/code/) of a country the container is placed in
  * `CLOUDFLARE_LOCATION` \- a name of a location the container is placed in
  * `CLOUDFLARE_REGION` \- a region name
  * `CLOUDFLARE_DURABLE_OBJECT_ID` \- the ID of the Durable Object instance that the container is bound to. You can use this to identify particular container instances on the dashboard.



## User-defined environment variables

You can set environment variables when defining a Container in your Worker, or when starting a container instance.

For example:
    
    
    class MyContainer extends Container {
    	defaultPort = 4000;
    	envVars = {
    		MY_CUSTOM_VAR: "value",
    		ANOTHER_VAR: "another_value",
    	};
    }

More details about defining environment variables and secrets can be found in [this example](https://developers.cloudflare.com/containers/examples/env-vars-and-secrets).

[PreviousConnect to Workers and Bindings](https://developers.cloudflare.com/containers/configuration/workers-connections/)[NextScaling and Routing](https://developers.cloudflare.com/containers/configuration/scaling-and-routing/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/containers/configuration/environment-variables.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
