#Login Flow
Picovico 2.0 API follows a simple login flow. Each account is provided with username and password which authenticates
user with the system. Upon successful login, access_key and access_token are provided in the response.

## Update: 
As of API Version 2.1, Login Flow has some modifications.
Each login request must provide [app_id] as a mandatory third parameter,
and two different endpoints of login have been provided.

* Endpoint 1 - __/login__  
  Login with `app_id`, `username` & `password`  
* Endpoint 2 - __/login/app__  
  Login with `app_id`, `app_secret`

Check the [Developer Signup](account/developer-signup) page for more details.

## Step 1 
## (First Method) Login with username and password
###POST `/login` 
###parameters    
* username        
* password        
* app_id
  

## (Second Method) Login with app_id and app_secret
###POST `/login/app`
###parameters
* app_id
* app_secret

###response
__Both the methods will return same response upon successful authentication. __

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
    
    