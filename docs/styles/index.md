Following endpoints are valid for styles.

##Endpoints

###URL `/styles`

###Method `GET`
* List of styles

###Response

    [
        {
            "category": "<some-category>",
            "is_featured": <some-is_featured>,
            "machine_name": "<some-machine_name>",
            "description": "<some-description>",
            "limits": {
                "quality": [
                    {
                        "res": "<some-resolution>",
                        "credits": <some-credits>
                    },
                    {
                        "res": "<some-resolution>",
                        "credits": <some-credits>
                    },
                    {
                        "res": "<some-resolution>",
                        "credits": <some-credits>
                    }
                ],
                "title_length": <some-title_length>,
                "text_length": <some-text_length>
            },
            "order": <some-order>,
            "sample_url": "<some-sample_url>",
            "thumbnail": "<some-thumbnail>",
            "name": "<some-name>"
        },
        ...
    ]
    
###URL `/styles/<machine_name>/`

###Method `GET`

###Response

###Endpoint `/me/styles`
    Authentication Headers is required.

###Method `GET`

###Response
