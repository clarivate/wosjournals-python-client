# Web of Science Journals API Python client
This API provides journal-level metadata and metrics for all journals in the Journal Citation Reports™ covered in the Web of Science Core Collection, including the Journal Impact Factor™ and other new metrics. Integrate journal data into your internal systems or retrieve journal indicators for bibliometrics studies.

## Resources
This API follows the REST approach to disclose resources in URL format. Only the GET method is currently available to perform requests over HTTP.

The API is available on the [Clarivate Developer Portal](https://developer.clarivate.com/apis/wos-journal). The access requires registration on the Portal and approval from the Clarivate Sales/Product teams to entitle to the API.

## Credentials
All requests require authentication with an API Key authentication flow. For more details, check the [Guide](https://developer.clarivate.com/help/api-access#key_access).

## API Client Libraries
The current languages/frameworks are supported: [Python](https://github.com/clarivate/wosjournals-python-client) | [Java](https://github.com/clarivate/wosjournals-java-client) | [Javascript](https://github.com/clarivate/wosjournals-javascript-client)

## Content
You can learn more about content at [Journal Citation Reports™ Product page](https://clarivate.com/webofsciencegroup/solutions/journal-citation-reports/), or in the [documentation](http://jcr.help.clarivate.com/Content/home.htm).

## <a name=\"search\"></a> Search (query parameter `q=`)
This API supports free-text search for a journal name, abbreviation, ISSN code, publisher, and Web of Science™ category name (only `/categories` endpoint). You need to provide a complete and valid ISSN code pattern; otherwise, the API will not look up for ISSN codes.

### Boolean operators
| Operator    | Description  | Example|
|-----|-----|------------------|
| + / \" \" | Search by two or more terms in the same field. Blank space is the same as an AND operator. The search retrieves all the records that contain the terms, e.g., | `/journals?q=matrix biology`<br> `/journals?q=nature+group` |
| OR | Search by at least one term in the field. The search retrieves all the records that contain one of the terms, e.g., | `/journals?q=gas OR oil` |
| NOT / - | Search by excluding specific terms. The search retrieves all the records that match the query specifics, e.g., | `/journals?q=genetics -nature` |

### Special symbols
The wildcards ( __*__ ) are allowed in the search that starts with the search query&#58; `/journals?q=nano*` will search indications that start from __nano__&#58; for example, _Nanotechnology_ or _nanotubes_.

Please note&#58; the free text search query (with the parameter `q=`) should contain at least three symbols.

## Filtering
The API supports several filters for Journals and Web of Science™ Categories, narrowing down the initial list of entities or search results.

There are two types of filters:

- Filter by one or multiple **values**: *edition*, *categoryCode*, *jcrYear*, *jifQuartile*
- Filter by **range**: *jif*, *jifPercentile*, *jci*, 

### Filter by values
The filter name goes before the equals sign, followed by one or multiple filter values, separated by a semicolon, like `categoryCode=RZ;RU`. You can combine various filters with or without the search. Filters are separated by an ampersand (**&amp;**): `q=nature&categoryCode=RU;KM&jcrYear=2018`

Please note&#58; filter by *jcrYear* allows only one year value as an input

### <a name='range'></a> Filter by range
The API supports range filtering for Journal Impact Factor (*jif*) or Journal Impact Factor Percentile (*jifPercentile*) with the following operators:

- ***eq*** (equal): if a Journal Impact Factor (Percentile) is equal to a specific number.<br /> For example: for `jif=eq:5.032` the result will include journals with Journal Impact Factor = 5.032.<br /> Not combinable with any other operator
- ***gt*** (greater than): if a Journal Impact Factor (Percentile) is greater than a specific number.<br /> For example: for `jif=gt:5` the result will include journals with Journal Impact Factor = 5.001 and higher.<br /> Combinable with *lt* and *lte* operators
- ***gte*** (greater than equal): if a Journal Impact Factor (Percentile) is greater than or equal to a specific number.<br /> For example: for `jif=gte:5` the result will include journals with Journal Impact Factor = 5.000 and higher.<br /> Combinable with *lt* and *lte* operators
- ***lt*** (less than): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lt:5` the result will include journals with Journal Impact Factor = 4.999 and less.<br /> Combinable with *gt* and *gte* operators
- ***lte*** (less than equal): if a Journal Impact Factor (Percentile) is less than a specific number.<br /> For example: for `jif=lte:5` the result will include journals with Journal Impact Factor = 5.000 and less.<br /> Combinable with *gt* and *gte* operators

Use `AND` to combine two operators, e.g.,`jifPercentile=gte:50 AND lte:80` responses with all journals in a percentile range from 50% to 80% (both included).

## Pagination
To ensure fast response time, each search or multiple entity calls (such as `/journals` or `/categories/ID/cited/year/YYYY`) retrieve only a certain number of hits/records.

There are two optional request parameters to browse along with the result&#58; _limit_ and _page_.

- limit&#58; Number of returned results, ranging from 0 to 50 (default **10**)
- page&#58; Specifying a page to retrieve (default **1**)

Moreover, this information is shown in the response body, in the tag **metadata**&#58;

```json
\"metadata\": {
  \"total\": 91,
  \"page\": 1,
  \"limit\": 10
}
```
## Errors
The WoS Journals API uses conventional HTTP success or failure status codes. For errors, some extra information is included to indicate what went wrong in the JSON response. The list of HTTP codes is listed below.

| Code  | Title  | Description |
|---|---|---|
| 400  | Bad request  | Request syntax error |
| 401  | Unauthorized  | The API key is invalid or missed |
| 404  | Not found  | The resource is not found |
| 405 | Method not allowed | Method other than GET is not allowed |
| 50X  | Server errors  | Technical error with servers|
Each error response (except `401 Unauthorized` error) contains the code of the error, the title of the error and detailed description of the error: a misprint in an endpoint, wrong URL parameter, etc. The example of the error message is shown below:

```json
\"error\": {
  \"status\": 404,
  \"title\": \"Resource couldn't be found\",
  \"details\": \"There is no information in WoS Journals API about the identifier ABC_DEF for the Journals content area. Sorry :(\"
}
```
For the `401 Unauthorized` error the response body is a little bit different:
```json
{
  \"error_description\": \"The access token is missing\",
  \"error\": \"invalid_request\"
}
```

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import clarivate.wos_journals.client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clarivate.wos_journals.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import clarivate.wos_journals.client
from pprint import pprint
from clarivate.wos_journals.client.api import categories_api
from clarivate.wos_journals.client.model.categories_cited import CategoriesCited
from clarivate.wos_journals.client.model.categories_citing import CategoriesCiting
from clarivate.wos_journals.client.model.category_list import CategoryList
from clarivate.wos_journals.client.model.category_record import CategoryRecord
from clarivate.wos_journals.client.model.category_reports import CategoryReports
# Defining the host is optional and defaults to http://wos-journals-snapshot.cortellis.int.clarivate.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clarivate.wos_journals.client.Configuration(
    host = "http://wos-journals-snapshot.cortellis.int.clarivate.com"
)



# Enter a context with an instance of the API client
with clarivate.wos_journals.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = categories_api.CategoriesApi(api_client)
    q = "q_example" # str | Free-text search by category name.  Search logic is described in the section [Search](#search). (optional)
edition = "edition_example" # str | Filter by Web of Sceince Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded (ournals across more than 170 disciplines) - SSCI - Social Sciences Citation Index (journals across more than 50 social science disciplines)  Multiple values are allowed, separated by semicolon ( **;** ) (optional)
jcr_year = 1 # int | Filter by Category Citation Report year (from 2003).  Only one value is allowed. (optional)
page = 1 # int | Specifying a page to retrieve (optional) (default to 1)
limit = 10 # int | Number of returned results, ranging from 0 to 50 (optional) (default to 10)

    try:
        # Search and filter across the journal categories
        api_response = api_instance.categories_get(q=q, edition=edition, jcr_year=jcr_year, page=page, limit=limit)
        pprint(api_response)
    except clarivate.wos_journals.client.ApiException as e:
        print("Exception when calling CategoriesApi->categories_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://wos-journals-snapshot.cortellis.int.clarivate.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CategoriesApi* | [**categories_get**](docs/CategoriesApi.md#categories_get) | **GET** /categories | Search and filter across the journal categories
*CategoriesApi* | [**categories_id_cited_year_year_get**](docs/CategoriesApi.md#categories_id_cited_year_year_get) | **GET** /categories/{id}/cited/year/{year} | Get journals that cite all journals in the category for the JCR year
*CategoriesApi* | [**categories_id_citing_year_year_get**](docs/CategoriesApi.md#categories_id_citing_year_year_get) | **GET** /categories/{id}/citing/year/{year} | Get journals that were cited by all journals from the category for the JCR year
*CategoriesApi* | [**categories_id_get**](docs/CategoriesApi.md#categories_id_get) | **GET** /categories/{id} | Get a category
*CategoriesApi* | [**categories_id_reports_year_year_get**](docs/CategoriesApi.md#categories_id_reports_year_year_get) | **GET** /categories/{id}/reports/year/{year} | Get category metrics for a year
*JournalsApi* | [**journals_get**](docs/JournalsApi.md#journals_get) | **GET** /journals | Search and filter across JCR Journals
*JournalsApi* | [**journals_id_cited_year_year_get**](docs/JournalsApi.md#journals_id_cited_year_year_get) | **GET** /journals/{id}/cited/year/{year} | Get journals that cite the journal for the JCR year
*JournalsApi* | [**journals_id_citing_year_year_get**](docs/JournalsApi.md#journals_id_citing_year_year_get) | **GET** /journals/{id}/citing/year/{year} | Get journals that were cited by the journal for the JCR year
*JournalsApi* | [**journals_id_get**](docs/JournalsApi.md#journals_id_get) | **GET** /journals/{id} | Get journal by id
*JournalsApi* | [**journals_id_history_get**](docs/JournalsApi.md#journals_id_history_get) | **GET** /journals/{id}/history | Get journal history by id
*JournalsApi* | [**journals_id_reports_year_year_get**](docs/JournalsApi.md#journals_id_reports_year_year_get) | **GET** /journals/{id}/reports/year/{year} | Get journal metrics for a year


## Documentation For Models

 - [Categories](docs/Categories.md)
 - [CategoriesCited](docs/CategoriesCited.md)
 - [CategoriesCitedHits](docs/CategoriesCitedHits.md)
 - [CategoriesCitedJournal](docs/CategoriesCitedJournal.md)
 - [CategoriesCiting](docs/CategoriesCiting.md)
 - [CategoriesCitingHits](docs/CategoriesCitingHits.md)
 - [CategoriesCitingJournal](docs/CategoriesCitingJournal.md)
 - [CategoryCitationReports](docs/CategoryCitationReports.md)
 - [CategoryData](docs/CategoryData.md)
 - [CategoryList](docs/CategoryList.md)
 - [CategoryListRecord](docs/CategoryListRecord.md)
 - [CategoryRecord](docs/CategoryRecord.md)
 - [CategoryReports](docs/CategoryReports.md)
 - [CategoryReportsJournals](docs/CategoryReportsJournals.md)
 - [CategoryReportsSourceData](docs/CategoryReportsSourceData.md)
 - [CategoryReportsSourceDataArticles](docs/CategoryReportsSourceDataArticles.md)
 - [CategoryReportsSourceDataReviews](docs/CategoryReportsSourceDataReviews.md)
 - [CitedData](docs/CitedData.md)
 - [Cites](docs/Cites.md)
 - [CitingData](docs/CitingData.md)
 - [Frequency](docs/Frequency.md)
 - [HalfLife](docs/HalfLife.md)
 - [Immediacy](docs/Immediacy.md)
 - [ImpactMetrics](docs/ImpactMetrics.md)
 - [InfluenceMetrics](docs/InfluenceMetrics.md)
 - [InfluenceMetricsEigenFactor](docs/InfluenceMetricsEigenFactor.md)
 - [Jif](docs/Jif.md)
 - [JifAggregate](docs/JifAggregate.md)
 - [JournalCitationReport](docs/JournalCitationReport.md)
 - [JournalData](docs/JournalData.md)
 - [JournalHistoryRecord](docs/JournalHistoryRecord.md)
 - [JournalHistoryRecordIsoTitle](docs/JournalHistoryRecordIsoTitle.md)
 - [JournalHistoryRecordIssn](docs/JournalHistoryRecordIssn.md)
 - [JournalHistoryRecordName](docs/JournalHistoryRecordName.md)
 - [JournalHistoryRecordPublisher](docs/JournalHistoryRecordPublisher.md)
 - [JournalHistoryRecordPublisher1](docs/JournalHistoryRecordPublisher1.md)
 - [JournalHistoryRecordYear](docs/JournalHistoryRecordYear.md)
 - [JournalHistoryRecordYear1](docs/JournalHistoryRecordYear1.md)
 - [JournalHistoryRecordYear2](docs/JournalHistoryRecordYear2.md)
 - [JournalHistoryRecordYear3](docs/JournalHistoryRecordYear3.md)
 - [JournalList](docs/JournalList.md)
 - [JournalListRecord](docs/JournalListRecord.md)
 - [JournalListRecordJournalCitationReports](docs/JournalListRecordJournalCitationReports.md)
 - [JournalListRecordMetrics](docs/JournalListRecordMetrics.md)
 - [JournalListRecordMetricsImpactMetrics](docs/JournalListRecordMetricsImpactMetrics.md)
 - [JournalListRecordMetricsSourceMetrics](docs/JournalListRecordMetricsSourceMetrics.md)
 - [JournalListRecordRanks](docs/JournalListRecordRanks.md)
 - [JournalListRecordRanksJci](docs/JournalListRecordRanksJci.md)
 - [JournalListRecordRanksJif](docs/JournalListRecordRanksJif.md)
 - [JournalProfile](docs/JournalProfile.md)
 - [JournalProfileCitableItems](docs/JournalProfileCitableItems.md)
 - [JournalProfileCitations](docs/JournalProfileCitations.md)
 - [JournalProfileOccurrenceCountries](docs/JournalProfileOccurrenceCountries.md)
 - [JournalProfileOccurrenceOrganizations](docs/JournalProfileOccurrenceOrganizations.md)
 - [JournalRecord](docs/JournalRecord.md)
 - [JournalReports](docs/JournalReports.md)
 - [JournalReportsJournal](docs/JournalReportsJournal.md)
 - [JournalReportsMetrics](docs/JournalReportsMetrics.md)
 - [JournalsCited](docs/JournalsCited.md)
 - [JournalsCitedHits](docs/JournalsCitedHits.md)
 - [JournalsCitesJournal](docs/JournalsCitesJournal.md)
 - [JournalsCiting](docs/JournalsCiting.md)
 - [JournalsCitingHits](docs/JournalsCitingHits.md)
 - [Metadata](docs/Metadata.md)
 - [OpenAccess](docs/OpenAccess.md)
 - [Publisher](docs/Publisher.md)
 - [RankQuartileData](docs/RankQuartileData.md)
 - [Ranks](docs/Ranks.md)
 - [RanksEsiCitations](docs/RanksEsiCitations.md)
 - [RanksJif](docs/RanksJif.md)
 - [SearchMatch](docs/SearchMatch.md)
 - [SourceData](docs/SourceData.md)
 - [SourceDataArticles](docs/SourceDataArticles.md)
 - [SourceMetrics](docs/SourceMetrics.md)
 - [SourceMetricsCitableItems](docs/SourceMetricsCitableItems.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in clarivate.wos_journals.client.apis and clarivate.wos_journals.client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from clarivate.wos_journals.client.api.default_api import DefaultApi`
- `from clarivate.wos_journals.client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import clarivate.wos_journals.client
from clarivate.wos_journals.client.apis import *
from clarivate.wos_journals.client.models import *
```

