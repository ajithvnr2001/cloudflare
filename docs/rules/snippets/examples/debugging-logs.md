---
url: https://developers.cloudflare.com/rules/snippets/examples/debugging-logs/
title: Debugging logs \u00b7 Cloudflare Rules docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:14:53.509014+00:00
---

# Debugging logs · Cloudflare Rules docs

> Source: https://developers.cloudflare.com/rules/snippets/examples/debugging-logs/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Rules](https://developers.cloudflare.com/rules/)
  3. /…

[Snippets](https://developers.cloudflare.com/rules/snippets/)

  4. /[Examples](https://developers.cloudflare.com/rules/snippets/examples/)
  5. /Debugging Logs



# Debugging logs

Send debugging information in an errored response to a logging service.

Last updated Oct 13, 2025|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/rules/snippets/examples/debugging-logs/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
    
    
    // Replace with your actual logging service endpoint
    const loggingEndpoint = "https://your-logging-endpoint";
    
    export default {
    	async fetch(request) {
    		try {
    			// Attempt to fetch the request from the origin server
    			const response = await fetch(request.clone());
    
    			// Check if the response status indicates an error (for example, 4xx or 5xx)
    			if (!response.ok) {
    				// Prepare error details and context for logging
    				const errorDetails = {
    					status: response.status,
    					statusText: response.statusText,
    					url: request.url,
    					method: request.method,
    					headers: Object.fromEntries(request.headers),
    				};
    
    				// Log error details to your logging service
    				await logError(errorDetails);
    
    				// Return the original response with status and statusText intact
    				return new Response(response.body, {
    					status: response.status,
    					statusText: response.statusText,
    					headers: response.headers,
    				});
    			}
    
    			// Return the successful response from the origin server
    			return response;
    		} catch (error) {
    			// Handle any exceptions that occur during fetch
    			const errorDetails = {
    				message: error.message,
    				stack: error.stack,
    				url: request.url,
    				method: request.method,
    				headers: Object.fromEntries(request.headers),
    			};
    
    			// Log error details to your logging service
    			await logError(errorDetails);
    
    			// Return a generic error response
    			return new Response("Internal Server Error", {
    				status: 500,
    			});
    		}
    	},
    };
    
    // Function to log error details to your logging service
    async function logError(details) {
    	try {
    		const response = await fetch(loggingEndpoint, {
    			method: "POST",
    			headers: {
    				"Content-Type": "application/json",
    			},
    			body: JSON.stringify(details),
    		});
    
    		if (!response.ok) {
    			console.error("Failed to log error:", response.statusText);
    		}
    	} catch (error) {
    		console.error("Error logging error:", error.message);
    	}
    }

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/rules/snippets/examples/debugging-logs.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
