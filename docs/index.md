# Picovico 2.7
[Picovico 2.7](http://picovico.com), the new version of Picovico, has been re-engineered and re-systematized from the core. The latter version is improved towards providing better user experience and stability.

## API Documentation
* __Platform Version__  
`2.7`
* __API Version__  
`2.7 - REST API`
* __Root URL__  
`http://api2.picovico.com/`__`v2.7`__  
* __Authentication__  
    - Headers
        - X-Access-Token: `<token_provided>`
        - X-Access-Key: `<key_provided>`

## Requests

Endpoint: `http://api2.picovico.com/v2.7/`

- Note: *For the sake of legibility, this portion of the URL will be assumed and omitted in the remaining code samples in this documentation.*

There are some API endpoints which are accessible without `access_key` and `token`

Most of user centric requests requires Authentication Headers.

Proceed to [Login Flow](account) for more details.



## Response
All response are json with HTTP status code playing the part for error or success of the request.

Errors are responded with:

    {
        'error': {'message': ''},
        'status': <http_status_code>  // 400
    }

Success [200 OK] will be responded in:

    
    Only Newer API respond with:

    {
        '_count': <no_of_response_data>,
        'data': [{<success_response_object>},]  # [] for 0 count
    }


*For backward compatibility, only newer API respond in this format. See corresponding endpoints for actual response.*

- Note: *Success also may have other meta information followed by `_` such as `_page` where necessary.*
    
    
