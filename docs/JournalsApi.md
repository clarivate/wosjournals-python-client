# wos-journals-client-py.JournalsApi

All URIs are relative to *https://api.clarivate.com/apis/wos-journals/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journals_get**](JournalsApi.md#journals_get) | **GET** /journals | Search and filter across JCR Journals
[**journals_id_cited_year_year_get**](JournalsApi.md#journals_id_cited_year_year_get) | **GET** /journals/{id}/cited/year/{year} | Get journals that cite the journal for the JCR year
[**journals_id_citing_year_year_get**](JournalsApi.md#journals_id_citing_year_year_get) | **GET** /journals/{id}/citing/year/{year} | Get journals that were cited by the journal for the JCR year
[**journals_id_get**](JournalsApi.md#journals_id_get) | **GET** /journals/{id} | Get journal by id
[**journals_id_reports_year_year_get**](JournalsApi.md#journals_id_reports_year_year_get) | **GET** /journals/{id}/reports/year/{year} | Get journal metrics for a year


# **journals_get**
> InlineResponse200 journals_get()

Search and filter across JCR Journals

The endpoint allows to search, filter, or browse across the Journals content.  The endpoint doesn't require any parameter to return results, although only main information for the first ten records sorted alphabetically will be retrieved.  To get comprehensive results, a set of parameters could be applied: - `q`: ISSN or title/publisher search - `edition`: filter by journal edition - `categoryCode`: filter by WoS journal category - `jcrYear`: filter by Journal Citation Report Year (since 1997) - `jif`: filter by Journal Impact Factor (JIF) - `jifPercentile`: filter by Journal Impact Factor Percentile (0-100) - `jifQuartile`: filter by Journal Impact Factor Rank Quartile - `limit`: set the limit of records on the page (1-50) - `page`: set the result page  By default, all the responses are sorted alphabetically, only in case of search the results will be sorted by relevance.  The response contains: - Main information about the number of records found, page and limit - Journals unique ID (based on JCR abbreviated title) - API Link to Journal record - Journal title - Search matches with the found phrase ***&lt;em&gt;*** *highlighted* ***&lt;/em&gt;*** - only if parameter `q` is requested - Category information (unique ID, category name, and edition) - only if the parameter `categoryCode` or `edition` is requested - Link to the Journal Citation Report - only if parameter `jcrYear` is requested - Metrics information (Impact metrics) - only if parameter `jif` is requested - Metrics information (Source metrics) - only if parameter `jifPercentile` is requested - Ranks information (JIF rank and quartile within the category) - only if parameter `jifQuartile` is requested

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import journals_api
from wos-journals-client-py.model.inline_response200 import InlineResponse200
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
    api_instance = journals_api.JournalsApi(api_client)
    q = "0945-053X" # str | Free-text search by journal name (e.g. *Nature Genetics*), JCR abbreviation (e.g. *NAT GENET*), publisher (e.g. *PUBLIC LIBRARY SCIENCE*) or [ISSN / eISSN code](https://www.issn.org/understanding-the-issn/what-is-an-issn/) (e.g. *1061-4036*)  The search logic is described in the section [Search](#search). (optional)
    edition = "SCIE" # str | Filter by Web of Science Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded (journals across more than 170 disciplines) - SSCI - Social Sciences Citation Index (journals across more than 50 social science disciplines)  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    category_code = "IP" # str | Filter journals by category identifiers.  Each journal in JCR is assigned to at least one of the subject categories, indicating a general area of science or the social sciences. Journals may be included in more than one subject category.  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    jcr_year = 2019 # int | Filter by Journal Citation Report year (from 1997).  **NOTE:** The filter **jcrYear** is mandatory while using **jif**, **jifPercentile**, and **jifQuartile** filters  Only one value is allowed. (optional)
    jif = "gte:5.0" # str | Filter by [Journal Impact Factor](http://jcr.help.clarivate.com/Content/glossary.htm#610062182_anchor28) (JIF).  **NOTE:** The filter **jcrYear** is mandatory while using **jif** filter  Filter logic is described in the section [Filter by range](#range) (optional)
    jif_percentile = "gte:70.0 AND lte:90.0" # str | Filter by [Journal Impact Factor Percentile](http://jcr.help.clarivate.com/Content/glossary-journal-impact-factor-percentile.htm), ranging from 0 to 100  **NOTE:** The filter **jcrYear** is mandatory while using **jifPercentile** filter  Filter logic is described in the section [Filter by range](#range) (optional)
    jif_quartile = "Q1" # str | Filter by journal impact factor quartile rank for a category, from highest to lowest based on their journal impact factor: <br />Q1 is represented by the top 25% of journals in the category; <br />Q2 is occupied by journals in the 25 to 50% group; <br />Q3 is occupied by journals in the 50 to 75% group; <br />Q4 is occupied by journals in the 75 to 100% group.  **NOTE:** The filter **jcrYear** is mandatory while using **jifQuartile** filter  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    page = 1 # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search and filter across JCR Journals
        api_response = api_instance.journals_get(q=q, edition=edition, category_code=category_code, jcr_year=jcr_year, jif=jif, jif_percentile=jif_percentile, jif_quartile=jif_quartile, page=page, limit=limit)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Free-text search by journal name (e.g. *Nature Genetics*), JCR abbreviation (e.g. *NAT GENET*), publisher (e.g. *PUBLIC LIBRARY SCIENCE*) or [ISSN / eISSN code](https://www.issn.org/understanding-the-issn/what-is-an-issn/) (e.g. *1061-4036*)  The search logic is described in the section [Search](#search). | [optional]
 **edition** | **str**| Filter by Web of Science Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded (journals across more than 170 disciplines) - SSCI - Social Sciences Citation Index (journals across more than 50 social science disciplines)  Multiple values are allowed, separated by a semicolon ( **;** ) | [optional]
 **category_code** | **str**| Filter journals by category identifiers.  Each journal in JCR is assigned to at least one of the subject categories, indicating a general area of science or the social sciences. Journals may be included in more than one subject category.  Multiple values are allowed, separated by a semicolon ( **;** ) | [optional]
 **jcr_year** | **int**| Filter by Journal Citation Report year (from 1997).  **NOTE:** The filter **jcrYear** is mandatory while using **jif**, **jifPercentile**, and **jifQuartile** filters  Only one value is allowed. | [optional]
 **jif** | **str**| Filter by [Journal Impact Factor](http://jcr.help.clarivate.com/Content/glossary.htm#610062182_anchor28) (JIF).  **NOTE:** The filter **jcrYear** is mandatory while using **jif** filter  Filter logic is described in the section [Filter by range](#range) | [optional]
 **jif_percentile** | **str**| Filter by [Journal Impact Factor Percentile](http://jcr.help.clarivate.com/Content/glossary-journal-impact-factor-percentile.htm), ranging from 0 to 100  **NOTE:** The filter **jcrYear** is mandatory while using **jifPercentile** filter  Filter logic is described in the section [Filter by range](#range) | [optional]
 **jif_quartile** | **str**| Filter by journal impact factor quartile rank for a category, from highest to lowest based on their journal impact factor: &lt;br /&gt;Q1 is represented by the top 25% of journals in the category; &lt;br /&gt;Q2 is occupied by journals in the 25 to 50% group; &lt;br /&gt;Q3 is occupied by journals in the 50 to 75% group; &lt;br /&gt;Q4 is occupied by journals in the 75 to 100% group.  **NOTE:** The filter **jcrYear** is mandatory while using **jifQuartile** filter  Multiple values are allowed, separated by a semicolon ( **;** ) | [optional]
 **page** | **int**| Specifying a page to retrieve | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Number of returned results, ranging from 0 to 50 | [optional] if omitted the server will use the default value of 10

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Journal list is sorted alphabetically when retrieving without or with fitlers only, and by relevance when searching. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journals_id_cited_year_year_get**
> InlineResponse2003 journals_id_cited_year_year_get(id, year)

Get journals that cite the journal for the JCR year

Cited Journal data show how many citations a journal received in the JCR year. Cited journal data is relevant when analyzing metrics such as the Journal Impact Factor and Market Share.  The response contains:  - Citing **Journal** with the link to WoS Journal API entity - **Cited Year (all)**:  The total number of citations from the citing journal. This total includes the number shown under each year and the number in the Rest column. - **Cited Year (10 years interval)**: Publication year of the cited articles. - **Cited Year (rest)**: All publication years of cited articles prior to the 10-year period defined by the table. For example, if the cited years shown are 2017-2008, the Rest column will show the number of citations from the citing journal in 2017 to articles published in the cited journal in 2007 and any earlier year.   Please see the detailed infomration in the [JCR Help page](http://jcr.help.clarivate.com/Content/cited-journal-data.htm)

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import journals_api
from wos-journals-client-py.model.inline_response2003 import InlineResponse2003
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
    api_instance = journals_api.JournalsApi(api_client)
    id = "PLOS_ONE" # str | Journal unique identifier
    year = 2017 # int | Journal Citation Report Year (from 1997)
    page = 1 # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get journals that cite the journal for the JCR year
        api_response = api_instance.journals_id_cited_year_year_get(id, year)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_cited_year_year_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get journals that cite the journal for the JCR year
        api_response = api_instance.journals_id_cited_year_year_get(id, year, page=page, limit=limit)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_cited_year_year_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Journal unique identifier |
 **year** | **int**| Journal Citation Report Year (from 1997) |
 **page** | **int**| Specifying a page to retrieve | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Number of returned results, ranging from 0 to 50 | [optional] if omitted the server will use the default value of 10

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Citing journals are sorted in descending order. At the top is the journal with the largest number of citations to the cited journal. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journals_id_citing_year_year_get**
> InlineResponse2004 journals_id_citing_year_year_get(id, year)

Get journals that were cited by the journal for the JCR year

The response contains:  - Cited **Journal** with the link to WoS Journal API entity - **Cited Year (all)**:  The total number of citations to the cited journal. This total includes the number shown under each year and the number in the Rest column. - **Cited Year (10 years interval)**: Publication year of the cited articles. - **Cited Year (rest)**: All publication years of cited articles prior to the 10-year period defined by the table. For example, if the cited years shown are 2017-2008, the Rest column will show the number of citations from the citing journal in 2017 to articles published in the cited journal in 2007 and any earlier year.   Please see the detailed infomration in the [JCR Help page](http://jcr.help.clarivate.com/Content/citing-journal-data.htm)

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import journals_api
from wos-journals-client-py.model.inline_response2004 import InlineResponse2004
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
    api_instance = journals_api.JournalsApi(api_client)
    id = "PLOS_ONE" # str | An Journal ID
    year = 2017 # int | A citing Year
    page = 1 # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # Get journals that were cited by the journal for the JCR year
        api_response = api_instance.journals_id_citing_year_year_get(id, year)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_citing_year_year_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get journals that were cited by the journal for the JCR year
        api_response = api_instance.journals_id_citing_year_year_get(id, year, page=page, limit=limit)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_citing_year_year_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An Journal ID |
 **year** | **int**| A citing Year |
 **page** | **int**| Specifying a page to retrieve | [optional] if omitted the server will use the default value of 1
 **limit** | **int**| Number of returned results, ranging from 0 to 50 | [optional] if omitted the server will use the default value of 10

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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

# **journals_id_get**
> InlineResponse2001 journals_id_get(id)

Get journal by id

A journal entity contains: - basic bibliographic information about the journal, including publisher, ISSN and e-ISSN (where available), open access status, language, frequency of publication, and Web of Science categorization. - links to the multi-year Journal Citation Report data, starting from 1997.  For more information about Journal inclusion in the index, please visit [this page](http://jcr.help.clarivate.com/Content/scope-notes.htm)

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import journals_api
from wos-journals-client-py.model.inline_response2001 import InlineResponse2001
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
    api_instance = journals_api.JournalsApi(api_client)
    id = "PLOS_ONE" # str | Journal unique identifier  Currently an identifier is a JCR abbreviation, where blank spaces are substituted with underscores (e.g. *PLOS ONE* Journal has the ID **PLOS_ONE**)

    # example passing only required values which don't have defaults set
    try:
        # Get journal by id
        api_response = api_instance.journals_id_get(id)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Journal unique identifier  Currently an identifier is a JCR abbreviation, where blank spaces are substituted with underscores (e.g. *PLOS ONE* Journal has the ID **PLOS_ONE**) |

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

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

# **journals_id_reports_year_year_get**
> InlineResponse2002 journals_id_reports_year_year_get(id, year)

Get journal metrics for a year

This endpoint returns the information about Journal Citation Report by year.  The response contains: - Journal name and link to the Journal entry - Key indications (metrics): impact, source and influence - Journal Impact Factor and ESI citations ranks - Journal Source Data - Three-year content analysis by country/region and organization - Links to the related Cited/Citing reports

### Example

* Api Key Authentication (key):
```python
import time
import wos-journals-client-py
from wos-journals-client-py.api import journals_api
from wos-journals-client-py.model.inline_response2002 import InlineResponse2002
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
    api_instance = journals_api.JournalsApi(api_client)
    id = "PLOS_ONE" # str | Journal unique identifier  Currently an identifier is a JCR abbreviation, where blank spaces are substituted with underscores (e.g. *PLOS ONE* Journal has the ID **PLOS_ONE**)
    year = 2017 # int | Journal Citation Report year (jcrYear)

    # example passing only required values which don't have defaults set
    try:
        # Get journal metrics for a year
        api_response = api_instance.journals_id_reports_year_year_get(id, year)
        pprint(api_response)
    except wos-journals-client-py.ApiException as e:
        print("Exception when calling JournalsApi->journals_id_reports_year_year_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Journal unique identifier  Currently an identifier is a JCR abbreviation, where blank spaces are substituted with underscores (e.g. *PLOS ONE* Journal has the ID **PLOS_ONE**) |
 **year** | **int**| Journal Citation Report year (jcrYear) |

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

