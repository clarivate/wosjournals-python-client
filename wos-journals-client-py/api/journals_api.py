"""
    Web of Science™ Journals API

    This API provides journal-level metadata and metrics for all journals in the Journal Citation Reports™ covered in the Web of Science Core Collection, including the Journal Impact Factor™ and other new metrics. Integrate journal data into your internal systems or retrieve journal indicators for bibliometrics studies.  ## Resources This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.  The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-journal). The access requires registration on the Portal and approval from the Clarivate Sales/Product teams to entitle to the API.  ## Credentials All requests require authentication with an API Key authentication flow. For more details, check the [Guide](https://developer.clarivate.com/help/api-access#key_access).   ## Content You can learn more about content at [Journal Citation Reports™ Product page](https://clarivate.com/webofsciencegroup/solutions/journal-citation-reports/), or in the [documentation](http://jcr.help.clarivate.com/Content/home.htm).  ## <a name=\"search\"></a> Search (query parameter `q=`) This API supports free-text search for a journal name, abbreviation, ISSN code, publisher, and Web of Science™ category name (only `/categories` endpoint). You need to provide a complete and valid ISSN code pattern; otherwise, the API will not look up for ISSN codes.  ### Boolean operators | Operator    | Description  | Example| |-----|-----|------------------| | + / \" \" | Search by two or more terms in the same field. Blank space is the same as an AND operator. The search retrieves all the records that contain the terms, e.g., | `/journals?q=matrix biology`<br> `/journals?q=nature+group` | | OR | Search by at least one term in the field. The search retrieves all the records that contain one of the terms, e.g., | `/journals?q=gas OR oil` | | NOT / - | Search by excluding specific terms. The search retrieves all the records that match the query specifics, e.g., | `/journals?q=genetics -nature` |  ### Special symbols The wildcards ( __*__ ) are allowed in the search that starts with the search query&#58; `/journals?q=nano*` will search indications that start from __nano__&#58; for example, _Nanotechnology_ or _nanotubes_.  Please note&#58; the free text search query (with the parameter `q=`) should contain at least three symbols.  ## Filtering The API supports several filters for Journals and Web of Science™ Categories, narrowing down the initial list of entities or search results.  There are two types of filters:  - Filter by one or multiple **values**: *edition*, *categoryCode*, *jcrYear*, *jifQuartile* - Filter by **range**: *jif*, *jifPercentile*  ### Filter by values The filter name goes before the equals sign, followed by one or multiple filter values, separated by a semicolon, like `categoryCode=RZ;RU`. You can combine various filters with or without the search. Filters are separated by an ampersand (**&amp;**): `q=nature&categoryCode=RU;KM&jcrYear=2018`  Please note&#58; filter by *jcrYear* allows only one year value as an input  ### <a name='range'></a> Filter by range The API supports range filtering for Journal Impact Factor (*jif*) or Journal Impact Factor Percentile (*jifPercentile*) with the following operators:  - ***eq*** (equal): if a Journal Impact Factor (Percentile) is equal to a specific number.<br /> For example: for `jif=eq:5.032` the result will include journals with Journal Impact Factor = 5.032.<br /> Not combinable with any other operator - ***gt*** (greater than): if a Journal Impact Factor (Percentile) is greater than a specific number.<br /> For example: for `jif=gt:5` the result will include journals with Journal Impact Factor = 5.001 and higher.<br /> Combinable with *lt* and *lte* operators - ***gte*** (greater than equal): if a Journal Impact Factor (Percentile) is greater than or equal to a specific number.<br /> For example: for `jif=gte:5` the result will include journals with Journal Impact Factor = 5.000 and higher.<br /> Combinable with *lt* and *lte* operators - ***lt*** (less than): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lt:5` the result will include journals with Journal Impact Factor = 4.999 and less.<br /> Combinable with *gt* and *gte* operators - ***gt*** (less than equal): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lte:5` the result will include journals with Journal Impact Factor = 5.000 and less.<br /> Combinable with *gt* and *gte* operators  Use `AND` to combine two operators, e.g.,`jifPercentile=gte:50 AND lte:80` responses with all journals in a percentile range from 50% to 80% (both included).  ## Pagination To ensure fast response time, each search or multiple entity calls (such as `/journals` or `/categories/ID/cited/year/YYYY`) retrieve only a certain number of hits/records.  There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.  - limit&#58; Number of returned results, ranging from 0 to 50 (default **10**) - page&#58; Specifying a page to retrieve (default **1**)  Moreover, this information is shown in the response body, in the tag **metadata**&#58;  ```json \"metadata\": {   \"total\": 91,   \"page\": 1,   \"limit\": 10 } ``` ## Errors The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.  | Code  | Title  | Description | |---|---|---| | 400  | Bad request  | Request syntax error | | 401  | Unauthorized  | The API key is invalid or missed | | 404  | Not found  | The resource is not found | | 405 | Method not allowed | Method other than GET is not allowed | | 50X  | Server errors  | Technical error with servers| Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:  ```json \"error\": {   \"status\": 404,   \"title\": \"Resource couldn't be found\",   \"details\": \"There is no information in WoS Journals API about the identifier ABC_DEF for the Journals content area. Sorry :(\" } ``` For the `401 Unauthorized` error the response body is a little bit different: ```json {   \"error_description\": \"The access token is missing\",   \"error\": \"invalid_request\" } ```  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from wos-journals-client-py.api_client import ApiClient, Endpoint as _Endpoint
from wos-journals-client-py.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from wos-journals-client-py.model.inline_response200 import InlineResponse200
from wos-journals-client-py.model.inline_response2001 import InlineResponse2001
from wos-journals-client-py.model.inline_response2002 import InlineResponse2002
from wos-journals-client-py.model.inline_response2003 import InlineResponse2003
from wos-journals-client-py.model.inline_response2004 import InlineResponse2004


class JournalsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __journals_get(
            self,
            **kwargs
        ):
            """Search and filter across JCR Journals  # noqa: E501

            The endpoint allows to search, filter, or browse across the Journals content.  The endpoint doesn't require any parameter to return results, although only main information for the first ten records sorted alphabetically will be retrieved.  To get comprehensive results, a set of parameters could be applied: - `q`: ISSN or title/publisher search - `edition`: filter by journal edition - `categoryCode`: filter by WoS journal category - `jcrYear`: filter by Journal Citation Report Year (since 1997) - `jif`: filter by Journal Impact Factor (JIF) - `jifPercentile`: filter by Journal Impact Factor Percentile (0-100) - `jifQuartile`: filter by Journal Impact Factor Rank Quartile - `limit`: set the limit of records on the page (1-50) - `page`: set the result page  By default, all the responses are sorted alphabetically, only in case of search the results will be sorted by relevance.  The response contains: - Main information about the number of records found, page and limit - Journals unique ID (based on JCR abbreviated title) - API Link to Journal record - Journal title - Search matches with the found phrase ***&lt;em&gt;*** *highlighted* ***&lt;/em&gt;*** - only if parameter `q` is requested - Category information (unique ID, category name, and edition) - only if the parameter `categoryCode` or `edition` is requested - Link to the Journal Citation Report - only if parameter `jcrYear` is requested - Metrics information (Impact metrics) - only if parameter `jif` is requested - Metrics information (Source metrics) - only if parameter `jifPercentile` is requested - Ranks information (JIF rank and quartile within the category) - only if parameter `jifQuartile` is requested  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.journals_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                q (str): Free-text search by journal name (e.g. *Nature Genetics*), JCR abbreviation (e.g. *NAT GENET*), publisher (e.g. *PUBLIC LIBRARY SCIENCE*) or [ISSN / eISSN code](https://www.issn.org/understanding-the-issn/what-is-an-issn/) (e.g. *1061-4036*)  The search logic is described in the section [Search](#search).. [optional]
                edition (str): Filter by Web of Science Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded (journals across more than 170 disciplines) - SSCI - Social Sciences Citation Index (journals across more than 50 social science disciplines)  Multiple values are allowed, separated by a semicolon ( **;** ). [optional]
                category_code (str): Filter journals by category identifiers.  Each journal in JCR is assigned to at least one of the subject categories, indicating a general area of science or the social sciences. Journals may be included in more than one subject category.  Multiple values are allowed, separated by a semicolon ( **;** ). [optional]
                jcr_year (int): Filter by Journal Citation Report year (from 1997).  **NOTE:** The filter **jcrYear** is mandatory while using **jif**, **jifPercentile**, and **jifQuartile** filters  Only one value is allowed.. [optional]
                jif (str): Filter by [Journal Impact Factor](http://jcr.help.clarivate.com/Content/glossary.htm#610062182_anchor28) (JIF).  **NOTE:** The filter **jcrYear** is mandatory while using **jif** filter  Filter logic is described in the section [Filter by range](#range). [optional]
                jif_percentile (str): Filter by [Journal Impact Factor Percentile](http://jcr.help.clarivate.com/Content/glossary-journal-impact-factor-percentile.htm), ranging from 0 to 100  **NOTE:** The filter **jcrYear** is mandatory while using **jifPercentile** filter  Filter logic is described in the section [Filter by range](#range). [optional]
                jif_quartile (str): Filter by journal impact factor quartile rank for a category, from highest to lowest based on their journal impact factor: <br />Q1 is represented by the top 25% of journals in the category; <br />Q2 is occupied by journals in the 25 to 50% group; <br />Q3 is occupied by journals in the 50 to 75% group; <br />Q4 is occupied by journals in the 75 to 100% group.  **NOTE:** The filter **jcrYear** is mandatory while using **jifQuartile** filter  Multiple values are allowed, separated by a semicolon ( **;** ). [optional]
                page (int): Specifying a page to retrieve. [optional] if omitted the server will use the default value of 1
                limit (int): Number of returned results, ranging from 0 to 50. [optional] if omitted the server will use the default value of 10
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse200
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.journals_get = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'key'
                ],
                'endpoint_path': '/journals',
                'operation_id': 'journals_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'q',
                    'edition',
                    'category_code',
                    'jcr_year',
                    'jif',
                    'jif_percentile',
                    'jif_quartile',
                    'page',
                    'limit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'edition',
                    'jif_quartile',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('edition',): {

                        "SCIE": "SCIE",
                        "SSCI": "SSCI"
                    },
                    ('jif_quartile',): {

                        "Q1": "Q1",
                        "Q2": "Q2",
                        "Q3": "Q3",
                        "Q4": "Q4"
                    },
                },
                'openapi_types': {
                    'q':
                        (str,),
                    'edition':
                        (str,),
                    'category_code':
                        (str,),
                    'jcr_year':
                        (int,),
                    'jif':
                        (str,),
                    'jif_percentile':
                        (str,),
                    'jif_quartile':
                        (str,),
                    'page':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'q': 'q',
                    'edition': 'edition',
                    'category_code': 'categoryCode',
                    'jcr_year': 'jcrYear',
                    'jif': 'jif',
                    'jif_percentile': 'jifPercentile',
                    'jif_quartile': 'jifQuartile',
                    'page': 'page',
                    'limit': 'limit',
                },
                'location_map': {
                    'q': 'query',
                    'edition': 'query',
                    'category_code': 'query',
                    'jcr_year': 'query',
                    'jif': 'query',
                    'jif_percentile': 'query',
                    'jif_quartile': 'query',
                    'page': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__journals_get
        )

        def __journals_id_cited_year_year_get(
            self,
            id,
            year,
            **kwargs
        ):
            """Get journals that cite the journal for the JCR year  # noqa: E501

            Cited Journal data show how many citations a journal received in the JCR year. Cited journal data is relevant when analyzing metrics such as the Journal Impact Factor and Market Share.  The response contains:  - Citing **Journal** with the link to WoS Journal API entity - **Cited Year (all)**:  The total number of citations from the citing journal. This total includes the number shown under each year and the number in the Rest column. - **Cited Year (10 years interval)**: Publication year of the cited articles. - **Cited Year (rest)**: All publication years of cited articles prior to the 10-year period defined by the table. For example, if the cited years shown are 2017-2008, the Rest column will show the number of citations from the citing journal in 2017 to articles published in the cited journal in 2007 and any earlier year.   Please see the detailed infomration in the [JCR Help page](http://jcr.help.clarivate.com/Content/cited-journal-data.htm)  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.journals_id_cited_year_year_get(id, year, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Journal unique identifier
                year (int): Journal Citation Report Year (from 1997)

            Keyword Args:
                page (int): Specifying a page to retrieve. [optional] if omitted the server will use the default value of 1
                limit (int): Number of returned results, ranging from 0 to 50. [optional] if omitted the server will use the default value of 10
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2003
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['year'] = \
                year
            return self.call_with_http_info(**kwargs)

        self.journals_id_cited_year_year_get = _Endpoint(
            settings={
                'response_type': (InlineResponse2003,),
                'auth': [
                    'key'
                ],
                'endpoint_path': '/journals/{id}/cited/year/{year}',
                'operation_id': 'journals_id_cited_year_year_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'year',
                    'page',
                    'limit',
                ],
                'required': [
                    'id',
                    'year',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'year':
                        (int,),
                    'page':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'year': 'year',
                    'page': 'page',
                    'limit': 'limit',
                },
                'location_map': {
                    'id': 'path',
                    'year': 'path',
                    'page': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__journals_id_cited_year_year_get
        )

        def __journals_id_citing_year_year_get(
            self,
            id,
            year,
            **kwargs
        ):
            """Get journals that were cited by the journal for the JCR year  # noqa: E501

            The response contains:  - Cited **Journal** with the link to WoS Journal API entity - **Cited Year (all)**:  The total number of citations to the cited journal. This total includes the number shown under each year and the number in the Rest column. - **Cited Year (10 years interval)**: Publication year of the cited articles. - **Cited Year (rest)**: All publication years of cited articles prior to the 10-year period defined by the table. For example, if the cited years shown are 2017-2008, the Rest column will show the number of citations from the citing journal in 2017 to articles published in the cited journal in 2007 and any earlier year.   Please see the detailed infomration in the [JCR Help page](http://jcr.help.clarivate.com/Content/citing-journal-data.htm)  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.journals_id_citing_year_year_get(id, year, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): An Journal ID
                year (int): A citing Year

            Keyword Args:
                page (int): Specifying a page to retrieve. [optional] if omitted the server will use the default value of 1
                limit (int): Number of returned results, ranging from 0 to 50. [optional] if omitted the server will use the default value of 10
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2004
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['year'] = \
                year
            return self.call_with_http_info(**kwargs)

        self.journals_id_citing_year_year_get = _Endpoint(
            settings={
                'response_type': (InlineResponse2004,),
                'auth': [
                    'key'
                ],
                'endpoint_path': '/journals/{id}/citing/year/{year}',
                'operation_id': 'journals_id_citing_year_year_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'year',
                    'page',
                    'limit',
                ],
                'required': [
                    'id',
                    'year',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'year':
                        (int,),
                    'page':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'year': 'year',
                    'page': 'page',
                    'limit': 'limit',
                },
                'location_map': {
                    'id': 'path',
                    'year': 'path',
                    'page': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__journals_id_citing_year_year_get
        )

        def __journals_id_get(
            self,
            id,
            **kwargs
        ):
            """Get journal by id  # noqa: E501

            A journal entity contains: - basic bibliographic information about the journal, including publisher, ISSN and e-ISSN (where available), open access status, language, frequency of publication, and Web of Science categorization. - links to the multi-year Journal Citation Report data, starting from 1997.  For more information about Journal inclusion in the index, please visit [this page](http://jcr.help.clarivate.com/Content/scope-notes.htm)  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.journals_id_get(id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Journal unique identifier  Currently an identifier is a JCR abbreviation, where blank spaces are substituted with underscores (e.g. *PLOS ONE* Journal has the ID **PLOS_ONE**)

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2001
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.journals_id_get = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [
                    'key'
                ],
                'endpoint_path': '/journals/{id}',
                'operation_id': 'journals_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__journals_id_get
        )

        def __journals_id_reports_year_year_get(
            self,
            id,
            year,
            **kwargs
        ):
            """Get journal metrics for a year  # noqa: E501

            This endpoint returns the information about Journal Citation Report by year.  The response contains: - Journal name and link to the Journal entry - Key indications (metrics): impact, source and influence - Journal Impact Factor and ESI citations ranks - Journal Source Data - Three-year content analysis by country/region and organization - Links to the related Cited/Citing reports  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.journals_id_reports_year_year_get(id, year, async_req=True)
            >>> result = thread.get()

            Args:
                id (str): Journal unique identifier  Currently an identifier is a JCR abbreviation, where blank spaces are substituted with underscores (e.g. *PLOS ONE* Journal has the ID **PLOS_ONE**)
                year (int): Journal Citation Report year (jcrYear)

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2002
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['id'] = \
                id
            kwargs['year'] = \
                year
            return self.call_with_http_info(**kwargs)

        self.journals_id_reports_year_year_get = _Endpoint(
            settings={
                'response_type': (InlineResponse2002,),
                'auth': [
                    'key'
                ],
                'endpoint_path': '/journals/{id}/reports/year/{year}',
                'operation_id': 'journals_id_reports_year_year_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'year',
                ],
                'required': [
                    'id',
                    'year',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                    'year':
                        (int,),
                },
                'attribute_map': {
                    'id': 'id',
                    'year': 'year',
                },
                'location_map': {
                    'id': 'path',
                    'year': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__journals_id_reports_year_year_get
        )
