---
url: https://developers.cloudflare.com/api/resources/ai/methods/run/
title: Run a Workers AI model | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:26.835794+00:00
---

# Run a Workers AI model | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/ai/methods/run/

[API Reference](https://developers.cloudflare.com/api)

[AI](https://developers.cloudflare.com/api/resources/ai)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Run a Workers AI model

POST/accounts/{account_id}/ai/run/{model_name}

Runs the Workers AI model specified in the URL path. Send the model’s inputs directly in the request body, without a model/input/options wrapper.

Accepts model-specific JSON or binary input. The response format depends on the model and the requested output.

See the [model catalog](https://developers.cloudflare.com/workers-ai/models/) for supported models and their input formats.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

API Email + API Key

The previous authorization scheme for interacting with the Cloudflare API, used in conjunction with a Global API key.

**Example:**`X-Auth-Email: user@example.com`

The previous authorization scheme for interacting with the Cloudflare API. When possible, use API tokens instead of Global API keys.

**Example:**`X-Auth-Key: 144c9defac04969c7bfad8efaa8ea194`

##### Accepted Permissions (at least one required)

`Workers AI Write``Workers AI Read`

##### Path ParametersExpand Collapse 

account_id: string

Cloudflare account ID used for this AI model request.

model_name: string

Workers AI model identifier, including its namespace and model name.

##### Body ParametersJSONExpand Collapse 

body: optional object { text }  or object { prompt, guidance, height, 8 more }  or object { prompt, lang }  or 12 more

One of the following:

TextClassification object { text } 

text: string

The text that you want to classify

minLength1

TextToImage object { prompt, guidance, height, 8 more } 

prompt: string

A text description of the image you want to generate

minLength1

guidance: optional number

Controls how closely the generated image should adhere to the prompt; higher values make the image more aligned with the prompt

height: optional number

The height of the generated image in pixels

maximum2048

minimum256

image: optional array of number

For use with img2img tasks. An array of integers that represent the image data constrained to 8-bit unsigned integer values

image_b64: optional string

For use with img2img tasks. A base64-encoded string of the input image

mask: optional array of number

An array representing An array of integers that represent mask image data for inpainting constrained to 8-bit unsigned integer values

negative_prompt: optional string

Text describing elements to avoid in the generated image

num_steps: optional number

The number of diffusion steps; higher values can improve quality but take longer

maximum20

seed: optional number

Random seed for reproducibility of the image generation

strength: optional number

A value between 0 and 1 indicating how strongly to apply the transformation during img2img tasks; lower values make the output closer to the input image

width: optional number

The width of the generated image in pixels

maximum2048

minimum256

TextToSpeech object { prompt, lang } 

prompt: string

A text description of the audio you want to generate

minLength1

lang: optional string

The speech language (e.g., ‘en’ for English, ‘fr’ for French). Defaults to ‘en’ if not specified

TextEmbeddings object { text } 

text: string or array of string

The text to embed

One of the following:

string

The text to embed

array of string

Batch of text values to embed

AutomaticSpeechRecognition object { audio, source_lang, target_lang } 

audio: array of number

An array of integers that represent the audio data constrained to 8-bit unsigned integer values

source_lang: optional string

The language of the recorded audio

target_lang: optional string

The language to translate the transcription into. Currently only English is supported.

ImageClassification object { image } 

image: array of number

An array of integers that represent the image data constrained to 8-bit unsigned integer values

ObjectDetection object { image } 

image: optional array of number

An array of integers that represent the image data constrained to 8-bit unsigned integer values

Prompt object { prompt, frequency_penalty, lora, 10 more } 

prompt: string

The input text prompt for the model to generate a response.

minLength1

frequency_penalty: optional number

Decreases the likelihood of the model repeating the same lines verbatim.

maximum2

minimum-2

lora: optional string

Name of the LoRA (Low-Rank Adaptation) model to fine-tune the base model.

max_tokens: optional number

The maximum number of tokens to generate in the response.

presence_penalty: optional number

Increases the likelihood of the model introducing new topics.

maximum2

minimum-2

raw: optional boolean

If true, a chat template is not applied and you must adhere to the specific model’s expected formatting.

repetition_penalty: optional number

Penalty for repeated tokens; higher values discourage repetition.

maximum2

minimum0

response_format: optional object { json_schema, type } 

json_schema: optional unknown

type: optional "json_object" or "json_schema"

One of the following:

"json_object"

"json_schema"

seed: optional number

Random seed for reproducibility of the generation.

maximum9999999999

minimum1

stream: optional boolean

If true, the response will be streamed back incrementally using SSE, Server Sent Events.

temperature: optional number

Controls the randomness of the output; higher values produce more random results.

maximum5

minimum0

top_k: optional number

Limits the AI to choose from the top ‘k’ most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

maximum50

minimum1

top_p: optional number

Adjusts the creativity of the AI’s responses by controlling how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

maximum1

minimum0.001

TextGeneration object { messages, frequency_penalty, functions, 11 more } 

messages: array of object { content, role } 

An array of message objects representing the conversation history.

content: string or array of object { text, type } 

The content of the message as a string.

One of the following:

string

The content of the message as a string.

array of object { text, type } 

Array of text content parts.

text: optional string

Text content

type: optional string

Type of the content (text)

role: string

The role of the message sender (e.g., ‘user’, ‘assistant’, ‘system’, ‘tool’).

frequency_penalty: optional number

Decreases the likelihood of the model repeating the same lines verbatim.

maximum2

minimum-2

functions: optional array of object { code, name } 

code: string

name: string

max_tokens: optional number

The maximum number of tokens to generate in the response.

presence_penalty: optional number

Increases the likelihood of the model introducing new topics.

maximum2

minimum-2

raw: optional boolean

If true, a chat template is not applied and you must adhere to the specific model’s expected formatting.

repetition_penalty: optional number

Penalty for repeated tokens; higher values discourage repetition.

maximum2

minimum0

response_format: optional object { json_schema, type } 

json_schema: optional unknown

type: optional "json_object" or "json_schema"

One of the following:

"json_object"

"json_schema"

seed: optional number

Random seed for reproducibility of the generation.

maximum9999999999

minimum1

stream: optional boolean

If true, the response will be streamed back incrementally using SSE, Server Sent Events.

temperature: optional number

Controls the randomness of the output; higher values produce more random results.

maximum5

minimum0

tools: optional array of object { description, name, parameters }  or object { function, type } 

A list of tools available for the assistant to use.

One of the following:

object { description, name, parameters } 

description: string

A brief description of what the tool does.

name: string

The name of the tool. More descriptive the better.

parameters: object { properties, type, required } 

Schema defining the parameters accepted by the tool.

properties: map[object { description, type } ]

Definitions of each parameter.

description: string

A description of the expected parameter.

type: string

The data type of the parameter.

type: string

The type of the parameters object (usually ‘object’).

required: optional array of string

List of required parameter names.

Function object { function, type } 

function: object { description, name, parameters } 

Details of the function tool.

description: string

A brief description of what the function does.

name: string

The name of the function.

parameters: object { properties, type, required } 

Schema defining the parameters accepted by the function.

properties: map[object { description, type } ]

Definitions of each parameter.

description: string

A description of the expected parameter.

type: string

The data type of the parameter.

type: string

The type of the parameters object (usually ‘object’).

required: optional array of string

List of required parameter names.

type: string

Specifies the type of tool (e.g., ‘function’).

top_k: optional number

Limits the AI to choose from the top ‘k’ most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

maximum50

minimum1

top_p: optional number

Adjusts the creativity of the AI’s responses by controlling how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

maximum1

minimum0.001

Translation object { target_lang, text, source_lang } 

target_lang: string

The language code to translate the text into (e.g., ‘es’ for Spanish)

text: string

The text to be translated

minLength1

source_lang: optional string

The language code of the source text (e.g., ‘en’ for English). Defaults to ‘en’ if not specified

Summarization object { input_text, max_length } 

input_text: string

The text that you want the model to summarize

minLength1

max_length: optional number

The maximum length of the generated summary in tokens

ImageToText object { image, frequency_penalty, max_tokens, 8 more } 

image: array of number

An array of integers that represent the image data constrained to 8-bit unsigned integer values

frequency_penalty: optional number

Decreases the likelihood of the model repeating the same lines verbatim.

max_tokens: optional number

The maximum number of tokens to generate in the response.

presence_penalty: optional number

Increases the likelihood of the model introducing new topics.

prompt: optional string

The input text prompt for the model to generate a response.

raw: optional boolean

If true, a chat template is not applied and you must adhere to the specific model’s expected formatting.

repetition_penalty: optional number

Penalty for repeated tokens; higher values discourage repetition.

seed: optional number

Random seed for reproducibility of the generation.

temperature: optional number

Controls the randomness of the output; higher values produce more random results.

top_k: optional number

Limits the AI to choose from the top ‘k’ most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

top_p: optional number

Controls the creativity of the AI’s responses by adjusting how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

object { image, prompt, frequency_penalty, 8 more } 

image: string

Image in base64 encoded format.

prompt: string

The input text prompt for the model to generate a response.

minLength1

frequency_penalty: optional number

Decreases the likelihood of the model repeating the same lines verbatim.

ignore_eos: optional boolean

Whether to ignore the EOS token and continue generating tokens after the EOS token is generated.

max_tokens: optional number

The maximum number of tokens to generate in the response.

presence_penalty: optional number

Increases the likelihood of the model introducing new topics.

repetition_penalty: optional number

Penalty for repeated tokens; higher values discourage repetition.

seed: optional number

Random seed for reproducibility of the generation.

temperature: optional number

Controls the randomness of the output; higher values produce more random results.

top_k: optional number

Limits the AI to choose from the top ‘k’ most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

top_p: optional number

Controls the creativity of the AI’s responses by adjusting how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

ImageTextToText object { image, messages, frequency_penalty, 8 more } 

image: string

Image in base64 encoded format.

messages: array of object { content, role } 

An array of message objects representing the conversation history.

content: string or array of object { type, image_url, text } 

The content of the message as a string.

One of the following:

string

The content of the message as a string.

array of object { type, image_url, text } 

Array of content parts (text, image_url, etc.).

type: string

Type of the content part (e.g. ‘text’, ‘image_url’).

image_url: optional object { url } 

Image URL object (when type is ‘image_url’).

url: string

Image URI with data (e.g. data:image/jpeg;base64,/9j/…).

text: optional string

Text content (when type is ‘text’).

role: string

The role of the message sender (e.g., ‘user’, ‘assistant’, ‘system’, ‘tool’).

frequency_penalty: optional number

Decreases the likelihood of the model repeating the same lines verbatim.

ignore_eos: optional boolean

Whether to ignore the EOS token and continue generating tokens after the EOS token is generated.

max_tokens: optional number

The maximum number of tokens to generate in the response.

presence_penalty: optional number

Increases the likelihood of the model introducing new topics.

repetition_penalty: optional number

Penalty for repeated tokens; higher values discourage repetition.

seed: optional number

Random seed for reproducibility of the generation.

temperature: optional number

Controls the randomness of the output; higher values produce more random results.

top_k: optional number

Limits the AI to choose from the top ‘k’ most probable words. Lower values make responses more focused; higher values introduce more variety and potential surprises.

top_p: optional number

Controls the creativity of the AI’s responses by adjusting how many possible words it considers. Lower values make outputs more predictable; higher values allow for more varied and creative responses.

MultimodalEmbeddings object { image, text } 

image: optional string

Image in base64 encoded format.

minLength1

text: optional array of string

##### ReturnsExpand Collapse 

result: optional array of object { label, score }  or string or object { audio }  or 12 more

An array of classification results for the input text

One of the following:

TextClassification = array of object { label, score } 

An array of classification results for the input text

label: optional string

The classification label assigned to the text (e.g., ‘POSITIVE’ or ‘NEGATIVE’)

score: optional number

Confidence score indicating the likelihood that the text belongs to the specified label

TextToImage = string

The generated image in PNG format

Audio object { audio } 

audio: optional string

The generated audio in MP3 format, base64-encoded

string

The generated audio in MP3 format

TextEmbeddings object { data, shape } 

data: optional array of array of number

Embeddings of the requested text values

shape: optional array of number

AutomaticSpeechRecognition object { text, vtt, word_count, words } 

text: string

The transcription

vtt: optional string

word_count: optional number

words: optional array of object { end, start, word } 

end: optional number

The ending second when the word completes

start: optional number

The second this word begins in the recording

word: optional string

ImageClassification = array of object { label, score } 

label: optional string

The predicted category or class for the input image based on analysis

score: optional number

A confidence value, between 0 and 1, indicating how certain the model is about the predicted label

ObjectDetection = array of object { box, label, score } 

An array of detected objects within the input image

box: optional object { xmax, xmin, ymax, ymin } 

Coordinates defining the bounding box around the detected object

xmax: optional number

The x-coordinate of the bottom-right corner of the bounding box

xmin: optional number

The x-coordinate of the top-left corner of the bounding box

ymax: optional number

The y-coordinate of the bottom-right corner of the bounding box

ymin: optional number

The y-coordinate of the top-left corner of the bounding box

label: optional string

The class label or name of the detected object

score: optional number

Confidence score indicating the likelihood that the detection is correct

object { response, tool_calls, usage } 

response: string

The generated text response from the model

tool_calls: optional array of object { arguments, name } 

An array of tool calls requests made during the response generation

arguments: optional unknown

The arguments passed to be passed to the tool call request

name: optional string

The name of the tool to be called

usage: optional object { completion_tokens, prompt_tokens, total_tokens } 

Usage statistics for the inference request

completion_tokens: optional number

Total number of tokens in output

prompt_tokens: optional number

Total number of tokens in input

total_tokens: optional number

Total number of input and output tokens

string

Translation object { translated_text } 

translated_text: optional string

The translated text in the target language

Summarization object { summary } 

summary: optional string

The summarized version of the input text

ImageToText object { description } 

description: optional string

ImageTextToText object { description } 

description: optional string

MultimodalEmbeddings object { data, shape } 

data: optional array of array of number

shape: optional array of number

### Run a Workers AI model

HTTP

HTTP

HTTP

TypeScript

TypeScript

Python

Python

Go

Go

Terraform

Terraform
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/ai/run/$MODEL_NAME \
        -X POST \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN"

200 example
    
    
    {
      "result": [
        {
          "label": "label",
          "score": 0
        }
      ]
    }

##### Returns Examples

200 example
    
    
    {
      "result": [
        {
          "label": "label",
          "score": 0
        }
      ]
    }
