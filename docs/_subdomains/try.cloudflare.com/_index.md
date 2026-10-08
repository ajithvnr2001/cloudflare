---
url: https://try.cloudflare.com/
title: Cloudflare Quick Tunnels
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:29.862867+00:00
---

# Cloudflare Quick Tunnels

> Source: https://try.cloudflare.com/

SEC 0.1 ____

01 · **Quick Tunnels**

# Put localhost on the Internet

One command creates a public, encrypted URL for anything running on your machine. No account, DNS records, or open ports.

Copy the command[View docs](https://developers.cloudflare.com/tunnel/get-started/#quick-tunnels-development)

__Run Terminal

$`cloudflared tunnel --url http://localhost:8000`

ConnectCloudflare edge

✓

**Secure connection established** localhost:8000 · HTTPS · no inbound ports

SharePublic URL

`https://quiet-marble-otter.trycloudflare.com`

SEC 0.2 ____

## Why use Quick Tunnels

### Ready in seconds

No sign-up, configuration file, or DNS propagation. Run one command and get a live URL.

### Cloudflare's network by default

Automatic HTTPS, edge DDoS protection, and globally reachable traffic without exposing your IP.

### Made for development loops

Share previews, receive webhooks, run browser tests, or give a coding agent a real endpoint.

SEC 0.3 ____

Outbound-only architecture

## Your machine stays  
private. The URL goes  
everywhere.

cloudflared establishes an encrypted connection to the nearest Cloudflare location.  
  
Requests return through that connection, so your router never accepts inbound traffic.

Public InternetCloudflare networkYour private network

Request**Teammates & agents**HTTPS from anywhere

Cloudflare edge**Secure global ingress** TLS · routing · DDoS

No inbound ports

Connector**cloudflared**

Origin**localhost:8000**

__Outbound-only connection

 __Automatic HTTPS

 __Ends with the process

SEC 0.4 ____

Agent-ready output

## One command in. One URL out.

Add `--output json` when a script or coding agent needs to read the result. The tunnel still works exactly the same way.

ephemeralmachine-readableno cleanup

agent-runnerTERMINAL

$`cloudflared tunnel --url http://localhost:8000 --output json`

 __Tunnel ready https://quiet-marble-otter.trycloudflare.com

location: lhr01 · protocol: quic

SEC 0.5 ____

Get started

## From localhost to live in three steps

macOSWindowsLinux

01 / INSTALL

### Install cloudflared

Use your package manager. No Cloudflare account required.

`brew install cloudflared`

02 / RUN

### Start your app

Run any local web server on the port you already use.

`npm run dev`

03 / CONNECT

### Open the tunnel

Copy the generated URL and send it anywhere.

`cloudflared tunnel --url http://localhost:8000`

SEC 0.6Start building

## Build without boundaries

Nothing to sign up for. Your next public URL is one command away.

Copy the command[Read the docs](https://developers.cloudflare.com/tunnel/get-started/#quick-tunnels-development)
