<h1 style='color:red; padding:2em; border:1px solid red'> This page is archived and no longer udpated. </h1>

##Callback URL
You can set your callback url in your applicatiion preferences. The data format is explained below
and the url should comply. A mail will be sent to owner of app in case of callback failure.

#Callback Data
- METHOD: `POST`
- HEADERS:
    - Content-Type: `application/json`
    - Accept: `application/json`
- DATA:
    
        {
            "type": 'video.created', //video.failed, video.preview.created, video.preview.failed 
            "created": <timestamp>,
            "status": 200,
            "data": {
                "object": {
                    "id": "",
                    "video": [{
                        "quality": 144,
                        "url": "",
                        "size": "",
                        "thumbnail": { //thumbnail is not available for preview
                            "url": "",
                            "size": ""
                        }
                    }], //information of size and all
                },
                "meta": {
                    "msg": '', //some readable message
                    "app_id": <app_used>
                    
                }
            }
        }

- RESPONSE:
    - `json` data
    - status: 200 OK
