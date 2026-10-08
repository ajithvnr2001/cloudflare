---
url: https://cloudflare.com/drop/
title: Cloudflare Drop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:29.801785+00:00
---

# Cloudflare Drop

> Source: https://cloudflare.com/drop/


    # Cloudflare Drop
    
    > Deploy static sites to Cloudflare's global network instantly, with no account required to start.
    
    ## How it works
    
    1. Drop a folder or .zip file containing your static site (HTML, CSS, JS).
    2. Cloudflare Drop uploads and distributes it to Cloudflare's global network.
    3. You get a live `workers.dev` URL.
    4. Claim the deployment within 60 minutes to keep it.
    
    ## For AI agents
    
    Use Cloudflare Drop at https://www.cloudflare.com/drop/ only when you have browser automation and a completed static site folder or .zip file to upload. After publishing, return both the live URL and claim URL.
    
    For local CLI project workflows, prefer Wrangler instead of Cloudflare Drop. If Wrangler is not authenticated with Cloudflare, use Wrangler 4.102.0 or later.
    
    If Wrangler is not installed globally, use `npx` or `npm exec`:
    
    ```sh
    npm exec --yes wrangler@latest -- deploy ./dist --name my-static-site --temporary --compatibility-date <YYYY-MM-DD>
    ```
    
    Replace `./dist` with the directory containing the final static files. Use today's date for `--compatibility-date`.
    
    For static site deployments:
    
    - Deploy a dedicated project output directory, such as `./dist`, `./build`, or another folder containing the final static files.
    - Ensure the deployed directory contains an `index.html`.
    - Pass a Worker name with `--name`.
    - If the first deploy creates a temporary account but fails because a name is missing, rerun with `--name`.
    - If the deploy fails because `compatibility_date` is required, rerun with `--compatibility-date <YYYY-MM-DD>`.
    
    After deployment, verify the live URL. If it initially returns 404, wait briefly and retry before changing the deployment, because the route and assets can take a short time to become available.
    
    Return both:
    
    - The live `workers.dev` URL
    - The claim URL
    
    The claim URL grants ownership of the temporary preview account. Treat it as sensitive and tell the user it expires after 60 minutes.
    
    Do not use `--temporary` when Wrangler is already authenticated with OAuth, `CLOUDFLARE_API_TOKEN`, or a global API key. In authenticated environments, use normal `wrangler deploy`.
    
    For details:
    
    - https://developers.cloudflare.com/workers/platform/claim-deployments/
    - https://developers.cloudflare.com/workers/wrangler/commands/workers/#deploy
    
