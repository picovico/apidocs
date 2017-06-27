###Response Object
```json
{
    "status": "initial", //'published', 'processing'
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
    "music_credits": ["title by artist"..],
    //assets is available only on initial status
    "assets": [{
        'musics': {
            "name": "music"
            "asset_id": <music_id>,
            "extras": {
                "preview_url": <music_url>,
            }
        },
        "frames": [{
            "name": "image" //can be text
            "asset_id": <image_id> //Not available for text,
            "data": {
                "text": "",
                "title": ""
            } // if image {"caption": ""},
            "attributes": {},
            "extras": {
                "url": "",
                "thumbnail_url": ""
            }
        },....]
    }
    ]
}
```
###Get Video list.
- URL: `/me/videos`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-pv-meta-app`: (required) APP Id from picovico developer.


###Create New Video Project.
- URL: `/me/videos`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-pv-meta-app`: (required) APP Id from picovico developer.
- PARAMS:
    - `name`: (required) Name of Video Project.
- RESPONSE:

            {
                '_count': 1,
                'data': [<response_object>]
            }

### Get specific video project
- URL: `/me/videos/<video_id>`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-pv-meta-app`: (required) APP Id from picovico developer.
- RESPONSE:

            {
                '_count': 1,
                'data': [<response_object>]
            }


###Update Video Project
- URL: `/me/videos/<video_id>`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-pv-meta-app`: (required) APP Id from picovico developer.
- PARAMETERS:
    - style: (required) style for video to be used.
    - privacy: (optional) privacy of video.
    - name: (optional) Name of video. *Will update*
    - quality: (optional) Quality to be used. By default 360.
    - aspect_ratio: (optional) Aspect Ratio of the video. Default is '16:9' *Only on supported style*
    - assets: (required) `JSON` objects of frames in video.
        - `json` format of *assets* is list of frames and music.
            
                [{
                'frames': [{
                    "name": 'image',
                    "asset_id": <image_id>,
                    "data": { //optional
                        "caption": ""
                    }
                },{
                    "name": "text",
                    "data": { //One is required `text` or `title`
                        "text": '',
                        "title": ''
                    }
                }...],
                'music': {
                        'asset_id': <music_id>, //id provided by picovico
                    } 
                }, ....]

- RESPONSE:
    
        {
            '_count': 1,
            'data': [<response_object>] 
        }

### Render Video Project
- URL: `/me/videos/<video_id>/render`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-pv-meta-app`: (required) APP Id from picovico developer.
- RESPONSE:
    - If video is being rendered for first time:
        
        `HTTP_STATUS: 202`
    
    - else:
        
            {
                'data': [<response_object>] //check 'status' of object.
                '_count': 1,
            }
    

### Preview Video Project
- URL: `/me/videos/<video_id>/preview`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-pv-meta-app`: (required) APP Id from picovico developer.
- RESPONSE: 
    - If preview is not available: `HTTP_STATUS: 202`
    - else:
        
            {
                '_count': 1,
                'data': [{'144': {'url': <preview_url>}}] 
            }
        
    
