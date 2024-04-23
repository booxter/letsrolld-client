# Film


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**rating** | **str** |  | [optional] 
**runtime** | **int** |  | [optional] 
**lb_url** | **str** |  | [optional] 
**jw_url** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**countries** | **List[str]** |  | [optional] 
**offers** | **List[str]** |  | [optional] 
**directors** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.film import Film

# TODO update the JSON string below
json = "{}"
# create an instance of Film from a JSON string
film_instance = Film.from_json(json)
# print the JSON string representation of the object
print Film.to_json()

# convert the object into a dict
film_dict = film_instance.to_dict()
# create an instance of Film from a dict
film_form_dict = film.from_dict(film_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


