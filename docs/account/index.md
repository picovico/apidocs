<h1 style='color:red; padding:2em; border:1px solid red'> This page is archived and no longer udpated. </h1>

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
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- PARAMS:
    - `app_secret`: (_required_) Application Secret Provided by picovico.
    - `device_id`: (_optional_) Some unique device identifier.
- RESPONSE:
        
        {
            "_count": 1,
            "data": [<response_object>]
        
        }


## User Login
- URL: `/login/`
- METHOD: `POST`
- HEADERS:
    - `X-PV-Meta-App`: (_required_) APP Id from picovico developer.
- PARAMS:
    - `username`: (_required_) Email of login user.
    - `password`: (_required_) Password of user.
    - `device_id`: (_optional_) Some unique device identifier.
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
    
    
