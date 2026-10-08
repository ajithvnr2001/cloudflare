---
url: https://developers.cloudflare.com/artifacts/api/errors/
title: Errors \u00b7 Artifacts \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:19.964267+00:00
---

# Errors · Artifacts · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/api/errors/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /API
  4. /Errors



# Errors

Last updated May 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/api/errors/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewError codes

This is a list of Artifacts errors.

## Error codes

Name | Code | Description  
---|---|---  
`ALREADY_EXISTS` | 10201 | The target repository already exists in the namespace.  
`NOT_FOUND` | 10200 | The repository or remote resource does not exist.  
`IMPORT_IN_PROGRESS` | 10302 | The repository is still being imported and is not yet available.  
`FORK_IN_PROGRESS` | 10303 | The repository is still being forked and is not yet available.  
`INVALID_INPUT` | 10100 | A request parameter is missing, malformed, or outside the accepted range.  
`INVALID_REPO_NAME` | 10101 | The repository name does not meet naming requirements.  
`INVALID_TTL` | 10103 | The token TTL is outside the allowed range (60–31,536,000 seconds).  
`INVALID_URL` | 10104 | The source URL does not point to a valid git repository.  
`REMOTE_AUTH_REQUIRED` | 10106 | The remote repository requires authentication.  
`UPSTREAM_UNAVAILABLE` | 10401 | The remote git server could not be reached.  
`MEMORY_LIMIT` | 10402 | The operation exceeds service memory limits.  
`INTERNAL_ERROR` | 10400 | An unexpected internal error occurred.  
  
[PreviousWrangler commands](https://developers.cloudflare.com/artifacts/api/wrangler/)[NextMetrics](https://developers.cloudflare.com/artifacts/observability/metrics/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/api/errors.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
