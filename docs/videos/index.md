# This page is archived and no longer udpated. 

###Response Object
```json
{
    "status": "initial", //'published', 'processing'
    "name": "<some-video-name>",
    "id": "<video_id>",
    "created_on": 1418879545,
    "video": [{
        "quality": 360,
        "url": <video_url>,
        "size": <video_size>,
        "thumbnail": <video_thumbnail>
    }],
    "modified_on": 1418879545,
    //Only available in single video request.
    "style": "<some-style>",
    "aspect_ratio": "16:9",
    "privacy": "unlisted",
    "description": "some video description"
    "duration": <some-duration>,
    //assets/credits is available only on initial status
    "assets": [{
        'music': {
            "start_time": 0,
            "end_time": 15,
            "id": <music_id>,
            "url": <some_url>, // when no id is present
        },
        "frames": [{
            "name": "image" //can be text
            "data": {
                "text": "",
                "title": ""
            } // if image {"caption": ""},
            "attributes": {'credits': ''},
            "start_time": 0,
            "end_time": 5,
            #for non text frames.
            "id": <image_id>,
            "url": <some_url>, //when no id is present
        },....]
    }
    ]
}
```
###Get Video list.
- URL: `/me/videos`
- METHOD: `GET`
- QUERY PARAMS:
    - `count`: (_optional_) No of videos to query.
- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- RESPONSE:
        
        {
            "_count": 15, #default 15
            "data": [<response_object>],
            "_total": <total_no_of_videos>,
            "_page": <page_num>,
        }


###Create New Video Project.
`NOTE: Content-Type: "application/json" is also supported with POST parameters as object keys`

- URL: `/me/videos`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- PARAMS:
    - `name`: (_required_) Name of Video Project.
    - `style`: (_optional_) style <machine_name> for video to be used.
    - `privacy`: (_optional_) privacy of video.
    - `name`: (_optional_) Name of video. *Will update*
    - `quality`: (_optional_) Quality to be used. By default 360.
    - `aspect_ratio`: (_optional_) Aspect Ratio of the video. Default is '16:9' *Only on supported style*
    - `assets`: (_optional_) `JSON` objects of frames in video.
        - `json` format of *assets* is list of frames and music.
            
                [{
                'frames': [{
                    "name": 'image',
                    "id": <image_id>,
                    "url": <direct_image_url>, //if no image_id
                    "data": { //optional
                        "caption": ""
                    },
                    "start_time": 4,
                    "end_time": 8
                },{
                    "name": "text",
                    "data": { //One is required `text` or `title`
                        "text": '',
                        "title": ''
                    },
                    "start_time": 0, //in seconds
                    "end_time": 9
                }...],
                'music': {
                        'id': <music_id>, //id provided by picovico
                        "url": <direct_music_url>, //if no music_id
                        "start_time": 0,
                        "end_time": 60
                    } 
                }, ....]
                
                
- RESPONSE:
                
        {
            '_count': 1,
            'data': [<response_object>]
        }
    



### Get specific video project
- URL: `/me/videos/<video_id>`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- QUERY PARAMS:
    - `restore`: (_optional_) Set this value to `1` if restoration of failed/cancelled video is required.
    - `owner`: (_optional_) Set this value to `1` if owner info is required.
    - `exports`: (_optional_) Set this value to `1` if exported data is required.
    - `extras`: (_optional_) Set this value to `1` if extra info such as cta is required.
- RESPONSE:

            {
                '_count': 1,
                'data': [<response_object>]
            }


###Update Video Project
- URL: `/me/videos/<video_id>`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- PARAMETERS:
    - `style`: (_required_) style <machine_name> for video to be used.
    - `privacy`: (_optional_) privacy of video.
    - `name`: (_optional_) Name of video. *Will update*
    - `quality`: (_optional_) Quality to be used. By default 360.
    - `aspect_ratio`: (_optional_) Aspect Ratio of the video. Default is '16:9' *Only on supported style*
    - `assets`: (_required_) `JSON` objects of frames in video.
        - `json` format of *assets* is list of frames and music.
            
                [{
                'frames': [{
                    "name": 'image',
                    "id": <image_id>,
                    "url": <direct_image_url>, //if no image_id
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
                        'id': <music_id>, //id provided by picovico
                        "url": <direct_music_url>, //if no music_id
                    } 
                }, ....]


- RESPONSE:
    
        {
            '_count': 1,
            'data': [<response_object>] 
        }

### Render Video Project [or Preview]
- URL: `/me/videos/<video_id>`
- METHOD: `PUT`
- QUERY PARAMS:
    `Rendering is done if no params`
    - `preview`: (_optional_) Set this value to `1` if preview is required.
    - `render`: (_optional_) Set this value to `1` along with `preview=1` if rendering is also required. 
- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- RESPONSE:
    
    - If video is being rendered/previewed for first time:
        
        `HTTP_STATUS: 202`
        
                {
                    '_count': 1,
                    'data': [{'message': 'Video is being processed.'}]
                }
    
    - else:
        - video_render_response:
        
                {
                    '_count': 1,
                    'data': [<response_object>] //check 'status' of object.
                }
        
        - video preview response:
            
                {
                    '_count': 1,
                    'data': [{'144': {'url': <preview_url>}}] 
                }
    

#Delete Video Object [Cancel Rendering]
- URL: `/me/videos/<video_id>`
- METHOD: `DELETE`
- QUERY PARAMS:
    - `cancel`: (_optional_) Set this value to `1` if you want to cancel rendering only.
- RESPONSE:
    
        {
            '_count': 1,
            'data': [{"message": "Video Deleted"}]
        }
