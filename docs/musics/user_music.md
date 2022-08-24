<h1 style='color:red; padding:2em; border:1px solid red'> This page is archived and no longer udpated. </h1>

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

    - RESPONSE:

            {
                'data': [<response_object>,.....]
                '_count': <no_of_music>,
            }

2. Get Single Music
    - URL: `/me/musics/<music_id>`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (_required_) Token Provided by Picovico.
        - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
    - RESPONSE:
            
            {
                'data': [<response_object>]
                '_count': 1,
            }

####Upload Musics
1. Upload Music File
    - URL: `/me/musics`
    - METHOD: `PUT`
    - HEADERS:
        - `X-Access-Token`: (_required_) Token Provided by Picovico.
        - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
    - BODY: __MUSIC_FILE__
    - RESPONSE:
    
            {
                'data': [<response_object>] 
                '_count': 1,
            }

####Delete User Musics
1. Add All Music to trashcan.
    - URL: `/me/musics`
    - METHOD: `DELETE`
    - HEADERS:
        - `X-Access-Token`: (_required_) Token Provided by Picovico.
        - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
    - RESPONSE: 
            
            {
                '_count': 1,
                data: [{message: "All Musics added to trashcan."}]
            }


2. Add Single Music to trashcan.
    - URL: `/me/musics/<music_id>`
    - METHOD: `DELETE`
    - HEADERS:
        - `X-Access-Token`: (_required_) Token Provided by Picovico.
        - `X-Access-Key`: (_required_) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
    - RESPONSE: 

            {
                '_count': 1,
                data: [{message: "<music_id> Musics added to trashcan."}]
            }

