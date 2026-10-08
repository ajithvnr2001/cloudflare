---
url: https://www.cloudflare.com/learning/cloud/what-is-block-storage/
title: What is block storage?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:53.922714+00:00
---

# What is block storage?

> Source: https://www.cloudflare.com/learning/cloud/what-is-block-storage/

[ Learning Center ](https://www.cloudflare.com/learning/) / the cloud

##  What is block storage? 

Block storage is a type of cloud storage that works by dividing data into blocks. Block storage allows for quick data retrieval. 

[Learning Center](https://www.cloudflare.com/learning)/the cloud/[What is application modernization?](https://www.cloudflare.com/learning/cloud/application-modernization/)[What is cloud-native security?](https://www.cloudflare.com/learning/cloud/cloud-native-security/)[How Cloudflare works with any cloud infrastructure](https://www.cloudflare.com/learning/cloud/cloudflare-and-the-cloud/)[What is a cloud-native application protection platform (CNAPP)?](https://www.cloudflare.com/learning/cloud/cnapp/)[How does hybrid cloud architecture work?](https://www.cloudflare.com/learning/cloud/how-does-hybrid-cloud-architecture-work/)[How to refactor applications](https://www.cloudflare.com/learning/cloud/how-to-refactor-applications/)[How to rehost applications](https://www.cloudflare.com/learning/cloud/how-to-rehost-applications/)[How to replatform applications](https://www.cloudflare.com/learning/cloud/how-to-replatform-applications/)[Multi-cloud vs. hybrid cloud: What's the difference?](https://www.cloudflare.com/learning/cloud/multicloud-vs-hybrid-cloud/)[Next-generation firewall (NGFW) vs. firewall-as-a-service (FWaaS)](https://www.cloudflare.com/learning/cloud/ngfw-vs-fwaas/)[Object storage vs. block storage: How are they different?](https://www.cloudflare.com/learning/cloud/object-storage-vs-block-storage/)[What are data egress fees?](https://www.cloudflare.com/learning/cloud/what-are-data-egress-fees/)[What is a connectivity cloud? | Connectivity cloud definition](https://www.cloudflare.com/learning/cloud/what-is-a-connectivity-cloud/)[What is a data lake?](https://www.cloudflare.com/learning/cloud/what-is-a-data-lake/)[What is a private cloud? | Private cloud vs. public cloud](https://www.cloudflare.com/learning/cloud/what-is-a-private-cloud/)[What is a public cloud? | Public vs. private cloud](https://www.cloudflare.com/learning/cloud/what-is-a-public-cloud/)[What is a virtual machine?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/)[What is a virtual private cloud (VPC)?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/)[What is AWS data transfer pricing? ](https://www.cloudflare.com/learning/cloud/what-is-aws-data-transfer-pricing/)[What is blob storage?](https://www.cloudflare.com/learning/cloud/what-is-blob-storage/)[What is block storage?](https://www.cloudflare.com/learning/cloud/what-is-block-storage/)[What is cloud migration? | Cloud migration strategy](https://www.cloudflare.com/learning/cloud/what-is-cloud-migration/)[What is cloud networking?](https://www.cloudflare.com/learning/cloud/what-is-cloud-networking/)[How does cloud security work? | Cloud computing security](https://www.cloudflare.com/learning/cloud/what-is-cloud-security/)[What is cloud storage?](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/)[What is cloud security posture management (CSPM)?](https://www.cloudflare.com/learning/cloud/what-is-cspm/)[What is a cloud workload protection platform (CWPP)?](https://www.cloudflare.com/learning/cloud/what-is-cwpp/)[What is data migration? | Definition and common processes](https://www.cloudflare.com/learning/cloud/what-is-data-migration/)[What is digital transformation?](https://www.cloudflare.com/learning/cloud/what-is-digital-transformation/)[What is data security posture management (DSPM)?](https://www.cloudflare.com/learning/cloud/what-is-dspm/)[What is IaaS (infrastructure-as-a-service)?](https://www.cloudflare.com/learning/cloud/what-is-iaas/)[What is multi-cloud management?](https://www.cloudflare.com/learning/cloud/what-is-multicloud-management/)[What is multitenancy? | Multitenant architecture](https://www.cloudflare.com/learning/cloud/what-is-multitenancy/)[What is object storage?](https://www.cloudflare.com/learning/cloud/what-is-object-storage/)[What is SaaS? | SaaS definition](https://www.cloudflare.com/learning/cloud/what-is-saas/)[What is a SaaS management platform (SMP)? ](https://www.cloudflare.com/learning/cloud/what-is-smp/)[What is SaaS security posture management (SSPM)?](https://www.cloudflare.com/learning/cloud/what-is-sspm/)[What is the cloud?](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)[What is vendor lock-in? | Vendor lock-in and cloud computing](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/)[What is multicloud?](https://www.cloudflare.com/learning/cloud/what-is-multicloud/)[What is hybrid cloud?](https://www.cloudflare.com/learning/cloud/what-is-hybrid-cloud/)[What is a cloud firewall?](https://www.cloudflare.com/learning/cloud/what-is-a-cloud-firewall/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define block storage 
  * Describe how block storage works 
  * Understand how block storage compares to object storage 



Related content  [ Object storage vs. block storage: How are they different? ](https://www.cloudflare.com/learning/cloud/object-storage-vs-block-storage/)[ What is cloud storage? ](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/)[ What is blob storage? ](https://www.cloudflare.com/learning/cloud/what-is-blob-storage/)[ What is object storage? ](https://www.cloudflare.com/learning/cloud/what-is-object-storage/)[ What is the cloud? ](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/)

On this page

  * What is block storage?

  * How does block storage work?

    * Data write

    * Unique identifier

    * Data lookup table

    * Data read

  * What are the benefits of block storage? What are the downsides?

  * How does block storage compare to object storage?

  * How does block storage compare to file storage?

  * What is Cloudflare R2?

  * FAQs

    * What is block storage?

    * What are common use cases for block storage?

    * How do unique identifiers work in block storage?

    * How does block storage compare to object storage?

    * Why is block storage considered high-performance?

    * What is the purpose of a data lookup table in block storage?

    * What are the metadata limitations of block storage?




## What is block storage?

Block storage is a type of [cloud storage](https://www.cloudflare.com/learning/cloud/what-is-cloud-storage/) that divides files and data into equally sized blocks. This storage method allows for fast retrieval of data, since it does not rely on a file system. Think of the difference between looking through a city library's digital catalog to find a book, and knowing exactly where a book is on the shelves. The former is more like file storage; the latter is more like block storage.

Developers often prefer block storage for applications that regularly need to load data from the backend. Block storage is fast and scales up extremely well. It also works well with several types of computing and networking models, including [container](https://www.cloudflare.com/learning/serverless/serverless-vs-containers/) computing, [virtual machines](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-machine/), and storage area networks (SANs).

However, block storage is not without its downsides. File metadata has to be very basic and usually cannot be customized (imagine a library where only the title of a book is recorded). Block storage is also a more costly storage option than some other cloud storage models, like [object storage](https://www.cloudflare.com/learning/cloud/what-is-object-storage/).

## How does block storage work?

#### Data write

When an application that uses block storage writes data to the block storage database, instead of storing it as one file, it divides the data into several sections — the "blocks." These blocks do not have to be stored in any particular order.

#### Unique identifier

Each block has a unique identifier number that enables the application to find it later.

#### Data lookup table

These unique identifiers are stored in a data lookup table — a format that allows the application to easily find where each block is when it is needed.

#### Data read

Whenever data stored in the blocks is requested, the application consults the data lookup table to find where the requested data is stored. Usually, the requested data is spread out over multiple blocks. The application uses the identifiers from the table to retrieve the data, and it merges the disparate blocks back into their original form.

## What are the benefits of block storage? What are the downsides?

Benefits include:

  * **Block storage is fast:** The use of unique identifiers, rather than searching for data using metadata or a file hierarchy, means that data can be retrieved extremely quickly.

  * **There are multiple paths to data:** Block storage allows data to be reached in multiple ways, since the unique identifier is all that is needed for retrieval. By contrast, file storage involves following the file hierarchy path until arriving at the desired file.




Downsides include:

  * **Block storage is expensive:** Partially because it is optimized for fast performance, block storage costs more than object storage. Consider how a race car costs more than a large passenger van.

  * **Block storage metadata is limited:** Block storage only includes basic file attributes as metadata.




## How does block storage compare to object storage?

Object storage keeps files and data in what is called a "[data lake](https://www.cloudflare.com/learning/cloud/what-is-a-data-lake/)," a non-hierarchical collection of unstructured data. Any type of data or file format can go into object storage, which means that unlike block storage, metadata can be complex and customized. Media (such as video and audio), logs, and disaster recovery backups are some of the common uses for object storage, although it is extremely flexible and works with a variety of use cases.

Because object storage is not structured or hierarchical, it can quickly, and almost limitlessly, store vast quantities of data — just as tossing clothes loosely into a big bag is a faster way to pack for a vacation than carefully folding and sorting clothes into a suitcase. However, much like packing in this fashion, object storage can make data retrieval less efficient.

Object storage vs. block storage Object storage Block storage

**Storage capacity** Almost unlimited Depends on vendor

**Data retrieval** Sometimes slow Fast

**Metadata** Customizable Basic, limited

[Blob storage](https://www.cloudflare.com/learning/cloud/what-is-blob-storage/) is another type of object storage, used for Binary Large Objects (colloquially called "blobs"). It also works best for unstructured data that does not need to be retrieved often.

## How does block storage compare to file storage?

Cloud file storage is essentially a traditional hierarchy of files and folders, hosted in [the cloud](https://www.cloudflare.com/learning/cloud/what-is-the-cloud/). Folders of data nest within directories and subdirectories, and inside each folder, files are tagged with metadata for easy identification. File storage keeps data organized, but it does not scale up to large amounts of data very well. Going through the hierarchy adds time to data retrieval.

However, file storage may work just fine for some use cases. Individuals who do not need to store and retrieve data on an enterprise-level scale may find that file storage fits their needs.

## What is Cloudflare R2?

The cost of data retrieval, also known as data egress, is a [major concern](https://www.cloudflare.com/the-net/cloud-egress-fees-challenge-future-ai/) for organizations today. To combat these rising costs, Cloudflare offers zero-egress-fee object storage via a service called [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/). R2 allows for fast and free data retrieval, and when paired with [Cloudflare Workers](https://workers.cloudflare.com/)' distributed code functions, it is endlessly customizable. Cloudflare aims to help developers and organizations avoid [vendor lock-in](https://www.cloudflare.com/learning/cloud/what-is-vendor-lock-in/) with this service.

## FAQs

#### What is block storage?

Block storage is a cloud storage method that splits data into equally sized blocks. Block storage data retrieval is fast because each block can be accessed directly, rather than searching through a file system.

#### What are common use cases for block storage?

Block storage is often used for applications that need to load backend data frequently. It works well with certain cloud infrastructure models, including containers, virtual machines, and storage area networks (SANs).

#### How do unique identifiers work in block storage?

Each block of data gets a unique identifier number. This number lets the system quickly find and retrieve specific blocks when needed.

#### How does block storage compare to object storage?

While object storage is overall more flexible, scalable, and cheaper, block storage is fast and efficient. Block storage divides data into blocks and assigns each block an identifier, object storage uses a data lake and finds data by searching via metadata. Object storage is essentially unlimited, while block storage capacity depends on the vendor, and expanding it can be expensive.

#### Why is block storage considered high-performance?

Block storage is fast because it retrieves data using unique identifiers instead of searching through a file hierarchy or using metadata.

#### What is the purpose of a data lookup table in block storage?

A data lookup table keeps track of where each block is stored using the blocks' identifiers. When data is requested, the system uses this table to find the right blocks.

#### What are the metadata limitations of block storage?

Block storage only stores basic file information as metadata. There is usually little ability to customize or add extra details about the data. This contrasts with object storage, which typically allows a lot of leeway for customizing metadata.
