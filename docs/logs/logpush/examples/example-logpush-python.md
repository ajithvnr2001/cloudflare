---
url: https://developers.cloudflare.com/logs/logpush/examples/example-logpush-python/
title: Manage Logpush with Python \u00b7 Cloudflare Logs docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:12:11.009456+00:00
---

# Manage Logpush with Python · Cloudflare Logs docs

> Source: https://developers.cloudflare.com/logs/logpush/examples/example-logpush-python/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Logs](https://developers.cloudflare.com/logs/)
  3. /…

[Logpush](https://developers.cloudflare.com/logs/logpush/)

  4. /Logpush examples
  5. /Manage Logpush with Python



# Manage Logpush with Python

Last updated Apr 23, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-python/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can manage your Cloudflare Logpush service using Python. In the script below you can find example requests to create a job, retrieve job details, update job settings, and delete a Logpush job.

Note

The examples below are for zone-scoped datasets. Account-scoped datasets should use `<ACCOUNT_ID>` instead of `<ZONE_ID>`.
    
    
    import json
    import requests
    
    url = "https://api.cloudflare.com/client/v4/"
    
    x_auth_email = "<EMAIL>"
    x_auth_key = "<API_KEY>"
    
    zone_id = "<ZONE_ID>"
    destination_conf = "s3://<BUCKET_NAME>/logs?region=us-west-1"
    
    logpush_url = url + "/zones/%s/logpush" % zone_id
    
    headers = {
      'X-Auth-Email': <EMAIL>,
      'X-Auth-Key': <API_KEY>,
      'Content-Type': 'application/json'
    }
    
    # Create job
    r = requests.post(logpush_url + "/jobs", headers=headers, data=json.dumps({"destination_conf":destination_conf}))
    print(r.status_code, r.text)
    assert r.status_code == 201
    assert r.json()["result"]["enabled"] == False
    
    # Keep id of the new job
    id = r.json()["result"]["id"]
    
    # Get job
    r = requests.get(logpush_url + "/jobs/%s" % id, headers=headers)
    print(r.status_code, r.text)
    assert r.status_code == 200
    
    # Get all jobs for a zone
    r = requests.get(logpush_url + "/jobs", headers=headers)
    print(r.status_code, r.text)
    assert r.status_code == 200
    assert len(r.json()["result"]) > 0
    
    # Update job
    r = requests.put(logpush_url + "/jobs/%s" % id, headers=headers, data=json.dumps({"enabled":True}))
    print(r.status_code, r.text)
    assert r.status_code == 200
    assert r.json()["result"]["enabled"] == True
    
    # Delete job
    r = requests.delete(logpush_url + "/jobs/%s" % id, headers=headers)
    print(r.status_code, r.text)
    assert r.status_code == 200

[PreviousManage Logpush with cURL](https://developers.cloudflare.com/logs/logpush/examples/example-logpush-curl/)[NextParse Cloudflare Logs JSON data](https://developers.cloudflare.com/logs/logpush/parsing-json-log-data/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/logs/logpush/examples/example-logpush-python.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
