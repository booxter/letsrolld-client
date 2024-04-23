# DirectorFilmsInner


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
from openapi_client.models.director_films_inner import DirectorFilmsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DirectorFilmsInner from a JSON string
director_films_inner_instance = DirectorFilmsInner.from_json(json)
# print the JSON string representation of the object
print DirectorFilmsInner.to_json()

# convert the object into a dict
director_films_inner_dict = director_films_inner_instance.to_dict()
# create an instance of DirectorFilmsInner from a dict
director_films_inner_form_dict = director_films_inner.from_dict(director_films_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


