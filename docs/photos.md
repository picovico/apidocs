#Photos
Following endpoints are valid for photos. `X-Access-Key` and `X-Access-Token` required wherever the endpoint expects 
authorization.
## Endpoints
### GET `/me/photos`
* Get list of user uploaded photos
* Categorized view from different sources
    
### PUT `/me/photos`
* Upload photo directly with the binary image file
* Supported format is .jpg/.png

### POST `/me/photos/external`
* Importing photos from external sources
* External sources may be facebook, flickr or other web urls

###  DELETE `/me/photos/<photo_id>`
* Deleting the photo

[More Details](photos/photo-details.md)