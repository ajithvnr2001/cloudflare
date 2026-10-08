---
url: https://developers.cloudflare.com/security-center/infrastructure/security-file/
title: Set up your security.txt file \u00b7 Cloudflare Security Center docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:15:29.950008+00:00
---

# Set up your security.txt file · Cloudflare Security Center docs

> Source: https://developers.cloudflare.com/security-center/infrastructure/security-file/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Security Center](https://developers.cloudflare.com/security-center/)
  3. /[Infrastructure](https://developers.cloudflare.com/security-center/infrastructure/)
  4. /Set up your security.txt file



# Set up your security.txt file

Last updated Aug 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/security-center/infrastructure/security-file/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

You can manage your [security.txt ↗︎](https://en.wikipedia.org/wiki/Security.txt) file via the dashboard or the [API](https://developers.cloudflare.com/api/resources/security_txt/).

Note

When using the API, the preferred languages field name is `preferred_languages` (snake_case). For example: `"preferred_languages": "en, de"`.

To manage your security.txt file via the Cloudflare dashboard:

  1. Log in to the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/), select your account and domain.
  2. Go to **Security** > **Settings** and filter by **Web application exploits**.
  3. Under **Security.txt** > **Configurations** , select the edit icon.



From here, you can create and manage your `security.txt` file to provide the security research team with a standardized way to report vulnerabilities.

Fill in the following information:

  * **(Required) Contact** : You can enter one of the following to contact you about security issues:

    * An email address: The email address must start with `mailto:` (for example, `mailto:help@example.com`).
    * A phone number: The phone number must start with `tel:` (for example, `tel:+1 1234567890`).
    * A URL link: The URL link must start with `https://` (for example, `https://example.com`).

Select **Add more** to add multiple contacts.

  * **(Required) Expires at** : Enter the expiration date and time of the `security.txt` file.

  * **Encryption** : A link to a key which security researchers can use to communicate with you.

  * **Acknowledgements** : A link to your acknowledgements page.

  * **Canonical** : Links to your `security.txt` file.

  * **Hiring** : A link to your security-related job openings.

  * **Policy** : A link to a policy describing what security researchers should do when searching for or reporting security issues.

  * **Preferred languages** : A list of language codes that your security team speaks.




Once you have entered the necessary information, select **Save**.

To edit your security.txt file:

  1. Go to **Security** > **Settings** and filter by **Web application exploits**.
  2. Under **Security.txt** > **Configurations** , select the edit icon.



To download your security.txt file:

  1. Go to **Security** > **Settings** and filter by **Web application exploits**.
  2. Under **Security.txt** > **Configurations** , select the download icon.



To delete your security.txt file:

  1. Select **Security** > **Settings** and filter by **Web application exploits**.
  2. Under **Security.txt** > **Configurations** , select the edit icon.
  3. Select **Delete**.



[PreviousOverview](https://developers.cloudflare.com/security-center/infrastructure/)[NextOverview](https://developers.cloudflare.com/security-center/investigate/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/security-center/infrastructure/security-file.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
