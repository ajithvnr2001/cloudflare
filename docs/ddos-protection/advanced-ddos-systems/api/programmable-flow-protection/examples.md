---
url: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/
title: Common API calls \u00b7 Cloudflare DDoS Protection docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:10:44.784844+00:00
---

# Common API calls · Cloudflare DDoS Protection docs

> Source: https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/

  1. [Home](https://developers.cloudflare.com/)
  2. /[DDoS Protection](https://developers.cloudflare.com/ddos-protection/)
  3. /…

Advanced DDoS systemsAPI configuration

  4. /[Programmable Flow Protection](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/)
  5. /Common API calls



# Common API calls

Last updated Jun 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewList all programsUpload a programUpdate a programDelete a programList all rulesCreate a ruleCreate a rule with regional scopeUpdate a ruleDelete a ruleDebug a program with PCAP

The following sections contain example requests for common API calls. For a list of available API endpoints, refer to [Endpoints](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/#endpoints).

## List all programs

This example fetches all Programmable Flow Protection programs in the account.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/programs" \
    --header "Authorization: Bearer <API_TOKEN>"

Responsejson
    
    
    {
      "result": [
        {
          "id": "<PROGRAM_ID>",
          "name": "rate-limiter",
          "status": "success",
          "created_on": "<TIMESTAMP>",
          "modified_on": "<TIMESTAMP>"
        }
      ],
      "success": true,
      "errors": [],
      "messages": []
    }

## Upload a program

This example uploads a new eBPF program written in C. The program source code is sent as the request body with `Content-Type: text/plain`.

Include the optional `X-Program-Name` header to specify a human-readable program name. If omitted, the API generates a UUID as the program name.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/programs" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: text/plain" \
    --header "X-Program-Name: my-rate-limiter" \
    --data-binary "@/path/to/program.c"

Responsejson
    
    
    {
      "result": {
        "id": "<PROGRAM_ID>",
        "name": "my-rate-limiter",
        "status": "success",
        "created_on": "<TIMESTAMP>",
        "modified_on": "<TIMESTAMP>"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

If the program fails compilation or verification, the API returns a detailed error message:

Example error responsejson
    
    
    {
      "result": null,
      "success": false,
      "errors": [
        {
          "code": 1001,
          "message": "Program verification failed: invalid memory access at line 42"
        }
      ],
      "messages": []
    }

## Update a program

This example updates an existing program with new source code. You can update a program even if it is currently in use by one or more rules. If the new program fails compilation or verification, the update fails and the existing program remains active.

Requestbash
    
    
    curl --request PATCH \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: text/plain" \
    --data-binary "@/path/to/updated-program.c"

Responsejson
    
    
    {
      "result": {
        "id": "<PROGRAM_ID>",
        "name": "program",
        "status": "success",
        "created_on": "<TIMESTAMP>",
        "modified_on": "<TIMESTAMP>"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

## Delete a program

This example deletes a program. You cannot delete a program that is currently referenced by an active rule.

Requestbash
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}" \
    --header "Authorization: Bearer <API_TOKEN>"

Responsejson
    
    
    {
      "result": null,
      "success": true,
      "errors": [],
      "messages": []
    }

## List all rules

This example fetches all Programmable Flow Protection rules in the account.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/rules" \
    --header "Authorization: Bearer <API_TOKEN>"

Responsejson
    
    
    {
      "result": [
        {
          "id": "<RULE_ID>",
          "program_id": "<PROGRAM_ID>",
          "scope": "global",
          "name": "global",
          "mode": "enabled",
          "expression": "",
          "created_on": "<TIMESTAMP>",
          "modified_on": "<TIMESTAMP>"
        }
      ],
      "success": true,
      "errors": [],
      "messages": []
    }

## Create a rule

This example creates a Programmable Flow Protection rule with a global scope in monitoring mode.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/rules" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "program_id": "<PROGRAM_ID>",
      "scope": "global",
      "name": "global",
      "mode": "monitoring"
    }'

Responsejson
    
    
    {
      "result": {
        "id": "<RULE_ID>",
        "program_id": "<PROGRAM_ID>",
        "scope": "global",
        "name": "global",
        "mode": "monitoring",
        "expression": "",
        "created_on": "<TIMESTAMP>",
        "modified_on": "<TIMESTAMP>"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

Refer to [JSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/) for more information on the fields in the JSON body.

## Create a rule with regional scope

This example creates a rule scoped to the Western Europe region with an expression filter.

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/rules" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "program_id": "<PROGRAM_ID>",
      "scope": "region",
      "name": "WEUR",
      "mode": "enabled",
      "expression": "ip.dst in { 192.0.2.0/24 }"
    }'

Responsejson
    
    
    {
      "result": {
        "id": "<RULE_ID>",
        "program_id": "<PROGRAM_ID>",
        "scope": "region",
        "name": "WEUR",
        "mode": "enabled",
        "expression": "ip.dst in { 192.0.2.0/24 }",
        "created_on": "<TIMESTAMP>",
        "modified_on": "<TIMESTAMP>"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

Refer to [JSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/) for more information on the fields in the JSON body.

## Update a rule

This example updates an existing rule. You can update the mode, scope, and expression, but not the program. To change the program, delete the rule and create a new one.

Requestbash
    
    
    curl --request PATCH \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/json" \
    --data '{
      "mode": "enabled"
    }'

Responsejson
    
    
    {
      "result": {
        "id": "<RULE_ID>",
        "program_id": "<PROGRAM_ID>",
        "scope": "global",
        "name": "global",
        "mode": "enabled",
        "expression": "",
        "created_on": "<TIMESTAMP>",
        "modified_on": "<TIMESTAMP>"
      },
      "success": true,
      "errors": [],
      "messages": []
    }

Refer to [JSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/) for more information on the fields in the JSON body.

## Delete a rule

This example deletes an existing rule.

Requestbash
    
    
    curl --request DELETE \
    "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/rules/{rule_id}" \
    --header "Authorization: Bearer <API_TOKEN>"

Responsejson
    
    
    {
      "result": null,
      "success": true,
      "errors": [],
      "messages": []
    }

## Debug a program with PCAP

This example runs a program against a PCAP file for debugging. The API returns an annotated PCAP file with the program verdict for each packet.

The request body must contain the PCAP file in binary format. The API automatically detects the IP header offset based on the input PCAP. To override automatic detection, use the optional `ip_offset` query parameter to specify the number of bytes the IP header is offset by in each packet (for example, `14` for Ethernet frames).

Requestbash
    
    
    curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/magic/programmable_flow_protection/configs/programs/{program_id}/pcap" \
    --header "Authorization: Bearer <API_TOKEN>" \
    --header "Content-Type: application/vnd.tcpdump.pcap" \
    --data-binary "@/path/to/input.pcap" \
    --output output.pcap

The output PCAP file contains the same packets as the input file, but with annotations on each packet. The Packet Comment annotation may contain:

  * Program return value: `CF_EBPF_PASS` or `CF_EBPF_DROP`
  * `Ignored`: if the incoming packet is not UDP
  * `Analytics tag`: the custom network analytics tag set by the program on this packet, if any
  * `Challenge packet`: the challenge packet emitted from the program back to the client, if any



[PreviousConfigure via the API](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/)[NextJSON objects](https://developers.cloudflare.com/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/json-objects/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/ddos-protection/advanced-ddos-systems/api/programmable-flow-protection/examples.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
