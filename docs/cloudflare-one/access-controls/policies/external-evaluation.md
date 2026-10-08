---
url: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/
title: External Evaluation rules \u00b7 Cloudflare One docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:08:21.940942+00:00
---

# External Evaluation rules · Cloudflare One docs

> Source: https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)
  3. /…

[Access controls](https://developers.cloudflare.com/cloudflare-one/access-controls/)

  4. /[Policies](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)
  5. /External Evaluation rules



# External Evaluation rules

Last updated May 6, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/external-evaluation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSet up external API and key with Cloudflare Workers Prerequisites 1\. Create a new Worker 2\. Program your business logic 3\. Generate a key 4\. Create an External Evaluation rule Troubleshooting the Worker

With Cloudflare Access, you can create Allow or Block policies which evaluate the user based on custom criteria. This is done by adding an **External Evaluation** rule to your policy. The **External Evaluation** selector requires two values:

  * **Evaluate URL** — the API endpoint containing your business logic.
  * **Keys URL** — the key that Access uses to verify that the response came from your API



After the user authenticates with your identity provider, Access sends the user's identity to the external API at **Evaluate URL**. The external API returns a True or False response to Access, which will then allow or deny access to the user. To protect against man-in-the-middle attacks, Access signs all requests with your Access account key and checks that responses are signed by the key at **Keys URL**.

You can set up External Evaluation rules using any API service, but to get started quickly we recommend using [Cloudflare Workers](https://developers.cloudflare.com/workers/).

## Set up external API and key with Cloudflare Workers

### Prerequisites

  * [Workers account](https://developers.cloudflare.com/workers/get-started/guide/)
  * Install [npm ↗︎](https://docs.npmjs.com/getting-started)
  * Install [Node.js ↗︎](https://nodejs.org/en/)
  * Application protected by Access



### 1\. Create a new Worker

  1. Open a terminal and clone our example project.
         
         npm create cloudflare@latest my-worker -- --template https://github.com/cloudflare/workers-access-external-auth-example

  2. Go to the project directory.
         
         cd my-worker

  3. Create a [Workers KV namespace](https://developers.cloudflare.com/kv/concepts/kv-namespaces/) to store the key. The binding name should be `KV` if you want to run the example as written.
         
         npx wrangler kv namespace create "KV"

The command will output the binding name and KV namespace ID, for example
         
         [[kv_namespaces]]
            binding = "KV"
            id = "YOUR_KV_NAMESPACE_ID"

  4. Open the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) in an editor and insert the following:

     * `[[kv_namespaces]]`: Add the output generated in the previous step.
     * `<TEAM_NAME>`: your Cloudflare One team name.


    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "my-worker",
      "workers_dev": true,
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "main": "index.js",
      "kv_namespaces": [
        {
          "binding": "KV",
          "id": "YOUR_KV_NAMESPACE_ID"
        }
      ],
      "vars": {
        "TEAM_DOMAIN": "<TEAM_NAME>.cloudflareaccess.com",
        "DEBUG": false
      }
    }
    
    
    "$schema" = "./node_modules/wrangler/config-schema.json"
    name = "my-worker"
    workers_dev = true
    # Set this to today's date
    compatibility_date = "2026-10-08"
    main = "index.js"
    
    [[kv_namespaces]]
    binding = "KV"
    id = "YOUR_KV_NAMESPACE_ID"
    
    [vars]
    TEAM_DOMAIN = "<TEAM_NAME>.cloudflareaccess.com"
    DEBUG = false

### 2\. Program your business logic

  1. Open `index.js` and modify the `externalEvaluation` function to perform logic on any identity-based data sent by Access.



Note

  * Sample code is available in our [GitHub repository ↗︎](https://github.com/cloudflare/workers-access-external-auth-example).
  * To view a list of identity-based data fields, log in to your Access application and append `/cdn-cgi/access/get-identity` to the URL. For example, if `www.example.com` is behind Access, visit `https://www.example.com/cdn-cgi/access/get-identity`.



  2. Deploy the Worker to Cloudflare's global network.
         
         npx wrangler deploy




The Worker will be deployed to your `*.workers.dev` subdomain at `my-worker.<YOUR_SUBDOMAIN>.workers.dev`.

### 3\. Generate a key

To generate an RSA private/public key pair:

  1. Open a browser and go to `https://my-worker.<YOUR_SUBDOMAIN>.workers.dev/keys`.

  2. (Optional) Verify that the key has been stored in the `KV` namespace:

     1. In the Cloudflare dashboard, go to the **Workers KV** page. [ Go to **Workers KV** ↗ ](https://dash.cloudflare.com/?to=/:account/workers/kv/namespaces)
     2. Select **View** next to `my-worker-KV`.



Other key formats (such as DSA) are not supported at this time.

### 4\. Create an External Evaluation rule

  1. In the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), go to **Zero Trust** > **Access controls** > **Policies**.

  2. Edit an existing policy or select **Add a policy**.

  3. Add the following rule to your policy:




Rule Type | Selector | Evaluate URL | Keys URL  
---|---|---|---  
Include | External Evaluation | `https://my-worker.<YOUR_SUBDOMAIN>.workers.dev/` | `https://my-worker.<YOUR_SUBDOMAIN>.workers.dev/keys/`  
  
  4. Save the policy.

  5. Go to **Access controls** > **Applications** and edit the application for which you want to apply the External Evaluation rule.

  6. In the **Policies** tab, add the policy that contains the External Evaluation rule.

  7. Select **Save**.




When a user logs in to your application, Access will now check their email, device, location, and other identity-based data against your business logic.

### Troubleshooting the Worker

To debug your External Evaluation rule:

  1. Go to your Worker directory.
         
         cd my-worker

  2. Open the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) in an editor and set the `debug` variable to `TRUE`.

  3. Deploy your changes.
         
         npx wrangler deploy

  4. Next, start a session to output realtime logs from your Worker.
         
         wrangler tail -f pretty

  5. Log in to your Access application.

The session logs should show an incoming and outgoing JWT. The incoming JWT was sent by Access to the Worker API, while the outgoing JWT was sent by the Worker back to Access.

  6. To decode the contents of a JWT, you can copy the token into [jwt.io ↗︎](https://jwt.io/).

The incoming JWT should contain the user's identity data. The outgoing JWT should look similar to:
         
         {
         "success": true,
         "iat": 1655409315,
         "exp": 1655409375,
         "nonce": "9J2E9Xg6wYj8tlnA5MV4Zgp6t8rzmS0Q"
         }

Access checks the outgoing JWT for all of the following criteria:

     * Token was signed by **Keys URL**.
     * Expiration date has not elapsed.
     * API returns `"success": true`.
     * `nonce` is unchanged from the incoming JWT. The `nonce` value is unique per request.

If any condition fails, the External Evaluation rule evaluates to false.




[PreviousRequire purpose justification](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/require-purpose-justification/)[NextIsolate self-hosted application](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/isolate-application/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/cloudflare-one/access-controls/policies/external-evaluation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
