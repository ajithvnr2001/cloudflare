---
url: https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/
title: What is image compression?
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:20.811147+00:00
---

# What is image compression?

> Source: https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/

[ Learning Center ](https://www.cloudflare.com/learning/) / performance

##  What is image compression? 

Compressing an image reduces its file size. Image compression can be either lossy or lossless. 

[Learning Center](https://www.cloudflare.com/learning)/performance/[What is cloud load balancing? | LBaaS](https://www.cloudflare.com/learning/performance/cloud-load-balancing-lbaas/)[What is application availability?](https://www.cloudflare.com/learning/performance/glossary/application-availability/)[What is an image optimizer? | How to reduce image sizes](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/)[What is image compression?](https://www.cloudflare.com/learning/performance/glossary/what-is-image-compression/)[What is latency? | How to fix latency](https://www.cloudflare.com/learning/performance/glossary/what-is-latency/)[How do DCL and FCP affect SEO? | Web performance metrics](https://www.cloudflare.com/learning/performance/how-dcl-and-fcp-affect-seo/)[Mobile performance: How to make a site mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-site-mobile-friendly/)[How to manage application performance](https://www.cloudflare.com/learning/performance/how-to-manage-app-performance/)[How to minify CSS for better website performance](https://www.cloudflare.com/learning/performance/how-to-minify-css/)[HTTP/2 vs. HTTP/1.1: How do they affect web performance?](https://www.cloudflare.com/learning/performance/http2-vs-http1.1)[Load balancing for multi-cloud and hybrid cloud: How it works](https://www.cloudflare.com/learning/performance/load-balancing-multi-cloud-hybrid-cloud/)[Log retention best practices](https://www.cloudflare.com/learning/performance/log-retention-best-practices/)[How to make the Internet faster for everyone](https://www.cloudflare.com/learning/performance/more/speed-up-the-web/)[How website performance affects conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/)[How to keep a website from going down](https://www.cloudflare.com/learning/performance/preventing-downtime/)[What is the difference between routing and smart routing?](https://www.cloudflare.com/learning/performance/routing-vs-smart-routing/)[Tips to improve website speed](https://www.cloudflare.com/learning/performance/speed-up-a-website/)[What is a static site generator?](https://www.cloudflare.com/learning/performance/static-site-generator/)[How to test the speed of a website](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/)[Types of load balancing algorithms](https://www.cloudflare.com/learning/performance/types-of-load-balancing-algorithms/)[What are the Core Web Vitals (CWV)?](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)[What is digital experience monitoring (DEM)?](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/)[What is DNS-based load balancing?](https://www.cloudflare.com/learning/performance/what-is-dns-load-balancing/)[What is HTTP/3?](https://www.cloudflare.com/learning/performance/what-is-http3/)[What is JAMstack?](https://www.cloudflare.com/learning/performance/what-is-jamstack/)[What is lazy loading?](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/)[What is load balancing? | How load balancers work](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[What is observability?](https://www.cloudflare.com/learning/performance/what-is-observability/)[What is server failover? | Failover meaning](https://www.cloudflare.com/learning/performance/what-is-server-failover/)[Why minify JavaScript code?](https://www.cloudflare.com/learning/performance/why-minify-javascript-code/)[Why does site speed matter?](https://www.cloudflare.com/learning/performance/why-site-speed-matters/)[How does website speed boost SEO?](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/)[How to make a website mobile friendly](https://www.cloudflare.com/learning/performance/how-to-make-a-website-mobile-friendly/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define image compression 
  * Explain why compression is important for image optimization 
  * Contrast lossy vs. lossless image compression 
  * Understand common image compression methods and algorithms 



Related content  [ What is load balancing? | How load balancers work ](https://www.cloudflare.com/learning/performance/what-is-load-balancing/)[ What are the Core Web Vitals (CWV)? ](https://www.cloudflare.com/learning/performance/what-are-core-web-vitals/)

On this page

  * What is image compression?

  * Why is image compression important?

  * What is lossy image compression?

    * Lossy image compression methods

  * What is lossless image compression?

    * Lossless compression methods

  * What are some common image compression algorithms?

  * How to compress an image using Cloudflare




## What is image compression?

Image compression is a process that makes image files smaller. Image compression most often works either by removing bytes of information from the image, or by using an image compression algorithm to rewrite the image file in a way that takes up less storage space. Compressing an image is an effective way to ensure that the image loads quickly when a user interacts with a website or application. It is an important part of [image optimization](https://www.cloudflare.com/learning/performance/glossary/what-is-an-image-optimizer/).

As an example, here is an image that is 96 KB in size:

![Example image of globe at 96 KB](https://images.ctfassets.net/slt3lc6tev37/5wELE1UkznykBr19t50hR4/5e4da734e64d5dcc75e5506a355b71ed/example-image-96-kb.jpg)Example image of globe at 96 KB

Here is the same image, compressed to 70 KB:

![Example image of globe at 70 KB](https://images.ctfassets.net/slt3lc6tev37/3HvNfky6HzFsLOx8cz4vdR/1c6801dde97ae3c8685553db5a4fb8ff/example-image-compressed-70-kb.jpeg)Example image of globe at 70 KB

And here it is compressed to 35 KB:

![Example image of globe at 35 KB, image is blurry](https://images.ctfassets.net/slt3lc6tev37/2Z8hRJMBxmExCiPDdi9bHg/5640fcd15d8c7c0e466fe76aef48bb3d/example-image-compressed-35-kb.jpeg)Example image of globe at 35 KB, image is blurry

## Why is image compression important?

Compressed images load faster than uncompressed images. This matters because the speed at which webpages and applications load has a huge impact on [SEO](https://www.cloudflare.com/learning/performance/how-website-speed-boosts-seo/), [conversion rates](https://www.cloudflare.com/learning/performance/more/website-performance-conversion-rates/), the user's [digital experience](https://www.cloudflare.com/learning/performance/what-is-digital-experience-monitoring/), and other crucial metrics. Improving [web performance](https://www.cloudflare.com/learning/performance/why-site-speed-matters/) is one of the major ways that developers optimize websites.

Image compression is typically used alongside [other methods](https://www.cloudflare.com/learning/performance/speed-up-a-website/) for improving web performance as well. For instance, a [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) caches content to deliver it more quickly to end users. [Load balancing](https://www.cloudflare.com/learning/performance/what-is-load-balancing/) helps prevent web servers from becoming overloaded. The use of [lazy loading](https://www.cloudflare.com/learning/performance/what-is-lazy-loading/) can allow the most important content of a webpage to load even faster. Overall, however, image compression is often one of the quickest ways of fixing slow page performance.

## What is lossy image compression?

Consider a traveler packing clothes for a trip. It is possible for the traveler to pack everything in their closet, from shoes to hats to formalwear. But such an approach results in a large amount of luggage that the traveler needs to carry around, slowing them down and perhaps costing more money to transport. Instead, the traveler selects the most important clothing items and packs them into a single suitcase.

Just as our traveler did not need to pack their entire wardrobe, people rarely need to view an entire image in its maximum resolution and largest dimensions. (The most-used desktop screen size is 1680x1050 pixels, and the most-used mobile screen size is even smaller, at 360x800 pixels. Even at those dimensions, it is rare that an image takes up the entire screen.) Usually, an image can be reduced in quality and size in a way that is not noticeable to the typical viewer — an approach that is called "lossy" image compression.

Lossy image compression retains the most significant information for the image without keeping every single pixel. There are several types of lossy compression algorithms, described in more detail below. But all work by removing information from the image file so that the file is comprised of fewer bytes.

#### Lossy image compression methods

Many images [hosted](https://www.cloudflare.com/developer-platform/solutions/hosting/) on the web are in a file format that uses lossy compression. This ensures the images load quickly and do not use too much bandwidth. Common examples of lossy compression methods include:

  * **JPEG:** This file format, named after the Joint Photographic Experts Group, is perhaps the most widely used image compression method. It can usually compress files by a ratio of 10:1 with a minimal reduction in image quality. More recent versions of JPEG include JPEG 2000 and JPEG XR, but many browsers do not support these formats.

  * **WebP:** While WebP also supports lossless compression, it is more commonly used for lossy image compression. Google originally developed WebP to replace the JPEG, PNG, and GIF file formats.

  * **High Efficiency Image Format (HEIF):** The High Efficiency Image Format (HEIF) is a type of container file for compressed images. Images compressed with this method are sometimes called HEIC files.




## What is lossless image compression?

If our traveler's desired clothes do not fit in the suitcase, they may try re-folding and rearranging the clothes to make them fit better. Similarly, "lossless" image compression uses mathematical algorithms to rewrite an image file without removing any information. An image treated with lossless compression should appear basically identical to the original, but should have a much smaller file size.

While lossless compression can reduce image file sizes by as much as 40%, it is still less effective than lossy compression for reducing file size and optimizing images for the web. Website builders should carefully consider the needs of their end users and [test the speed of their websites](https://www.cloudflare.com/learning/performance/test-the-speed-of-a-website/) when deciding between lossy and lossless image compression.

#### Lossless compression methods

Widely used lossless compression methods include:

  * _Portable Network Graphics (PNG)_ , which is sometimes used on the web instead of JPEG or WebP.

  * _Graphics Interchange Format (GIF)_ , often used on the web as well.

  * _Bitmap (BMP)_ files are usually too large for practical use on the web.

  * _RAW_ images are not compressed at all. Digital cameras shoot photos in RAW, but the photos should be converted to another format and compressed before they are used on a website (unless the website is specifically intended for displaying extremely high-quality images).




## What are some common image compression algorithms?

Both lossy and lossless compression methods use various image compression algorithms (an algorithm is a set of rules for a computer to follow) to achieve smaller file sizes. Transform coding, run-length encoding, arithmetic coding, LZW, flate/deflate, and Huffman coding are all examples of image compression algorithms.

**Transform coding** is a lossy image compression algorithm that often uses a technique called discrete cosine transform (DCT), which is a way to mathematically represent a file using less information. JPEG relies on transform coding.

**Run-length encoding (RLE)** is a lossless compression algorithm that encodes repeated pixels. For instance, if there are eight white pixels in a row, instead of writing out all eight pixels (like WWWWWWWW), it records the number of pixels (like 8W).

**Arithmetic coding** is another kind of lossless compression algorithm. Like any digital file, digital images are represented on lower computational levels with a string of characters. Arithmetic coding encodes frequently used characters in an image file with fewer bits and less-used characters with more bits. The result is fewer bits overall compared to the original string of characters.

**Huffman coding** is somewhat similar to arithmetic encoding, but usually does not reduce file size by quite as much.

**LZW** — the Lempel–Ziv–Welch algorithm is a lossless compression method based on LZ77 and LZ78, two older compression algorithms.

**Flate/deflate** is a lossless compression algorithm based on Huffman coding and LZ77 compression.

## How to compress an image using Cloudflare

Cloudflare offers three products for storing, caching, optimizing, and resizing images to ensure they load as quickly as possible:

  * [Cloudflare Images](https://www.cloudflare.com/developer-platform/cloudflare-images/)

  * [Cloudflare Image Resizing](https://developers.cloudflare.com/images/image-resizing/)

  * [Cloudflare Polish](https://developers.cloudflare.com/images/polish/)




With these services, website owners can optimize images with a click, convert images to compressed file formats like WebP, and customize which image sizes load for which devices. Learn more about these services in the links above, or [get started with a Cloudflare plan here](https://www.cloudflare.com/plans/).
