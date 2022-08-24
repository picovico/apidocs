# This page is archived and no longer udpated. 

####Response Object
```json
{
    "url": <photo_url>,
    "thumbnail_url": "<thumbnail_url>"
    "id": "<photo_id>"
}
```
### Get Photos
1. List Photos
    - URL: `/me/photos`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE: 

2. Get Specific Photo
    - URL: `/me/photos/<photo_id>`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE: `<response_object>`
#### Upload Photos
*`JPG` and `PNG` Format are only supported for uploads.*

1. Upload Photo/Image File
    - URL: `/me/photos`
    - METHOD: `PUT`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - BODY: `<IMAGE_FILE>`
    - RESPONSE: `<response_object>`

#### Delete Photos

1. Delete All Uploaded Photos
