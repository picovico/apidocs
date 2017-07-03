###Response Object

```json
{
    "category": "<style_category>",
    "is_featured": <true|false>,
    "machine_name": "<machine_name>",
    "description": "<small_description>",
    "limits": { //slide limits of style
    "slide": {
        "text": {
        "max": -1, //max text slide allowed -1 is unlimited, 0 is restricted.
        "title_len": 50, //character length of title
        "text_len": 50, // character length of text body
        "min": -1 //minimum text slide. -1 is unlimited, 0 is restricted.
        },
        "image": {
        "caption_len": 50, //character length of caption
        "max": -1,
        "min": -1
        },
        "videoclip": {
        "max": -1,
        "min": -1
        },
        "music": {
        "max": -1,
        "min": -1
        },
        "logo": {
        "max": -1,
        "min": -1
        }
    },
    "quality": [
        {
        "res": "720", //resolution of style 
        "supported": true, //whether resolution is supported or not.
        "white_labeled": false, // whether watermark is allowed or not for user.
        "allowed": false // whether user is allowed the resolution or not. [Always false for non logged in user]
        },
        {
        "res": "1080",
        "supported": false,
        "white_labeled": false,
        "allowed": false
        },
        {
        "res": "480",
        "supported": true,
        "white_labeled": false,
        "allowed": false
        },
        {
        "res": "360",
        "supported": true,
        "white_labeled": false,
        "allowed": false
        }
    ],
    },
    "musics": [],
    "order": 1,
    "thumbnail": "<thumbnail_url>",
    "meta": {
        "related_styles": [],
        "recommended_for": []
    },
    "sponsored": { //sponsored slide content. Should be included in video if included.
        "begin": [
            {
            "url": "<url>",
            "duration": 3 // time duration of slide.
        }
        ],
        "end": []
        },
    "scope": "<style_summary>",
    "sample_url": "<sample_url>",
    "size": [ //aspect_ratio supported by style
        "16:9"
        ],
    "type": "<type_of_style>", // type of style in context to pricing plan
    "youtube_url": "<youtube_id>", // youtube id for sample of style.
    "is_story": false, // whether style is of storyboard type with preconfigured slides.
    "name": "<name_of_style>"
}
```
###Publicly Available Styles.

1 List All Public Styles.

- URL: `/styles`
- METHOD: `GET`
- QUERY PARAMS:
    - `count`: Number of styles.
    - `page`: Page Number if available.
- HEADERS:
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE: 
        
        {
            "_total": <total_no_of_styles>, 
            "data": [<style_response_object>,...],
            "_count": 10, //We provide 10 styles by default, can query more with num.
            "_page": 1
        }
    
2 Get Single Specific Style

- URL: `/styles/<machine_name>/`
- METHOD: `GET`
- HEADERS:
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE:

        {
            "_count": 1,
            "data": [<style_response_object>] 
        }
            
###User Allowed Styles

1 List All User Allowed Styles.

- URL: `/me/styles`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- QUERY PARAMS:
    - `count`: Number of styles.
    - `page`: Page Number if available.
- RESPONSE:
        
        {
            "_total": <total_styles>,
            "data": [<style_response_object>,...],
            "_count": 10, #as queried
            "_page": 1 
        } 

2 Get Single Specific User Allowed Style
    
- URL: `/me/styles/<machine_name>`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE:

        {
            "_count": 1,
            "data": [<style_response_object>] 
        }
