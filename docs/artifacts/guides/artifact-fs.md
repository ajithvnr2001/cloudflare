---
url: https://developers.cloudflare.com/artifacts/guides/artifact-fs/
title: ArtifactFS \u00b7 Cloudflare Artifacts docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:21.325753+00:00
---

# ArtifactFS · Cloudflare Artifacts docs

> Source: https://developers.cloudflare.com/artifacts/guides/artifact-fs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Artifacts](https://developers.cloudflare.com/artifacts/)
  3. /Guides
  4. /ArtifactFS



# ArtifactFS

Last updated Apr 25, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/artifacts/guides/artifact-fs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewChoose ArtifactFS whenUnderstand how it behavesMount an Artifacts repo

ArtifactFS mounts a Git repository as a local filesystem without waiting for a full clone. It works well when your environment needs a working tree quickly and can tolerate file contents hydrating on demand.

Use ArtifactFS for large repos in sandboxes, containers, and virtual machines. For smaller repos, a regular `git clone` is usually simpler.

ArtifactFS works with [Artifacts Git remotes](https://developers.cloudflare.com/artifacts/api/git-protocol/) and other Git repositories.

## Choose ArtifactFS when

  * startup time matters more than a complete local clone
  * the repo is large enough that cloning slows down sandbox startup
  * tools need a mounted working tree instead of direct Git access



For smaller repos, start with a regular `git clone`. It is usually fast enough and simpler to operate.

## Understand how it behaves

ArtifactFS starts with a blobless clone. It fetches commits, trees, and refs first, then mounts the working tree through FUSE.

File contents hydrate asynchronously as tools read them. Reads only block when a requested blob is not hydrated yet, and later reads come from the local blob cache.

ArtifactFS prioritizes files that usually unblock developer tools first, such as package manifests, dependency files, and common source files. Large binary assets are deprioritized.

## Mount an Artifacts repo

This example installs ArtifactFS, builds an authenticated Artifacts remote from a repo token, mounts the repo, and reads files from the mounted working tree.

This example assumes you already have a working FUSE implementation on the host, a repo-scoped Artifacts token, and the repo `remote` value from a create or get response.
    
    
    go install github.com/cloudflare/artifact-fs/cmd/artifact-fs@latest
    
    export ARTIFACTS_REMOTE="<PASTE_REMOTE_FROM_CREATE_OR_GET_RESPONSE>"
    export ARTIFACTS_TOKEN="<YOUR_READ_TOKEN>"
    export ARTIFACTS_TOKEN_SECRET="${ARTIFACTS_TOKEN%%\?expires=*}"
    export ARTIFACTS_AUTH_REMOTE="https://x:${ARTIFACTS_TOKEN_SECRET}@${ARTIFACTS_REMOTE#https://}"
    
    artifact-fs add-repo \
      --name starter-repo \
      --remote "$ARTIFACTS_AUTH_REMOTE" \
      --branch main \
      --mount-root /tmp
    
    artifact-fs daemon --root /tmp &
    
    ls /tmp/starter-repo/
    cat /tmp/starter-repo/README.md
    git -C /tmp/starter-repo log --oneline -5

Use a short-lived token in the authenticated remote URL. If you need a smaller repo or a simpler local workflow, use a normal [Git protocol](https://developers.cloudflare.com/artifacts/api/git-protocol/) clone instead.

[PreviousImport repositories](https://developers.cloudflare.com/artifacts/guides/import-repositories/)[NextEvent subscriptions](https://developers.cloudflare.com/artifacts/guides/event-subscriptions/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/artifacts/guides/artifact-fs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
