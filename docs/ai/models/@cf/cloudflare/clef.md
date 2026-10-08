---
url: https://developers.cloudflare.com/ai/models/%40cf/cloudflare/clef/
title: clef (Cloudflare) \u00b7 Cloudflare AI docs \u00b7 Cloudflare AI docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:44.921100+00:00
---

# clef (Cloudflare) · Cloudflare AI docs · Cloudflare AI docs

> Source: https://developers.cloudflare.com/ai/models/%40cf/cloudflare/clef/

  1. [Home](https://developers.cloudflare.com/)
  2. /[AI](https://developers.cloudflare.com/ai/)
  3. /[Models](https://developers.cloudflare.com/ai/models/)
  4. /Models



![Cloudflare logo](https://developers.cloudflare.com/_astro/cloudflare.DP8rkHys.svg)

# clef

Text Generation • Cloudflare

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ai/models/%40cf/cloudflare/clef/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

`@cf/cloudflare/clef`

  * Cloudflare-hosted
  * Vision



Clef is a 27B multimodal decision model that turns a state and a schema of typed questions into decisions. It reads the state as text, JSON, images, or video, and returns a probability for every allowed option of every question.

Model Info|   
---|---  
Context Window[ ↗](https://developers.cloudflare.com/workers-ai/platform/glossary/)| 65,536 tokens  
Terms and License| [link ↗](https://huggingface.co/Cloudflare/clef/blob/main/LICENSE)  
More information| [link ↗](https://huggingface.co/Cloudflare/clef)  
Vision| Yes  
Unit Pricing| $0.24 per M input tokens  
  
## Usage
    
    
    export interface Env {
    	AI: Ai;
    }
    
    export default {
    	async fetch(request, env): Promise<Response> {
    		const response = await env.AI.run("@cf/cloudflare/clef", {
    			model: "clef",
    			state: "Checkout has been failing for every customer for the last hour.",
    			questions: {
    				urgent: {
    					type: "noul",
    					instructions: "Is this support request urgent?",
    				},
    				team: {
    					type: "choice",
    					instructions: "Which team should handle this request?",
    					criteria: {
    						billing: "Payments, invoices, and refunds",
    						technical: "Outages, errors, and configuration",
    						sales: "Plans and upgrades",
    					},
    				},
    				severity: {
    					type: "score",
    					instructions: "How severe is the customer impact?",
    					criteria: ["No impact", "Minor", "Major", "Critical"],
    				},
    			},
    		});
    
    		// response.answers.urgent   -> probability the request is urgent
    		// response.answers.team     -> chosen team with per-option probabilities
    		// response.answers.severity -> probability-weighted score (0 = lowest level)
    		return Response.json(response);
    	},
    } satisfies ExportedHandler<Env>;
    
    
    import os
    import requests
    
    ACCOUNT_ID = "your-account-id"
    AUTH_TOKEN = os.environ.get("CLOUDFLARE_AUTH_TOKEN")
    
    response = requests.post(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/@cf/cloudflare/clef",
        headers={"Authorization": f"Bearer {AUTH_TOKEN}"},
        json={
            "model": "clef",
            "state": "Checkout has been failing for every customer for the last hour.",
            "questions": {
                "urgent": {
                    "type": "noul",
                    "instructions": "Is this support request urgent?",
                },
                "team": {
                    "type": "choice",
                    "instructions": "Which team should handle this request?",
                    "criteria": {
                        "billing": "Payments, invoices, and refunds",
                        "technical": "Outages, errors, and configuration",
                        "sales": "Plans and upgrades",
                    },
                },
                "severity": {
                    "type": "score",
                    "instructions": "How severe is the customer impact?",
                    "criteria": ["No impact", "Minor", "Major", "Critical"],
                },
            },
        },
    )
    print(response.json())
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/cloudflare/clef \
      -X POST \
      -H "Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN" \
      -d '{
        "model": "clef",
        "state": "Checkout has been failing for every customer for the last hour.",
        "questions": {
          "urgent": { "type": "noul", "instructions": "Is this support request urgent?" },
          "team": {
            "type": "choice",
            "instructions": "Which team should handle this request?",
            "criteria": {
              "billing": "Payments, invoices, and refunds",
              "technical": "Outages, errors, and configuration",
              "sales": "Plans and upgrades"
            }
          },
          "severity": {
            "type": "score",
            "instructions": "How severe is the customer impact?",
            "criteria": ["No impact", "Minor", "Major", "Critical"]
          }
        }
      }'

## Parameters

model

`string`requiredpattern: ^\s*(clef|clef-flash)\s*$Required. The model selector: "clef" for @cf/cloudflare/clef, "clef-flash" for @cf/cloudflare/clef-flash.

state

``requiredRequired. The content to evaluate: a string, or structured data (object/array) such as records, chat logs, or application state. Long text state is truncated to fit the model's token limit.

▶questions{}

`object`requiredminProperties: 1maxProperties: 64Map of question id to a typed question (noul, choice, or score). 1 to 64 questions; ids may use letters, digits, '_', '.', '-' (max 100 chars). Answers are returned under the same ids.

▶images[]

`array`maxItems: 4Clef extension to the System One API. Optional embedded PNG, JPEG, or WebP images placed before the state (max 4; 4 MiB and 16 megapixels each, 8 MiB total decoded; whole request body max 13 MiB). Remote URLs are not accepted.

model

`string`The model that performed the evaluation.

▶answers{}

`object`One answer per question, keyed by the question ids from the request.

▶usage{}

`object`

## API Schemas (Raw)

Input[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clef/schema-input.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clef/schema-input.json "Download")

Output[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clef/schema-output.json "Open")[](https://developers.cloudflare.com/ai/models/@cf/cloudflare/clef/schema-output.json "Download")

Was this helpful?

YesNo

[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
