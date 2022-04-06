# JournalRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Journal unique identifier | [optional] 
**name** | **str** | Journal title | [optional] 
**jcr_title** | **str** | Journal JCR abbreviation | [optional] 
**iso_title** | **str** | Journal title in [ISO format](https://www.issn.org/services/online-services/access-to-the-ltwa/) | [optional] 
**issn** | **str** | Current [ISSN identifier](https://www.issn.org/understanding-the-issn/what-is-an-issn/) | [optional] 
**previous_issn** | **[str]** | Previously assignled ISSN identifiers | [optional] 
**e_issn** | **str** | (For online journals) [Electronic ISSN](https://www.issn.org/understanding-the-issn/assignment-rules/the-issn-for-electronic-media/) identifier | [optional] 
**publisher** | [**Publisher**](Publisher.md) |  | [optional] 
**frequency** | **int** | Number of times per year the journal is published | [optional] 
**first_issue_year** | **int** | First year the journal was published | [optional] 
**language** | **str** | Journal publication language | [optional] 
**open_access** | [**OpenAccess**](OpenAccess.md) |  | [optional] 
**categories** | [**Categories**](Categories.md) |  | [optional] 
**journal_citation_reports** | [**JournalCitationReport**](JournalCitationReport.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


