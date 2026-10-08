---
url: https://developers.cloudflare.com/artifacts/guides/authentication/
title: Authentication \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.423540+00:00
---

# Authentication · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/guides/authentication/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Guides
  4. /Authentication



# Authentication

Last updated Apr 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/guides/authentication/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewCompare auth methodsAuthenticate the Workers bindingAuthenticate the REST APIAuthenticate the Git protocol

Artifacts uses a different authentication path for each interface. Choose auth based on how your code reaches the repo.

Review [Namespaces](https://developers.cloudflare.com/artifacts/concepts/namespaces/) first, then use one namespace name consistently across each interface.

## Compare auth methods

Interface | Authenticate with | Permissions or scopes | Use for  
---|---|---|---  
Workers binding | Configured `artifacts` binding | Wrangler auth is only for local Wrangler commands such as `dev` and `deploy`. | Worker code that calls `env.ARTIFACTS`  
REST API | Cloudflare API token in `Authorization: Bearer ...` | **Artifacts** > **Read** for read routes and **Artifacts** > **Edit** for write routes. | Control-plane HTTP requests  
Git protocol | Repo-scoped Artifacts token | `read` for clone, fetch, and pull. `write` for push. | Standard Git over HTTPS  
  
Cloudflare API tokens authenticate control-plane access. Repo-scoped Artifacts tokens authenticate Git access.

## Authenticate the Workers binding

The Workers binding uses the `artifacts` binding you configure in Wrangler. Your Worker code does not pass a token when it calls `env.ARTIFACTS`.

Add the binding in your Wrangler config:
    
    
    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "artifacts-worker",
      "main": "src/index.ts",
      // Set this to today's date
      "compatibility_date": "2026-10-08",
      "artifacts": [
        {
          "binding": "ARTIFACTS",
          "namespace": "default"
        }
      ]
    }
    
    
    name = "artifacts-worker"
    main = "src/index.ts"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [[artifacts]]
    binding = "ARTIFACTS"
    namespace = "default"

At runtime, deployed Workers use the configured binding directly. For local Wrangler commands such as `wrangler dev`, `wrangler deploy`, or `wrangler types`, authenticate Wrangler first. For local OAuth authentication, refer to [`wrangler login`](https://developers.cloudflare.com/workers/wrangler/commands/general/#login). For CI or headless environments, refer to [Running Wrangler in CI/CD](https://developers.cloudflare.com/workers/ci-cd/).

## Authenticate the REST API

The REST API uses a Cloudflare API token in the `Authorization` header.
    
    
    export ACCOUNT_ID="<YOUR_ACCOUNT_ID>"
    export ARTIFACTS_NAMESPACE="default"
    export CLOUDFLARE_API_TOKEN="<YOUR_API_TOKEN>"
    export ARTIFACTS_BASE_URL="https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE"

Read repo metadata:
    
    
    curl "$ARTIFACTS_BASE_URL/repos/starter-repo" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

Create a repo:
    
    
    curl --request POST "$ARTIFACTS_BASE_URL/repos" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "starter-repo"
      }'

## Authenticate the Git protocol

Git uses repo-scoped Artifacts tokens, not Cloudflare API tokens. Mint these tokens from the Workers binding or the REST API, then use them with the repo `remote` URL.

Token scope | Allowed commands  
---|---  
`read` | `git clone`, `git fetch`, `git pull`  
`write` | `git clone`, `git fetch`, `git pull`, `git push`  
  
Use the exact repo `remote` value returned by the Workers binding or REST API:
    
    
    export ARTIFACTS_REMOTE="<PASTE_REMOTE_FROM_CREATE_OR_GET_RESPONSE>"

Use a read token to clone:
    
    
    git -c http.extraHeader="Authorization: Bearer <YOUR_READ_TOKEN>" clone "$ARTIFACTS_REMOTE" artifacts-clone

Use a write token to push:
    
    
    git -c http.extraHeader="Authorization: Bearer <YOUR_WRITE_TOKEN>" push "$ARTIFACTS_REMOTE" HEAD:main

For more information on token handling and authenticated remotes, refer to [Git protocol](https://developers.cloudflare.com/artifacts/api/git-protocol/).

[PreviousREST API](https://developers.cloudflare.com/artifacts/get-started/rest-api/)[NextImport repositories](https://developers.cloudflare.com/artifacts/guides/import-repositories/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/guides/authentication.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
