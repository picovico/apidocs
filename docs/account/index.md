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
- URL: `/login/`
- METHOD: `POST`
- PARAMS:
    - `app_id`: (required) Application Identifier Provided by picovico.
    - `app_secret`: (required) Application Secret Provided by picovico.
    - `device_id`: (optional) Some unique device identifier.
- RESPONSE: `<response_object>`


## User Login
- URL: `/login/`
- METHOD: `POST`
- PARAMS:
    - `username`: (required) Email of login user.
    - `password`: (required) Password of user.
    - `app_id`: (required) Application ID for login.
    - `device_id`: (optional) Some unique device identifier.
- RESPONSE: `<response_object>`

Check the [Developer Signup](account/developer-signup) page for more details.

Use the `access_key` and `access_token` as headers for making other subsequent requests.

###Authentication Headers

    X-Access-Key: access_key  
    X-Access-Token: access_token
    
    
