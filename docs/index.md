# Picovico 2.0
[Picovico 2.0](http://picovico.com), the new version of Picovico, has been re-engineered and re-systematized from the core. The latter version is improved towards providing better user experience and stability.

## API Documentation
* __Platform Version__  
`2.0`
* __Authentication__  
`Basic Auth`
* __API Version__  
`2.1.0 - REST API`
* __Root URL__  
`http://uapi-f1.picovico.com/`__`v2.1`__  
* __Update__  
_`v2.0` is deprecated_

## Authentication
Each request is authorized based upon the `X-Access-Token` and `X-Access-Key` supplied as headers. 
Proceed to [Login Flow](account) for more details.

## Request node
All requests must be made over to `http://uapi-f1.picovico.com/v2.1/ `, so for the sake of legibility, this portion 
of the URL will be assumed and omitted in the remaining code samples in this documentation.

## Response
API response is always a valid JSON response.
