###Response Object
```json
{
    "status": "published",
    "style": "<some-style>",
    "name": "<some-video-name>",
    "assets": [],
    "duration": <some-duration>,
    "owner": {
        "profile_pic": "<some-image-link>",
        "id": "<some-user-id>",
        "name": "<some-name>"
    },
    "id": "<video_id>",
    "created_on": 1418879545,
    "video": {
        "360": {
            "url": "<some-url>",
            "size": 2647812
        },
        "480": {
            "url": "<some-url>",
            "size": 4068889
        },
        "720": {
            "url": "<some-url>",
            "size": 5477751
        }
    },
    "modified_on": 1418879545,
    "view": 0,
    "quality": 360,
    "thumbnail": {
        "360": "<some-url>",
        "480": "<some-url>",
        "720": "<some-url>"
    },
    "music_credits": ["title by artist"..]
}
```
###Get Video list.
- URL: `/me/videos`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.


###Create New Video Project.
- URL: `/me/videos`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
- PARAMS:
    - `name`: (required) Name of Video Project.

### Get specific video project
- URL: `/me/videos/<video_id>`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
- RESPONSE: <response_object>

###Update Video Project
- URL: `/me/videos/<video_id>`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
- RESPONSE: <response_object>

### Render Video Project
- URL: `/me/videos/<video_id>/render`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
- RESPONSE:
    - If video is being rendered for first time.
        {
            "message": "video being created." 
        }
    -else
        `<response_object>`
    

### Preview Video Project
- URL: `/me/videos/<video_id>/preview`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
- RESPONSE: 
    - If preview is not available.
        {
            "message": "video preview being created." 
        }
    
    
