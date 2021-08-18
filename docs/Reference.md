# Reference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_reference_description** | **bool** | Indicates whether this specific publication serves as the reference description for the model. There has to be at least one reference where this field is set to &#x27;True&#x27; | 
**publication_type** | **str** | The type of publication, e.g. Report, Journal article, Book, Online database, ... | [optional] 
**_date** | **date** | Temporal information on the publication date | [optional] 
**pmid** | **str** | The PubMed ID related to this publication | [optional] 
**doi** | **str** | The DOI related to this publication | 
**author_list** | **str** | Name and surname of the authors who contributed to this publication | [optional] 
**title** | **str** | Title of the publication in which the model or the data has been described | 
**abstract** | **str** | Abstract of the publication in which the model or the data has been described | [optional] 
**journal** | **str** | Data on the details of the journal in which the model or the data has been described | [optional] 
**volume** | **str** | Data on the details of the journal in which the model or the data has been described | [optional] 
**issue** | **str** | Data on the details of the journal in which the model or the data has been described | [optional] 
**status** | **str** | The status of this publication, e.g. Published, Submitted, etc. | [optional] 
**website** | **str** | A link to the publication website (different from DOI) | [optional] 
**comment** | **str** | Further comments related to the reference description, e.g. which section in there describes the specific model or which figure in there can be reproduced with the visualization script | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

