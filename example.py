import time
import clarivate.wos_journals.client
from clarivate.wos_journals.client.api import journals_api
from clarivate.wos_journals.client.model.journal_list import JournalList
from pprint import pprint

# See configuration.py for a list of all supported configuration parameters.

configuration = clarivate.wos_journals.client.Configuration()
configuration.api_key['key'] = 'YOUR API KEY'

# Enter a context with an instance of the API client
with clarivate.wos_journals.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journals_api.JournalsApi(api_client)
    q = "cancer"  # str | Free-text search by journal name (e.g. *Nature Genetics*), JCR abbreviation (e.g. *NAT GENET*), publisher (e.g. *PUBLIC LIBRARY SCIENCE*) or [ISSN / eISSN code](https://www.issn.org/understanding-the-issn/what-is-an-issn/) (e.g. *1061-4036*)  The search logic is described in the section [Search](#search). (optional)
    edition = "SCIE"  # str | Filter by Web of Science Citation Index. The following indexes (editions) are presented: - SCIE - Science Citation Index Expanded - SSCI - Social Sciences Citation Index - AHCI - Arts & Humanities Citation Index - ESCI - Emerging Sources Citation Index  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    category_code = None  # str | Filter journals by category identifiers.  Each journal in JCR is assigned to at least one of the subject categories, indicating a general area of science or the social sciences. Journals may be included in more than one subject category.  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    jcr_year = 2020  # int | Filter by Journal Citation Report year (from 1997).  **NOTE:** The filter **jcrYear** is mandatory while using **jif**, **jifPercentile**, **jifQuartile**, and **jci** filters  Only one value is allowed. (optional)
    jif = "gte:0.0"  # str | Filter by [Journal Impact Factor](http://jcr.help.clarivate.com/Content/jcr3-glossary.htm) (JIF).  **NOTE:** The filter **jcrYear** is mandatory while using **jif** filter  Filter logic is described in the section [Filter by range](#range) (optional)
    jif_percentile = "gte:70 AND lte:90.0"  # str | Filter by [Journal Impact Factor Percentile](http://jcr.help.clarivate.com/Content/glossary-journal-impact-factor-percentile.htm), ranging from 0 to 100  **NOTE:** The filter **jcrYear** is mandatory while using **jifPercentile** filter  Filter logic is described in the section [Filter by range](#range) (optional)
    jif_quartile = "Q1"  # str | Filter by JIF quartile rank for a category, from highest to lowest based on their JIF value: <br />Q1 is represented by the top 25% of journals in the category; <br />Q2 is occupied by journals in the 25 to 50% group; <br />Q3 is occupied by journals in the 50 to 75% group; <br />Q4 is occupied by journals in the 75 to 100% group.  **NOTE:** The filter **jcrYear** is mandatory while using **jifQuartile** filter  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    jci = "gte:0"  # str | Filter by [Journal Citation Indicator](http://jcr.help.clarivate.com/Content/jcr3-glossary.htm) (JCI).  **NOTE:** The filter **jcrYear** is mandatory while using **jci** filter  Filter logic is described in the section [Filter by range](#range) (optional)
    jci_quartile = "Q1"  # str | Filter by JCI quartile rank for a category, from highest to lowest based on their JCI value: Q1 is represented by the top 25% of journals in the category; Q2 is occupied by journals in the 25 to 50% group; Q3 is occupied by journals in the 50 to 75% group; Q4 is occupied by journals in the 75 to 100% group.  **NOTE:** The filter **jcrYear** is mandatory while using **jciQuartile** filter  Multiple values are allowed, separated by a semicolon ( **;** ) (optional)
    jci_percentile = "gte:70.0 AND lte:90.0"  # str | Filter by Journal Citation Indicator (JCI) percentile, ranging from 0 to 100  **NOTE:** The filter **jcrYear** is mandatory while using **jciPercentile** filter  Filter logic is described in the section [Filter by range](#range) (optional)
    page = 1  # int | Specifying a page to retrieve (optional) if omitted the server will use the default value of 1
    limit = 10  # int | Number of returned results, ranging from 0 to 50 (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search and filter across JCR Journals

        api_response_all_journals = api_instance.journals_get()
        api_response_filtered = api_instance.journals_get(q=q, edition=edition, jcr_year=jcr_year,
                                                 jif=jif, jif_percentile=jif_percentile, jif_quartile=jif_quartile,
                                                 jci=jci, jci_quartile=jci_quartile, jci_percentile=jci_percentile,
                                                 page=page, limit=limit)
        pprint(api_response_all_journals)
        pprint(api_response_filtered)
    except clarivate.wos_journals.client.ApiException as e:
        print("Exception when calling JournalsApi->journals_get: %s\n" % e)
