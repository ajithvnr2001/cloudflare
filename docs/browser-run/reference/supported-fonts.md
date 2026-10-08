---
url: https://developers.cloudflare.com/browser-run/reference/supported-fonts/
title: Supported fonts \u00b7 Cloudflare Browser Run docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:39.080474+00:00
---

# Supported fonts · Cloudflare Browser Run docs

> Source: https://developers.cloudflare.com/browser-run/reference/supported-fonts/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Browser Run](https://developers.cloudflare.com/browser-run/)
  3. /Reference
  4. /Supported fonts



# Supported fonts

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/browser-run/reference/supported-fonts/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPre-installed fonts Generic CSS font family support Common system fonts Open source and extended fonts International fonts

Browser Run uses a managed Chromium environment that includes a standard set of fonts. When you generate a screenshot or PDF, text is rendered using the fonts available in this environment.

If your webpage specifies a font that is not supported yet, Chromium will automatically fall back to a similar supported font. If you would like to use a font that is not currently supported, refer to [Custom fonts](https://developers.cloudflare.com/browser-run/features/custom-fonts/).

## Pre-installed fonts

The following sections list the fonts available in the Browser Run environment.

### Generic CSS font family support

The following generic CSS font families are supported:

  * `serif`
  * `sans-serif`
  * `monospace`
  * `cursive`
  * `fantasy`



### Common system fonts

  * Andale Mono
  * Arial
  * Arial Black
  * Comic Sans MS
  * Courier
  * Courier New
  * Georgia
  * Helvetica
  * Impact
  * Lucida Handwriting
  * Times
  * Times New Roman
  * Trebuchet MS
  * Verdana
  * Webdings



### Open source and extended fonts

  * Bitstream Vera (Serif, Sans, Mono)
  * Cyberbit
  * DejaVu (Serif, Sans, Mono)
  * FreeFont (FreeSerif, FreeSans, FreeMono)
  * GFS Neohellenic
  * Liberation (Serif, Sans, Mono)
  * Open Sans
  * Roboto



### International fonts

Browser Run includes additional font packages for non-Latin scripts and emoji:

  * IPAfont Gothic (Japanese)
  * Indic fonts (Devanagari, Bengali, Tamil, and others)
  * KACST fonts (Arabic)
  * Noto CJK (Chinese, Japanese, Korean)
  * Noto Color Emoji
  * TLWG Thai fonts
  * WenQuanYi Zen Hei (Chinese)



[PreviousAutomatic request headers](https://developers.cloudflare.com/browser-run/reference/automatic-request-headers/)[NextQuick Actions timeouts](https://developers.cloudflare.com/browser-run/reference/timeouts/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/browser-run/reference/supported-fonts.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
