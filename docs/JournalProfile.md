# JournalProfile

Journal Profile uses JCR year source data, and the two prior years to develop a picture of the countries, regions, and organizations that have published materials in this journal in the past three years.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_year** | **int** | First year of the profile | [optional] 
**end_year** | **int** | Last year of the profile (equal to the Report year) | [optional] 
**citable_items** | [**JournalProfileCitableItems**](JournalProfileCitableItems.md) |  | [optional] 
**citations** | [**JournalProfileCitations**](JournalProfileCitations.md) |  | [optional] 
**occurrence_countries** | [**[JournalProfileOccurrenceCountries]**](JournalProfileOccurrenceCountries.md) | Information about of the top 10 countries and regions that have published materials in this journal in the past three years. | [optional] 
**occurrence_organizations** | [**[JournalProfileOccurrenceOrganizations]**](JournalProfileOccurrenceOrganizations.md) | Information about of the top 10 organizations that have published materials in this journal in the past three years. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


