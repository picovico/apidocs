#Login Flow
Picovico 2.0 API follows a simple login flow. Each account is provided with username and password which authenticates
user with the system. Upon successful login, access_key and access_token are provided in the response.

## Step 1

###POST `/v2.0/login`  
###parameters
* username
* password

###response
    {
        "access_key" : "<some-random-access-key>",
        "access_token" : "<some-random-access-token>",
        "id" : "<system-wide-unique-resource-id>"
    }
    
## Step 2
Use the `access_key` and `access_token` as headers for making other subsequent requests.

###headers

    X-Access-Key: access_key  
    X-Access-Token: access_token
    
    