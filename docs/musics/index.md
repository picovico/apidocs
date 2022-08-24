# This page is archived and no longer udpated. 

###Response Object
```json
{
    "category": "",
    "is_featured": true,
    "artist": "<Artist of music if available>",
    "title": "<Title of music if available>",
    "url": "<preview_url>",
    "duration": <duration_in_seconds>,
    "id": "<music_id>"
}
```
###List all picovico provided musics
>- URL: `/musics`
>- METHOD: `GET`
>- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
>- RESPONSE:
        
        {
            'data': [<response_object>,.....]
            '_count': 25,
        }

###Get Single Specific Music
>- URL: `/musics/<music_id>`
>- METHOD: `GET`
>- HEADERS:
    - `X-Access-Token`: (_required_) Token Provided by Picovico.
    - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
>- RESPONSE:
    
    {
        'data': [<response_object>]
        '_count': 1,
    }
