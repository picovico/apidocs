#Videos
Following endpoints are valid for videos. `X-Access-Key` and `X-Access-Token` required wherever the endpoint expects 
authorization.
## Endpoints
### GET `/v2.0/me/videos`
* List of videos created or being created

### GET `/v2.0/v/video-resource-id/video-name.mp4`
* Direct Link to video file after a video is created successfully.
* Authorization is NOT required

### POST `/v2.0/me/videos`
* Create a new video project, or get the last draft project

### POST `/v2.0/me/videos/video-resource-id`
* Define or update a video content

### GET `/v2.0/me/videos/video-resource-id`
* Get the status, details of any video

### POST `/v2.0/me/videos/video-resource-id/render`
* Send the video rendering request to rendering engine


[More Details](details.md)
    
    