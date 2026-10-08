---
url: https://developers.cloudflare.com/agent-memory/api/http-api/
title: HTTP API \u00b7 Cloudflare Agent Memory docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:05.301876+00:00
---

# HTTP API · Cloudflare Agent Memory docs

> Source: https://developers.cloudflare.com/agent-memory/api/http-api/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agent Memory](https://developers.cloudflare.com/agent-memory/)
  3. /API
  4. /HTTP API



# HTTP API

Last updated Jun 2, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agent-memory/api/http-api/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewAuthenticationNamespace management Create a namespace List namespaces Get a namespace Delete a namespaceProfiles Delete a profile Delete a session Ingest messages Remember a memory Recall memories List memories Get a memory Delete a memory Get a summaryError responses

Use the HTTP API to call Agent Memory from services that do not run inside [Cloudflare Workers](https://developers.cloudflare.com/workers/). For Workers applications, use the [Workers API](https://developers.cloudflare.com/agent-memory/api/workers-api/) through an `agent_memory` binding.

The HTTP API uses namespaces and profiles. A namespace scopes profiles for your application, and each profile is an isolated memory store. Profiles are created automatically when you first write to them.

## Authentication

All requests require an [API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the appropriate Agent Memory permissions.

Include your API token in the `Authorization` header:
    
    
    Authorization: Bearer <API_TOKEN>

For information about calling the Cloudflare API, refer to [Make API calls](https://developers.cloudflare.com/fundamentals/api/how-to/make-api-calls/).

## Namespace management

A [namespace](https://developers.cloudflare.com/agent-memory/concepts/namespaces-profiles/) is a top-level container that scopes memory profiles for your application.

### Create a namespace

Creates a new namespace for the given account.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{"name": "support-agent"}'

The response includes the namespace name that you use in Worker bindings and HTTP API calls.
    
    
    {
    	"result": {
    		"id": "01JSGCEXAMPLE000000000000",
    		"name": "support-agent",
    		"created_at": "2026-04-21T00:00:00.000Z",
    		"updated_at": "2026-04-21T00:00:00.000Z"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### List namespaces

Lists all namespaces for the given account. Results are paginated.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces?per_page=50" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": [
    		{
    			"id": "01JSGCEXAMPLE000000000000",
    			"name": "support-agent",
    			"created_at": "2026-04-21T00:00:00.000Z",
    			"updated_at": "2026-04-21T00:00:00.000Z"
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result_info": {
    		"cursor": "next-cursor",
    		"per_page": 50,
    		"count": 1
    	}
    }

### Get a namespace

Retrieves a single namespace by name.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": {
    		"id": "01JSGCEXAMPLE000000000000",
    		"name": "support-agent",
    		"created_at": "2026-04-21T00:00:00.000Z",
    		"updated_at": "2026-04-21T00:00:00.000Z"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Delete a namespace

Marks a namespace for deletion. The namespace name becomes available for reuse after deletion.
    
    
    curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": null,
    	"success": true,
    	"errors": [],
    	"messages": []
    }

## Profiles

Use profile endpoints to manage profiles and operate on memory stored in a named profile. Profiles are created automatically when you first write to them.

### Delete a profile

Marks a profile and all its memories and messages for deletion.
    
    
    curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": null,
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Delete a session

Marks all memories and messages in a profile that are tagged with the given session ID for deletion. Rows from other sessions in the same profile are untouched. Idempotent: deleting a session ID that has no rows is a no-op.
    
    
    curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/sessions/<SESSION_ID>" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": null,
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Ingest messages

Processes a conversation and extracts structured memories from it. Agent Memory identifies facts, events, instructions, and tasks automatically, so you do not need to specify what to remember.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/ingest" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "messages": [
          {
            "role": "user",
            "content": "I prefer concise answers.",
            "timestamp": "2026-04-21T00:00:00.000Z"
          }
        ],
        "sessionId": "chat-2026-04-21"
      }'
    
    
    {
    	"result": null,
    	"success": true,
    	"errors": [],
    	"messages": []
    }

`ingest` is idempotent. Re-ingesting the same conversation does not create duplicate memories.

### Remember a memory

Stores a single memory explicitly. Use `remember` when your application or agent already knows what should be stored.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/remember" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "content": "The user prefers concise answers.",
        "sessionId": "chat-2026-04-21"
      }'
    
    
    {
    	"result": {
    		"id": "01JSGCEXAMPLE000000000000",
    		"type": "instruction",
    		"summary": "The user prefers concise answers.",
    		"content": "The user prefers concise answers.",
    		"sessionId": "chat-2026-04-21",
    		"createdAt": "2026-04-21T00:00:00.000Z",
    		"updatedAt": "2026-04-21T00:00:00.000Z"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Recall memories

Searches stored memories in the profile and returns a synthesized answer grounded in the stored content.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/recall" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{
        "query": "How should I answer this user?",
        "thinkingLevel": "low",
        "responseLength": "medium"
      }'
    
    
    {
    	"result": {
    		"answer": "The user prefers concise answers.",
    		"count": 1,
    		"candidates": [
    			{
    				"id": "01JSGCEXAMPLE000000000000",
    				"summary": "The user prefers concise answers.",
    				"sessionId": "chat-2026-04-21",
    				"score": 0.87
    			}
    		]
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

If no memories match the query, `recall` returns an empty answer.

### List memories

Lists memories stored in the profile.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/memories?per_page=50" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": [
    		{
    			"id": "01JSGCEXAMPLE000000000000",
    			"type": "instruction",
    			"summary": "The user prefers concise answers.",
    			"sessionId": "chat-2026-04-21",
    			"createdAt": "2026-04-21T00:00:00.000Z",
    			"updatedAt": "2026-04-21T00:00:00.000Z"
    		}
    	],
    	"success": true,
    	"errors": [],
    	"messages": [],
    	"result_info": {
    		"cursor": "next-cursor",
    		"per_page": 50,
    		"count": 1
    	}
    }

List entries omit `content`. Use the get memory endpoint to retrieve the full memory.

To filter memories, use the `session_id` and `type` query parameters.

### Get a memory

Retrieves a memory by ID.
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/memories/<MEMORY_ID>" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": {
    		"id": "01JSGCEXAMPLE000000000000",
    		"type": "instruction",
    		"summary": "The user prefers concise answers.",
    		"content": "The user prefers concise answers.",
    		"sessionId": "chat-2026-04-21",
    		"createdAt": "2026-04-21T00:00:00.000Z",
    		"updatedAt": "2026-04-21T00:00:00.000Z"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Delete a memory

Deletes a memory by ID. Removes the memory and any source messages linked to it. Returns the deleted memory.
    
    
    curl -X DELETE "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/memories/<MEMORY_ID>" \
      -H "Authorization: Bearer <API_TOKEN>"
    
    
    {
    	"result": {
    		"id": "01JSGCEXAMPLE000000000000",
    		"type": "instruction",
    		"summary": "The user prefers concise answers.",
    		"content": "The user prefers concise answers.",
    		"sessionId": "chat-2026-04-21",
    		"createdAt": "2026-04-21T00:00:00.000Z",
    		"updatedAt": "2026-04-21T00:00:00.000Z"
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

### Get a summary

Generates a structured Markdown summary of everything stored in a memory profile. Use it to inspect what Agent Memory remembers about a profile.
    
    
    curl -X POST "https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/agent-memory/namespaces/<NAMESPACE_NAME>/profiles/<PROFILE_NAME>/summary" \
      -H "Authorization: Bearer <API_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{}'
    
    
    {
    	"result": {
    		"summary": "## Summary\n\nThe user prefers concise answers."
    	},
    	"success": true,
    	"errors": [],
    	"messages": []
    }

To scope the "Last Session" section of the summary, include the `sessionId` field in the request body.

## Error responses

All endpoints return standard Cloudflare V4 error responses on failure:
    
    
    {
    	"result": null,
    	"success": false,
    	"errors": [
    		{
    			"code": 10008,
    			"message": "Namespace name already exists"
    		}
    	],
    	"messages": []
    }

Common error scenarios include:

Scenario | HTTP status  
---|---  
Invalid namespace name format | `400`  
Authentication failure | `401`  
Namespace name already exists | `409`  
Namespace not found | `404`  
Profile not found | `404`  
  
[PreviousWorkers API](https://developers.cloudflare.com/agent-memory/api/workers-api/)[NextLimits](https://developers.cloudflare.com/agent-memory/platform/limits/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agent-memory/api/http-api.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
