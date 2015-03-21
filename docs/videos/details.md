#Videos
Following endpoints are valid for videos. `X-Access-Key` and `X-Access-Token` required wherever the endpoint expects 
authorization.
## Endpoints
### GET `/v/<video-id>/video-name.mp4`
* Direct Link to video file after a video is created successfully.
* Authorization is NOT required

### GET `/me/videos`
* List of videos created or being created

#### Response

    {
        "paging": {
            "count": 15,
            "next_url": "/me/videos?count=15&from=1418715805",
            "prev_url": "/me/videos?count=15&to=1418879545"
        },
        "videos": [
            {
                "status": "published",
                "style": "<some-style>",
                "name": "<some-video-name>",
                "assets": [],
                "duration": <some-duration>,
                "tags": [],
                "owner": {
                    "profile_pic": "<some-image-link>",
                    "id": "<some-user-id>",
                    "name": "<some-name>"
                },
                "id": "<some-id>",
                "credit": [],
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
                }
            },
            ...
        ]
    }

### POST `/me/videos`
* Create a new video project, or get the last draft project

#### Parameters
* `name`      -   Name of video we are making

#### Response

    {
        "status": "initial",
        "style": "<some-style>",
        "name": "<some-name>",
        "assets": [],
        "duration": 0,
        "tags": [],
        "comment_count": 0,
        "owner": {
            "profile_pic": "<some-url>",
            "id": "<some-id>",
            "name": "<some-name>"
        },
        "id": "<some-id>",
        "credit": [],
        "created_on": 1418884737,
        "video": null,
        "modified_on": 1418884737,
        "view": 0,
        "quality": 360,
        "thumbnail": null,
    }


### GET `/me/videos/<video-id>`
* Get the status, details of any video

#### Response

    {
        "status": "initial",
        "style": "<some-style>",
        "name": "<some-name>",
        "assets": [],
        "duration": 0,
        "owner": {
            "profile_pic": "<some-url>",
            "id": "<some-id>",
            "name": "<some-name>"
        },
        "id": "<some-id>",
        "credit": [],
        "created_on": 1418884737,
        "video": null,
        "modified_on": 1418884737,
        "view": 0,
        "quality": 360,
        "thumbnail": null,
    }

### POST `/me/videos/<video-id>`
* Define or update a video content

#### Parameters

| Key                   |   Data Type   |   Description |
| ----------------------|---------------|-------------- |
| `name`      [optional]  |   String      |   name of video |
| `style`     [optional]  |   String      |   set style |
| `credit`    [optional]  |   Array of Array (eg. [["key1", "value1"],["key2", "value2"],["key3", "value3"]])      |   set credits at end of video | 
| `quality`   [optional]  |   String (eg. 360)     |   set quality |
| `assets`    [optional]  |   Array of frames object     |   set assets |

#### Response
Same as GET Video object

### POST `/me/videos/<video-id>/duplicate`
* Duplicate any published video into current draft

#### Parameters
None

#### Response
Same as GET Video Object (Returns details for the duplicate copy)

### DELETE `/me/videos/<video-id>`
* Delete the video

#### Parameters
Not required

#### Response

    {
        "message" : "Video deleted",
    }
    
### POST `/me/videos/<video-id>/render`
* Send the video rendering request to rendering engine

#### Parameters
Not required

#### Response

    {
        "message" : "Video is being created",
        "status" : 7101
    }
    
#### Response Codes

|   Status Code     |   Description                 |
|-------------------|-------------------------------|
|   7201            |   Video is being created      |
|   7202            |   Video successfully created  |
|   7401            |   Style not defined           |
|   7402            |   Music not defined           |
|   7403            |   Insufficient Assets         |
|   7404            |   No title                    |
|   7405            |   Insufficient credits amount |

