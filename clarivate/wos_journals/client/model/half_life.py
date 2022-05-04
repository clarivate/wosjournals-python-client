"""
    Web of Science™ Journals API

    This API provides journal-level metadata and metrics for all journals in the Journal Citation Reports™ covered in the Web of Science Core Collection, including the Journal Impact Factor™ and other new metrics. Integrate journal data into your internal systems or retrieve journal indicators for bibliometrics studies.  ## Resources This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.  The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-journal). The access requires registration on the Portal and approval from the Clarivate Sales/Product teams to entitle to the API.  ## Credentials All requests require authentication with an API Key authentication flow. For more details, check the [Guide](https://developer.clarivate.com/help/api-access#key_access).  ## Content You can learn more about content at [Journal Citation Reports™ Product page](https://clarivate.com/webofsciencegroup/solutions/journal-citation-reports/), or in the [documentation](http://jcr.help.clarivate.com/Content/home.htm).  ## <a name=\"search\"></a> Search (query parameter `q=`) This API supports free-text search for a journal name, abbreviation, ISSN code, publisher, and Web of Science™ category name (only `/categories` endpoint). You need to provide a complete and valid ISSN code pattern; otherwise, the API will not look up for ISSN codes.  ### Boolean operators | Operator    | Description  | Example| |-----|-----|------------------| | + / \" \" | Search by two or more terms in the same field. Blank space is the same as an AND operator. The search retrieves all the records that contain the terms, e.g., | `/journals?q=matrix biology`<br> `/journals?q=nature+group` | | OR | Search by at least one term in the field. The search retrieves all the records that contain one of the terms, e.g., | `/journals?q=gas OR oil` | | NOT / - | Search by excluding specific terms. The search retrieves all the records that match the query specifics, e.g., | `/journals?q=genetics -nature` |  ### Special symbols The wildcards ( __*__ ) are allowed in the search that starts with the search query&#58; `/journals?q=nano*` will search indications that start from __nano__&#58; for example, _Nanotechnology_ or _nanotubes_.  Please note&#58; the free text search query (with the parameter `q=`) should contain at least three symbols.  ## Filtering The API supports several filters for Journals and Web of Science™ Categories, narrowing down the initial list of entities or search results.  There are two types of filters:  - Filter by one or multiple **values**: *edition*, *categoryCode*, *jcrYear*, *jifQuartile* - Filter by **range**: *jif*, *jifPercentile*, *jci*,   ### Filter by values The filter name goes before the equals sign, followed by one or multiple filter values, separated by a semicolon, like `categoryCode=RZ;RU`. You can combine various filters with or without the search. Filters are separated by an ampersand (**&amp;**): `q=nature&categoryCode=RU;KM&jcrYear=2018`  Please note&#58; filter by *jcrYear* allows only one year value as an input  ### <a name='range'></a> Filter by range The API supports range filtering for Journal Impact Factor (*jif*) or Journal Impact Factor Percentile (*jifPercentile*) with the following operators:  - ***eq*** (equal): if a Journal Impact Factor (Percentile) is equal to a specific number.<br /> For example: for `jif=eq:5.032` the result will include journals with Journal Impact Factor = 5.032.<br /> Not combinable with any other operator - ***gt*** (greater than): if a Journal Impact Factor (Percentile) is greater than a specific number.<br /> For example: for `jif=gt:5` the result will include journals with Journal Impact Factor = 5.001 and higher.<br /> Combinable with *lt* and *lte* operators - ***gte*** (greater than equal): if a Journal Impact Factor (Percentile) is greater than or equal to a specific number.<br /> For example: for `jif=gte:5` the result will include journals with Journal Impact Factor = 5.000 and higher.<br /> Combinable with *lt* and *lte* operators - ***lt*** (less than): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lt:5` the result will include journals with Journal Impact Factor = 4.999 and less.<br /> Combinable with *gt* and *gte* operators - ***lte*** (less than equal): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lte:5` the result will include journals with Journal Impact Factor = 5.000 and less.<br /> Combinable with *gt* and *gte* operators  Use `AND` to combine two operators, e.g.,`jifPercentile=gte:50 AND lte:80` responses with all journals in a percentile range from 50% to 80% (both included).  ## Pagination To ensure fast response time, each search or multiple entity calls (such as `/journals` or `/categories/ID/cited/year/YYYY`) retrieve only a certain number of hits/records.  There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.  - limit&#58; Number of returned results, ranging from 0 to 50 (default **10**) - page&#58; Specifying a page to retrieve (default **1**)  Moreover, this information is shown in the response body, in the tag **metadata**&#58;  ```json \"metadata\": {   \"total\": 91,   \"page\": 1,   \"limit\": 10 } ``` ## Errors The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.  | Code  | Title  | Description | |---|---|---| | 400  | Bad request  | Request syntax error | | 401  | Unauthorized  | The API key is invalid or missed | | 404  | Not found  | The resource is not found | | 404  | Suppressed Title | Suppressed Journal from specific year. Read more at [https://jcr.help.clarivate.com/Content/title-suppressions.htm](https://jcr.help.clarivate.com/Content/title-suppressions.htm) | | 405 | Method not allowed | Method other than GET is not allowed | | 50X  | Server errors  | Technical error with servers| Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:  ```json \"error\": {   \"status\": 404,   \"title\": \"Resource couldn't be found\",   \"details\": \"There is no information in WoS Journals API about the identifier ABC_DEF for the Journals content area. Sorry :(\" } ``` For the `401 Unauthorized` error the response body is a little bit different: ```json {   \"error_description\": \"The access token is missing\",   \"error\": \"invalid_request\" } ```  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from clarivate.wos_journals.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from clarivate.wos_journals.client.exceptions import ApiAttributeError



class HalfLife(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'cited': (float,),  # noqa: E501
            'citing': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'cited': 'cited',  # noqa: E501
        'citing': 'citing',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """HalfLife - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cited (float): [optional]  # noqa: E501
            citing (float): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """HalfLife - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cited (float): [optional]  # noqa: E501
            citing (float): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
