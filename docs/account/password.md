# This page is archived and no longer udpated. 

#Login Flow
Picovico 2.0 API follows a simple login flow. Each account is provided with username and password which authenticates
user with the system. Upon successful login, access_key and access_token are provided in the response.

## Step 1

###POST `/me/changepassword`  
###parameters
* `old_password` [optional](not required, if user registered from facebook)    - old password
* `new_password1`       - new password
* `new_password2`       - confirm password

###response
    {
        "message" : "Password successfully changed"
    }
    