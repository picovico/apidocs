#Videos
Following endpoints are valid for videos. `X-Access-Key` and `X-Access-Token` required wherever the endpoint expects 
authorization.

## Endpoints
### GET `/me/videos`
* List of videos created or being created

### GET `/v/video-resource-id/video-name.mp4`
* Direct Link to video file after a video is created successfully.
* Authorization is NOT required

### POST `/me/videos`
* Create a new video project, or get the last draft project

### POST `/me/videos/video-resource-id`
* Define or update a video content

### GET `/me/videos/video-resource-id`
Get the status, details of any video

### POST `/me/videos/video-resource-id/render`
* Send the video rendering request to rendering engine

    
    