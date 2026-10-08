---
url: https://blog.cloudflare.com/tag/kubernetes/
title: Posts tagged \"Kubernetes\" \u2014 Cloudflare Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:09:22.802087+00:00
---

# Posts tagged "Kubernetes" — Cloudflare Blog

> Source: https://blog.cloudflare.com/tag/kubernetes/

TAG

# Kubernetes

[Subscribe to Kubernetes RSS feed](https://blog.cloudflare.com/tag/kubernetes/rss)

March 26, 2026## [A one-line Kubernetes fix that saved 600 hours a year](https://blog.cloudflare.com/one-line-kubernetes-fix-saved-600-hours-a-year/)

When we investigated why our Atlantis instance took 30 minutes to restart, we discovered a bottleneck in how Kubernetes handles volume permissions. By adjusting the fsGroupChangePolicy, we reduced restart times to 30 seconds.

![Braxton Schafer](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45N6SPVMSAH9848VNNQD2K.png&w=64&h=64&f=webp&fit=cover&position=center)

[Braxton Schafer](https://blog.cloudflare.com/author/braxton-schafer/)

October 8, 2024## [Leveraging Kubernetes virtual machines at Cloudflare with KubeVirt](https://blog.cloudflare.com/leveraging-kubernetes-virtual-machines-with-kubevirt/)

The Kubernetes team runs several multi-tenant clusters across Cloudflare’s core data centers. When multi-tenant cluster isolation is too limiting for an application, we use KubeVirt. KubeVirt is a cloud-native solution that enables our developers to run virtual machines alongside containers.

![Justin Cichra](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48EAA1E9PF3JQT3M2B9H89.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Justin Cichra](https://blog.cloudflare.com/author/justin-cichra/)

January 24, 2023## [Intelligent, automatic restarts for unhealthy Kafka consumers](https://blog.cloudflare.com/intelligent-automatic-restarts-for-unhealthy-kafka-consumers/)

At Cloudflare, we take steps to ensure we are resilient against failure at all levels of our infrastructure. This includes Kafka, which we use for critical workflows such as sending time-sensitive emails and alerts.

![Chris Shepherd](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49MF4X0CXYBD687QQNEWE7.jpeg&w=64&h=64&f=webp&fit=cover&position=center)![Andrea Medda](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW458J6VKAH8TA0PVJH5SJP3.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Chris Shepherd](https://blog.cloudflare.com/author/chris-shepherd/) and [Andrea Medda](https://blog.cloudflare.com/author/andrea/)

June 24, 2022## [Kubectl with Cloudflare Zero Trust](https://blog.cloudflare.com/kubectl-with-zero-trust/)

Using Cloudflare Zero Trust with Kubernetes to enable kubectl without SOCKS proxies

![Terin Stock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45QWF9AN2RPHJF6DE6J4C2.png&w=64&h=64&f=webp&fit=cover&position=center)

[Terin Stock](https://blog.cloudflare.com/author/terin-stock/)

July 15, 2021## [Automatic Remediation of Kubernetes Nodes](https://blog.cloudflare.com/automatic-remediation-of-kubernetes-nodes/)

In Cloudflare’s core data centers, we are using Kubernetes to run many of the diverse services that help us control Cloudflare’s edge. We are automating some aspects of node remediation to keep the Kubernetes clusters healthy.

![Andrew DeMaria](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48HHS9CKKZA31T5GQQF66R.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Andrew DeMaria](https://blog.cloudflare.com/author/andrew-demaria/)

March 20, 2021## [Moving k8s communication to gRPC](https://blog.cloudflare.com/moving-k8s-communication-to-grpc/)

How we use gRPC in combination with Kubernetes to improve the performance and usability of internal APIs.

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/)

March 12, 2021## [Lessons Learned from Scaling Up Cloudflare’s Anomaly Detection Platform](https://blog.cloudflare.com/lessons-learned-from-scaling-up-cloudflare-anomaly-detection-platform/)

Anomaly Detection uses an algorithm called Histogram-Based Outlier Scoring (HBOS) to detect anomalous traffic in a scalable way. While HBOS is less precise than algorithms like kNN when it comes to local outliers, it is able to score global outliers quickly (in linear time).

![Jeffrey Tang](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW4862FC8G4A83KZ6GH2BZZM.jpeg&w=64&h=64&f=webp&fit=cover&position=center)

[Jeffrey Tang](https://blog.cloudflare.com/author/jeffrey/)

November 20, 2020## [Getting to the Core: Benchmarking Cloudflare’s Latest Server Hardware](https://blog.cloudflare.com/getting-to-the-core/)

A refresh of the hardware that Cloudflare uses to run analytics provided big efficiency improvements.

![Brian Bassett](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49KZ26BMXHN3CYG0QRXFGS.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Brian Bassett](https://blog.cloudflare.com/author/brian-bassett/)

November 13, 2020## [Automated Origin CA for Kubernetes](https://blog.cloudflare.com/automated-origin-ca-for-kubernetes/)

Today we're releasing origin-ca-issuer, an extension to cert-manager integrating with Cloudflare Origin CA to easily create and renew certificates for your account's domains.

![Terin Stock](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45QWF9AN2RPHJF6DE6J4C2.png&w=64&h=64&f=webp&fit=cover&position=center)

[Terin Stock](https://blog.cloudflare.com/author/terin-stock/)

September 15, 2020## [Secondary DNS - Deep Dive](https://blog.cloudflare.com/secondary-dns-deep-dive/)

The goal of Cloudflare operated Secondary DNS is to allow our customers with custom DNS solutions, be it on-premise or some other DNS provider, to be able to take advantage of Cloudflare's DNS performance and more recently, through Secondary Override, our proxying and security capabilities too.

![Alex Fattouche](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48H0J66VY9AP4Y8GXCS4RZ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Alex Fattouche](https://blog.cloudflare.com/author/alex-fattouche/)

April 27, 2020## [Releasing kubectl support in Access](https://blog.cloudflare.com/releasing-kubectl-support-in-access/)

Starting today, you can use Cloudflare Access and Argo Tunnel to securely manage your Kubernetes cluster with the kubectl command-line tool. SSO requirements and a zero-trust model to your Kubernetes management in under 30 minutes.

![Sam Rhea](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW45B32X8M7A8CXY9C0SX0EQ.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sam Rhea](https://blog.cloudflare.com/author/sam/)

July 8, 2018## [How To Minikube + Cloudflare](https://blog.cloudflare.com/minikube-cloudflare/)

A step-by-step guide for how to run production Minikube deployments using the Cloudflare Ingress Controller.

![Guest Author](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW49CMNZB4K93ARXNZ9HVTKX.png&w=64&h=64&f=webp&fit=cover&position=center)

[Guest Author](https://blog.cloudflare.com/author/guest-author/)

April 26, 2018## [Copenhagen & London developers, join us for five events this May](https://blog.cloudflare.com/copenhagen-london-developers/)

Are you based in Copenhagen or London? Drop by some talks we're hosting about the use of Go, Kubernetes, and Cloudflare’s Mobile SDK.

![Andrew Fitch](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW46B2D5FFFT8H3M3HAW8PRR.avif&w=64&h=64&f=webp&fit=cover&position=center)

[Andrew Fitch](https://blog.cloudflare.com/author/andrew-fitch/)

February 23, 2018## [Creating a single pane of glass for your multi-cloud Kubernetes workloads with Cloudflare](https://blog.cloudflare.com/creating-a-single-pane-of-glass-for-your-multi-cloud-kubernetes-workloads-with-cloudflare/)

One of the great things about container technology is that it delivers the same experience and functionality across different platforms. This frees you as a developer from having to rewrite or update your application to deploy it on a new cloud provider.

![Kamilla Amirova](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47PD2FSZX7PJ4T3672TFYM.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[Kamilla Amirova](https://blog.cloudflare.com/author/kamilla-amirova/)

December 5, 2017## [Introducing the Cloudflare Warp Ingress Controller for Kubernetes](https://blog.cloudflare.com/cloudflare-ingress-controller/)

It’s ironic that the one thing most programmers would really rather not have to spend time dealing with is... a computer. 

![John Graham-Cumming](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW47SEV81RPKWD16DDB0V03K.jpg&w=64&h=64&f=webp&fit=cover&position=center)

[John Graham-Cumming](https://blog.cloudflare.com/author/john-graham-cumming/)

November 21, 2017## [Living In A Multi-Cloud World](https://blog.cloudflare.com/living-in-a-multi-cloud-world/)

A few months ago at Cloudflare’s Internet Summit, we hosted a discussion on A Cloud Without Handcuffs with Joe Beda, one of the creators of Kubernetes, and Brandon Phillips, the co-founder of CoreOS.

![Sergi Isasi](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW44GA2M8TX4RHAHVAP55XN1.png&w=64&h=64&f=webp&fit=cover&position=center)

[Sergi Isasi](https://blog.cloudflare.com/author/sergi/)

September 14, 2017## [A Cloud Without Handcuffs](https://blog.cloudflare.com/a-cloud-without-handcuffs/)

Brandon Philips, Co-Founder & CTO, CoreOS, and Joe Beda, CTO, Heptio, & Co-Founder, Kubernetes 

![Internet Summit Team](https://blog.cloudflare.com/_image?href=https%3A%2F%2Fblog.cloudflare.com%2F_emdash%2Fapi%2Fmedia%2Ffile%2F01KW48P6RGRBR7G9T4YDJ9EAQ4.png&w=64&h=64&f=webp&fit=cover&position=center)

[Internet Summit Team](https://blog.cloudflare.com/author/summit-team/)
