<h1 style='color:red; padding:2em; border:1px solid red'> This page is archived and no longer udpated. </h1>

We provide `signedurls` to upload directly to our s3 bucket.
Currently this feature is supported for `videoclip` asset but
we will be opening it for `music` and `photos` as well.

The workflow is simple, the user provides us the `md5` and `size` of content. We provide the
user the URL for such upload. You upload the content and finally acknowledge with picovico about
final action.

### Get DirectUpload URLs
1. Get the directupload url from md5 checksum.
    
    MD5 checksum is required in URL and should be calculated.
    
        'size' is required as the URL responded is broken for chunk uploads of 5MB.
        'mime'(optional) should be sent if it is other than 'video/mp4'(default).
        Optional 'filename' can be sent as well.
        'asset' is one of videoclip, photo, music. Currently 'videoclip' is only supported
    
    - URL: `/me/directupload/<asset>/<checksum>/?size=<FILE_SIZE>&filename=<OPTIONAL_FILENAME>&(optional)mime=video/mp4`
    - METHOD: `GET`
    - HEADERS:
        - `X-Access-Token`: (required) Token Provided by Picovico.
        - `X-Access-Key`: (required) Access Key Provided by Picovico.
        - `X-PV-Meta-App`: (required) APP Id from picovico developer.
    - RESPONSE:
        - If the checksum object is already present:
            
                {
                "_count": 1,
                "data": [{ //will contain asset object
                "url": "<preview_url>",
                "preview_gif": "<preview_gif>",
                "thumbnail_url": "<thumbnail_url>",
                "id": "<videoclip_id>",
                "status": "<status_of_clip>" //pending,available
                }],
                "_upload": false, //check from this meta whether upload is necessary or not
                }
        
        - Else:
                
                {
                '_count': 1,
                '_upload': true,
                'data': [{
                        'upload_id': <aws_upload_id>,
                        'chunk_size': <chunk_size>, //5*1024*1024
                        'urls': [{
                            'PartNumber': <part_of_chunk>,
                            'url': <signed_url>
                            },...]
                    
                    }]
                }

2. Finalize your upload

    Once the upload happens at s3. There is a need to finalize the upload.
- URL: `/me/directupload/<asset>/<checksum>/`
- METHOD: `POST`
- HEADERS:
    - `X-Access-Token`: (required) Token Provided by Picovico.
    - `X-Access-Key`: (required) Access Key Provided by Picovico.
    - `X-PV-Meta-App`: (required) APP Id from picovico developer.
- PARAMS:
    - `uploads`: (required) `json` format `[{"PartNumber": 1, "ETag": ""},..]` responded by s3 upload.  
- RESPONSE:
        
        {
            "_count": 1,
            "data": [{ //will contain asset object
            "url": "<preview_url>",
            "preview_gif": "<preview_gif>",
            "thumbnail_url": "<thumbnail_url>",
            "id": "<videoclip_id>",
            "status": "<status_of_clip>" //pending,available
            }]
        }
        
