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
        "total_videos": 0,
        "bio": '',
        "plan": {
            'id': '',
            'type': '',
            'expires_on': '',
            'on_trial': false,
            'on_coupon': false,
            'trial_ends_on': '',
            'video_count': [{"quality": 360, "count": 1}],
            'payment_method': [],
            'private': false,
            'subscription': true,
            'cancelled': false,
            'cancelled_at': '',
            'max_quality': 720
        },
        "preferences": {
            'cta': {},
            'email': {},
            'timezone': '',
            'publisher_name': '',
            'logo': {}
        },
        'payment_key': { //Included for payment purpose
            'stripe': '', 
        }
    }

## Get Profile
- URL: `/me`  
- METHOD: `GET`
- QUERY PARAMS:
    - `plan`: Set this to `1` to include user plan.
    - `pref`: Set this to `1` to include user preferences.
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE:
    
        {
            "_count": 1,
            "data": [<response_object>]
        }

## Get User Plan
- URL: `/me/inventory`
- METHOD: `GET`
- QUERY PARAMS:
    - `limit`: Set this to `1` for including plan limit.
    - `payment`: Set this to `1` for including for payment info.
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE:
        
        {
            "_count": 1,
            "data": [{
                'id': '',
                'type': '',
                'expires_on': '',
                'on_trial': false,
                'on_coupon': false,
                'trial_ends_on': '',
                'video_count': [],
                'max_quality': 720,
                'payment_method': [],
                'limits': {
                    'logo': true,
                    'cta_allowed': true,
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
            }] 
        }

## Get User Preferences:
- URL: `/me/preferences/<logo|cta|email>/`
- METHOD: `GET`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- RESPONSE:
    
        {
            "_count": 1
            "data": [{
                "id": <user_id>,
                "name": <name of user>,
                "preferences": {
                "cta": {},
                "logo": {},
                "email": {}
                    
                }
            }]
        }
