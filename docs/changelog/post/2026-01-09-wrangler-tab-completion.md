---
url: https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/
title: Shell tab completions for Wrangler CLI \u00b7 Changelog
method: scrapling+scrapegraph
fetched_at: 2026-10-10T14:38:45.362770+00:00
---

# Shell tab completions for Wrangler CLI · Changelog

> Source: https://developers.cloudflare.com/changelog/post/2026-01-09-wrangler-tab-completion/

# Changelog

New updates and improvements at Cloudflare.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)January 9, 2026

## Shell tab completions for Wrangler CLI

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now includes built-in shell tab completion support, making it faster and easier to navigate commands without memorizing every option. Press Tab as you type to autocomplete commands, subcommands, flags, and even option values like log levels.

Tab completions are supported for Bash, Zsh, Fish, and PowerShell.

#### Setup

Generate the completion script for your shell and add it to your configuration file:
    
    
    # Bash
    wrangler complete bash >> ~/.bashrc
    
    # Zsh
    wrangler complete zsh >> ~/.zshrc
    
    # Fish
    wrangler complete fish >> ~/.config/fish/config.fish
    
    # PowerShell
    wrangler complete powershell >> $PROFILE

After adding the script, restart your terminal or source your configuration file for the changes to take effect. Then you can simply press Tab to see available completions:
    
    
    wrangler d<TAB>          # completes to 'deploy', 'dev', 'd1', etc.
    wrangler kv <TAB>        # shows subcommands: namespace, key, bulk

Tab completions are dynamically generated from Wrangler's command registry, so they stay up-to-date as new commands and options are added. This feature is powered by [`@bomb.sh/tab` ↗︎](https://github.com/bombshell-dev/tab/).

See the [`wrangler complete` documentation](https://developers.cloudflare.com/workers/wrangler/commands/general/#complete) for more details.
