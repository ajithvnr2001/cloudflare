---
url: https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/
title: Stablecoin payments \u00b7 Cloudflare Billing docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:30.431322+00:00
---

# Stablecoin payments · Cloudflare Billing docs

> Source: https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Billing](https://developers.cloudflare.com/billing/)
  3. /Payment methods
  4. /Stablecoin payments



# Stablecoin payments

Last updated Jun 12, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/billing/payment-methods/stablecoin-payments/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow stablecoin payments workSupported stablecoins and walletsRecurring billingPayment failuresRefundsView your payment historyFAQ

You can pay for Cloudflare services with USDC stablecoin at the checkout. Stablecoin payments support one-time charges and recurring billing, including usage-based products.

## How stablecoin payments work

  1. **Checkout** : Select **Crypto** in the payment method picker, alongside card, Apple Pay, and Google Pay.
  2. **Wallet connection** : You are redirected to a Stripe-hosted page at `crypto.stripe.com` to connect your wallet.
  3. **Smart contract permit** : Sign a one-time permit to authorize the initial charge and, for recurring subscriptions, future automatic charges.
  4. **On-chain confirmation** : Your subscription activates after on-chain confirmation, typically within seconds.



For recurring billing, Cloudflare charges your saved wallet each cycle. You only need to act if your wallet balance runs out or you revoke the permit.

## Supported stablecoins and wallets

Item | Value  
---|---  
Stablecoins | USDC on Base and Polygon  
Wallets | MetaMask, Phantom, Coinbase Wallet, and 400+ wallets via WalletConnect  
Invoice currency | US dollars (USD)  
Chargebacks and disputes | Not available. Stablecoin payments are final once confirmed on-chain.  
  
## Recurring billing

The smart contract permit authorizes future automatic charges for:

  * Monthly or annual subscription renewals for paid plans
  * Usage-based charges billed at threshold for Workers, R2, and Stream
  * Prorated charges for plan upgrades



Each charge is processed against the saved permit. No action is required between cycles.

## Payment failures

Stablecoin payments fail for a small number of well-defined reasons:

Reason | What happens | How to resolve  
---|---|---  
Insufficient funds | Your wallet does not have enough USDC | Add USDC to the wallet, then retry. Subscriptions enter dunning until the payment succeeds.  
Approval revoked | You revoked or reduced the permit below the payment amount | Return to the checkout and reconnect your wallet to issue a new permit  
Wallet screening | Pre-transaction screening flagged the wallet | Use a different wallet or payment method  
  
Note

If you have a card on file, Cloudflare falls back to it when a stablecoin charge fails. This protects usage-based products from interruption when your wallet balance fluctuates. Refer to [Additional payment method auto-retry](https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/).

## Refunds

Refunds for stablecoin payments are returned as USDC to the wallet you paid from. Refunds typically arrive within minutes, compared to 5–10 business days for card refunds.

## View your payment history

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/).

  2. Go to **Manage Account** > **Billing**.

[ Go to **Billing** ↗ ](https://dash.cloudflare.com/?to=/:account/billing)
  3. Select **Invoices**. Stablecoin payments are listed with payment method `crypto`.




## FAQ

Network fees and gas

Gas fees for the on-chain transaction are paid by your wallet to the network. Cloudflare does not add a markup or transaction fee for stablecoin payments. The amount charged in USDC matches your invoice amount in USD.

Smart contract permit scope

The permit authorizes charges for the specific subscription you are activating. You can revoke it at any time from your wallet. Revoking it stops future automatic charges; existing subscriptions enter dunning until you reconnect a wallet or switch payment methods.

Multiple payment methods

You can have a crypto wallet and a card on file at the same time. The card serves as a fallback if the wallet charge fails.

Pending state during on-chain confirmation

Stablecoin payments pass through a `processing` state while the on-chain transaction confirms. This typically takes a few seconds but can take longer if the network is congested. The payment resolves automatically.

[PreviousAdditional payment method auto-retry](https://developers.cloudflare.com/billing/payment-methods/additional-payment-method-auto-retry/)[NextHow Cloudflare billing works](https://developers.cloudflare.com/billing/understand/how-billing-works/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/billing/payment-methods/stablecoin-payments.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
