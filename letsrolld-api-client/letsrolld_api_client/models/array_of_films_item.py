from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArrayOfFilmsItem")


@_attrs_define
class ArrayOfFilmsItem:
    """
    Attributes:
        title (str):
        id (Union[Unset, int]):
        description (Union[Unset, str]):
        year (Union[Unset, int]):
        rating (Union[Unset, str]):
        runtime (Union[Unset, int]):
        lb_url (Union[Unset, str]):
        jw_url (Union[None, Unset, str]):
        genres (Union[Unset, List[str]]):
        countries (Union[Unset, List[str]]):
        offers (Union[Unset, List[str]]):
        directors (Union[Unset, List[int]]):
    """

    title: str
    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    rating: Union[Unset, str] = UNSET
    runtime: Union[Unset, int] = UNSET
    lb_url: Union[Unset, str] = UNSET
    jw_url: Union[None, Unset, str] = UNSET
    genres: Union[Unset, List[str]] = UNSET
    countries: Union[Unset, List[str]] = UNSET
    offers: Union[Unset, List[str]] = UNSET
    directors: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        id = self.id

        description = self.description

        year = self.year

        rating = self.rating

        runtime = self.runtime

        lb_url = self.lb_url

        jw_url: Union[None, Unset, str]
        if isinstance(self.jw_url, Unset):
            jw_url = UNSET
        else:
            jw_url = self.jw_url

        genres: Union[Unset, List[str]] = UNSET
        if not isinstance(self.genres, Unset):
            genres = self.genres

        countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.countries, Unset):
            countries = self.countries

        offers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.offers, Unset):
            offers = self.offers

        directors: Union[Unset, List[int]] = UNSET
        if not isinstance(self.directors, Unset):
            directors = self.directors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if year is not UNSET:
            field_dict["year"] = year
        if rating is not UNSET:
            field_dict["rating"] = rating
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if lb_url is not UNSET:
            field_dict["lb_url"] = lb_url
        if jw_url is not UNSET:
            field_dict["jw_url"] = jw_url
        if genres is not UNSET:
            field_dict["genres"] = genres
        if countries is not UNSET:
            field_dict["countries"] = countries
        if offers is not UNSET:
            field_dict["offers"] = offers
        if directors is not UNSET:
            field_dict["directors"] = directors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        year = d.pop("year", UNSET)

        rating = d.pop("rating", UNSET)

        runtime = d.pop("runtime", UNSET)

        lb_url = d.pop("lb_url", UNSET)

        def _parse_jw_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        jw_url = _parse_jw_url(d.pop("jw_url", UNSET))

        genres = cast(List[str], d.pop("genres", UNSET))

        countries = cast(List[str], d.pop("countries", UNSET))

        offers = cast(List[str], d.pop("offers", UNSET))

        directors = cast(List[int], d.pop("directors", UNSET))

        array_of_films_item = cls(
            title=title,
            id=id,
            description=description,
            year=year,
            rating=rating,
            runtime=runtime,
            lb_url=lb_url,
            jw_url=jw_url,
            genres=genres,
            countries=countries,
            offers=offers,
            directors=directors,
        )

        array_of_films_item.additional_properties = d
        return array_of_films_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
