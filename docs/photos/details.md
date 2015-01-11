#Photos
Following endpoints are valid for photos. `X-Access-Key` and `X-Access-Token` required wherever the endpoint expects 
authorization.

## Endpoints

### GET `/me/photos`
* Get list of user uploaded photos
* Uploaded photo may be from different sources
	* Direct upload
	* Import from facebook

#### Response
Response is a valid JSON with following output

    {
        "albums": [
            {
                "album_name": "Picovico Library"
                "photos": [
                    {
                        "url": "<some_url>",
                        "thumbnail_url": "<some_thumbnail_url>",
                        "id": "<some_id>"
                    },
                    {
                        "url": "<some_url>",
                        "thumbnail_url": "<some_thumbnail_url>",
                        "id": "<some_id>"
                    },
                    ...
                ]
            },
            {
                "album_name": "Imported from Facebook"
                "photos": "<
                    {
                        "url": "<some_url>",
                        "thumbnail_url": "<some_thumbnail_url>",
                        "id": "<some_id>"
                    },
                    ...
                ]
            },
            ...
        ]
    }
        
### PUT `/me/photos`
* upload photo directly with the binary image file
* supported format is .jpg/.png

#### Response
Response is a valid JSON with following output

    {
        "url": "<some_url>",
        "thumbnail_url": "<some_thumbnail_url>",
        "id": "<some_id>"
    }

### POST `/me/photos/external`
* importing photos from external sources
* external sources may be facebook, flickr or other web urls

#### Parameters
* `url`               : Original photo path
* `thumbnail_url`     : thumbnail photo path
* `service`           : Service name from which photo is uploaded

#### Response
Response is a valid JSON with following output

    {
        "url": "<some_url>",
        "thumbnail_url": "<some_thumbnail_url>",
        "id": "<some_id>"
    }


###  DELETE `/me/photos/<photo_id>`
* deleting the photo

#### Response
Response is a valid JSON with following output

    {
        "status" : 200,
        "message" : "Photo deleted successfully"
    }
