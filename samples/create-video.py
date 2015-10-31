#!/usr/bin/env python
import requests, json, sys

picovico_api_endpoint = "https://uapi-f1.picovico.com/v2.1/"
picovico_device_id = 'com.picovico.api.example'
picovico_app_id = 'some-app-id'
# if login with app_secret instead of username / password
picovico_app_secret ='some-app-secret'
# if login with username and password (App ID is mandatory for both cases)
picovico_username = ''
picovico_password = '' 

# temporary variables
picovico_access_key = None
picovico_access_token = None

def picovico_app_login():
   print "## : ## Login with app_id, app_secret"
   response = requests.post(picovico_api_endpoint + 'login/app', 
      data = {'app_id': picovico_app_id, 
         'app_secret': picovico_app_secret, 
         'device_id': picovico_device_id})
   return json.loads(response.text)

def picovico_login():
   print "## : ## Login with username / password"
   requests.post(picovico_api_endpoint + 'login', 
      data = {'username': picovico_username,
         'password': picovico_password, 
         'app_id': picovico_app_id, 
         'device_id': picovico_device_id})
   return json.loads(response.text)

def picovico_authenticated_request(url, method='GET', data={}):
   picovico_auth_headers = {'X-Access-Key': picovico_access_key, 
      'X-Access-Token' : picovico_access_token}
   if method == 'GET' or method == 'get':
      print "## : ## Making GET request to /{0}".format(url)
      response = requests.get(picovico_api_endpoint + url, headers=picovico_auth_headers)
   elif method == 'POST' or method == 'post':
      print "## : ## Making POST request to /{0}".format(url)
      response = requests.post(picovico_api_endpoint + url, data=data, headers=picovico_auth_headers)
   else:
      return False

   return json.loads(response.text)

# if login with app_id and app_secret
login_response = picovico_app_login()
# if login with username and password uncomment below.
# login_response = picovico_login()

if 'access_key' in login_response:
   picovico_access_key = login_response['access_key']
   picovico_access_token = login_response['access_token']
else:
   print "## : ## Login failed"
   sys.exit()

print "## : ## Access Token - ", picovico_access_token
print "## : ## Access Key - ", picovico_access_key

# Get Draft or start new project
project_data = picovico_authenticated_request("me/videos", method='POST', data={ "name": "New Picovico Video", "style": "vanilla", "quality": "360p"})
project_id = project_data.get('id', None)

if project_id is None:
   print "## : ## Project Not created. ERROR "
   print project_data
   sys.exit()

print "## : ## Project ID received " + project_id

# Make PUT request to upload image.
# Make POST request to upload third party hosted image.
# In both cases, id is received which needs to be provided as asset_id in the assets array.

assets= [  
      {  
         "start_time":0,
         "end_time":5,
         "name":"text",
         "data":{  
            "text":"Aweomse place to stay"
         }
      },
      {  
         "start_time":5,
         "end_time":10,
         "name":"text",
         "data":{  
            "title":"Hey",
            "text":"I am here to share you some of my favorite places"
         }
      },
      {  
         "start_time":10,
         "end_time":15,
         "name":"text",
         "data":{  
            "title":"Furnishing",
            "text":"The house is fully furnished with awesome furnitures."
         }
      },
      {  
         "start_time":15,
         "end_time":20,
         "name":"text",
         "data":{  
            "title":"Locality",
            "text":"Locality is quite good with good people around"
         }
       },
     # {  
     #     "start_time":20,
     #     "end_time":23,
     #     "asset_id":"<some-asset-id>",
     #     "name":"image",
     #     "data":{  
     #        "text":"Aweomse place to stay1"
     #     }
     #  },
     # {  
     #     "start_time":23,
     #     "end_time":26,
     #     "asset_id":"<some-asset-id>",
     #     "name":"image",
     #     "data":{  
     #        "text":"Aweomse place to stay2"
     #     }
     #  },
     # {  
     #     "start_time":26,
     #     "end_time":30,
     #     "asset_id":"<some-asset-id>",
     #     "name":"image",
     #     "data":{  
     #        "text":"Aweomse place to stay3"
     #     }
     #  },
     {  
         "start_time":0,
         "end_time":0,
         "name":"music",
         "asset_id":"NhLIo" # Library Music ID
      }    
   ]

# Save Project Assets information
project_define_response = picovico_authenticated_request('me/videos/'+ project_id, 
   method='POST',
   data = {'name':'commonTour', 
      'style': 'focus', 
      'quality': '360', 
      'assets':json.dumps(assets),
      'credits':'[["Music:","Kevin MacLeod"]]'})

# Send the Render request
render_response = picovico_authenticated_request('me/videos/'+project_id+'/render', method='POST')

import time
while ( True ) :
   status_response = picovico_authenticated_request('me/videos/' + project_id, method='GET')
   if 'video' in status_response:
      print "## : ## Video is READY"
      print status_response.get('video')
      break    

   time.sleep(20) 
