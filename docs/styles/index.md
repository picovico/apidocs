###Response Object

```json
{
    "category": "<style_category>",
    "is_featured": <true|false>,
    "machine_name": "<machine_name>",
    "description": "<small_description>",
    "thumbnail": "<thumbnail_url>",
    "sample_url": "<sample_url>",
    "scope": "<style_summary>",
    "type": "<type_of_style>", // type of style in context to pricing plan
    "youtube_url": "<youtube_id>", // youtube id for sample of style.
    "is_story": false, // whether style is of storyboard type with preconfigured slides.
    "name": "<name_of_style>"
    //Only responded if querying `all` information
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
    "sponsored": { //sponsored slide content. Will be included in video automatically.
        "begin": [
            {
            "url": "<url>",
            "duration": 3 // time duration of slide.
        }
        ],
        "end": []
        },
    "size": [ //aspect_ratio supported by style
        "16:9"
        ],
}
```
###Publicly Available Styles.

1 List All Public Styles.

- URL: `/styles`
- METHOD: `GET`
- QUERY PARAMS:
    - `page`: Page Number if available.
    - `count`: Number of styles.
    - `story`: Whether you want to filter `story` in style.
    - `type`: Whether you want to filter `types` in style.
    - `all`: Whether include extra information such as `limits` and `quality` etc in response. 
- HEADERS:
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE: 
        
        {
            "_total": <total_no_of_styles_available>, 
            "data": [<style_response_object>,...],
            "_count": 10, //We provide 10 styles by default, can query more with count.
            "_page": 1
        }
    
2 Get Single Specific Style

- URL: `/styles/<machine_name>/`
- METHOD: `GET`
- QUERY PARAMS:
    - `story`: Whether you want to filter `story` in style.
    - `type`: Whether you want to filter `types` in style.
    - `all`: Whether include extra information such as `limits` and `quality` etc in response. 
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
- QUERY PARAMS:
    - `page`: Page Number if available.
    - `count`: Number of styles.
    - `story`: Whether you want to filter `story` in style.
    - `type`: Whether you want to filter `types` in style.
    - `all`: Whether include extra information such as `limits` and `quality` etc in response. 
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
- QUERY PARAMS:
    - `story`: Whether you want to filter `story` in style.
    - `type`: Whether you want to filter `types` in style.
    - `all`: Whether include extra information such as `limits` and `quality` etc in response. 
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE:

        {
            "_count": 1,
            "data": [<style_response_object>] 
        }
