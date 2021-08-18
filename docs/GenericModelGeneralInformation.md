# GenericModelGeneralInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name given to the model or data | 
**source** | **str** | A source from which the model/data is derived | [optional] 
**identifier** | **str** | An unambiguous ID given to the model or data. This can also be created automatically by a software tool | 
**author** | [**list[Contact]**](Contact.md) | Person(s) who generated the model code or generated the data set originally | [optional] 
**creator** | [**list[Contact]**](Contact.md) | The person(s) that created this FSK file including all metadata | [optional] 
**creation_date** | **date** | Creation date/time of the FSK file | 
**modification_date** | **list[date]** | Date/time of the last version of the FSK file | [optional] 
**rights** | **str** | Rights granted for usage, distribution and modification of this FSK file | 
**availability** | **str** | Availability of data or model, i.e. if the annotated model code / data is included in this FSK file | [optional] 
**url** | **str** | Web address referencing the resource location (data for example) | [optional] 
**format** | **str** | File extension of the model or data file (including version number of format if applicable) | [optional] 
**reference** | [**list[Reference]**](Reference.md) |  | 
**language** | **str** | A language of the resource (some data or reports can be available in French language for example) | [optional] 
**software** | **str** | The program or software language in which the model has been implemented | [optional] 
**language_written_in** | **str** | Software language used to write the model, e.g. R or MatLab | [optional] 
**model_category** | [**ModelCategory**](ModelCategory.md) |  | [optional] 
**status** | **str** | The curation status of the model | [optional] 
**objective** | **str** | Objective of the model or data | [optional] 
**description** | **str** | General description of the study, data or model | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

