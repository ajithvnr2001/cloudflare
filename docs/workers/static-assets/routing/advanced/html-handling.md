---
url: https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/
title: HTML handling \u00b7 Cloudflare Workers docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:17:53.138176+00:00
---

# HTML handling · Cloudflare Workers docs

> Source: https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Workers](https://developers.cloudflare.com/workers/)
  3. /…

[Static Assets](https://developers.cloudflare.com/workers/static-assets/)Routing

  4. /Advanced
  5. /HTML handling



# HTML handling

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/workers/static-assets/routing/advanced/html-handling/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAutomatic trailing slashes (default)Force trailing slashesDrop trailing slashesDisable HTML handling

Forcing or dropping trailing slashes on request paths (for example, `example.com/page/` vs. `example.com/page`) is often something that developers wish to control for cosmetic reasons. Additionally, it can impact SEO because search engines often treat URLs with and without trailing slashes as different, separate pages. This distinction can lead to duplicate content issues, indexing problems, and overall confusion about the correct canonical version of a page.

The [`assets.html_handling` configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#assets) determines the redirects and rewrites of requests for HTML content. It is used to specify the pattern for canonical URLs, thus where Cloudflare serves HTML content from, and additionally, where Cloudflare redirects non-canonical URLs to.

Take the following directory structure:

  * dist 
    * file.html
    * folder 
      * index.html



## Automatic trailing slashes (default)

This will usually give you the desired behavior automatically: individual files (e.g. `foo.html`) will be served _without_ a trailing slash and folder index files (e.g. `foo/index.html`) will be served _with_ a trailing slash.
    
    
    {
    	"name": "my-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"assets": {
    		"directory": "./dist/",
    		"html_handling": "auto-trailing-slash"
    	}
    }
    
    
    name = "my-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [assets]
    directory = "./dist/"
    html_handling = "auto-trailing-slash"

Based on the incoming requests, the following assets would be served:

Incoming Request | Response | Asset Served  
---|---|---  
/file | 200 | /dist/file.html  
/file.html | 307 to /file | -  
/file/ | 307 to /file | -  
/file/index | 307 to /file | -  
/file/index.html | 307 to /file | -  
/folder | 307 to /folder/ | -  
/folder.html | 307 to /folder | -  
/folder/ | 200 | /dist/folder/index.html  
/folder/index | 307 to /folder | -  
/folder/index.html | 307 to /folder | -  
  
## Force trailing slashes

Alternatively, you can force trailing slashes (`force-trailing-slash`).
    
    
    {
    	"name": "my-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"assets": {
    		"directory": "./dist/",
    		"html_handling": "force-trailing-slash"
    	}
    }
    
    
    name = "my-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [assets]
    directory = "./dist/"
    html_handling = "force-trailing-slash"

Based on the incoming requests, the following assets would be served:

Incoming Request | Response | Asset Served  
---|---|---  
/file | 307 to /file/ | -  
/file.html | 307 to /file/ | -  
/file/ | 200 | /dist/file.html  
/file/index | 307 to /file/ | -  
/file/index.html | 307 to /file/ | -  
/folder | 307 to /folder/ | -  
/folder.html | 307 to /folder/ | -  
/folder/ | 200 | /dist/folder/index.html  
/folder/index | 307 to /folder/ | -  
/folder/index.html | 307 to /folder/ | -  
  
## Drop trailing slashes

Or you can drop trailing slashes (`drop-trailing-slash`).
    
    
    {
    	"name": "my-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"assets": {
    		"directory": "./dist/",
    		"html_handling": "drop-trailing-slash"
    	}
    }
    
    
    name = "my-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [assets]
    directory = "./dist/"
    html_handling = "drop-trailing-slash"

Based on the incoming requests, the following assets would be served:

Incoming Request | Response | Asset Served  
---|---|---  
/file | 200 | /dist/file.html  
/file.html | 307 to /file | -  
/file/ | 307 to /file | -  
/file/index | 307 to /file | -  
/file/index.html | 307 to /file | -  
/folder | 200 | /dist/folder/index.html  
/folder.html | 307 to /folder | -  
/folder/ | 307 to /folder | -  
/folder/index | 307 to /folder | -  
/folder/index.html | 307 to /folder | -  
  
## Disable HTML handling

Alternatively, if you have bespoke needs, you can disable the built-in HTML handling entirely (`none`).
    
    
    {
    	"name": "my-worker",
    	// Set this to today's date
    	"compatibility_date": "2026-10-08",
    	"assets": {
    		"directory": "./dist/",
    		"html_handling": "none"
    	}
    }
    
    
    name = "my-worker"
    # Set this to today's date
    compatibility_date = "2026-10-08"
    
    [assets]
    directory = "./dist/"
    html_handling = "none"

Based on the incoming requests, the following assets would be served:

Incoming Request | Response | Asset Served  
---|---|---  
/file | Depends on `not_found_handling` | Depends on `not_found_handling`  
/file.html | 200 | /dist/file.html  
/file/ | Depends on `not_found_handling` | Depends on `not_found_handling`  
/file/index | Depends on `not_found_handling` | Depends on `not_found_handling`  
/file/index.html | Depends on `not_found_handling` | Depends on `not_found_handling`  
/folder | Depends on `not_found_handling` | Depends on `not_found_handling`  
/folder.html | Depends on `not_found_handling` | Depends on `not_found_handling`  
/folder/ | Depends on `not_found_handling` | Depends on `not_found_handling`  
/folder/index | Depends on `not_found_handling` | Depends on `not_found_handling`  
/folder/index.html | 200 | /dist/folder/index.html  
  
[PreviousGradual rollouts ↗︎](https://developers.cloudflare.com/workers/versions-and-deployments/gradual-deployments/version-affinity/#static-assets)[NextServing a subdirectory](https://developers.cloudflare.com/workers/static-assets/routing/advanced/serving-a-subdirectory/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/workers/static-assets/routing/advanced/html-handling.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
