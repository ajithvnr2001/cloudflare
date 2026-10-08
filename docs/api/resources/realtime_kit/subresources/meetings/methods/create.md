---
url: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/
title: Create a meeting | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:26:45.165866+00:00
---

# Create a meeting | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/

[API Reference](https://developers.cloudflare.com/api)

[Realtime Kit](https://developers.cloudflare.com/api/resources/realtime_kit)

[Meetings](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Create a meeting

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings

Create a meeting for the given App ID.

##### Security

API Token

The preferred authorization scheme for interacting with the Cloudflare API. [Create a token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/).

**Example:**`Authorization: Bearer Sn3lZJTBX6kkg7OdcBUAxOO963GEIyGQqnFTOFYY`

##### Accepted Permissions (at least one required)

`Realtime Admin``Realtime`

##### Path ParametersExpand Collapse 

account_id: string

The account identifier tag.

maxLength32

app_id: string

The app identifier tag.

##### Body ParametersJSONExpand Collapse 

ai_config: optional object { summarization, transcription } 

The AI Config allows you to customize the behavior of meeting transcriptions and summaries

summarization: optional object { summary_type, text_format, word_limit } 

Summary Config

summary_type: optional "general" or "team_meeting" or "sales_call" or 6 more

Defines the style of the summary, such as general, team meeting, or sales call.

One of the following:

"general"

"team_meeting"

"sales_call"

"client_check_in"

"interview"

"daily_standup"

"one_on_one_meeting"

"lecture"

"code_review"

text_format: optional "plain_text" or "markdown"

Determines the text format of the summary, such as plain text or markdown.

One of the following:

"plain_text"

"markdown"

word_limit: optional number

Sets the maximum number of words in the meeting summary.

maximum1000

minimum150

transcription: optional object { keywords, language, profanity_filter } 

Transcription Configurations

keywords: optional array of string

Adds specific terms to improve accurate detection during transcription.

language: optional "en-US" or "en-IN" or "de" or 7 more

Specifies the language code for transcription to ensure accurate results.

One of the following:

"en-US"

"en-IN"

"de"

"hi"

"sv"

"ru"

"pl"

"el"

"fr"

"nl"

profanity_filter: optional boolean

Control the inclusion of offensive language in transcriptions.

live_stream_on_start: optional boolean

Specifies if the meeting should start getting livestreamed on start.

persist_chat: optional boolean

If a meeting is set to persist_chat, meeting chat would remain for a week within the meeting space.

record_on_start: optional boolean

Specifies if the meeting should start getting recorded as soon as someone joins the meeting.

recording_config: optional object { audio_config, file_name_prefix, live_streaming_config, 4 more } 

Recording Configurations to be used for this meeting. This level of configs takes higher preference over App level configs on the RealtimeKit developer portal.

audio_config: optional object { channel, codec, export_file } 

Object containing configuration regarding the audio that is being recorded.

channel: optional "mono" or "stereo"

Audio signal pathway within an audio file that carries a specific sound source.

One of the following:

"mono"

"stereo"

codec: optional "MP3" or "AAC"

Codec using which the recording will be encoded. If VP8/VP9 is selected for videoConfig, changing audioConfig is not allowed. In this case, the codec in the audioConfig is automatically set to vorbis.

One of the following:

"MP3"

"AAC"

export_file: optional boolean

Controls whether to export audio file seperately

file_name_prefix: optional string

Adds a prefix to the beginning of the file name of the recording.

live_streaming_config: optional object { rtmp_url } 

rtmp_url: optional string

RTMP URL to stream to

formaturi

max_seconds: optional number

Specifies the maximum duration for recording in seconds, ranging from a minimum of 60 seconds to a maximum of 24 hours.

maximum86400

minimum60

realtimekit_bucket_config: optional object { enabled } 

enabled: boolean

Controls whether recordings are uploaded to RealtimeKit’s bucket. If set to false, `download_url`, `audio_download_url`, `download_url_expiry` won’t be generated for a recording.

storage_config: optional object { access_key, auth_method, bucket, 9 more }  or object { access_key, region, auth_method, 9 more }  or object { private_key, access_key, auth_method, 9 more }  or object { password, access_key, auth_method, 9 more } 

One of the following:

object { access_key, auth_method, bucket, 9 more } 

access_key: optional string

Access key of the storage medium. Access key is not required for the `gcs` storage media type.

Note that this field is not readable by clients, only writeable.

auth_method: optional "KEY" or "PASSWORD"

Authentication method used for “sftp” type storage medium

One of the following:

"KEY"

"PASSWORD"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

password: optional string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

private_key: optional string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

region: optional string

Region of the storage medium.

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "gcs"

username: optional string

SSH destination server username for SFTP type storage medium

object { access_key, region, auth_method, 9 more } 

access_key: unknown

minLength1

region: unknown

minLength1

auth_method: optional "KEY" or "PASSWORD"

Authentication method used for “sftp” type storage medium

One of the following:

"KEY"

"PASSWORD"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

password: optional string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

private_key: optional string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "aws" or "azure" or "digitalocean"

One of the following:

"aws"

"azure"

"digitalocean"

username: optional string

SSH destination server username for SFTP type storage medium

object { private_key, access_key, auth_method, 9 more } 

private_key: string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

access_key: optional string

Access key of the storage medium. Access key is not required for the `gcs` storage media type.

Note that this field is not readable by clients, only writeable.

auth_method: optional "KEY"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

password: optional string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

region: optional string

Region of the storage medium.

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "aws" or "azure" or "digitalocean" or 2 more

Type of storage media.

One of the following:

"aws"

"azure"

"digitalocean"

"gcs"

"sftp"

username: optional string

SSH destination server username for SFTP type storage medium

object { password, access_key, auth_method, 9 more } 

password: string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

access_key: optional string

Access key of the storage medium. Access key is not required for the `gcs` storage media type.

Note that this field is not readable by clients, only writeable.

auth_method: optional "PASSWORD"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

private_key: optional string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

region: optional string

Region of the storage medium.

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "aws" or "azure" or "digitalocean" or 2 more

Type of storage media.

One of the following:

"aws"

"azure"

"digitalocean"

"gcs"

"sftp"

username: optional string

SSH destination server username for SFTP type storage medium

video_config: optional object { codec, export_file, height, 2 more } 

codec: optional "H264" or "VP8" or "VP9"

Codec using which the recording will be encoded.

One of the following:

"H264"

"VP8"

"VP9"

export_file: optional boolean

Controls whether to export video file seperately

height: optional number

Height of the recording video in pixels

maximum1920

minimum1

watermark: optional object { position, size, url } 

Watermark to be added to the recording

position: optional "left top" or "right top" or "left bottom" or "right bottom"

Position of the watermark

One of the following:

"left top"

"right top"

"left bottom"

"right bottom"

size: optional object { height, width } 

Size of the watermark

height: optional number

Height of the watermark in px

minimum1

width: optional number

Width of the watermark in px

minimum1

url: optional string

URL of the watermark image

formaturi

width: optional number

Width of the recording video in pixels

maximum1920

minimum1

session_keep_alive_time_in_secs: optional number

Time in seconds, for which a session remains active, after the last participant has left the meeting.

maximum600

minimum60

summarize_on_end: optional boolean

Automatically generate summary of meetings using transcripts. Requires Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

title: optional string

Title of the meeting

transcribe_on_end: optional boolean

Automatically generate transcripts when the meeting ends.

##### ReturnsExpand Collapse 

success: boolean

Success status of the operation

data: optional object { id, created_at, updated_at, 10 more } 

Data returned by the operation

id: string

ID of the meeting.

formatuuid

created_at: string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

updated_at: string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

ai_config: optional object { summarization, transcription } 

The AI Config allows you to customize the behavior of meeting transcriptions and summaries

summarization: optional object { summary_type, text_format, word_limit } 

Summary Config

summary_type: optional "general" or "team_meeting" or "sales_call" or 6 more

Defines the style of the summary, such as general, team meeting, or sales call.

One of the following:

"general"

"team_meeting"

"sales_call"

"client_check_in"

"interview"

"daily_standup"

"one_on_one_meeting"

"lecture"

"code_review"

text_format: optional "plain_text" or "markdown"

Determines the text format of the summary, such as plain text or markdown.

One of the following:

"plain_text"

"markdown"

word_limit: optional number

Sets the maximum number of words in the meeting summary.

maximum1000

minimum150

transcription: optional object { keywords, language, profanity_filter } 

Transcription Configurations

keywords: optional array of string

Adds specific terms to improve accurate detection during transcription.

language: optional "en-US" or "en-IN" or "de" or 7 more

Specifies the language code for transcription to ensure accurate results.

One of the following:

"en-US"

"en-IN"

"de"

"hi"

"sv"

"ru"

"pl"

"el"

"fr"

"nl"

profanity_filter: optional boolean

Control the inclusion of offensive language in transcriptions.

live_stream_on_start: optional boolean

Specifies if the meeting should start getting livestreamed on start.

persist_chat: optional boolean

Specifies if Chat within a meeting should persist for a week.

record_on_start: optional boolean

Specifies if the meeting should start getting recorded as soon as someone joins the meeting.

recording_config: optional object { audio_config, file_name_prefix, live_streaming_config, 4 more } 

Recording Configurations to be used for this meeting. This level of configs takes higher preference over App level configs on the RealtimeKit developer portal.

audio_config: optional object { channel, codec, export_file } 

Object containing configuration regarding the audio that is being recorded.

channel: optional "mono" or "stereo"

Audio signal pathway within an audio file that carries a specific sound source.

One of the following:

"mono"

"stereo"

codec: optional "MP3" or "AAC"

Codec using which the recording will be encoded. If VP8/VP9 is selected for videoConfig, changing audioConfig is not allowed. In this case, the codec in the audioConfig is automatically set to vorbis.

One of the following:

"MP3"

"AAC"

export_file: optional boolean

Controls whether to export audio file seperately

file_name_prefix: optional string

Adds a prefix to the beginning of the file name of the recording.

live_streaming_config: optional object { rtmp_url } 

rtmp_url: optional string

RTMP URL to stream to

formaturi

max_seconds: optional number

Specifies the maximum duration for recording in seconds, ranging from a minimum of 60 seconds to a maximum of 24 hours.

maximum86400

minimum60

realtimekit_bucket_config: optional object { enabled } 

enabled: boolean

Controls whether recordings are uploaded to RealtimeKit’s bucket. If set to false, `download_url`, `audio_download_url`, `download_url_expiry` won’t be generated for a recording.

storage_config: optional object { access_key, auth_method, bucket, 9 more }  or object { access_key, region, auth_method, 9 more }  or object { private_key, access_key, auth_method, 9 more }  or object { password, access_key, auth_method, 9 more } 

One of the following:

object { access_key, auth_method, bucket, 9 more } 

access_key: optional string

Access key of the storage medium. Access key is not required for the `gcs` storage media type.

Note that this field is not readable by clients, only writeable.

auth_method: optional "KEY" or "PASSWORD"

Authentication method used for “sftp” type storage medium

One of the following:

"KEY"

"PASSWORD"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

password: optional string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

private_key: optional string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

region: optional string

Region of the storage medium.

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "gcs"

username: optional string

SSH destination server username for SFTP type storage medium

object { access_key, region, auth_method, 9 more } 

access_key: unknown

minLength1

region: unknown

minLength1

auth_method: optional "KEY" or "PASSWORD"

Authentication method used for “sftp” type storage medium

One of the following:

"KEY"

"PASSWORD"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

password: optional string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

private_key: optional string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "aws" or "azure" or "digitalocean"

One of the following:

"aws"

"azure"

"digitalocean"

username: optional string

SSH destination server username for SFTP type storage medium

object { private_key, access_key, auth_method, 9 more } 

private_key: string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

access_key: optional string

Access key of the storage medium. Access key is not required for the `gcs` storage media type.

Note that this field is not readable by clients, only writeable.

auth_method: optional "KEY"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

password: optional string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

region: optional string

Region of the storage medium.

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "aws" or "azure" or "digitalocean" or 2 more

Type of storage media.

One of the following:

"aws"

"azure"

"digitalocean"

"gcs"

"sftp"

username: optional string

SSH destination server username for SFTP type storage medium

object { password, access_key, auth_method, 9 more } 

password: string

SSH destination server password for SFTP type storage medium when auth_method is “PASSWORD”. If auth_method is “KEY”, this specifies the password for the ssh private key.

access_key: optional string

Access key of the storage medium. Access key is not required for the `gcs` storage media type.

Note that this field is not readable by clients, only writeable.

auth_method: optional "PASSWORD"

bucket: optional string

Name of the storage medium’s bucket.

host: optional string

SSH destination server host for SFTP type storage medium

path: optional string

Path relative to the bucket root at which the recording will be placed.

port: optional number

SSH destination server port for SFTP type storage medium

private_key: optional string

Private key used to login to destination SSH server for SFTP type storage medium, when auth_method used is “KEY”

region: optional string

Region of the storage medium.

secret: optional string

Secret key of the storage medium. Similar to `access_key`, it is only writeable by clients, not readable.

type: optional "aws" or "azure" or "digitalocean" or 2 more

Type of storage media.

One of the following:

"aws"

"azure"

"digitalocean"

"gcs"

"sftp"

username: optional string

SSH destination server username for SFTP type storage medium

video_config: optional object { codec, export_file, height, 2 more } 

codec: optional "H264" or "VP8" or "VP9"

Codec using which the recording will be encoded.

One of the following:

"H264"

"VP8"

"VP9"

export_file: optional boolean

Controls whether to export video file seperately

height: optional number

Height of the recording video in pixels

maximum1920

minimum1

watermark: optional object { position, size, url } 

Watermark to be added to the recording

position: optional "left top" or "right top" or "left bottom" or "right bottom"

Position of the watermark

One of the following:

"left top"

"right top"

"left bottom"

"right bottom"

size: optional object { height, width } 

Size of the watermark

height: optional number

Height of the watermark in px

minimum1

width: optional number

Width of the watermark in px

minimum1

url: optional string

URL of the watermark image

formaturi

width: optional number

Width of the recording video in pixels

maximum1920

minimum1

session_keep_alive_time_in_secs: optional number

Time in seconds, for which a session remains active, after the last participant has left the meeting.

maximum600

minimum60

status: optional "ACTIVE" or "INACTIVE"

Whether the meeting is `ACTIVE` or `INACTIVE`. Users will not be able to join an `INACTIVE` meeting.

One of the following:

"ACTIVE"

"INACTIVE"

summarize_on_end: optional boolean

Automatically generate summary of meetings using transcripts. Requires Transcriptions to be enabled, and can be retrieved via Webhooks or summary API.

title: optional string

Title of the meeting.

transcribe_on_end: optional boolean

Automatically generate transcripts when the meeting ends.

### Create a meeting

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
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -d '{}'

200 example
    
    
    {
      "success": true,
      "data": {
        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "created_at": "2019-12-27T18:11:19.117Z",
        "updated_at": "2019-12-27T18:11:19.117Z",
        "ai_config": {
          "summarization": {
            "summary_type": "general",
            "text_format": "plain_text",
            "word_limit": 150
          },
          "transcription": {
            "keywords": [
              "string"
            ],
            "language": "en-US",
            "profanity_filter": true
          }
        },
        "live_stream_on_start": true,
        "persist_chat": true,
        "record_on_start": true,
        "recording_config": {
          "audio_config": {
            "channel": "mono",
            "codec": "MP3",
            "export_file": true
          },
          "file_name_prefix": "file_name_prefix",
          "live_streaming_config": {
            "rtmp_url": "rtmp://a.rtmp.youtube.com/live2"
          },
          "max_seconds": 60,
          "realtimekit_bucket_config": {
            "enabled": true
          },
          "storage_config": {
            "auth_method": "KEY",
            "bucket": "bucket",
            "host": "host",
            "path": "path",
            "port": 0,
            "region": "us-east-1",
            "type": "gcs",
            "username": "username"
          },
          "video_config": {
            "codec": "H264",
            "export_file": true,
            "height": 720,
            "watermark": {
              "position": "left top",
              "size": {
                "height": 1,
                "width": 1
              },
              "url": "https://example.com"
            },
            "width": 1280
          }
        },
        "session_keep_alive_time_in_secs": 60,
        "status": "ACTIVE",
        "summarize_on_end": true,
        "title": "title",
        "transcribe_on_end": true
      }
    }

##### Returns Examples

200 example
    
    
    {
      "success": true,
      "data": {
        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        "created_at": "2019-12-27T18:11:19.117Z",
        "updated_at": "2019-12-27T18:11:19.117Z",
        "ai_config": {
          "summarization": {
            "summary_type": "general",
            "text_format": "plain_text",
            "word_limit": 150
          },
          "transcription": {
            "keywords": [
              "string"
            ],
            "language": "en-US",
            "profanity_filter": true
          }
        },
        "live_stream_on_start": true,
        "persist_chat": true,
        "record_on_start": true,
        "recording_config": {
          "audio_config": {
            "channel": "mono",
            "codec": "MP3",
            "export_file": true
          },
          "file_name_prefix": "file_name_prefix",
          "live_streaming_config": {
            "rtmp_url": "rtmp://a.rtmp.youtube.com/live2"
          },
          "max_seconds": 60,
          "realtimekit_bucket_config": {
            "enabled": true
          },
          "storage_config": {
            "auth_method": "KEY",
            "bucket": "bucket",
            "host": "host",
            "path": "path",
            "port": 0,
            "region": "us-east-1",
            "type": "gcs",
            "username": "username"
          },
          "video_config": {
            "codec": "H264",
            "export_file": true,
            "height": 720,
            "watermark": {
              "position": "left top",
              "size": {
                "height": 1,
                "width": 1
              },
              "url": "https://example.com"
            },
            "width": 1280
          }
        },
        "session_keep_alive_time_in_secs": 60,
        "status": "ACTIVE",
        "summarize_on_end": true,
        "title": "title",
        "transcribe_on_end": true
      }
    }
