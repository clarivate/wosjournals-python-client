# JournalListRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Journal unique identifier | [optional] 
**self** | **str** | Link to the journal entity | [optional] 
**matches** | [**[SearchMatch]**](SearchMatch.md) |  | [optional] 
**name** | **str** | Journal full name | [optional] 
**categories** | [**Categories**](Categories.md) |  | [optional] 
**journal_citation_reports** | [**[JournalListRecordJournalCitationReports]**](JournalListRecordJournalCitationReports.md) | Journal citation report link (only if the filter \&quot;jcrYear\&quot; was selected) | [optional] 
**metrics** | [**JournalListRecordMetrics**](JournalListRecordMetrics.md) |  | [optional] 
**ranks** | [**JournalListRecordRanks**](JournalListRecordRanks.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


