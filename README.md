## pymongo_crud_use

### MongoDB Function Usage Guide

This guide explains the usage of each function provided in the MongoDB function module.

## 1. `initialize_collection(uri, db_name, collection_name)`

Initialize and return the MongoDB collection.

Parameters:

- `uri`: MongoDB connection URI.
- `db_name`: Name of the MongoDB database.
- `collection_name`: Name of the MongoDB collection.

Returns:

- MongoDB collection object.

## 2. `initialize_collection_with_certificate(uri, certificate_path, db_name, collection_name)`

Initialize and return the MongoDB collection using TLS certificate authentication.

Parameters:

- `uri`: MongoDB connection URI.
- `certificate_path`: Path to the TLS certificate file.
- `db_name`: Name of the MongoDB database.
- `collection_name`: Name of the MongoDB collection.

Returns:

- MongoDB collection object.

## 3. `set_data(collection, data)`

Insert data into the MongoDB collection.

Parameters:

- `collection`: MongoDB collection object.
- `data`: Dictionary containing the data to be inserted.

Returns:

- MongoDB insert result.

## 4. `get_data(collection)`

Retrieve data from the MongoDB collection where 'available' is True.

Parameters:

- `collection`: MongoDB collection object.

Returns:

- Cursor pointing to the retrieved data.

## 5. `get_all_data(collection)`

Retrieve all data from the MongoDB collection.

Parameters:

- `collection`: MongoDB collection object.

Returns:

- Cursor pointing to all data in the collection.

## 6. `get_data_one(collection, id_data)`

Retrieve a single document from the MongoDB collection by its ID.

Parameters:

- `collection`: MongoDB collection object.
- `id_data`: ID of the document to retrieve.

Returns:

- Single document matching the provided ID.

## 7. `remove_data_bool(collection, id_data)`

Remove data from the MongoDB collection by its ID and set 'available' to False.

Parameters:

- `collection`: MongoDB collection object.
- `id_data`: ID of the document to remove.

Returns:

- MongoDB update result.

## 8. `remove_data(collection, id_data)`

Remove data from the MongoDB collection by its ID.

Parameters:

- `collection`: MongoDB collection object.
- `id_data`: ID of the document to remove.

Returns:

- MongoDB delete result.

## 9. `update_data(collection, id_data, data)`

Update data in the MongoDB collection by its ID.

Parameters:

- `collection`: MongoDB collection object.
- `id_data`: ID of the document to update.
- `data`: Updated data as a dictionary.

Returns:

- MongoDB update result.

## 10. `delete_db(collection)`

Delete all data from the MongoDB collection.

Parameters:

- `collection`: MongoDB collection object.

Returns:

- MongoDB delete result.

## 11. `count_db_bool(collection)`

Count documents in the MongoDB collection where 'available' is True.

Parameters:

- `collection`: MongoDB collection object.

Returns:

- Number of documents where 'available' is True.

## 12. `count_all_db(collection)`

Count all documents in the MongoDB collection.

Parameters:

- `collection`: MongoDB collection object.

Returns:

- Total number of documents in the collection.

## 13. `search_data_by_field(collection, field_name, field_value)`

Retrieve data from the MongoDB collection based on a specific field and its value.

Parameters:

- `collection`: MongoDB collection object.
- `field_name`: Name of the field to search.
- `field_value`: Value to search for in the specified field.

Returns:

- Cursor pointing to the retrieved data.

## 14. `upsert_data(collection, query, data)`

Update existing data if found, or insert new data if not found.

Parameters:

- `collection`: MongoDB collection object.
- `query`: Query to identify the document to update.
- `data`: Data to be updated or inserted.

Returns:

- MongoDB update result.

## 15. `search_across_fields(collection, search_query)`

Search across all fields of the MongoDB collection and return matching documents.

Parameters:

- `collection`: MongoDB collection object.
- `search_query`: Search query string.

Returns:

- Cursor pointing to the retrieved data.

## 16. `search_all_fields(collection, search_term)`

Search for the given term in all fields of the MongoDB collection.

Parameters:

- `collection`: MongoDB collection object.
- `search_term`: Term to search for in all fields.

Returns:

- Cursor pointing to the retrieved data.

## 17. `close_connection(collection)`

Close the connection to the MongoDB database.

Parameters:

- `collection`: MongoDB collection object.

## 18. `uuid_id()`

Generate a UUID using the [uuid7 · PyPI](https://pypi.org/project/uuid7/) strategy.

Returns:

- UUID string.
