---
url: https://developers.cloudflare.com/basin-catalog/get-started/
title: Getting started \u00b7 Cloudflare Basin Catalog docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:05:24.336196+00:00
---

# Getting started · Cloudflare Basin Catalog docs

> Source: https://developers.cloudflare.com/basin-catalog/get-started/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Basin Catalog](https://developers.cloudflare.com/basin-catalog/)
  3. /Getting started



# Getting started

Last updated Oct 1, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/basin-catalog/get-started/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisites1\. Create an R2 bucket and enable the data catalog2\. Create an API token3\. Install uv4\. Install marimo and set up your project with uv5\. Create a Python notebook to interact with the data warehouseLearn more

This guide will instruct you through:

  * Creating your first [R2 bucket](https://developers.cloudflare.com/r2/buckets/) and enabling its [data catalog](https://developers.cloudflare.com/basin-catalog/).
  * Creating an [API token](https://developers.cloudflare.com/r2/api/tokens/) needed for query engines to authenticate with your data catalog.
  * Using [PyIceberg ↗︎](https://py.iceberg.apache.org/) to create your first Iceberg table in a [marimo ↗︎](https://marimo.io/) Python notebook.
  * Using [PyIceberg ↗︎](https://py.iceberg.apache.org/) to load sample data into your table and query it.



## Prerequisites

  1. Sign up for a [Cloudflare account ↗︎](https://dash.cloudflare.com/sign-up/workers-and-pages).
  2. Install [`Node.js` ↗︎](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).



Node.js version manager

Use a Node version manager like [Volta ↗︎](https://volta.sh/) or [nvm ↗︎](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## 1\. Create an R2 bucket and enable the data catalog

  1. If not already logged in, run:

npmyarnpnpm
         
         npx wrangler login
         
         yarn wrangler login
         
         pnpm wrangler login

  2. Create an R2 bucket:

npmyarnpnpm
         
         npx wrangler r2 bucket create r2-data-catalog-tutorial
         
         yarn wrangler r2 bucket create r2-data-catalog-tutorial
         
         pnpm wrangler r2 bucket create r2-data-catalog-tutorial

  3. Enable the catalog on your bucket:

npmyarnpnpm
         
         npx wrangler basin catalog enable r2-data-catalog-tutorial
         
         yarn wrangler basin catalog enable r2-data-catalog-tutorial
         
         pnpm wrangler basin catalog enable r2-data-catalog-tutorial

When you run this command, take note of the **Warehouse** and **Catalog URI**. You will need these later.




  1. In the Cloudflare dashboard, go to the **Basin Catalog** page.

[ Go to **Basin Catalog** ↗ ](https://dash.cloudflare.com/?to=/:account/data-catalog/overview)
  2. Select **Create catalog**.

  3. Enter the bucket name `r2-data-catalog-tutorial`. The wizard creates the bucket automatically if it does not already exist. Optionally choose a location hint.

  4. Review the configuration and select **Create catalog**.

  5. Once created, the catalog detail page displays your **Catalog URI** and **Warehouse name**. Note these values for later.




## 2\. Create an API token

Iceberg clients (including [PyIceberg ↗︎](https://py.iceberg.apache.org/)) must authenticate to the catalog with an [R2 API token](https://developers.cloudflare.com/r2/api/tokens/) that has both R2 and catalog permissions.

  1. In the Cloudflare dashboard, go to the **R2 object storage** page.

[ Go to **Overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/overview)
  2. Select **Manage API tokens**.

  3. Select **Create API token**.

  4. Select the **R2 Token** text to edit your API token name.

  5. Under **Permissions** , choose the **Admin Read & Write** permission. This guide creates and writes to tables, so it requires read and write access. For query-only clients, you can instead use an **Admin Read only** token. For details on choosing the right permission level, refer to [Authenticate your Iceberg engine](https://developers.cloudflare.com/basin-catalog/manage-catalogs/#authenticate-your-iceberg-engine).

  6. Select **Create API Token**.

  7. Note the **Token value**.




## 3\. Install uv

You need to install a Python package manager. In this guide, use [uv ↗︎](https://docs.astral.sh/uv/). If you do not already have uv installed, follow the [installing uv guide ↗︎](https://docs.astral.sh/uv/getting-started/installation/).

## 4\. Install marimo and set up your project with uv

We will use [marimo ↗︎](https://github.com/marimo-team/marimo) as a Python notebook.

  1. Create a directory where our notebook will be stored:
         
         mkdir r2-data-catalog-notebook

  2. Change into our new directory:
         
         cd r2-data-catalog-notebook

  3. Initialize a new uv project (this creates a `.venv` and a `pyproject.toml`):
         
         uv init

  4. Add marimo and required dependencies:
         
         uv add marimo pyiceberg pyarrow pandas




## 5\. Create a Python notebook to interact with the data warehouse

  1. Create a file called `r2-data-catalog-tutorial.py`.

  2. Paste the following code snippet into your `r2-data-catalog-tutorial.py` file:
         
         import marimo
         
         __generated_with = "0.11.31"
         app = marimo.App(width="medium")
         
         
         @app.cell
         def _():
         		import marimo as mo
         		return (mo,)
         
         
         @app.cell
         def _():
         		import pandas
         		import pyarrow as pa
         		import pyarrow.compute as pc
         		import pyarrow.parquet as pq
         
         		from pyiceberg.catalog.rest import RestCatalog
         
         		# Define catalog connection details (replace variables)
         		WAREHOUSE = "<WAREHOUSE>"
         		TOKEN = "<TOKEN>"
         		CATALOG_URI = "<CATALOG_URI>"
         
                 # Connect to Basin Catalog
         		catalog = RestCatalog(
         				name="my_catalog",
         				warehouse=WAREHOUSE,
         				uri=CATALOG_URI,
         				token=TOKEN,
         		)
         		return (
         				CATALOG_URI,
         				RestCatalog,
         				TOKEN,
         				WAREHOUSE,
         				catalog,
         				pa,
         				pandas,
         				pc,
         				pq,
         		)
         
         
         @app.cell
         def _(catalog):
         		# Create default namespace if needed
         		catalog.create_namespace_if_not_exists("default")
         		return
         
         
         @app.cell
         def _(pa):
         		# Create simple PyArrow table
         		df = pa.table({
         				"id": [1, 2, 3],
         				"name": ["Alice", "Bob", "Charlie"],
         				"score": [80.0, 92.5, 88.0],
         		})
         		return (df,)
         
         
         @app.cell
         def _(catalog, df):
         		# Create or load Iceberg table
         		test_table = ("default", "people")
         		if not catalog.table_exists(test_table):
         				print(f"Creating table: {test_table}")
         				table = catalog.create_table(
         						test_table,
         						schema=df.schema,
         				)
         		else:
         				table = catalog.load_table(test_table)
         		return table, test_table
         
         
         @app.cell
         def _(df, table):
         		# Append data
         		table.append(df)
         		return
         
         
         @app.cell
         def _(table):
         		print("Table contents:")
         		scanned = table.scan().to_arrow()
         		print(scanned.to_pandas())
         		return (scanned,)
         
         
         @app.cell
         def _():
         		# Optional cleanup. To run uncomment and run cell
         		# print(f"Deleting table: {test_table}")
         		# catalog.drop_table(test_table)
         		# print("Table dropped.")
         		return
         
         
         if __name__ == "__main__":
         		app.run()

  3. Replace the `CATALOG_URI`, `WAREHOUSE`, and `TOKEN` variables with your values from sections **1** and **2** respectively.

  4. Launch the notebook editor in your browser:
         
         uv run marimo edit r2-data-catalog-tutorial.py

Once your notebook connects to the catalog, the catalog along with its namespaces and tables will appear in the Datasources panel in marimo.




In the Python notebook above, you:

  1. Connect to your catalog.
  2. Create the `default` namespace.
  3. Create a simple PyArrow table.
  4. Create (or load) the `people` table in the `default` namespace.
  5. Append sample data to the table.
  6. Print the contents of the table.
  7. (Optional) Drop the `people` table we created for this tutorial.



## Learn more

### [Managing catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/)

Enable or disable Basin Catalog on your bucket, retrieve configuration details, and authenticate your Iceberg engine.

### [Connect to Iceberg engines](https://developers.cloudflare.com/basin-catalog/config-examples/)

Find detailed setup instructions for Apache Spark and other common query engines.

[PreviousOverview](https://developers.cloudflare.com/basin-catalog/)[NextManage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/basin-catalog/get-started.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
