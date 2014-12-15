#Musics

Following endpoints are valid for musics.

##Endpoints

###GET `/me/musics`

* List of musics from Picovico Library

####Response

The response is a valid json with list of musics.

    {
        "musics": [
            {
                "duration": <some-duration>,
                "artist": "<some-artist>",
                "url": "<some-url>",
                "title": "<some-title>",
                "preview_url": "<some-preview_url>",
                "id": "<some-id>"
            },
        ]
    }
    
###PUT `/me/musics`

* Upload music

####Parameters
 
`url`

####Response

    {
        "title": "<some-title>", 
        "url": "<some-url>", 
        "artist": "<some-artist>", 
        "preview_url": "<some-preview_url>", 
        "duration": <some-duration>, 
        "id": "<some-id>"
    }