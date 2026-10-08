---
url: https://developers.cloudflare.com/api/resources/realtime_kit/
title: Realtime Kit | Cloudflare API
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:18:54.621487+00:00
---

# Realtime Kit | Cloudflare API

> Source: https://developers.cloudflare.com/api/resources/realtime_kit/

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

* * *

**Copy Markdown**

**View as Markdown**

# Realtime Kit

#### Realtime KitApps

##### [Fetch all apps](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps/methods/get)

GET/accounts/{account_id}/realtime/kit/apps

##### [Create App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps/methods/post)

POST/accounts/{account_id}/realtime/kit/apps

##### ModelsExpand Collapse 

AppGetResponse object { data, paging, success } 

data: optional array of object { id, created_at, name } 

id: optional string

formatuuid

created_at: optional string

formatdate-time

name: optional string

paging: optional object { end_offset, start_offset, total_count } 

end_offset: optional number

start_offset: optional number

total_count: optional number

success: optional boolean

AppPostResponse object { data, success } 

data: optional object { app } 

app: optional object { id, created_at, name } 

id: optional string

formatuuid

created_at: optional string

formatdate-time

name: optional string

success: optional boolean

#### Realtime KitMeetings

##### [Fetch all meetings for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings

##### [Create a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings

##### [Fetch a meeting for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get_meeting_by_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}

##### [Update a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/update_meeting_by_id)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}

##### [Replace a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/replace_meeting_by_id)

PUT/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}

##### [Fetch all participants of a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get_meeting_participants)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants

##### [Add a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants

##### [Fetch a participant's detail](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/get_meeting_participant)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}

##### [Edit a participant's detail](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/edit_participant)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}

##### [Delete a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/delete_meeting_participant)

DELETE/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}

##### [Refresh participant's authentication token](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/refresh_participant_token)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/participants/{participant_id}/token

##### ModelsExpand Collapse 

MeetingGetResponse object { data, paging, success } 

data: array of object { id, created_at, updated_at, 9 more } 

id: string

ID of the meeting.

formatuuid

created_at: string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

updated_at: string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

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

paging: object { end_offset, start_offset, total_count } 

end_offset: number

start_offset: number

total_count: number

minimum0

success: boolean

MeetingCreateResponse object { success, data } 

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

MeetingGetMeetingByIDResponse object { success, data } 

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

MeetingUpdateMeetingByIDResponse object { success, data } 

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

MeetingReplaceMeetingByIDResponse object { success, data } 

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

MeetingGetMeetingParticipantsResponse object { data, paging, success } 

data: array of object { id, created_at, custom_participant_id, 4 more } 

id: string

ID of the participant.

formatuuid

created_at: string

When this object was created. The time is returned in ISO format.

formatdate-time

custom_participant_id: string

A unique participant ID generated by the client.

preset_name: string

Preset applied to the participant.

updated_at: string

When this object was updated. The time is returned in ISO format.

formatdate-time

name: optional string

Name of the participant.

picture: optional string

URL to a picture of the participant.

formaturi

paging: object { end_offset, start_offset, total_count } 

end_offset: number

start_offset: number

total_count: number

minimum0

success: boolean

MeetingAddParticipantResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { id, token, created_at, 5 more } 

Represents a participant.

id: string

ID of the participant.

formatuuid

token: string

The participant’s auth token that can be used for joining a meeting from the client side.

created_at: string

When this object was created. The time is returned in ISO format.

formatdate-time

custom_participant_id: string

A unique participant ID generated by the client.

preset_name: string

Preset applied to the participant.

updated_at: string

When this object was updated. The time is returned in ISO format.

formatdate-time

name: optional string

Name of the participant.

picture: optional string

URL to a picture of the participant.

formaturi

MeetingGetMeetingParticipantResponse object { data, success } 

data: object { id, created_at, custom_participant_id, 4 more } 

Data returned by the operation

id: string

ID of the participant.

formatuuid

created_at: string

When this object was created. The time is returned in ISO format.

formatdate-time

custom_participant_id: string

A unique participant ID generated by the client.

preset_name: string

Preset applied to the participant.

updated_at: string

When this object was updated. The time is returned in ISO format.

formatdate-time

name: optional string

Name of the participant.

picture: optional string

URL to a picture of the participant.

formaturi

success: boolean

Success status of the operation

MeetingEditParticipantResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { id, token, created_at, 5 more } 

Represents a participant.

id: string

ID of the participant.

formatuuid

token: string

The participant’s auth token that can be used for joining a meeting from the client side.

created_at: string

When this object was created. The time is returned in ISO format.

formatdate-time

custom_participant_id: string

A unique participant ID generated by the client.

preset_name: string

Preset applied to the participant.

updated_at: string

When this object was updated. The time is returned in ISO format.

formatdate-time

name: optional string

Name of the participant.

picture: optional string

URL to a picture of the participant.

formaturi

MeetingDeleteMeetingParticipantResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { created_at, custom_participant_id, preset_id, updated_at } 

Data returned by the operation

created_at: string

Timestamp this object was created at. The time is returned in ISO format.

formatdate-time

custom_participant_id: string

A unique participant ID generated by the client.

preset_id: string

ID of the preset applied to this participant.

formatuuid

updated_at: string

Timestamp this object was updated at. The time is returned in ISO format.

formatdate-time

MeetingRefreshParticipantTokenResponse object { data, success } 

data: object { token } 

Data returned by the operation

token: string

Regenerated participant’s authentication token.

success: boolean

Success status of the operation

#### Realtime KitPresets

##### [Fetch all presets](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/get)

GET/accounts/{account_id}/realtime/kit/{app_id}/presets

##### [Create a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create)

POST/accounts/{account_id}/realtime/kit/{app_id}/presets

##### [Fetch details of a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/get_preset_by_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### [Delete a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/delete)

DELETE/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### [Update a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/update)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### [Replace a preset](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/replace_preset_by_id)

PUT/accounts/{account_id}/realtime/kit/{app_id}/presets/{preset_id}

##### ModelsExpand Collapse 

PresetGetResponse object { data, paging, success } 

data: array of object { id, created_at, name, updated_at } 

id: optional string

ID of the preset

formatuuid

created_at: optional string

Timestamp this preset was created at

formatdate-time

name: optional string

Name of the preset

updated_at: optional string

Timestamp this preset was last updated

formatdate-time

paging: object { end_offset, start_offset, total_count } 

end_offset: number

start_offset: number

total_count: number

minimum0

success: boolean

PresetCreateResponse object { data, success } 

data: object { id, config, created_at, 4 more } 

Data returned by the operation

id: string

ID of the preset

formatuuid

config: object { max_screenshare_count, max_video_streams, media, 2 more } 

max_screenshare_count: number

Maximum number of screen shares that can be active at a given time

max_video_streams: object { desktop, mobile } 

Maximum number of streams that are visible on a device

desktop: number

Maximum number of video streams visible on desktop devices

mobile: number

Maximum number of streams visible on mobile devices

media: object { screenshare, video, audio } 

Media configuration options. eg: Video quality

screenshare: object { frame_rate, quality } 

Configuration options for participant screen shares

frame_rate: number

Frame rate of screen share

quality: "hd" or "vga" or "qvga" or 2 more

Quality of screen share

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

video: object { frame_rate, quality, simulcast } 

Configuration options for participant videos

frame_rate: number

Frame rate of participants’ video

maximum30

quality: "hd" or "vga" or "qvga" or 2 more

Video quality of participants

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

simulcast: optional boolean

Enable simulcast for participant videos.

audio: optional object { enable_high_bitrate, enable_stereo } 

Control options for Audio quality.

enable_high_bitrate: optional boolean

Enable High Quality Audio for your meetings

enable_stereo: optional boolean

Enable Stereo for your meetings

view_type: "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or "LIVESTREAM"

Type of the meeting

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

livestream_viewer_qualities: optional array of number

Livestream viewer quality levels.

created_at: string

Timestamp this preset was created at

formatdate-time

name: string

Name of the preset

permissions: object { accept_waiting_requests, can_accept_production_requests, can_change_participant_permissions, 23 more } 

accept_waiting_requests: boolean

Whether this participant can accept waiting requests

can_accept_production_requests: boolean

can_change_participant_permissions: boolean

can_edit_display_name: boolean

can_livestream: boolean

can_record: boolean

can_spotlight: boolean

chat: object { private, public } 

private: object { can_receive, can_send, files, text } 

can_receive: boolean

can_send: boolean

files: boolean

text: boolean

public: object { can_send, files, text } 

can_send: boolean

Can send messages in general

files: boolean

Can send file messages

text: boolean

Can send text messages

connected_meetings: object { can_alter_connected_meetings, can_switch_connected_meetings, can_switch_to_parent_meeting } 

can_alter_connected_meetings: boolean

can_switch_connected_meetings: boolean

can_switch_to_parent_meeting: boolean

disable_participant_audio: boolean

disable_participant_screensharing: boolean

disable_participant_video: boolean

hidden_participant: boolean

Whether this participant is visible to others or not

kick_participant: boolean

media: object { audio, screenshare, video } 

Media permissions

audio: object { can_produce } 

Audio permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce audio

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

screenshare: object { can_produce } 

Screenshare permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce screen share video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

video: object { can_produce } 

Video permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

pin_participant: boolean

plugins: object { can_close, can_edit_config, can_start, config } 

Plugin permissions

can_close: boolean

Can close plugins that are already open

can_edit_config: boolean

Can edit plugin config

can_start: boolean

Can start plugins

config: map[object { access_control, handles_view_only } ]

Plugin configuration keyed by plugin UUID.

access_control: optional "FULL_ACCESS" or "VIEW_ONLY"

One of the following:

"FULL_ACCESS"

"VIEW_ONLY"

handles_view_only: optional boolean

polls: object { can_create, can_view, can_vote } 

Poll permissions

can_create: boolean

Can create polls

can_view: boolean

Can view polls

can_vote: boolean

Can vote on polls

recorder_type: "RECORDER" or "LIVESTREAMER" or "NONE"

Type of the recording peer

One of the following:

"RECORDER"

"LIVESTREAMER"

"NONE"

show_participant_list: boolean

waiting_room_type: "SKIP" or "ON_PRIVILEGED_USER_ENTRY" or "SKIP_ON_ACCEPT"

Waiting room type

One of the following:

"SKIP"

"ON_PRIVILEGED_USER_ENTRY"

"SKIP_ON_ACCEPT"

accept_stage_requests: optional boolean

is_recorder: optional boolean

stage_access: optional "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

stage_enabled: optional boolean

transcription_enabled: optional boolean

ui: object { design_tokens } 

design_tokens: object { border_radius, border_width, colors, 5 more } 

border_radius: "sharp" or "rounded" or "extra-rounded" or "circular"

One of the following:

"sharp"

"rounded"

"extra-rounded"

"circular"

border_width: "none" or "thin" or "fat"

One of the following:

"none"

"thin"

"fat"

colors: object { background, brand, danger, 5 more } 

background: object { "1000", "600", "700", 2 more } 

"1000": string

"600": string

"700": string

"800": string

"900": string

brand: object { "300", "400", "500", 2 more } 

"300": string

"400": string

"500": string

"600": string

"700": string

danger: string

success: string

text: string

text_on_brand: string

video_bg: string

warning: string

spacing_base: number

minimum1

theme: "darkest" or "dark" or "light"

One of the following:

"darkest"

"dark"

"light"

font_family: optional string

google_font: optional string

logo: optional string

formaturi

updated_at: string

Timestamp this preset was last updated

formatdate-time

success: boolean

Success status of the operation

PresetGetPresetByIDResponse object { data, success } 

data: object { id, config, created_at, 4 more } 

Data returned by the operation

id: string

ID of the preset

formatuuid

config: object { max_screenshare_count, max_video_streams, media, 2 more } 

max_screenshare_count: number

Maximum number of screen shares that can be active at a given time

max_video_streams: object { desktop, mobile } 

Maximum number of streams that are visible on a device

desktop: number

Maximum number of video streams visible on desktop devices

mobile: number

Maximum number of streams visible on mobile devices

media: object { screenshare, video, audio } 

Media configuration options. eg: Video quality

screenshare: object { frame_rate, quality } 

Configuration options for participant screen shares

frame_rate: number

Frame rate of screen share

quality: "hd" or "vga" or "qvga" or 2 more

Quality of screen share

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

video: object { frame_rate, quality, simulcast } 

Configuration options for participant videos

frame_rate: number

Frame rate of participants’ video

maximum30

quality: "hd" or "vga" or "qvga" or 2 more

Video quality of participants

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

simulcast: optional boolean

Enable simulcast for participant videos.

audio: optional object { enable_high_bitrate, enable_stereo } 

Control options for Audio quality.

enable_high_bitrate: optional boolean

Enable High Quality Audio for your meetings

enable_stereo: optional boolean

Enable Stereo for your meetings

view_type: "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or "LIVESTREAM"

Type of the meeting

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

livestream_viewer_qualities: optional array of number

Livestream viewer quality levels.

created_at: string

Timestamp this preset was created at

formatdate-time

name: string

Name of the preset

permissions: object { accept_waiting_requests, can_accept_production_requests, can_change_participant_permissions, 23 more } 

accept_waiting_requests: boolean

Whether this participant can accept waiting requests

can_accept_production_requests: boolean

can_change_participant_permissions: boolean

can_edit_display_name: boolean

can_livestream: boolean

can_record: boolean

can_spotlight: boolean

chat: object { private, public } 

private: object { can_receive, can_send, files, text } 

can_receive: boolean

can_send: boolean

files: boolean

text: boolean

public: object { can_send, files, text } 

can_send: boolean

Can send messages in general

files: boolean

Can send file messages

text: boolean

Can send text messages

connected_meetings: object { can_alter_connected_meetings, can_switch_connected_meetings, can_switch_to_parent_meeting } 

can_alter_connected_meetings: boolean

can_switch_connected_meetings: boolean

can_switch_to_parent_meeting: boolean

disable_participant_audio: boolean

disable_participant_screensharing: boolean

disable_participant_video: boolean

hidden_participant: boolean

Whether this participant is visible to others or not

kick_participant: boolean

media: object { audio, screenshare, video } 

Media permissions

audio: object { can_produce } 

Audio permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce audio

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

screenshare: object { can_produce } 

Screenshare permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce screen share video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

video: object { can_produce } 

Video permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

pin_participant: boolean

plugins: object { can_close, can_edit_config, can_start, config } 

Plugin permissions

can_close: boolean

Can close plugins that are already open

can_edit_config: boolean

Can edit plugin config

can_start: boolean

Can start plugins

config: map[object { access_control, handles_view_only } ]

Plugin configuration keyed by plugin UUID.

access_control: optional "FULL_ACCESS" or "VIEW_ONLY"

One of the following:

"FULL_ACCESS"

"VIEW_ONLY"

handles_view_only: optional boolean

polls: object { can_create, can_view, can_vote } 

Poll permissions

can_create: boolean

Can create polls

can_view: boolean

Can view polls

can_vote: boolean

Can vote on polls

recorder_type: "RECORDER" or "LIVESTREAMER" or "NONE"

Type of the recording peer

One of the following:

"RECORDER"

"LIVESTREAMER"

"NONE"

show_participant_list: boolean

waiting_room_type: "SKIP" or "ON_PRIVILEGED_USER_ENTRY" or "SKIP_ON_ACCEPT"

Waiting room type

One of the following:

"SKIP"

"ON_PRIVILEGED_USER_ENTRY"

"SKIP_ON_ACCEPT"

accept_stage_requests: optional boolean

is_recorder: optional boolean

stage_access: optional "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

stage_enabled: optional boolean

transcription_enabled: optional boolean

ui: object { design_tokens } 

design_tokens: object { border_radius, border_width, colors, 5 more } 

border_radius: "sharp" or "rounded" or "extra-rounded" or "circular"

One of the following:

"sharp"

"rounded"

"extra-rounded"

"circular"

border_width: "none" or "thin" or "fat"

One of the following:

"none"

"thin"

"fat"

colors: object { background, brand, danger, 5 more } 

background: object { "1000", "600", "700", 2 more } 

"1000": string

"600": string

"700": string

"800": string

"900": string

brand: object { "300", "400", "500", 2 more } 

"300": string

"400": string

"500": string

"600": string

"700": string

danger: string

success: string

text: string

text_on_brand: string

video_bg: string

warning: string

spacing_base: number

minimum1

theme: "darkest" or "dark" or "light"

One of the following:

"darkest"

"dark"

"light"

font_family: optional string

google_font: optional string

logo: optional string

formaturi

updated_at: string

Timestamp this preset was last updated

formatdate-time

success: boolean

Success status of the operation

PresetDeleteResponse object { data, success } 

data: object { id, config, created_at, 4 more } 

Data returned by the operation

id: string

ID of the preset

formatuuid

config: object { max_screenshare_count, max_video_streams, media, 2 more } 

max_screenshare_count: number

Maximum number of screen shares that can be active at a given time

max_video_streams: object { desktop, mobile } 

Maximum number of streams that are visible on a device

desktop: number

Maximum number of video streams visible on desktop devices

mobile: number

Maximum number of streams visible on mobile devices

media: object { screenshare, video, audio } 

Media configuration options. eg: Video quality

screenshare: object { frame_rate, quality } 

Configuration options for participant screen shares

frame_rate: number

Frame rate of screen share

quality: "hd" or "vga" or "qvga" or 2 more

Quality of screen share

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

video: object { frame_rate, quality, simulcast } 

Configuration options for participant videos

frame_rate: number

Frame rate of participants’ video

maximum30

quality: "hd" or "vga" or "qvga" or 2 more

Video quality of participants

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

simulcast: optional boolean

Enable simulcast for participant videos.

audio: optional object { enable_high_bitrate, enable_stereo } 

Control options for Audio quality.

enable_high_bitrate: optional boolean

Enable High Quality Audio for your meetings

enable_stereo: optional boolean

Enable Stereo for your meetings

view_type: "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or "LIVESTREAM"

Type of the meeting

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

livestream_viewer_qualities: optional array of number

Livestream viewer quality levels.

created_at: string

Timestamp this preset was created at

formatdate-time

name: string

Name of the preset

permissions: object { accept_waiting_requests, can_accept_production_requests, can_change_participant_permissions, 23 more } 

accept_waiting_requests: boolean

Whether this participant can accept waiting requests

can_accept_production_requests: boolean

can_change_participant_permissions: boolean

can_edit_display_name: boolean

can_livestream: boolean

can_record: boolean

can_spotlight: boolean

chat: object { private, public } 

private: object { can_receive, can_send, files, text } 

can_receive: boolean

can_send: boolean

files: boolean

text: boolean

public: object { can_send, files, text } 

can_send: boolean

Can send messages in general

files: boolean

Can send file messages

text: boolean

Can send text messages

connected_meetings: object { can_alter_connected_meetings, can_switch_connected_meetings, can_switch_to_parent_meeting } 

can_alter_connected_meetings: boolean

can_switch_connected_meetings: boolean

can_switch_to_parent_meeting: boolean

disable_participant_audio: boolean

disable_participant_screensharing: boolean

disable_participant_video: boolean

hidden_participant: boolean

Whether this participant is visible to others or not

kick_participant: boolean

media: object { audio, screenshare, video } 

Media permissions

audio: object { can_produce } 

Audio permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce audio

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

screenshare: object { can_produce } 

Screenshare permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce screen share video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

video: object { can_produce } 

Video permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

pin_participant: boolean

plugins: object { can_close, can_edit_config, can_start, config } 

Plugin permissions

can_close: boolean

Can close plugins that are already open

can_edit_config: boolean

Can edit plugin config

can_start: boolean

Can start plugins

config: map[object { access_control, handles_view_only } ]

Plugin configuration keyed by plugin UUID.

access_control: optional "FULL_ACCESS" or "VIEW_ONLY"

One of the following:

"FULL_ACCESS"

"VIEW_ONLY"

handles_view_only: optional boolean

polls: object { can_create, can_view, can_vote } 

Poll permissions

can_create: boolean

Can create polls

can_view: boolean

Can view polls

can_vote: boolean

Can vote on polls

recorder_type: "RECORDER" or "LIVESTREAMER" or "NONE"

Type of the recording peer

One of the following:

"RECORDER"

"LIVESTREAMER"

"NONE"

show_participant_list: boolean

waiting_room_type: "SKIP" or "ON_PRIVILEGED_USER_ENTRY" or "SKIP_ON_ACCEPT"

Waiting room type

One of the following:

"SKIP"

"ON_PRIVILEGED_USER_ENTRY"

"SKIP_ON_ACCEPT"

accept_stage_requests: optional boolean

is_recorder: optional boolean

stage_access: optional "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

stage_enabled: optional boolean

transcription_enabled: optional boolean

ui: object { design_tokens } 

design_tokens: object { border_radius, border_width, colors, 5 more } 

border_radius: "sharp" or "rounded" or "extra-rounded" or "circular"

One of the following:

"sharp"

"rounded"

"extra-rounded"

"circular"

border_width: "none" or "thin" or "fat"

One of the following:

"none"

"thin"

"fat"

colors: object { background, brand, danger, 5 more } 

background: object { "1000", "600", "700", 2 more } 

"1000": string

"600": string

"700": string

"800": string

"900": string

brand: object { "300", "400", "500", 2 more } 

"300": string

"400": string

"500": string

"600": string

"700": string

danger: string

success: string

text: string

text_on_brand: string

video_bg: string

warning: string

spacing_base: number

minimum1

theme: "darkest" or "dark" or "light"

One of the following:

"darkest"

"dark"

"light"

font_family: optional string

google_font: optional string

logo: optional string

formaturi

updated_at: string

Timestamp this preset was last updated

formatdate-time

success: boolean

Success status of the operation

PresetUpdateResponse object { data, success } 

data: object { id, config, created_at, 4 more } 

Data returned by the operation

id: string

ID of the preset

formatuuid

config: object { max_screenshare_count, max_video_streams, media, 2 more } 

max_screenshare_count: number

Maximum number of screen shares that can be active at a given time

max_video_streams: object { desktop, mobile } 

Maximum number of streams that are visible on a device

desktop: number

Maximum number of video streams visible on desktop devices

mobile: number

Maximum number of streams visible on mobile devices

media: object { screenshare, video, audio } 

Media configuration options. eg: Video quality

screenshare: object { frame_rate, quality } 

Configuration options for participant screen shares

frame_rate: number

Frame rate of screen share

quality: "hd" or "vga" or "qvga" or 2 more

Quality of screen share

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

video: object { frame_rate, quality, simulcast } 

Configuration options for participant videos

frame_rate: number

Frame rate of participants’ video

maximum30

quality: "hd" or "vga" or "qvga" or 2 more

Video quality of participants

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

simulcast: optional boolean

Enable simulcast for participant videos.

audio: optional object { enable_high_bitrate, enable_stereo } 

Control options for Audio quality.

enable_high_bitrate: optional boolean

Enable High Quality Audio for your meetings

enable_stereo: optional boolean

Enable Stereo for your meetings

view_type: "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or "LIVESTREAM"

Type of the meeting

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

livestream_viewer_qualities: optional array of number

Livestream viewer quality levels.

created_at: string

Timestamp this preset was created at

formatdate-time

name: string

Name of the preset

permissions: object { accept_waiting_requests, can_accept_production_requests, can_change_participant_permissions, 23 more } 

accept_waiting_requests: boolean

Whether this participant can accept waiting requests

can_accept_production_requests: boolean

can_change_participant_permissions: boolean

can_edit_display_name: boolean

can_livestream: boolean

can_record: boolean

can_spotlight: boolean

chat: object { private, public } 

private: object { can_receive, can_send, files, text } 

can_receive: boolean

can_send: boolean

files: boolean

text: boolean

public: object { can_send, files, text } 

can_send: boolean

Can send messages in general

files: boolean

Can send file messages

text: boolean

Can send text messages

connected_meetings: object { can_alter_connected_meetings, can_switch_connected_meetings, can_switch_to_parent_meeting } 

can_alter_connected_meetings: boolean

can_switch_connected_meetings: boolean

can_switch_to_parent_meeting: boolean

disable_participant_audio: boolean

disable_participant_screensharing: boolean

disable_participant_video: boolean

hidden_participant: boolean

Whether this participant is visible to others or not

kick_participant: boolean

media: object { audio, screenshare, video } 

Media permissions

audio: object { can_produce } 

Audio permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce audio

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

screenshare: object { can_produce } 

Screenshare permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce screen share video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

video: object { can_produce } 

Video permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

pin_participant: boolean

plugins: object { can_close, can_edit_config, can_start, config } 

Plugin permissions

can_close: boolean

Can close plugins that are already open

can_edit_config: boolean

Can edit plugin config

can_start: boolean

Can start plugins

config: map[object { access_control, handles_view_only } ]

Plugin configuration keyed by plugin UUID.

access_control: optional "FULL_ACCESS" or "VIEW_ONLY"

One of the following:

"FULL_ACCESS"

"VIEW_ONLY"

handles_view_only: optional boolean

polls: object { can_create, can_view, can_vote } 

Poll permissions

can_create: boolean

Can create polls

can_view: boolean

Can view polls

can_vote: boolean

Can vote on polls

recorder_type: "RECORDER" or "LIVESTREAMER" or "NONE"

Type of the recording peer

One of the following:

"RECORDER"

"LIVESTREAMER"

"NONE"

show_participant_list: boolean

waiting_room_type: "SKIP" or "ON_PRIVILEGED_USER_ENTRY" or "SKIP_ON_ACCEPT"

Waiting room type

One of the following:

"SKIP"

"ON_PRIVILEGED_USER_ENTRY"

"SKIP_ON_ACCEPT"

accept_stage_requests: optional boolean

is_recorder: optional boolean

stage_access: optional "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

stage_enabled: optional boolean

transcription_enabled: optional boolean

ui: object { design_tokens } 

design_tokens: object { border_radius, border_width, colors, 5 more } 

border_radius: "sharp" or "rounded" or "extra-rounded" or "circular"

One of the following:

"sharp"

"rounded"

"extra-rounded"

"circular"

border_width: "none" or "thin" or "fat"

One of the following:

"none"

"thin"

"fat"

colors: object { background, brand, danger, 5 more } 

background: object { "1000", "600", "700", 2 more } 

"1000": string

"600": string

"700": string

"800": string

"900": string

brand: object { "300", "400", "500", 2 more } 

"300": string

"400": string

"500": string

"600": string

"700": string

danger: string

success: string

text: string

text_on_brand: string

video_bg: string

warning: string

spacing_base: number

minimum1

theme: "darkest" or "dark" or "light"

One of the following:

"darkest"

"dark"

"light"

font_family: optional string

google_font: optional string

logo: optional string

formaturi

updated_at: string

Timestamp this preset was last updated

formatdate-time

success: boolean

Success status of the operation

PresetReplacePresetByIDResponse object { data, success } 

data: object { id, config, created_at, 4 more } 

Data returned by the operation

id: string

ID of the preset

formatuuid

config: object { max_screenshare_count, max_video_streams, media, 2 more } 

max_screenshare_count: number

Maximum number of screen shares that can be active at a given time

max_video_streams: object { desktop, mobile } 

Maximum number of streams that are visible on a device

desktop: number

Maximum number of video streams visible on desktop devices

mobile: number

Maximum number of streams visible on mobile devices

media: object { screenshare, video, audio } 

Media configuration options. eg: Video quality

screenshare: object { frame_rate, quality } 

Configuration options for participant screen shares

frame_rate: number

Frame rate of screen share

quality: "hd" or "vga" or "qvga" or 2 more

Quality of screen share

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

video: object { frame_rate, quality, simulcast } 

Configuration options for participant videos

frame_rate: number

Frame rate of participants’ video

maximum30

quality: "hd" or "vga" or "qvga" or 2 more

Video quality of participants

One of the following:

"hd"

"vga"

"qvga"

"fhd"

"uhd"

simulcast: optional boolean

Enable simulcast for participant videos.

audio: optional object { enable_high_bitrate, enable_stereo } 

Control options for Audio quality.

enable_high_bitrate: optional boolean

Enable High Quality Audio for your meetings

enable_stereo: optional boolean

Enable Stereo for your meetings

view_type: "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or "LIVESTREAM"

Type of the meeting

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

livestream_viewer_qualities: optional array of number

Livestream viewer quality levels.

created_at: string

Timestamp this preset was created at

formatdate-time

name: string

Name of the preset

permissions: object { accept_waiting_requests, can_accept_production_requests, can_change_participant_permissions, 23 more } 

accept_waiting_requests: boolean

Whether this participant can accept waiting requests

can_accept_production_requests: boolean

can_change_participant_permissions: boolean

can_edit_display_name: boolean

can_livestream: boolean

can_record: boolean

can_spotlight: boolean

chat: object { private, public } 

private: object { can_receive, can_send, files, text } 

can_receive: boolean

can_send: boolean

files: boolean

text: boolean

public: object { can_send, files, text } 

can_send: boolean

Can send messages in general

files: boolean

Can send file messages

text: boolean

Can send text messages

connected_meetings: object { can_alter_connected_meetings, can_switch_connected_meetings, can_switch_to_parent_meeting } 

can_alter_connected_meetings: boolean

can_switch_connected_meetings: boolean

can_switch_to_parent_meeting: boolean

disable_participant_audio: boolean

disable_participant_screensharing: boolean

disable_participant_video: boolean

hidden_participant: boolean

Whether this participant is visible to others or not

kick_participant: boolean

media: object { audio, screenshare, video } 

Media permissions

audio: object { can_produce } 

Audio permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce audio

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

screenshare: object { can_produce } 

Screenshare permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce screen share video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

video: object { can_produce } 

Video permissions

can_produce: "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

Can produce video

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

pin_participant: boolean

plugins: object { can_close, can_edit_config, can_start, config } 

Plugin permissions

can_close: boolean

Can close plugins that are already open

can_edit_config: boolean

Can edit plugin config

can_start: boolean

Can start plugins

config: map[object { access_control, handles_view_only } ]

Plugin configuration keyed by plugin UUID.

access_control: optional "FULL_ACCESS" or "VIEW_ONLY"

One of the following:

"FULL_ACCESS"

"VIEW_ONLY"

handles_view_only: optional boolean

polls: object { can_create, can_view, can_vote } 

Poll permissions

can_create: boolean

Can create polls

can_view: boolean

Can view polls

can_vote: boolean

Can vote on polls

recorder_type: "RECORDER" or "LIVESTREAMER" or "NONE"

Type of the recording peer

One of the following:

"RECORDER"

"LIVESTREAMER"

"NONE"

show_participant_list: boolean

waiting_room_type: "SKIP" or "ON_PRIVILEGED_USER_ENTRY" or "SKIP_ON_ACCEPT"

Waiting room type

One of the following:

"SKIP"

"ON_PRIVILEGED_USER_ENTRY"

"SKIP_ON_ACCEPT"

accept_stage_requests: optional boolean

is_recorder: optional boolean

stage_access: optional "ALLOWED" or "NOT_ALLOWED" or "CAN_REQUEST"

One of the following:

"ALLOWED"

"NOT_ALLOWED"

"CAN_REQUEST"

stage_enabled: optional boolean

transcription_enabled: optional boolean

ui: object { design_tokens } 

design_tokens: object { border_radius, border_width, colors, 5 more } 

border_radius: "sharp" or "rounded" or "extra-rounded" or "circular"

One of the following:

"sharp"

"rounded"

"extra-rounded"

"circular"

border_width: "none" or "thin" or "fat"

One of the following:

"none"

"thin"

"fat"

colors: object { background, brand, danger, 5 more } 

background: object { "1000", "600", "700", 2 more } 

"1000": string

"600": string

"700": string

"800": string

"900": string

brand: object { "300", "400", "500", 2 more } 

"300": string

"400": string

"500": string

"600": string

"700": string

danger: string

success: string

text: string

text_on_brand: string

video_bg: string

warning: string

spacing_base: number

minimum1

theme: "darkest" or "dark" or "light"

One of the following:

"darkest"

"dark"

"light"

font_family: optional string

google_font: optional string

logo: optional string

formaturi

updated_at: string

Timestamp this preset was last updated

formatdate-time

success: boolean

Success status of the operation

#### Realtime KitSessions

##### [Fetch all sessions of an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_sessions)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions

##### [Fetch details of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_details)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}

##### [Fetch participants list of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_participants)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants

##### [Fetch details of a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_participant_details)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/participants/{participant_id}

##### [Fetch all chat messages of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_chat)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/chat

##### [Fetch the complete transcript for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/transcript

##### [Fetch summary of transcripts for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary

##### [Generate summary of Transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts)

POST/accounts/{account_id}/realtime/kit/{app_id}/sessions/{session_id}/summary

##### [Fetch details of peer](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_participant_data_from_peer_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/sessions/peer-report/{peer_id}

##### ModelsExpand Collapse 

SessionGetSessionsResponse object { data, paging, success } 

data: optional object { sessions } 

sessions: optional array of object { id, associated_id, created_at, 11 more } 

id: string

ID of the session

associated_id: string

ID of the meeting this session is associated with. In the case of V2 meetings, it is always a UUID. In V1 meetings, it is a room name of the form `abcdef-ghijkl`

created_at: string

timestamp when session created

live_participants: number

number of participants currently in the session

max_concurrent_participants: number

number of maximum participants that were in the session

meeting_display_name: string

Title of the meeting this session belongs to

minutes_consumed: number

number of minutes consumed since the session started

organization_id: string

App id that hosted this session

started_at: string

timestamp when session started

status: "LIVE" or "ENDED"

current status of session

One of the following:

"LIVE"

"ENDED"

type: "meeting" or "livestream" or "participant"

type of session

One of the following:

"meeting"

"livestream"

"participant"

updated_at: string

timestamp when session was last updated

breakout_rooms: optional array of unknown

ended_at: optional string

timestamp when session ended

paging: optional object { end_offset, start_offset, total_count } 

end_offset: optional number

start_offset: optional number

total_count: optional number

minimum0

success: optional boolean

SessionGetSessionDetailsResponse object { data, success } 

data: optional object { id, associated_id, created_at, 11 more } 

id: string

ID of the session

associated_id: string

ID of the meeting this session is associated with. In the case of V2 meetings, it is always a UUID. In V1 meetings, it is a room name of the form `abcdef-ghijkl`

created_at: string

timestamp when session created

live_participants: number

number of participants currently in the session

max_concurrent_participants: number

number of maximum participants that were in the session

meeting_display_name: string

Title of the meeting this session belongs to

minutes_consumed: number

number of minutes consumed since the session started

organization_id: string

App id that hosted this session

started_at: string

timestamp when session started

status: "LIVE" or "ENDED"

current status of session

One of the following:

"LIVE"

"ENDED"

type: "meeting" or "livestream" or "participant"

type of session

One of the following:

"meeting"

"livestream"

"participant"

updated_at: string

timestamp when session was last updated

breakout_rooms: optional array of unknown

ended_at: optional string

timestamp when session ended

success: optional boolean

SessionGetSessionParticipantsResponse object { data, success } 

data: optional object { participants } 

participants: optional array of object { id, created_at, custom_participant_id, 8 more } 

id: optional string

Participant ID. This maps to the corresponding peerId.

created_at: optional string

timestamp when this participant was created.

custom_participant_id: optional string

ID passed by client to create this participant.

display_name: optional string

Display name of participant when joining the session.

duration: optional number

number of minutes for which the participant was in the session.

joined_at: optional string

timestamp at which participant joined the session.

left_at: optional string

timestamp at which participant left the session.

peer_events: optional array of object { id, created_at, event_name, 7 more } 

Connection lifecycle events for the participant’s peer. Only included when `include_peer_events` is true.

id: optional string

ID of the peer event.

created_at: optional string

Timestamp when this peer event was created.

event_name: optional "PEER_CREATED" or "PEER_JOINING" or "PEER_LEAVING"

Name of the peer event.

One of the following:

"PEER_CREATED"

"PEER_JOINING"

"PEER_LEAVING"

minutes_consumed: optional number

Minutes consumed attributed to this event.

participant_id: optional string

ID of the participant this event belongs to.

peer_id: optional string

Peer ID this event belongs to.

preset_view_type: optional "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or 2 more

View type of the preset associated with the peer.

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

"CHAT"

session_id: optional string

ID of the session this event belongs to.

socket_session_id: optional string

ID of the socket session associated with this event.

updated_at: optional string

Timestamp when this peer event was last updated.

preset_name: optional string

Name of the preset associated with the participant.

updated_at: optional string

timestamp when this participant’s data was last updated.

user_id: optional string

User id for this participant.

success: optional boolean

SessionGetSessionParticipantDetailsResponse object { data, success } 

data: optional object { participant } 

participant: optional object { id, created_at, custom_participant_id, 8 more } 

id: optional string

Participant ID. This maps to the corresponding peerId.

created_at: optional string

timestamp when this participant was created.

custom_participant_id: optional string

ID passed by client to create this participant.

display_name: optional string

Display name of participant when joining the session.

duration: optional number

number of minutes for which the participant was in the session.

joined_at: optional string

timestamp at which participant joined the session.

left_at: optional string

timestamp at which participant left the session.

peer_events: optional array of object { id, created_at, event_name, 7 more } 

Connection lifecycle events for the participant’s peer. Only included when `include_peer_events` is true.

id: optional string

ID of the peer event.

created_at: optional string

Timestamp when this peer event was created.

event_name: optional "PEER_CREATED" or "PEER_JOINING" or "PEER_LEAVING"

Name of the peer event.

One of the following:

"PEER_CREATED"

"PEER_JOINING"

"PEER_LEAVING"

minutes_consumed: optional number

Minutes consumed attributed to this event.

participant_id: optional string

ID of the participant this event belongs to.

peer_id: optional string

Peer ID this event belongs to.

preset_view_type: optional "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or 2 more

View type of the preset associated with the peer.

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

"CHAT"

session_id: optional string

ID of the session this event belongs to.

socket_session_id: optional string

ID of the socket session associated with this event.

updated_at: optional string

Timestamp when this peer event was last updated.

preset_name: optional string

Name of the preset associated with the participant.

updated_at: optional string

timestamp when this participant’s data was last updated.

user_id: optional string

User id for this participant.

success: optional boolean

SessionGetSessionChatResponse object { data, success } 

data: optional object { chat_download_url, chat_download_url_expiry } 

chat_download_url: string

URL where the chat logs can be downloaded

chat_download_url_expiry: string

Time when the download URL will expire

success: optional boolean

SessionGetSessionTranscriptsResponse object { data, success } 

data: optional object { sessionId, transcript_download_url, transcript_download_url_expiry } 

sessionId: string

transcript_download_url: string

URL where the transcript can be downloaded

transcript_download_url_expiry: string

Time when the download URL will expire

success: optional boolean

SessionGetSessionSummaryResponse object { data, success } 

data: optional object { sessionId, summaryDownloadUrl, summaryDownloadUrlExpiry } 

sessionId: string

summaryDownloadUrl: string

URL where the summary of transcripts can be downloaded

summaryDownloadUrlExpiry: string

Time of Expiry before when you need to download the csv file.

success: optional boolean

SessionGenerateSummaryOfTranscriptsResponse object { data, success } 

data: optional object { session_id, status } 

session_id: optional string

formatuuid

status: optional string

success: optional boolean

SessionGetParticipantDataFromPeerIDResponse object { data, success } 

data: optional object { participant } 

participant: optional object { id, created_at, custom_participant_id, 10 more } 

id: optional string

ID of the participant.

formatuuid

created_at: optional string

timestamp when this participant was created.

custom_participant_id: optional string

ID passed by client to create this participant.

display_name: optional string

Display name of participant when joining the session.

duration: optional number

number of minutes for which the participant was in the session.

joined_at: optional string

timestamp at which participant joined the session.

left_at: optional string

timestamp at which participant left the session.

peer_events: optional array of object { id, created_at, event_name, 7 more } 

Connection lifecycle events for the participant’s peer.

id: optional string

ID of the peer event.

created_at: optional string

Timestamp when this peer event was created.

event_name: optional "PEER_CREATED" or "PEER_JOINING" or "PEER_LEAVING"

Name of the peer event.

One of the following:

"PEER_CREATED"

"PEER_JOINING"

"PEER_LEAVING"

minutes_consumed: optional number

Minutes consumed attributed to this event.

participant_id: optional string

ID of the participant this event belongs to.

peer_id: optional string

Peer ID this event belongs to.

preset_view_type: optional "GROUP_CALL" or "WEBINAR" or "AUDIO_ROOM" or 2 more

View type of the preset associated with the peer.

One of the following:

"GROUP_CALL"

"WEBINAR"

"AUDIO_ROOM"

"LIVESTREAM"

"CHAT"

session_id: optional string

ID of the session this event belongs to.

socket_session_id: optional string

ID of the socket session associated with this event.

updated_at: optional string

Timestamp when this peer event was last updated.

peer_report: optional object { metadata, quality } 

Peer call statistics report.

metadata: optional object { audio_devices_updates, browser_metadata, candidate_pairs, 12 more } 

Connection and device metadata for the participant.

audio_devices_updates: optional array of object { added, removed, timestamp } 

added: optional array of object { device_id, kind, label } 

Devices that became available.

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

removed: optional array of object { device_id, kind, label } 

Devices that became unavailable.

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

timestamp: optional string

Timestamp of the device update.

browser_metadata: optional object { browser, browser_version, engine, 2 more } 

browser: optional string

browser_version: optional string

engine: optional string

user_agent: optional string

webgl_support: optional boolean

candidate_pairs: optional object { consuming_transport, producing_transport } 

consuming_transport: optional array of object { available_incoming_bitrate, available_outgoing_bitrate, bytes_discarded_on_send, 25 more } 

available_incoming_bitrate: optional number

available_outgoing_bitrate: optional number

bytes_discarded_on_send: optional number

bytes_received: optional number

bytes_sent: optional number

current_round_trip_time: optional number

last_packet_received_timestamp: optional number

Epoch milliseconds when the last packet was received.

last_packet_sent_timestamp: optional number

Epoch milliseconds when the last packet was sent.

local_candidate_address: optional string

local_candidate_id: optional string

local_candidate_network_type: optional string

local_candidate_port: optional number

local_candidate_protocol: optional string

local_candidate_related_address: optional string

local_candidate_related_port: optional number

local_candidate_type: optional string

local_candidate_url: optional string

nominated: optional boolean

packets_discarded_on_send: optional number

packets_received: optional number

packets_sent: optional number

remote_candidate_address: optional string

remote_candidate_id: optional string

remote_candidate_port: optional number

remote_candidate_protocol: optional string

remote_candidate_type: optional string

remote_candidate_url: optional string

total_round_trip_time: optional number

producing_transport: optional array of object { available_incoming_bitrate, available_outgoing_bitrate, bytes_discarded_on_send, 25 more } 

available_incoming_bitrate: optional number

available_outgoing_bitrate: optional number

bytes_discarded_on_send: optional number

bytes_received: optional number

bytes_sent: optional number

current_round_trip_time: optional number

last_packet_received_timestamp: optional number

Epoch milliseconds when the last packet was received.

last_packet_sent_timestamp: optional number

Epoch milliseconds when the last packet was sent.

local_candidate_address: optional string

local_candidate_id: optional string

local_candidate_network_type: optional string

local_candidate_port: optional number

local_candidate_protocol: optional string

local_candidate_related_address: optional string

local_candidate_related_port: optional number

local_candidate_type: optional string

local_candidate_url: optional string

nominated: optional boolean

packets_discarded_on_send: optional number

packets_received: optional number

packets_sent: optional number

remote_candidate_address: optional string

remote_candidate_id: optional string

remote_candidate_port: optional number

remote_candidate_protocol: optional string

remote_candidate_type: optional string

remote_candidate_url: optional string

total_round_trip_time: optional number

device_info: optional object { cpus, is_mobile, os, os_version } 

cpus: optional number

is_mobile: optional boolean

os: optional string

os_version: optional string

events: optional array of object { metadata, name, timestamp } 

metadata: optional map[string or number or boolean]

Event-specific metadata. Keys vary per event; values are primitive scalars (string, number, boolean, or null).

One of the following:

string

number

boolean

name: optional string

Name of the event.

timestamp: optional string

Timestamp when the event occurred.

ip_information: optional object { asn, city, country, 4 more } 

asn: optional object { asn, domain, name, 2 more } 

asn: optional string

domain: optional string

name: optional string

route: optional string

type: optional string

city: optional string

country: optional string

ipv4: optional string

org: optional string

region: optional string

timezone: optional string

native_metadata: optional object { audio_encoder, video_encoder } 

audio_encoder: optional string

video_encoder: optional string

pc_metadata: optional array of object { effective_network_type, reflexive_connectivity, relay_connectivity, 3 more } 

effective_network_type: optional string

reflexive_connectivity: optional boolean

relay_connectivity: optional boolean

sdp: optional array of string

timestamp: optional string

turn_connectivity: optional boolean

room_view_type: optional string

sdk_name: optional string

sdk_type: optional string

sdk_version: optional string

selected_device_updates: optional array of object { device, timestamp } 

device: optional object { device_id, kind, label } 

A media device (camera, microphone, or speaker).

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

timestamp: optional string

speaker_devices_updates: optional array of object { added, removed, timestamp } 

added: optional array of object { device_id, kind, label } 

Devices that became available.

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

removed: optional array of object { device_id, kind, label } 

Devices that became unavailable.

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

timestamp: optional string

Timestamp of the device update.

video_devices_updates: optional array of object { added, removed, timestamp } 

added: optional array of object { device_id, kind, label } 

Devices that became available.

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

removed: optional array of object { device_id, kind, label } 

Devices that became unavailable.

device_id: optional string

ID of the device.

kind: optional string

Kind of device, for example audioinput or videoinput.

label: optional string

Human-readable label of the device.

timestamp: optional string

Timestamp of the device update.

quality: optional object { audio_consumer, audio_consumer_cumulative, audio_producer, 13 more } 

Media quality statistics for the participant.

audio_consumer: optional array of object { bytes_received, concealment_events, consumer_id, 11 more } 

bytes_received: optional number

concealment_events: optional number

consumer_id: optional string

jitter: optional number

jitter_buffer_delay: optional number

jitter_buffer_emitted_count: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_received: optional number

peer_id: optional string

producer_id: optional string

ssrc: optional number

timestamp: optional string

audio_consumer_cumulative: optional object { jitter_buffer_delay, packet_loss, quality_mos } 

Aggregated inbound (consumer) audio statistics for the session.

jitter_buffer_delay: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

audio_producer: optional array of object { bytes_sent, jitter, mid, 7 more } 

bytes_sent: optional number

jitter: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_sent: optional number

producer_id: optional string

rtt: optional number

ssrc: optional number

timestamp: optional string

audio_producer_cumulative: optional object { packet_loss, quality_mos, rtt } 

Aggregated outbound (producer) audio statistics for the session.

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

rtt: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

screenshare_audio_consumer: optional array of object { bytes_received, concealment_events, consumer_id, 11 more } 

bytes_received: optional number

concealment_events: optional number

consumer_id: optional string

jitter: optional number

jitter_buffer_delay: optional number

jitter_buffer_emitted_count: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_received: optional number

peer_id: optional string

producer_id: optional string

ssrc: optional number

timestamp: optional string

screenshare_audio_consumer_cumulative: optional object { jitter_buffer_delay, packet_loss, quality_mos } 

Aggregated inbound (consumer) audio statistics for the session.

jitter_buffer_delay: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

screenshare_audio_producer: optional array of object { bytes_sent, jitter, mid, 7 more } 

bytes_sent: optional number

jitter: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_sent: optional number

producer_id: optional string

rtt: optional number

ssrc: optional number

timestamp: optional string

screenshare_audio_producer_cumulative: optional object { packet_loss, quality_mos, rtt } 

Aggregated outbound (producer) audio statistics for the session.

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

rtt: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

screenshare_video_consumer: optional array of object { bytes_received, consumer_id, fir_count, 17 more } 

bytes_received: optional number

consumer_id: optional string

fir_count: optional number

frame_height: optional number

frame_width: optional number

frames_decoded: optional number

frames_dropped: optional number

frames_per_second: optional number

jitter: optional number

jitter_buffer_delay: optional number

jitter_buffer_emitted_count: optional number

key_frames_decoded: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_received: optional number

peer_id: optional string

producer_id: optional string

ssrc: optional number

timestamp: optional string

screenshare_video_consumer_cumulative: optional object { frame_per_second, frame_width, issues, 4 more } 

Aggregated inbound (consumer) video statistics for the session.

frame_per_second: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

frame_width: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

issues: optional object { lag_fraction, no_video_fraction, poor_resolution_fraction } 

lag_fraction: optional number

no_video_fraction: optional number

poor_resolution_fraction: optional number

jitter_buffer_delay: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

key_frames_decoded_fraction: optional number

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

screenshare_video_producer: optional array of object { bytes_sent, fir_count, frame_height, 17 more } 

bytes_sent: optional number

fir_count: optional number

frame_height: optional number

frame_width: optional number

frames_encoded: optional number

frames_per_second: optional number

jitter: optional number

key_frames_encoded: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_sent: optional number

pli_count: optional number

producer_id: optional string

quality_limitation_durations: optional object { bandwidth, cpu, none, other } 

bandwidth: optional number

cpu: optional number

none: optional number

other: optional number

quality_limitation_reason: optional "cpu" or "bandwidth" or "none" or "other"

One of the following:

"cpu"

"bandwidth"

"none"

"other"

quality_limitation_resolution_changes: optional number

rtt: optional number

ssrc: optional number

timestamp: optional string

screenshare_video_producer_cumulative: optional object { frame_per_second, frame_width, high_negative_feedback_fraction, 5 more } 

Aggregated outbound (producer) video statistics for the session.

frame_per_second: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

frame_width: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

high_negative_feedback_fraction: optional number

issues: optional object { bandwidth_quality_limitation_fraction, cpu_quality_limitation_fraction, no_video_fraction, 2 more } 

bandwidth_quality_limitation_fraction: optional number

cpu_quality_limitation_fraction: optional number

no_video_fraction: optional number

poor_resolution_fraction: optional number

quality_limitation_fraction: optional number

key_frames_encoded_fraction: optional number

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

rtt: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

video_consumer: optional array of object { bytes_received, consumer_id, fir_count, 17 more } 

bytes_received: optional number

consumer_id: optional string

fir_count: optional number

frame_height: optional number

frame_width: optional number

frames_decoded: optional number

frames_dropped: optional number

frames_per_second: optional number

jitter: optional number

jitter_buffer_delay: optional number

jitter_buffer_emitted_count: optional number

key_frames_decoded: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_received: optional number

peer_id: optional string

producer_id: optional string

ssrc: optional number

timestamp: optional string

video_consumer_cumulative: optional object { frame_per_second, frame_width, issues, 4 more } 

Aggregated inbound (consumer) video statistics for the session.

frame_per_second: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

frame_width: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

issues: optional object { lag_fraction, no_video_fraction, poor_resolution_fraction } 

lag_fraction: optional number

no_video_fraction: optional number

poor_resolution_fraction: optional number

jitter_buffer_delay: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

key_frames_decoded_fraction: optional number

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

video_producer: optional array of object { bytes_sent, fir_count, frame_height, 17 more } 

bytes_sent: optional number

fir_count: optional number

frame_height: optional number

frame_width: optional number

frames_encoded: optional number

frames_per_second: optional number

jitter: optional number

key_frames_encoded: optional number

mid: optional string

mos_quality: optional number

packets_lost: optional number

packets_sent: optional number

pli_count: optional number

producer_id: optional string

quality_limitation_durations: optional object { bandwidth, cpu, none, other } 

bandwidth: optional number

cpu: optional number

none: optional number

other: optional number

quality_limitation_reason: optional "cpu" or "bandwidth" or "none" or "other"

One of the following:

"cpu"

"bandwidth"

"none"

"other"

quality_limitation_resolution_changes: optional number

rtt: optional number

ssrc: optional number

timestamp: optional string

video_producer_cumulative: optional object { frame_per_second, frame_width, high_negative_feedback_fraction, 5 more } 

Aggregated outbound (producer) video statistics for the session.

frame_per_second: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

frame_width: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

high_negative_feedback_fraction: optional number

issues: optional object { bandwidth_quality_limitation_fraction, cpu_quality_limitation_fraction, no_video_fraction, 2 more } 

bandwidth_quality_limitation_fraction: optional number

cpu_quality_limitation_fraction: optional number

no_video_fraction: optional number

poor_resolution_fraction: optional number

quality_limitation_fraction: optional number

key_frames_encoded_fraction: optional number

packet_loss: optional object { "10_or_greater_event_fraction", "25_or_greater_event_fraction", "5_or_greater_event_fraction", 2 more } 

Cumulative packet loss distribution.

"10_or_greater_event_fraction": optional number

"25_or_greater_event_fraction": optional number

"5_or_greater_event_fraction": optional number

"50_or_greater_event_fraction": optional number

avg: optional number

quality_mos: optional object { avg, p50, p75, p90 } 

Distribution summary with average and percentiles.

avg: optional number

p50: optional number

p75: optional number

p90: optional number

rtt: optional object { "100ms_or_greater_event_fraction", "250ms_or_greater_event_fraction", "500ms_or_greater_event_fraction", avg } 

Cumulative latency distribution (milliseconds-based thresholds).

"100ms_or_greater_event_fraction": optional number

"250ms_or_greater_event_fraction": optional number

"500ms_or_greater_event_fraction": optional number

avg: optional number

role: optional string

Name of the preset associated with the participant.

session_id: optional string

formatuuid

updated_at: optional string

timestamp when this participant’s data was last updated.

user_id: optional string

User id for this participant.

success: optional boolean

#### Realtime KitRecordings

##### [Fetch all recordings for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_recordings)

GET/accounts/{account_id}/realtime/kit/{app_id}/recordings

##### [Start recording a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings)

POST/accounts/{account_id}/realtime/kit/{app_id}/recordings

##### [Fetch active recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings)

GET/accounts/{account_id}/realtime/kit/{app_id}/recordings/active-recording/{meeting_id}

##### [Fetch details of a recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording)

GET/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}

##### [Pause/Resume/Stop recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/pause_resume_stop_recording)

PUT/accounts/{account_id}/realtime/kit/{app_id}/recordings/{recording_id}

##### [Start recording participant audio tracks](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_track_recording)

POST/accounts/{account_id}/realtime/kit/{app_id}/recordings/track

##### ModelsExpand Collapse 

RecordingGetRecordingsResponse object { data, paging, success } 

data: array of object { id, audio_download_url, download_url, 11 more } 

id: string

ID of the recording

formatuuid

audio_download_url: string

If the audio_config is passed, the URL for downloading the audio recording is returned.

formaturi

download_url: string

URL where the recording can be downloaded.

formaturi

download_url_expiry: string

Timestamp when the download URL expires.

formatdate-time

file_size: number

File size of the recording, in bytes.

invoked_time: string

Timestamp when this recording was invoked.

formatdate-time

output_file_name: string

File name of the recording.

session_id: string

ID of the meeting session this recording is for.

formatuuid

started_time: string

Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.

formatdate-time

status: "INVOKED" or "RECORDING" or "UPLOADING" or 3 more

Current status of the recording.

One of the following:

"INVOKED"

"RECORDING"

"UPLOADING"

"UPLOADED"

"ERRORED"

"PAUSED"

stopped_time: string

Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.

formatdate-time

meeting: optional object { id, created_at, updated_at, 9 more } 

id: string

ID of the meeting.

formatuuid

created_at: string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

updated_at: string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

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

recording_duration: optional number

Total recording time in seconds.

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

paging: object { end_offset, start_offset, total_count } 

end_offset: number

start_offset: number

total_count: number

minimum0

success: boolean

RecordingStartRecordingsResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { id, audio_download_url, download_url, 12 more } 

Data returned by the operation

id: string

ID of the recording

formatuuid

audio_download_url: string

If the audio_config is passed, the URL for downloading the audio recording is returned.

formaturi

download_url: string

URL where the recording can be downloaded.

formaturi

download_url_expiry: string

Timestamp when the download URL expires.

formatdate-time

file_size: number

File size of the recording, in bytes.

invoked_time: string

Timestamp when this recording was invoked.

formatdate-time

output_file_name: string

File name of the recording.

session_id: string

ID of the meeting session this recording is for.

formatuuid

started_time: string

Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.

formatdate-time

status: "INVOKED" or "RECORDING" or "UPLOADING" or 3 more

Current status of the recording.

One of the following:

"INVOKED"

"RECORDING"

"UPLOADING"

"UPLOADED"

"ERRORED"

"PAUSED"

stopped_time: string

Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.

formatdate-time

recording_duration: optional number

Total recording time in seconds.

start_reason: optional object { caller, reason } 

caller: optional object { name, type, user_Id } 

name: optional string

Name of the user who started the recording.

type: optional "ORGANIZATION" or "USER"

The type can be an App or a user. If the type is `user`, then only the `user_Id` and `name` are returned.

One of the following:

"ORGANIZATION"

"USER"

user_Id: optional string

The user ID of the person who started the recording.

formatuuid

reason: optional "API_CALL" or "RECORD_ON_START"

Specifies if the recording was started using the “Start a Recording”API or using the parameter RECORD_ON_START in the “Create a meeting” API.

If the recording is initiated using the “RECORD_ON_START” parameter, the user details will not be populated.

One of the following:

"API_CALL"

"RECORD_ON_START"

stop_reason: optional object { caller, reason } 

caller: optional object { name, type, user_Id } 

name: optional string

Name of the user who stopped the recording.

type: optional "ORGANIZATION" or "USER"

The type can be an App or a user. If the type is `user`, then only the `user_Id` and `name` are returned.

One of the following:

"ORGANIZATION"

"USER"

user_Id: optional string

The user ID of the person who stopped the recording.

formatuuid

reason: optional "API_CALL" or "INTERNAL_ERROR" or "ALL_PEERS_LEFT"

Specifies the reason why the recording stopped.

One of the following:

"API_CALL"

"INTERNAL_ERROR"

"ALL_PEERS_LEFT"

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

RecordingGetActiveRecordingsResponse object { data, success } 

data: object { id, audio_download_url, download_url, 9 more } 

Data returned by the operation

id: string

ID of the recording

formatuuid

audio_download_url: string

If the audio_config is passed, the URL for downloading the audio recording is returned.

formaturi

download_url: string

URL where the recording can be downloaded.

formaturi

download_url_expiry: string

Timestamp when the download URL expires.

formatdate-time

file_size: number

File size of the recording, in bytes.

invoked_time: string

Timestamp when this recording was invoked.

formatdate-time

output_file_name: string

File name of the recording.

session_id: string

ID of the meeting session this recording is for.

formatuuid

started_time: string

Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.

formatdate-time

status: "INVOKED" or "RECORDING" or "UPLOADING" or 3 more

Current status of the recording.

One of the following:

"INVOKED"

"RECORDING"

"UPLOADING"

"UPLOADED"

"ERRORED"

"PAUSED"

stopped_time: string

Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.

formatdate-time

recording_duration: optional number

Total recording time in seconds.

success: boolean

Success status of the operation

RecordingGetOneRecordingResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { id, audio_download_url, download_url, 12 more } 

Data returned by the operation

id: string

ID of the recording

formatuuid

audio_download_url: string

If the audio_config is passed, the URL for downloading the audio recording is returned.

formaturi

download_url: string

URL where the recording can be downloaded.

formaturi

download_url_expiry: string

Timestamp when the download URL expires.

formatdate-time

file_size: number

File size of the recording, in bytes.

invoked_time: string

Timestamp when this recording was invoked.

formatdate-time

output_file_name: string

File name of the recording.

session_id: string

ID of the meeting session this recording is for.

formatuuid

started_time: string

Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.

formatdate-time

status: "INVOKED" or "RECORDING" or "UPLOADING" or 3 more

Current status of the recording.

One of the following:

"INVOKED"

"RECORDING"

"UPLOADING"

"UPLOADED"

"ERRORED"

"PAUSED"

stopped_time: string

Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.

formatdate-time

recording_duration: optional number

Total recording time in seconds.

start_reason: optional object { caller, reason } 

caller: optional object { name, type, user_Id } 

name: optional string

Name of the user who started the recording.

type: optional "ORGANIZATION" or "USER"

The type can be an App or a user. If the type is `user`, then only the `user_Id` and `name` are returned.

One of the following:

"ORGANIZATION"

"USER"

user_Id: optional string

The user ID of the person who started the recording.

formatuuid

reason: optional "API_CALL" or "RECORD_ON_START"

Specifies if the recording was started using the “Start a Recording”API or using the parameter RECORD_ON_START in the “Create a meeting” API.

If the recording is initiated using the “RECORD_ON_START” parameter, the user details will not be populated.

One of the following:

"API_CALL"

"RECORD_ON_START"

stop_reason: optional object { caller, reason } 

caller: optional object { name, type, user_Id } 

name: optional string

Name of the user who stopped the recording.

type: optional "ORGANIZATION" or "USER"

The type can be an App or a user. If the type is `user`, then only the `user_Id` and `name` are returned.

One of the following:

"ORGANIZATION"

"USER"

user_Id: optional string

The user ID of the person who stopped the recording.

formatuuid

reason: optional "API_CALL" or "INTERNAL_ERROR" or "ALL_PEERS_LEFT"

Specifies the reason why the recording stopped.

One of the following:

"API_CALL"

"INTERNAL_ERROR"

"ALL_PEERS_LEFT"

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

RecordingPauseResumeStopRecordingResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { id, audio_download_url, download_url, 12 more } 

Data returned by the operation

id: string

ID of the recording

formatuuid

audio_download_url: string

If the audio_config is passed, the URL for downloading the audio recording is returned.

formaturi

download_url: string

URL where the recording can be downloaded.

formaturi

download_url_expiry: string

Timestamp when the download URL expires.

formatdate-time

file_size: number

File size of the recording, in bytes.

invoked_time: string

Timestamp when this recording was invoked.

formatdate-time

output_file_name: string

File name of the recording.

session_id: string

ID of the meeting session this recording is for.

formatuuid

started_time: string

Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.

formatdate-time

status: "INVOKED" or "RECORDING" or "UPLOADING" or 3 more

Current status of the recording.

One of the following:

"INVOKED"

"RECORDING"

"UPLOADING"

"UPLOADED"

"ERRORED"

"PAUSED"

stopped_time: string

Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.

formatdate-time

recording_duration: optional number

Total recording time in seconds.

start_reason: optional object { caller, reason } 

caller: optional object { name, type, user_Id } 

name: optional string

Name of the user who started the recording.

type: optional "ORGANIZATION" or "USER"

The type can be an App or a user. If the type is `user`, then only the `user_Id` and `name` are returned.

One of the following:

"ORGANIZATION"

"USER"

user_Id: optional string

The user ID of the person who started the recording.

formatuuid

reason: optional "API_CALL" or "RECORD_ON_START"

Specifies if the recording was started using the “Start a Recording”API or using the parameter RECORD_ON_START in the “Create a meeting” API.

If the recording is initiated using the “RECORD_ON_START” parameter, the user details will not be populated.

One of the following:

"API_CALL"

"RECORD_ON_START"

stop_reason: optional object { caller, reason } 

caller: optional object { name, type, user_Id } 

name: optional string

Name of the user who stopped the recording.

type: optional "ORGANIZATION" or "USER"

The type can be an App or a user. If the type is `user`, then only the `user_Id` and `name` are returned.

One of the following:

"ORGANIZATION"

"USER"

user_Id: optional string

The user ID of the person who stopped the recording.

formatuuid

reason: optional "API_CALL" or "INTERNAL_ERROR" or "ALL_PEERS_LEFT"

Specifies the reason why the recording stopped.

One of the following:

"API_CALL"

"INTERNAL_ERROR"

"ALL_PEERS_LEFT"

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

RecordingStartTrackRecordingResponse object { success, data } 

success: boolean

Success status of the operation

data: optional object { recording } 

Data returned by the operation

recording: object { id, audio_download_url, download_url, 9 more } 

id: string

ID of the recording

formatuuid

audio_download_url: string

If the audio_config is passed, the URL for downloading the audio recording is returned.

formaturi

download_url: string

URL where the recording can be downloaded.

formaturi

download_url_expiry: string

Timestamp when the download URL expires.

formatdate-time

file_size: number

File size of the recording, in bytes.

invoked_time: string

Timestamp when this recording was invoked.

formatdate-time

output_file_name: string

File name of the recording.

session_id: string

ID of the meeting session this recording is for.

formatuuid

started_time: string

Timestamp when this recording actually started after being invoked. Usually a few seconds after `invoked_time`.

formatdate-time

status: "INVOKED" or "RECORDING" or "UPLOADING" or 3 more

Current status of the recording.

One of the following:

"INVOKED"

"RECORDING"

"UPLOADING"

"UPLOADED"

"ERRORED"

"PAUSED"

stopped_time: string

Timestamp when this recording was stopped. Optional; is present only when the recording has actually been stopped.

formatdate-time

recording_duration: optional number

Total recording time in seconds.

#### Realtime KitWebhooks

##### [Fetch all webhooks details](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/get_webhooks)

GET/accounts/{account_id}/realtime/kit/{app_id}/webhooks

##### [Add a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/create_webhook)

POST/accounts/{account_id}/realtime/kit/{app_id}/webhooks

##### [Fetch details of a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/get_webhook_by_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### [Replace a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/replace_webhook)

PUT/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### [Edit a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/edit_webhook)

PATCH/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### [Delete a webhook](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/webhooks/methods/delete_webhook)

DELETE/accounts/{account_id}/realtime/kit/{app_id}/webhooks/{webhook_id}

##### ModelsExpand Collapse 

WebhookGetWebhooksResponse object { data, success } 

data: array of object { id, created_at, enabled, 4 more } 

id: string

ID of the webhook

formatuuid

created_at: string

Timestamp when this webhook was created

formatdate-time

enabled: boolean

Set to true if the webhook is active

events: array of "meeting.started" or "meeting.ended" or "meeting.participantJoined" or 6 more

Events this webhook will send updates for

One of the following:

"meeting.started"

"meeting.ended"

"meeting.participantJoined"

"meeting.participantLeft"

"meeting.chatSynced"

"recording.statusUpdate"

"livestreaming.statusUpdate"

"meeting.transcript"

"meeting.summary"

name: string

Name of the webhook

updated_at: string

Timestamp when this webhook was updated

formatdate-time

url: string

URL the webhook will send events to

formaturi

success: boolean

WebhookCreateWebhookResponse object { data, success } 

data: object { id, created_at, enabled, 4 more } 

id: string

ID of the webhook

formatuuid

created_at: string

Timestamp when this webhook was created

formatdate-time

enabled: boolean

Set to true if the webhook is active

events: array of "meeting.started" or "meeting.ended" or "meeting.participantJoined" or 6 more

Events this webhook will send updates for

One of the following:

"meeting.started"

"meeting.ended"

"meeting.participantJoined"

"meeting.participantLeft"

"meeting.chatSynced"

"recording.statusUpdate"

"livestreaming.statusUpdate"

"meeting.transcript"

"meeting.summary"

name: string

Name of the webhook

updated_at: string

Timestamp when this webhook was updated

formatdate-time

url: string

URL the webhook will send events to

formaturi

success: boolean

WebhookGetWebhookByIDResponse object { data, success } 

data: object { id, created_at, enabled, 4 more } 

id: string

ID of the webhook

formatuuid

created_at: string

Timestamp when this webhook was created

formatdate-time

enabled: boolean

Set to true if the webhook is active

events: array of "meeting.started" or "meeting.ended" or "meeting.participantJoined" or 6 more

Events this webhook will send updates for

One of the following:

"meeting.started"

"meeting.ended"

"meeting.participantJoined"

"meeting.participantLeft"

"meeting.chatSynced"

"recording.statusUpdate"

"livestreaming.statusUpdate"

"meeting.transcript"

"meeting.summary"

name: string

Name of the webhook

updated_at: string

Timestamp when this webhook was updated

formatdate-time

url: string

URL the webhook will send events to

formaturi

success: boolean

WebhookReplaceWebhookResponse object { data, success } 

data: object { id, created_at, enabled, 4 more } 

id: string

ID of the webhook

formatuuid

created_at: string

Timestamp when this webhook was created

formatdate-time

enabled: boolean

Set to true if the webhook is active

events: array of "meeting.started" or "meeting.ended" or "meeting.participantJoined" or 6 more

Events this webhook will send updates for

One of the following:

"meeting.started"

"meeting.ended"

"meeting.participantJoined"

"meeting.participantLeft"

"meeting.chatSynced"

"recording.statusUpdate"

"livestreaming.statusUpdate"

"meeting.transcript"

"meeting.summary"

name: string

Name of the webhook

updated_at: string

Timestamp when this webhook was updated

formatdate-time

url: string

URL the webhook will send events to

formaturi

success: boolean

WebhookEditWebhookResponse object { data, success } 

data: object { id, created_at, enabled, 4 more } 

id: string

ID of the webhook

formatuuid

created_at: string

Timestamp when this webhook was created

formatdate-time

enabled: boolean

Set to true if the webhook is active

events: array of "meeting.started" or "meeting.ended" or "meeting.participantJoined" or 6 more

Events this webhook will send updates for

One of the following:

"meeting.started"

"meeting.ended"

"meeting.participantJoined"

"meeting.participantLeft"

"meeting.chatSynced"

"recording.statusUpdate"

"livestreaming.statusUpdate"

"meeting.transcript"

"meeting.summary"

name: string

Name of the webhook

updated_at: string

Timestamp when this webhook was updated

formatdate-time

url: string

URL the webhook will send events to

formaturi

success: boolean

WebhookDeleteWebhookResponse object { data, success } 

data: object { id, created_at, enabled, 4 more } 

id: string

ID of the webhook

formatuuid

created_at: string

Timestamp when this webhook was created

formatdate-time

enabled: boolean

Set to true if the webhook is active

events: array of "meeting.started" or "meeting.ended" or "meeting.participantJoined" or 6 more

Events this webhook will send updates for

One of the following:

"meeting.started"

"meeting.ended"

"meeting.participantJoined"

"meeting.participantLeft"

"meeting.chatSynced"

"recording.statusUpdate"

"livestreaming.statusUpdate"

"meeting.transcript"

"meeting.summary"

name: string

Name of the webhook

updated_at: string

Timestamp when this webhook was updated

formatdate-time

url: string

URL the webhook will send events to

formaturi

success: boolean

#### Realtime KitActive Session

##### [Fetch details of an active session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/get_active_session)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session

##### [Kick participants from an active session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_participants)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick

##### [Kick all participants](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/kick-all

##### [Create a poll](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/create_poll)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-session/poll

##### ModelsExpand Collapse 

ActiveSessionGetActiveSessionResponse object { data, success } 

data: optional object { id, associated_id, created_at, 11 more } 

id: string

ID of the session

associated_id: string

ID of the meeting this session is associated with. In the case of V2 meetings, it is always a UUID. In V1 meetings, it is a room name of the form `abcdef-ghijkl`

created_at: string

timestamp when session created

live_participants: number

number of participants currently in the session

max_concurrent_participants: number

number of maximum participants that were in the session

meeting_display_name: string

Title of the meeting this session belongs to

minutes_consumed: number

number of minutes consumed since the session started

organization_id: string

App id that hosted this session

started_at: string

timestamp when session started

status: "LIVE" or "ENDED"

current status of session

One of the following:

"LIVE"

"ENDED"

type: "meeting" or "livestream" or "participant"

type of session

One of the following:

"meeting"

"livestream"

"participant"

updated_at: string

timestamp when session was last updated

breakout_rooms: optional array of unknown

ended_at: optional string

timestamp when session ended

success: optional boolean

ActiveSessionKickParticipantsResponse object { data, success } 

data: optional object { action, participants } 

action: optional string

participants: optional array of object { id, created_at, updated_at, 3 more } 

id: string

ID of the session participant

created_at: string

updated_at: string

email: optional string

Email of the session participant.

name: optional string

Name of the session participant.

picture: optional string

A URL pointing to a picture of the participant.

success: optional boolean

ActiveSessionKickAllParticipantsResponse object { data, success } 

data: optional object { action, kicked_participants_count } 

action: optional string

kicked_participants_count: optional number

success: optional boolean

ActiveSessionCreatePollResponse object { data, success } 

data: optional object { action, poll } 

action: optional string

poll: optional object { id, options, question, 4 more } 

id: string

ID of the poll

options: array of object { count, text, votes } 

Answer options

count: number

text: string

Text of the answer option

votes: array of object { id, name } 

id: string

name: string

question: string

Question asked by the poll

anonymous: optional boolean

created_by: optional string

hide_votes: optional boolean

voted: optional array of string

success: optional boolean

#### Realtime KitLivestreams

##### [Fetch all livestreams](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_all_livestreams)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams

##### [Stop livestreaming a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/stop_livestreaming_a_meeting)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream/stop

##### [Start livestreaming a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/start_livestreaming_a_meeting)

POST/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/livestreams

##### [Fetch complete analytics data for your livestreams](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_analytics_complete)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/overall

##### [Fetch day-wise analytics data for your livestreams](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_analytics_daywise)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/livestreams/daywise

##### [Fetch day-wise session and recording analytics data for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_org_analytics)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise

##### [Fetch active livestreams for a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_meeting_active_livestreams)

GET/accounts/{account_id}/realtime/kit/{app_id}/meetings/{meeting_id}/active-livestream

##### [Fetch livestream session details using livestream session ID](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_session_details_for_session_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/sessions/{livestream-session-id}

##### [Fetch active livestream session details](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_active_livestreams_for_livestream_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}/active-livestream-session

##### [Fetch livestream details using livestream ID](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/livestreams/methods/get_livestream_session_for_livestream_id)

GET/accounts/{account_id}/realtime/kit/{app_id}/livestreams/{livestream_id}

##### ModelsExpand Collapse 

LivestreamGetAllLivestreamsResponse object { data, success } 

data: optional object { id, created_at, disabled, 8 more } 

id: optional string

The ID of the livestream.

formatuuid

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

disabled: optional string

Specifies if the livestream was disabled.

ingest_server: optional string

The server URL to which the RTMP encoder sends the video and audio data.

meeting_id: optional string

ID of the meeting.

name: optional string

Name of the livestream.

paging: optional object { end_offset, start_offset, total_count } 

end_offset: optional number

start_offset: optional number

total_count: optional number

playback_url: optional string

The web address that viewers can use to watch the livestream.

status: optional "LIVE" or "IDLE" or "ERRORED" or "INVOKED"

One of the following:

"LIVE"

"IDLE"

"ERRORED"

"INVOKED"

stream_key: optional string

Unique key for accessing each livestream.

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

success: optional boolean

LivestreamStopLivestreamingAMeetingResponse object { data, success } 

data: optional object { message } 

message: optional string

success: optional boolean

LivestreamStartLivestreamingAMeetingResponse object { data, success } 

data: optional object { id, ingest_server, playback_url, 2 more } 

id: optional string

The livestream ID.

ingest_server: optional string

The server URL to which the RTMP encoder sends the video and audio data.

playback_url: optional string

The web address that viewers can use to watch the livestream.

status: optional "LIVE" or "IDLE" or "ERRORED" or "INVOKED"

One of the following:

"LIVE"

"IDLE"

"ERRORED"

"INVOKED"

stream_key: optional string

Unique key for accessing each livestream.

success: optional boolean

LivestreamGetLivestreamAnalyticsCompleteResponse object { data, success } 

data: optional object { count, total_ingest_seconds, total_viewer_seconds } 

count: optional number

Count of total livestreams.

total_ingest_seconds: optional number

Total time duration for which the input was given or the meeting was streamed.

total_viewer_seconds: optional number

Total view time for which the viewers watched the stream.

success: optional boolean

LivestreamGetLivestreamAnalyticsDaywiseResponse object { data, success } 

data: optional array of object { count, date, total_ingest_seconds, total_viewer_seconds } 

count: optional number

Count of total livestream sessions.

date: optional string

Analytics date.

total_ingest_seconds: optional number

Total time duration for which the input was given or the meeting was streamed.

total_viewer_seconds: optional number

Total view time for which the viewers watched the stream.

success: optional boolean

LivestreamGetOrgAnalyticsResponse object { data, success } 

data: optional object { recording_stats, session_stats } 

recording_stats: optional object { day_stats, recording_count, recording_minutes_consumed } 

Recording statistics of an App during the range specified

day_stats: optional array of object { day, total_recording_minutes, total_recordings } 

Day wise recording stats

day: optional string

total_recording_minutes: optional number

Total recording minutes for a specific day

total_recordings: optional number

Total number of recordings for a specific day

recording_count: optional number

Total number of recordings during the range specified

recording_minutes_consumed: optional number

Total recording minutes during the range specified

session_stats: optional object { day_stats, sessions_count, sessions_minutes_consumed } 

Session statistics of an App during the range specified

day_stats: optional array of object { day, total_session_minutes, total_sessions } 

Day wise session stats

day: optional string

total_session_minutes: optional number

Total session minutes for a specific day

total_sessions: optional number

Total number of sessions for a specific day

sessions_count: optional number

Total number of sessions during the range specified

sessions_minutes_consumed: optional number

Total session minutes during the range specified

success: optional boolean

LivestreamGetMeetingActiveLivestreamsResponse object { data, success } 

data: optional object { id, created_at, disabled, 7 more } 

id: optional string

The livestream ID.

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

disabled: optional string

Specifies if the livestream was disabled.

ingest_server: optional string

The server URL to which the RTMP encoder sends the video and audio data.

meeting_id: optional string

name: optional string

Name of the livestream.

playback_url: optional string

The web address that viewers can use to watch the livestream.

status: optional "LIVE" or "IDLE" or "ERRORED" or "INVOKED"

One of the following:

"LIVE"

"IDLE"

"ERRORED"

"INVOKED"

stream_key: optional string

Unique key for accessing each livestream.

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

success: optional boolean

LivestreamGetLivestreamSessionDetailsForSessionIDResponse object { data, success } 

data: optional object { id, created_at, err_message, 6 more } 

id: optional string

The livestream ID.

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

err_message: optional string

The server URL to which the RTMP encoder sends the video and audio data.

ingest_seconds: optional number

Name of the livestream.

livestream_id: optional string

started_time: optional string

Unique key for accessing each livestream.

stopped_time: optional string

The web address that viewers can use to watch the livestream.

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

viewer_seconds: optional number

Specifies if the livestream was disabled.

success: optional boolean

LivestreamGetActiveLivestreamsForLivestreamIDResponse object { data, success } 

data: optional object { livestream, session } 

livestream: optional object { id, created_at, disabled, 7 more } 

id: optional string

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

disabled: optional string

Specifies if the livestream was disabled.

ingest_server: optional string

The server URL to which the RTMP encoder sends the video and audio data.

meeting_id: optional string

ID of the meeting.

name: optional string

Name of the livestream.

playback_url: optional string

The web address that viewers can use to watch the livestream.

status: optional "LIVE" or "IDLE" or "ERRORED" or "INVOKED"

One of the following:

"LIVE"

"IDLE"

"ERRORED"

"INVOKED"

stream_key: optional string

Unique key for accessing each livestream.

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

session: optional object { id, created_at, err_message, 7 more } 

id: optional string

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

err_message: optional string

ingest_seconds: optional string

The time duration for which the input was given or the meeting was streamed.

invoked_time: optional string

Timestamp the object was invoked. The time is returned in ISO format.

formatdate-time

livestream_id: optional string

started_time: optional string

Timestamp the object was started. The time is returned in ISO format.

formatdate-time

stopped_time: optional string

Timestamp the object was stopped. The time is returned in ISO format.

formatdate-time

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

viewer_seconds: optional string

The total view time for which the viewers watched the stream.

success: optional boolean

LivestreamGetLivestreamSessionForLivestreamIDResponse object { data, success } 

data: optional object { livestream, paging, session } 

livestream: optional object { id, created_at, disabled, 7 more } 

id: optional string

ID of the livestream.

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

disabled: optional string

Specifies if the livestream was disabled.

ingest_server: optional string

The server URL to which the RTMP encoder sends the video and audio data.

meeting_id: optional string

The ID of the meeting.

name: optional string

Name of the livestream.

playback_url: optional string

The web address that viewers can use to watch the livestream.

status: optional "LIVE" or "IDLE" or "ERRORED" or "INVOKED"

One of the following:

"LIVE"

"IDLE"

"ERRORED"

"INVOKED"

stream_key: optional string

Unique key for accessing each livestream.

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

paging: optional object { end_offset, start_offset, total_count } 

end_offset: optional number

start_offset: optional number

total_count: optional number

session: optional object { id, created_at, err_message, 7 more } 

id: optional string

ID of the session.

created_at: optional string

Timestamp the object was created at. The time is returned in ISO format.

formatdate-time

err_message: optional string

ingest_seconds: optional number

The time duration for which the input was given or the meeting was streamed.

invoked_time: optional string

Timestamp the object was invoked. The time is returned in ISO format.

formatdate-time

livestream_id: optional string

started_time: optional string

Timestamp the object was started. The time is returned in ISO format.

formatdate-time

stopped_time: optional string

Timestamp the object was stopped. The time is returned in ISO format.

formatdate-time

updated_at: optional string

Timestamp the object was updated at. The time is returned in ISO format.

formatdate-time

viewer_seconds: optional number

The total view time for which the viewers watched the stream.

success: optional boolean

#### Realtime KitAnalytics

##### [Fetch day-wise session and recording analytics data for an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/analytics/methods/get_org_analytics)

GET/accounts/{account_id}/realtime/kit/{app_id}/analytics/daywise

##### ModelsExpand Collapse 

AnalyticsGetOrgAnalyticsResponse object { data, success } 

data: optional object { recording_stats, session_stats } 

recording_stats: optional object { day_stats, recording_count, recording_minutes_consumed } 

Recording statistics of an App during the range specified

day_stats: optional array of object { day, total_recording_minutes, total_recordings } 

Day wise recording stats

day: optional string

total_recording_minutes: optional number

Total recording minutes for a specific day

total_recordings: optional number

Total number of recordings for a specific day

recording_count: optional number

Total number of recordings during the range specified

recording_minutes_consumed: optional number

Total recording minutes during the range specified

session_stats: optional object { day_stats, sessions_count, sessions_minutes_consumed } 

Session statistics of an App during the range specified

day_stats: optional array of object { day, total_session_minutes, total_sessions } 

Day wise session stats

day: optional string

total_session_minutes: optional number

Total session minutes for a specific day

total_sessions: optional number

Total number of sessions for a specific day

sessions_count: optional number

Total number of sessions during the range specified

sessions_minutes_consumed: optional number

Total session minutes during the range specified

success: optional boolean

[ Previous

* * *

Tokens ](https://developers.cloudflare.com/api/resources/moq/subresources/relays/subresources/tokens)[ Next

* * *

Apps ](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/apps)
