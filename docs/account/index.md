Picovico provides `app` login as well as `user` login. Currently, both app login and user login provides
`access_key` and `access_token` which is then used for all authentications.


##Response Object

```json
{
    'access_key': <picovico_access_key>,
    'access_token': <picovico_access_token>,
    'id': <user_id>
}
```


## App Login
- URL: `/login/app/`
- METHOD: `POST`
- HEADERS:
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- PARAMS:
    - `app_id`: (required) Application Identifier Provided by picovico.
    - `app_secret`: (required) Application Secret Provided by picovico.
    - `device_id`: (optional) Some unique device identifier.
- RESPONSE:
        
        {
            "_count": 1,
            "data": [<response_object>]
        
        }


## User Login
- URL: `/login/`
- METHOD: `POST`
- HEADERS:
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- PARAMS:
    - `username`: (required) Email of login user.
    - `password`: (required) Password of user.
    - `device_id`: (optional) Some unique device identifier.
- RESPONSE:

        {
            "_count": 1,
            "data": [<response_object>]
        }

Use the `access_key` and `access_token` as headers for making other subsequent requests.

###Authentication Headers
These headers are used with all urls with prefix `/me`

    X-Access-Key: access_key  
    X-Access-Token: access_token
    
    
