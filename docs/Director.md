# Director


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**lb_url** | **str** |  | [optional] 
**films** | [**List[DirectorFilmsInner]**](DirectorFilmsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.director import Director

# TODO update the JSON string below
json = "{}"
# create an instance of Director from a JSON string
director_instance = Director.from_json(json)
# print the JSON string representation of the object
print Director.to_json()

# convert the object into a dict
director_dict = director_instance.to_dict()
# create an instance of Director from a dict
director_form_dict = director.from_dict(director_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


