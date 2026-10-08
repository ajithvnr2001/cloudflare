---
url: https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/
title: How does HTML5 video work? | HTML video
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:04:23.388063+00:00
---

# How does HTML5 video work? | HTML video

> Source: https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/

[ Learning Center ](https://www.cloudflare.com/learning/) / video streaming

##  How does HTML5 video work? | HTML video 

HTML5 is the latest version of HTML. Unlike previous versions of HTML, HTML5 enables developers to easily add video to webpages with a video tag. 

[Learning Center](https://www.cloudflare.com/learning)/video streaming/[How does HTML5 video work? | HTML video](https://www.cloudflare.com/learning/video-streaming/how-html5-video-works/)[How WebRTC works: What is WebRTC used for?](https://www.cloudflare.com/learning/video-streaming/how-webrtc-works/)[How does live stream encoding work? | Video encoding](https://www.cloudflare.com/learning/video-streaming/live-stream-encoding/)[MOV vs. MP4 | Video file formats](https://www.cloudflare.com/learning/video-streaming/mov-vs-mp4/)[What is a TURN server?](https://www.cloudflare.com/learning/video-streaming/turn-server/)[What are video encoding formats? | Video formats](https://www.cloudflare.com/learning/video-streaming/video-encoding-formats/)[What is adaptive bitrate streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-adaptive-bitrate-streaming/)[What does buffering mean? | Buffering in video streaming](https://www.cloudflare.com/learning/video-streaming/what-is-buffering/)[What is H.264? | Advanced Video Coding (AVC)](https://www.cloudflare.com/learning/video-streaming/what-is-h264-avc/)[What is HDS streaming? | HLS vs. HDS](https://www.cloudflare.com/learning/video-streaming/what-is-http-dynamic-streaming/)[What is MP4? | MPEG-4 vs. MP4](https://www.cloudflare.com/learning/video-streaming/what-is-mp4/)[What is MPEG-DASH? | HLS vs. DASH](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)[What is streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[What is a video CDN?](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[What is voice over Internet Protocol (VoIP)?](https://www.cloudflare.com/learning/video-streaming/what-is-voip/)[What is live streaming?](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[How does live stream encoding work?](https://www.cloudflare.com/learning/video-streaming/what-is-streaming-encoding/)[What is HLS?](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)

######  Learning objectives 

After reading this article you will be able to: 

  * Define HTML5 
  * Describe how HTML5 enables streaming without a plugin 
  * Learn how to use the HTML5 video element 



Related content  [ What is streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-streaming/)[ What is a video CDN? ](https://www.cloudflare.com/learning/video-streaming/what-is-video-cdn/)[ What is live streaming? ](https://www.cloudflare.com/learning/video-streaming/what-is-live-streaming/)[ What is HLS? ](https://www.cloudflare.com/learning/video-streaming/what-is-http-live-streaming/)[ What is MPEG-DASH? | HLS vs. DASH ](https://www.cloudflare.com/learning/video-streaming/what-is-mpeg-dash/)

On this page

  * What is HTML5?

  * How does the HTML5 video element work?

  * What streaming protocol is used with HTML5?

  * Do all browsers support HTML5?

  * How did websites include video content before HTML5?

  * What is a browser plugin?

  * How are Cloudflare Stream videos embedded?




## What is HTML5?

HTML5 is the latest version of Hypertext Markup Language (HTML), a coding language for formatting content on the Internet. All webpages use HTML to tell browsers how to display their content. Compared to earlier versions of HTML, HTML5 has a number of additional features, one of which is the ability to add videos to a webpage. Other HTML5 features include support for SVG graphics, tags for defining the navigation on a website, and header and footer tags.

## How does the HTML5 video element work?

The HTML5 video element tells the browser to load a video file from another source by specifying the video file's location, similar to the way a browser loads an image file (the image itself is not stored in the HTML file — the browser pulls it from somewhere else). Width, height, and other attributes can also be included to tell the browser how to display the video. Other markup code can tell the browser where to place it on the page.

The HTML5 video tag is `<video>`, and the tag is closed, similar to other HTML elements, with `</video>`.

In between those tags, a `<source>` tag indicates the location of the video file. Within this tag, both the video source (src) and the type of file (type) are indicated like this:
    
    
    `
    <video>
      <source src="example.mp4" type="video/mp4">
    </video>
    `
    

The following important attributes also can go inside the `<video>` tag:

  * **Width:** This specifies the video's width in pixels. The number of pixels goes between quotation marks: `width="370"`

  * **Height:** This specifies the video's height. It works similarly to the width attribute.

  * **Play, pause, volume:** These controls enable the user to control video playback. Add `controls` to the `<video>` tag to include them.




Alternate sources for the video can also go between the `<video>` tags in case a browser does not support the first file format. Browsers always use the first source listed.

In addition, text can be placed between the `<video>` tags; this text is displayed only if the user's browser does not support HTML5 video.

Putting it all together, HTML5 code for an embedded video might look like this:
    
    
    `
    <video controls width="370" height="130">
      <source src="example.mp4" type="video/mp4">
      <source src="alternate-example.webm" type="video/webm">
    Your browser does not support HTML5 video.
    </video>
    `
    

A number of other attributes, such as `autoplay` (to play the video as soon as the page loads), `loop` (to loop videos), `muted` (to mute videos), and `poster` (to show an image before the video loads), can be used within the video element as well. Mozilla has good [documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video) about these attributes.

## What streaming protocol is used with HTML5?

HTML5 is not itself a [streaming](https://www.cloudflare.com/learning/video/what-is-streaming/) protocol. Websites built with HTML5 can use several different streaming protocols to play video, including HTTP live streaming ([HLS](https://www.cloudflare.com/learning/video/what-is-http-live-streaming/)) and [MPEG-DASH](https://www.cloudflare.com/learning/video/what-is-mpeg-dash/). This is configured on the [server side](https://www.cloudflare.com/learning/serverless/glossary/client-side-vs-server-side/), not in the HTML markup code.

## Do all browsers support HTML5?

All major browsers support HTML5, meaning they can interpret HTML5 tags that were not part of earlier versions of HTML. However, not all browsers support all features of HTML5. Developers have to keep in mind that some users might have an outdated version of a browser that cannot interpret the HTML5 video element.

## How did websites include video content before HTML5?

Before the release of HTML5 in 2008, videos were most often embedded by using the Adobe Flash plugin. HTML5 enabled developers to embed videos on webpages using just a few HTML tags, eliminating the need for a plugin. As a result, Flash became less necessary, and Adobe finally stopped supporting Flash on December 31, 2020.

Today, most users can stream video without an additional browser plugin, and developers can use a variety of methods for embedding videos without relying on a plugin. The HTML5 video element is one of the most used methods for doing so.

## What is a browser plugin?

A browser plugin is a piece of software that adds a feature to a browser that is not otherwise included. It used to be the case that browsers did not include the ability to play video. Third-party plugins like Adobe Flash helped fill this gap.

However, plugins can also present a security threat. They offer one more attack surface — an additional way for external attackers to compromise a browsing session — on top of the [attack surfaces](https://www.cloudflare.com/learning/security/what-is-an-attack-surface/) presented by the browser and the website. Additionally, plugins can slow down page functionality. Relying on plugins means multiple pieces of software have to work properly and quickly to load a webpage, not just one.

If a video is embedded natively, which is possible in HTML5, it will load more quickly. Avoiding the use of a plugin is also more secure.

## How are Cloudflare Stream videos embedded?

Cloudflare Stream is an on-demand video platform that combines video encoding, storage, delivery, and playback. See the [Cloudflare Stream documentation](https://developers.cloudflare.com/stream/) to learn how to upload video files to Stream and embed them into webpages. Or, [learn more about Cloudflare Stream](https://www.cloudflare.com/developer-platform/products/cloudflare-stream/) before getting started.
