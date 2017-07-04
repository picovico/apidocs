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
                    "status": "preview" //preview or video status
                },
                "meta": {
                    "message": '', //some readable message
                    "application_id": <app_used>
                    
                }
            }
        }
