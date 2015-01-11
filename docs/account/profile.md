#Login Flow
Picovico 2.0 API follows a simple login flow. Each account is provided with username and password which authenticates
user with the system. Upon successful login, access_key and access_token are provided in the response.

## Step 1

### GET `/me`  
* Get user related profile information

###response

    {
        "profile_pic": "<some-link>",
        "video_count": <some-user-video-count>,
        "name": "<some-user-full-name>",
        "bio": "<some-bio-tagline>",
        "gender": "male/female",
        "address": "<some-address>",
        "id": "<some-user-id>",
        "date_of_birth": <date-timestamp>,
        "country": "<some-country>",
        "email": "<some-email>",
    }
    

### POST `/me`
* Update profile information

###parameters
* `name`        -   Full Name
* `bio`         -   User bio / Tagline
* `address`     -   User Address
* `country`     -   User Country
* `gender`      -   Gender 
* `date_of_birth` - Date of birth

###response
    {
        "profile_pic": "<some-link>",
        "video_count": <some-user-video-count>,
        "name": "<some-user-full-name>",
        "bio": "<some-bio-tagline>",
        "gender": "male/female",
        "address": "<some-address>",
        "id": "<some-user-id>",
        "date_of_birth": <date-timestamp>,
        "country": "<some-country>",
        "email": "<some-email>",
    }
    
    