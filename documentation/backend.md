# Stebbins backend architecture overview

## Updates
An updates table will store updates made by admins with a time stamp. A client can check for updates by making a request containing the date of the last update received. The response to this request will be a JSON object listing updated elements ids. The client will then perform GET requets for the updated data.

## Guide Elements
Guide elements are composite pieces of data with fields common name, latin name, images, description. All of the text based data is stored in a table called Guide Element Text and all of the image paths are stored in a table called Guide Element Image.

Guide Element Text:
- element: Foreign Key Guide Element ID
- common name: Text !Nullable
- latin name: Text Nullable
- description: Text !Nullable

Guide Element Image:
- element: Foreign Key Guide Element ID
- path: Text !Nullable

Guide Element:
- Screen: Text Primary Key
- ID: UUID/INT

### Request Example
`GET https://url.com/endpoint/guide_elements?screen="mammals"&format="bytes"&id=""&updated_since=""`

### Response Example
Responses that contain binary image data will use the
Multipart-Form-Data format, ones that do not will use plain json and image urls will be transmitted instead.

```
{
    "total": 13,
    "items": [
        {
            "id": "id",
            "common name": "common name",
            "latin name": "latin name",
            "description": "description",
            "images": [
                {
                    "id": "id",
                    "encoding": "bytes",
                    "type": "jpeg",
                    bytes...
                },
                ...
            ]

        },
        ...
    ]
}
```
