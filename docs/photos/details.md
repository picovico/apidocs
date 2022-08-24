<h1 style='color:red; padding:2em; border:1px solid red'> This page is archived and no longer udpated. </h1>

####Response Object
```json
{
    "url": <url>,
    "thumbnail_url": "<preview_url>"
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
        - `X-pv-meta-app`: (required) APP Id from picovico developer.
    - RESPONSE: 
        {
            '_count': <no_of_response_data>,
            'data': [<response_object>,...]  # [] for 0 count
        }

2. Get Specific Photo
    - URL: `/me/photos/<photo_id>`
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
#### Upload Photos
*`JPG` and `PNG` Format are only supported for uploads.*

1. Upload Photo/Image File
    - URL: `/me/photos`
    - METHOD: `PUT`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-pv-meta-app`: (required) APP Id from picovico developer.
    - BODY: `<IMAGE_FILE>`
    - RESPONSE: 
    {
        '_count': 1,
        'data': [<response_object>]
    }
