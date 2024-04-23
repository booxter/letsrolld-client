# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directors_get**](DefaultApi.md#directors_get) | **GET** /directors | Get Directors
[**directors_id_get**](DefaultApi.md#directors_id_get) | **GET** /directors/{id} | Get Director
[**films_get**](DefaultApi.md#films_get) | **GET** /films | Get Films
[**films_id_get**](DefaultApi.md#films_id_get) | **GET** /films/{id} | Get Film


# **directors_get**
> Director directors_get(limit=limit)

Get Directors

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.director import Director
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    limit = 10 # int | Number of directors to return (optional) (default to 10)

    try:
        # Get Directors
        api_response = api_instance.directors_get(limit=limit)
        print("The response of DefaultApi->directors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->directors_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of directors to return | [optional] [default to 10]

### Return type

[**Director**](Director.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns directors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directors_id_get**
> Director directors_id_get(id)

Get Director

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.director import Director
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | id

    try:
        # Get Director
        api_response = api_instance.directors_id_get(id)
        print("The response of DefaultApi->directors_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->directors_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Director**](Director.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a director |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **films_get**
> Film films_get(limit=limit, genre=genre, country=country, offer=offer)

Get Films

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.film import Film
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    limit = 10 # int | Number of films to return (optional) (default to 10)
    genre = 'genre_example' # str | Genre to filter by (optional)
    country = 'country_example' # str | Country to filter by (optional)
    offer = 'offer_example' # str | Offer to filter by (optional)

    try:
        # Get Films
        api_response = api_instance.films_get(limit=limit, genre=genre, country=country, offer=offer)
        print("The response of DefaultApi->films_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->films_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of films to return | [optional] [default to 10]
 **genre** | **str**| Genre to filter by | [optional] 
 **country** | **str**| Country to filter by | [optional] 
 **offer** | **str**| Offer to filter by | [optional] 

### Return type

[**Film**](Film.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns films |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **films_id_get**
> Film films_id_get(id)

Get Film

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.film import Film
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | id

    try:
        # Get Film
        api_response = api_instance.films_id_get(id)
        print("The response of DefaultApi->films_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->films_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id | 

### Return type

[**Film**](Film.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a film |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

