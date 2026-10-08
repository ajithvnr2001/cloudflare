---
url: https://developers.cloudflare.com/durable-objects/api/webgpu/
title: WebGPU \u00b7 Cloudflare Durable Objects docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:11:06.323323+00:00
---

# WebGPU · Cloudflare Durable Objects docs

> Source: https://developers.cloudflare.com/durable-objects/api/webgpu/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Durable Objects](https://developers.cloudflare.com/durable-objects/)
  3. /Workers Binding API
  4. /WebGPU



# WebGPU

Last updated Apr 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/durable-objects/api/webgpu/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewExamples

Caution

The WebGPU API is only available in local development. You cannot deploy Durable Objects to Cloudflare that rely on the WebGPU API. See [Workers AI](https://developers.cloudflare.com/workers-ai/) for information on running machine learning models on the GPUs in Cloudflare's global network.

The [WebGPU API ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) allows you to use the GPU directly from JavaScript.

The WebGPU API is only accessible from within [Durable Objects](https://developers.cloudflare.com/durable-objects/). You cannot use the WebGPU API from within Workers.

To use the WebGPU API in local development, enable the `experimental` and `webgpu` [compatibility flags](https://developers.cloudflare.com/workers/configuration/compatibility-flags/) in the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) of your Durable Object.
    
    
    compatibility_flags = ["experimental", "webgpu"]

The following subset of the WebGPU API is available from within Durable Objects:

API | Supported? | Notes  
---|---|---  
[`navigator.gpu` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/gpu) | ✅ |   
[`GPU.requestAdapter` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPU/requestAdapter) | ✅ |   
[`GPUAdapterInfo` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUAdapterInfo) | ✅ |   
[`GPUAdapter` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUAdapter) | ✅ |   
[`GPUBindGroupLayout` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroupLayout) | ✅ |   
[`GPUBindGroup` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUBindGroup) | ✅ |   
[`GPUBuffer` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUBuffer) | ✅ |   
[`GPUCommandBuffer` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUCommandBuffer) | ✅ |   
[`GPUCommandEncoder` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUCommandEncoder) | ✅ |   
[`GPUComputePassEncoder` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUComputePassEncoder) | ✅ |   
[`GPUComputePipeline` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUComputePipeline) | ✅ |   
[`GPUComputePipelineError` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUPipelineError) | ✅ |   
[`GPUDevice` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUDevice) | ✅ |   
[`GPUOutOfMemoryError` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUOutOfMemoryError) | ✅ |   
[`GPUValidationError` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUValidationError) | ✅ |   
[`GPUInternalError` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUInternalError) | ✅ |   
[`GPUDeviceLostInfo` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUDeviceLostInfo) | ✅ |   
[`GPUPipelineLayout` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUPipelineLayout) | ✅ |   
[`GPUQuerySet` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUQuerySet) | ✅ |   
[`GPUQueue` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUQueue) | ✅ |   
[`GPUSampler` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUSampler) | ✅ |   
[`GPUCompilationMessage` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUCompilationMessage) | ✅ |   
[`GPUShaderModule` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule) | ✅ |   
[`GPUSupportedFeatures` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedFeatures) | ✅ |   
[`GPUSupportedLimits` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedLimits) | ✅ |   
[`GPUMapMode` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API#reading_the_results_back_to_javascript) | ✅ |   
[`GPUShaderStage` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API#create_a_bind_group_layout) | ✅ |   
[`GPUUncapturedErrorEvent` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUUncapturedErrorEvent) | ✅ |   
  
The following subset of the WebGPU API is not yet supported:

API | Supported? | Notes  
---|---|---  
[`GPU.getPreferredCanvasFormat` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPU/getPreferredCanvasFormat) |  |   
[`GPURenderBundle` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPURenderBundle) |  |   
[`GPURenderBundleEncoder` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPURenderBundleEncoder) |  |   
[`GPURenderPassEncoder` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPURenderPassEncoder) |  |   
[`GPURenderPipeline` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPURenderPipeline) |  |   
[`GPUShaderModule` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUShaderModule) |  |   
[`GPUTexture` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUTexture) |  |   
[`GPUTextureView` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUTextureView) |  |   
[`GPUExternalTexture` ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/GPUExternalTexture) |  |   
  
## Examples

  * [workers-wonnx ↗︎](https://github.com/cloudflare/workers-wonnx/) — Image classification, running on a GPU via the WebGPU API, using the [wonnx ↗︎](https://github.com/webonnx/wonnx) model inference runtime.



[PreviousAlarms](https://developers.cloudflare.com/durable-objects/api/alarms/)[NextTroubleshooting](https://developers.cloudflare.com/durable-objects/observability/troubleshooting/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/durable-objects/api/webgpu.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
