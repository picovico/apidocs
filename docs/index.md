# Picovico 2.5
[Picovico 2.5](http://picovico.com), the new version of Picovico, has been re-engineered and re-systematized from the core. The latter version is improved towards providing better user experience and stability.

## API Documentation
* __Platform Version__  
`2.5`
* __API Version__  
`2.5 - REST API`
* __Root URL__  
`http://api2.picovico.com/`__`v2.5`__  
* __Authentication__  

*Following headers should be included in requests:*


    X-Access-Token: <token_provided>
    X-Access-Key: <key_provided>

## Requests

Endpoint: `http://api2.picovico.com/v2.5/`

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

    {
        '_count': <no_of_response_data>,
        'data': [{<success_response_object>},]  # [] for 0 count
    }


- Note: *Success also may have other meta information followed by `_` such as `_page` where necessary.*
