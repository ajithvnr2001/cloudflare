---
url: https://developers.cloudflare.com/artifacts/examples/git-client/
title: Git client \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:20.913863+00:00
---

# Git client · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/examples/git-client/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Examples
  4. /Git client



# Git client

Last updated May 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/examples/git-client/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewFetch the remote and clone the repo Authentication

You can use a standard Git client to interact with Artifacts repos. This example walks through clone, but the same approach works for fetch, pull, push, and any other Git operation.

To do this, you need to:

  * Fetch the repo's remote URL from the REST API
  * Mint a short-lived token scoped to that repo



Once you have the remote URL and token, you can use them to run Git commands against the repo.

This example assumes the repo already exists and that you have a [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with **Artifacts** > **Edit**.

## Fetch the remote and clone the repo

Replace the placeholder values with your account ID, API token, and repo name. The script fetches the repo's remote URL from the API, mints a read-only token that expires in one hour, and clones the repo to a local directory.

The example below uses `jq` to extract fields from the JSON responses.
    
    
    # Set your account details
    export ACCOUNT_ID="<YOUR_ACCOUNT_ID>"
    export ARTIFACTS_NAMESPACE="default"
    export ARTIFACTS_REPO="starter-repo"
    export CLOUDFLARE_API_TOKEN="<YOUR_API_TOKEN>"
    export ARTIFACTS_BASE_URL="https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/artifacts/namespaces/$ARTIFACTS_NAMESPACE"
    
    # Fetch the repo's remote URL
    REPO_JSON=$(curl --silent "$ARTIFACTS_BASE_URL/repos/$ARTIFACTS_REPO" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN")
    
    ARTIFACTS_REMOTE=$(printf '%s' "$REPO_JSON" | jq -r '.result.remote')
    
    # Mint a short-lived read token
    TOKEN_JSON=$(curl --silent "$ARTIFACTS_BASE_URL/tokens" \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data "{\"repo\":\"$ARTIFACTS_REPO\",\"scope\":\"read\",\"ttl\":3600}")
    
    ARTIFACTS_TOKEN=$(printf '%s' "$TOKEN_JSON" | jq -r '.result.plaintext')
    
    # Clone the repo
    git -c http.extraHeader="Authorization: Bearer $ARTIFACTS_TOKEN" clone "$ARTIFACTS_REMOTE" artifacts-clone

You now have a standard Git checkout in `./artifacts-clone`.

This flow is useful when another system owns repo discovery or access control, but your local tooling still expects a normal git remote.

### Authentication

Treat `ARTIFACTS_TOKEN` as a secret. Keep it out of logs, and prefer `http.extraHeader` over saving credentials in a remote URL.

If you need a self-contained remote URL for a short-lived workflow, extract the token secret and build the authenticated remote only for that command:
    
    
    ARTIFACTS_TOKEN_SECRET="${ARTIFACTS_TOKEN%%\?expires=*}"
    ARTIFACTS_AUTH_REMOTE="https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}"
    
    git clone "$ARTIFACTS_AUTH_REMOTE" artifacts-clone

[PreviousMetrics](https://developers.cloudflare.com/artifacts/observability/metrics/)[Nextisomorphic-git](https://developers.cloudflare.com/artifacts/examples/isomorphic-git/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/examples/git-client.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
