# wos-journals-client-py.CategoriesApi

All URIs are relative to *https://api.clarivate.com/apis/wos-journals/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_get**](CategoriesApi.md#categories_get) | **GET** /categories | Search and filter across the journal categories
[**categories_id_cited_year_year_get**](CategoriesApi.md#categories_id_cited_year_year_get) | **GET** /categories/{id}/cited/year/{year} | Get journals that cite all journals in the category for the JCR year
[**categories_id_citing_year_year_get**](CategoriesApi.md#categories_id_citing_year_year_get) | **GET** /categories/{id}/citing/year/{year} | Get journals that were cited by all journals from the category for the JCR year
[**categories_id_get**](CategoriesApi.md#categories_id_get) | **GET** /categories/{id} | Get a category
[**categories_id_reports_year_year_get**](CategoriesApi.md#categories_id_reports_year_year_get) | **GET** /categories/{id}/reports/year/{year} | Get category metrics for a year


# **categories_get**
> InlineResponse2005 categories_get()

Search and filter across the journal categories

The endpoint allows to search, filter, or browse across the Categories content.  The endpoint doesn't require any parameter to return results, although only main information for the first ten records sorted alphabetically will be retrieved.  To get comprehensive results, a set of parameters could be applied: - `q`: Category name - `edition`: filter by category edition - `jcrYear`: filter by Category Report Year (since 203) - `limit`: set the limit of records on the page (1-50) - `page`: set the result page  By default, all the responses are sorted alphabetically, only in case of search the results will be sorted by relevance.  The response contains: - Main information about the number of records found, page and limit - Category unique ID (based on category code and edition) - API Link to Category record - Category title - Search matches with the found phrase ***&lt;em&gt;*** *highlighted* ***&lt;/em&gt;*** - only if parameter `q` is requested - Edition information - only if the parameter `edition` is requested - Link to the Category Report - only if parameter `jcrYear` is requested

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import categories_api
from wos-journals-client-py.model.inline_response2005 import InlineResponse2005
from pprint import pprint
# Defining the host is optional and defaults to https://api.clarivate.com/apis/wos-journals/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wos-journals-client-py.Configuration(
    host = "https://api.clarivate.com/apis/wos-journals/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Enter a context with an instance of the API client
with wos-journals-client-py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = categories_api.CategoriesApi(api_client)
    q = "q_example" # str | Free-text search by category name.  Search logic is described in the section [Search](#search). (optional)
    edition = "edition_example" # str | Filter by Web of Sceince Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded (ournals across more than 170 disciplines) - SSCI - Social Sciences Citation Index (journals across more than 50 social science disciplines)  Multiple values are allowed, separated by semicolon ( **;** ) (optional)
    jcr_year = 1 # int | Filter by Category Citation Report year (from 2003).  Only one value is allowed. (optional)
    page = 1 # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search and filter across the journal categories
        api_response = api_instance.categories_get(q=q, edition=edition, jcr_year=jcr_year, page=page, limit=limit)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free-text search by category name.  Search logic is described in the section [Search](#search). | [optional]
 **edition** | **str**| Filter by Web of Sceince Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded (ournals across more than 170 disciplines) - SSCI - Social Sciences Citation Index (journals across more than 50 social science disciplines)  Multiple values are allowed, separated by semicolon ( **;** ) | [optional]
 **jcr_year** | **int**| Filter by Category Citation Report year (from 2003).  Only one value is allowed. | [optional]
 **page** | **int**| Specifying a page to retrieve | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Number of returned results, ranging from 0 to 50 | [optional] if omitted the server will use the default value of 10

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_id_cited_year_year_get**
> InlineResponse2008 categories_id_cited_year_year_get(id, year)

Get journals that cite all journals in the category for the JCR year

The Cited Subject Category table lists journals that cite other journals in the subject category.  Category Cited data contains:  - Citing **Journal** with the link to WoS Journal API entity.<br /> Citing journals are sorted in descending order. At the top is the journal with the largest number of citations to the subject category. - **Cited journals**: The number of journals in the subject category. - **Cited year (all)**:  The total number of citations from the citing journal. This total includes the number shown under each year and the number in the \"Rest\". - **Cited Year (10-year interval)**: The publication year of the cited articles. - **Cited Year (rest)**: All publication years of cited articles prior to the ten-year period defined. For example, if the cited years are 2013-2004, the Rest number will show the number of citations from the citing journal in 2012 to articles published in 2003 and earlier in journals in the subject category.     Numbers in the \"All Journals\" are sums of the numbers for each year. \"All others\" refers to citing journals not listed by name.    For detailed information, please visit [this page](http://jcr.help.clarivate.com/Content/cited-category-data.htm)

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import categories_api
from wos-journals-client-py.model.inline_response2008 import InlineResponse2008
from pprint import pprint
# Defining the host is optional and defaults to https://api.clarivate.com/apis/wos-journals/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wos-journals-client-py.Configuration(
    host = "https://api.clarivate.com/apis/wos-journals/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Enter a context with an instance of the API client
with wos-journals-client-py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = categories_api.CategoriesApi(api_client)
    id = "RU_SCIE" # str | Category ID
    year = 2014 # int | JCR Year (from 2003)
    page = 1 # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get journals that cite all journals in the category for the JCR year
        api_response = api_instance.categories_id_cited_year_year_get(id, year)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_id_cited_year_year_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get journals that cite all journals in the category for the JCR year
        api_response = api_instance.categories_id_cited_year_year_get(id, year, page=page, limit=limit)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_id_cited_year_year_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category ID |
 **year** | **int**| JCR Year (from 2003) |
 **page** | **int**| Specifying a page to retrieve | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Number of returned results, ranging from 0 to 50 | [optional] if omitted the server will use the default value of 10

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_id_citing_year_year_get**
> InlineResponse2009 categories_id_citing_year_year_get(id, year)

Get journals that were cited by all journals from the category for the JCR year

Category Citing data contains:  - Cited **Journal** with the link to WoS Journal API entity.<br /> Cited journals are sorted in descending order. At the top is the journal with the largest number of citations to the subject category. - **Citing journals**: The number of journals in the subject category. - **Cited year (all)**:  The total number of citations to the citing journal. This total includes the number shown under each year and the number in the \"Rest\". - **Cited Year (10-year interval)**: The publication year of the cited articles. - **Cited Year (rest)**: All publication years of cited articles prior to the ten-year period defined. For example, if the cited years are 2013-2004, the Rest number will show the number of citations from the citing journal in 2012 to articles published in 2003 and earlier in journals in the subject category.     Numbers in the \"All Journals\" are sums of the numbers for each year. \"All others\" refers to citing journals not listed by name.    For detailed information, please visit [this page](http://jcr.help.clarivate.com/Content/citing-category-data.htm)

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import categories_api
from wos-journals-client-py.model.inline_response2009 import InlineResponse2009
from pprint import pprint
# Defining the host is optional and defaults to https://api.clarivate.com/apis/wos-journals/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wos-journals-client-py.Configuration(
    host = "https://api.clarivate.com/apis/wos-journals/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Enter a context with an instance of the API client
with wos-journals-client-py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = categories_api.CategoriesApi(api_client)
    id = "RU_SCIE" # str | Category ID
    year = 2014 # int | JCR Year (from 2003)
    page = 1 # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get journals that were cited by all journals from the category for the JCR year
        api_response = api_instance.categories_id_citing_year_year_get(id, year)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_id_citing_year_year_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get journals that were cited by all journals from the category for the JCR year
        api_response = api_instance.categories_id_citing_year_year_get(id, year, page=page, limit=limit)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_id_citing_year_year_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category ID |
 **year** | **int**| JCR Year (from 2003) |
 **page** | **int**| Specifying a page to retrieve | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Number of returned results, ranging from 0 to 50 | [optional] if omitted the server will use the default value of 10

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_id_get**
> InlineResponse2006 categories_id_get(id)

Get a category

The category profile provides a comprehensive overview, beginning in 2003, for each of more than 230 different subject categories in the JCR.  Information contain the name, description and links to each JCR Category Year Report (starting from 2003)

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import categories_api
from wos-journals-client-py.model.inline_response2006 import InlineResponse2006
from pprint import pprint
# Defining the host is optional and defaults to https://api.clarivate.com/apis/wos-journals/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wos-journals-client-py.Configuration(
    host = "https://api.clarivate.com/apis/wos-journals/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Enter a context with an instance of the API client
with wos-journals-client-py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = categories_api.CategoriesApi(api_client)
    id = "RU_SCIE" # str | Category ID, consisting of a two-letter category code and four-letter edition, separated by **_** (i.e., ***RZ_SSCI*** or ***IP_SCIE***)

    # example passing only required values which don't have defaults set
    try:
        # Get a category
        api_response = api_instance.categories_id_get(id)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category ID, consisting of a two-letter category code and four-letter edition, separated by **_** (i.e., ***RZ_SSCI*** or ***IP_SCIE***) |

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **categories_id_reports_year_year_get**
> InlineResponse2007 categories_id_reports_year_year_get(id, year)

Get category metrics for a year

For each JCR year all metrics related to a subject category in the Journal Citation Record are available, including: number of journals and articles in the category, Total Cites, Median Impact Factor, Aggregate Impact Factor, Aggregate Immediacy Index, and Cited and Citing category half-life.  Please find detailed information about the metrics in the Journals by JCR Year Report output

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import categories_api
from wos-journals-client-py.model.inline_response2007 import InlineResponse2007
from pprint import pprint
# Defining the host is optional and defaults to https://api.clarivate.com/apis/wos-journals/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wos-journals-client-py.Configuration(
    host = "https://api.clarivate.com/apis/wos-journals/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Enter a context with an instance of the API client
with wos-journals-client-py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = categories_api.CategoriesApi(api_client)
    id = "RU_SCIE" # str | Category ID
    year = 2016 # int | Category report year

    # example passing only required values which don't have defaults set
    try:
        # Get category metrics for a year
        api_response = api_instance.categories_id_reports_year_year_get(id, year)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling CategoriesApi->categories_id_reports_year_year_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Category ID |
 **year** | **int**| Category report year |

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

