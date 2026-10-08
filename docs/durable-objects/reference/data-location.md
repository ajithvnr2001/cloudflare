---
url: https://developers.cloudflare.com/durable-objects/reference/data-location/
title: Data location \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:09.869449+00:00
---

# Data location · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/reference/data-location/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Reference
  4. /Data location



# Data location

Last updated Jun 26, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/reference/data-location/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewRestrict Durable Objects to a jurisdiction Supported locations Read the jurisdiction from inside a Durable ObjectProvide a location hint Supported locationsAdditional resources

## Restrict Durable Objects to a jurisdiction

Jurisdictions are used to create Durable Objects that only run and store data within a region to comply with local regulations such as the [GDPR ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

Workers may still access Durable Objects constrained to a jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data. Consider using [Regional Services](https://developers.cloudflare.com/data-localization/regional-services/) to control the regions from which Cloudflare responds to requests.

Logging

A [`DurableObjectId`](https://developers.cloudflare.com/durable-objects/api/id) will be logged outside of the specified jurisdiction for billing and debugging purposes.

Durable Objects can be restricted to a specific jurisdiction by creating a [`DurableObjectNamespace`](https://developers.cloudflare.com/durable-objects/api/namespace/) restricted to a jurisdiction. All [Durable Object ID methods](https://developers.cloudflare.com/durable-objects/api/id/) are valid on IDs within a namespace restricted to a jurisdiction.
    
    
    const euSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction("eu");
    const euId = euSubnamespace.newUniqueId();

  * It is possible to have the same name represent different IDs in different jurisdictions.
        
        const euId1 = env.MY_DURABLE_OBJECT.idFromName("my-name");
        const euId2 = env.MY_DURABLE_OBJECT.jurisdiction("eu").idFromName("my-name");
        console.assert(!euId1.equal(euId2), "This should always be true");

  * You will run into an error if the jurisdiction on your [`DurableObjectNamespace`](https://developers.cloudflare.com/durable-objects/api/namespace/) and the jurisdiction on [`DurableObjectId`](https://developers.cloudflare.com/durable-objects/api/id) are different.

  * You will not run into an error if the [`DurableObjectNamespace`](https://developers.cloudflare.com/durable-objects/api/namespace/) is not associated with a jurisdiction.

  * All [Durable Object ID methods](https://developers.cloudflare.com/durable-objects/api/id/) are valid on IDs within a namespace restricted to a jurisdiction.
        
        const euSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction("eu");
        const euId = euSubnamespace.idFromName(name);
        const stub = env.MY_DURABLE_OBJECT.get(euId);




Use `DurableObjectNamespace.jurisdiction`

When specifying a jurisdiction, Cloudflare recommends you first create a namespace restricted to a jurisdiction, using `const euSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction("eu")`.

Note that it is also possible to specify a jurisdiction by creating an individual [`DurableObjectId`](https://developers.cloudflare.com/durable-objects/api/id) restricted to a jurisdiction, using `const euId = env.MY_DURABLE_OBJECT.newUniqueId({ jurisdiction: "eu" })`.

**However, Cloudflare does not recommend this approach.**

### Supported locations

Parameter | Location  
---|---  
eu | The European Union  
us | The United States  
fedramp | FedRAMP-Moderate data centers  
  
### Read the jurisdiction from inside a Durable Object

The jurisdiction of a Durable Object is available inside the object via [`ctx.id.jurisdiction`](https://developers.cloudflare.com/durable-objects/api/id/#jurisdiction). The value is preserved across `toString()` and `idFromString()` round-trips and is also available inside [alarm handlers](https://developers.cloudflare.com/durable-objects/api/alarms/) for alarms scheduled on 2026-03-15 or later, which makes it suitable for region-aware logic inside the Durable Object.

## Provide a location hint

Durable Objects, as with any stateful API, will often add response latency as requests must be forwarded to the data center where the Durable Object, or state, is located.

Durable Objects do not currently change locations after they are created1. By default, a Durable Object is instantiated in a data center close to where the initial `get()` request is made. This may not be in the same data center that the `get()` request is made from, but in most cases, it will be in close proximity.

Initial requests to Durable Objects

It can negatively impact latency to pre-create Durable Objects prior to the first client request or when the first client request is not representative of where the majority of requests will come from. It is better for latency to create Durable Objects in response to actual production traffic or provide explicit location hints.

Location hints are the mechanism provided to specify the location that a Durable Object should be located regardless of where the initial `get()` request comes from.

To manually create Durable Objects in another location, provide an optional `locationHint` parameter to `get()`. Only the first call to `get()` for a particular Object will respect the hint.
    
    
    let durableObjectStub = OBJECT_NAMESPACE.get(id, { locationHint: "enam" });

Caution

Hints are a best effort and not a guarantee. Unlike with jurisdictions, Durable Objects will not necessarily be instantiated in the hinted location, but instead instantiated in a data center selected to minimize latency from the hinted location.

### Supported locations

Parameter | Location  
---|---  
wnam | Western North America  
enam | Eastern North America  
sam | South America 2  
weur | Western Europe  
eeur | Eastern Europe  
apac | Asia-Pacific  
apac-ne | Northeast Asia-Pacific 3  
apac-se | Southeast Asia-Pacific 3  
oc | Oceania  
afr | Africa 2  
me | Middle East 2  
  
1 Dynamic relocation of existing Durable Objects is planned for the future.

2 Durable Objects currently do not spawn in this location. Instead, the Durable Object will spawn in a nearby location which does support Durable Objects. For example, Durable Objects hinted to South America spawn in Eastern North America instead.

3`apac-ne` (Northeast Asia-Pacific) and `apac-se` (Southeast Asia-Pacific) are narrower sub-regions within `apac` (Asia-Pacific). Prefer `apac` for general Asia-Pacific placement. Choose `apac-ne` or `apac-se` only when your users are concentrated in the northeast or southeast of the region and you want to minimize latency for them.

## Additional resources

  * You can find our more about where Durable Objects are located using the website: [Where Durable Objects Live ↗︎](https://where.durableobjects.live/).



[PreviousData security](https://developers.cloudflare.com/durable-objects/reference/data-security/)[NextEnvironments](https://developers.cloudflare.com/durable-objects/reference/environments/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/reference/data-location.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
