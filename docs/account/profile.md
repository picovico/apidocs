User Profile Data

###Response Object

    {
        "id": '<user_id>',
        "profile_pic": '', 
        "email": '',
        "address": '',
        "gender": '',
        "country": '',
        "date_of_birth": '',
        "name": '',
        "video_count": 0,
        "bio": '',
        "plan": {
            'id': '',
            'type': '',
            'expires_on': '',
            'on_trial': false,
            'on_coupon': false,
            'trial_ends_on': '',
            'video_count': {},
            'payment_method': [],
            'limits': {
                'logo': true,
                'video': {
                    "min": -1,
                    "max": -1
                },
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
                }
            },
            'private': false,
            'subscription': true,
            'cancelled': false,
            'cancelled_at': '',
            'payment_key': {
                'stripe': '', 
            }
        },
        "preferences": {
            'cta': {},
            'email': {},
            'timezone': '',
            'publisher_name': '',
            'logo': {}
        },
        "limit": {
            'has_password': true,
            'usable_email': true,
            'max_projects': 10,
            'cta_allowed': false,
            'trial_disabled': false
        }
    }

## Get Profile
- URL: `/me`  
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE: `<response_object>`
