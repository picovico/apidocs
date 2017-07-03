####Response Object
```json
{
    "url": <preview_url>, //we create preview of uploaded music
    "artist": "<Artist of music if available>",
    "title": "<Title of music if available>",
    "duration": <duration_in_seconds>,
    "id": "<music_id>"
}
```

####Get User Musics 
1. Get List of uploaded Musics.
    - URL: `/me/musics`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE:
            {
                'data': [<response_object>,.....] //check 'status' of object.
                '_count': <no_of_music>,
            }

2. Get Single Music
    - URL: `/me/musics/<music_id>`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE:
            {
                'data': [<response_object>] //check 'status' of object.
                '_count': 1,
            }

####Upload Musics
1. Upload Music File
    - URL: `/me/musics`
    - METHOD: `PUT`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
        - `X-Music-Title` (optional) Title of music to be set.
        - `X-Music-Artist` (optional) Artist of music to be set.
    - RESPONSE:
            {
                'data': [<response_object>] //check 'status' of object.
                '_count': 1,
            }

####Delete User Musics
1. Add All Music to trashcan.
    - URL: `/me/musics`
    - METHOD: `DELETE`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE: 
```json
{
    '_count': 1,
    data: [{message: "All Musics added to trashcan."}]
}
```

2. Add Single Music to trashcan.
    - URL: `/me/musics/<music_id>`
    - METHOD: `DELETE`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE: 
```json
{
    '_count': 1,
    data: [{message: "<music_id> Musics added to trashcan."}]
}
```
