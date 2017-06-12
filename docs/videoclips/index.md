####Response Object
```json
{
    "url": "<preview_url>",
    "preview_gif": "<preview_gif>",
    "thumbnail_url": "<thumbnail_url>",
    "id": "<videoclip_id>",
    "status": "<status_of_clip>" // 'pending', 'available', 'failed'
}
```
### Get VideoClips
1. List VideoClips
    - URL: `/me/videoclips`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - RESPONSE: 

2. Get Specific VideoClip
    - URL: `/me/videoclips/<videoclip_id>`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - RESPONSE: `<response_object>`

#### Upload VideoClip
*`MOV`, `AVI` and `MP4` Format are only supported for uploads.*

[We Provide direct bucket upload URL for our amazon s3](directupload/index.md)
