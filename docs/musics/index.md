###Response Object
```json
{
    "category": "<some_musical_category>", //E.g. Rock
    "is_featured": true,
    "artist": "<Artist of music if available>",
    "title": "<Title of music if available>",
    "preview_url": "<preview_url>"
    "duration": <duration_in_seconds>,
    "id": "<music_id>"
}
```
###List all picovico provided musics
>- URL: `/musics`
>- METHOD: `GET`
>- RESPONSE: `[<response_object>,...]`

###Get Single Specific Musics
>- URL: `/musics/<music_id>`
>- METHOD: `GET`
>- RESPONSE: `<response_object>`
