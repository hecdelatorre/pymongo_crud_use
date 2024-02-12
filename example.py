from mongo_functions import initialize_collection, set_data, get_data, get_all_data, \
    get_data_one, remove_data_bool, remove_data, update_data, delete_db, count_db_bool, \
    count_all_db, search_data_by_field, upsert_data, search_across_fields, search_all_fields, \
    uuid_id, close_connection

# MongoDB connection URI
MONGO_URI = "mongodb+srv://user:itXYIQkmR2cRfRN1@example.itpoo6h.mongodb.net/?retryWrites=true&w=majority"

# Database and collection names
DB_NAME = "mydatabase"
COLLECTION_NAME = "mycollection"

# Initialize MongoDB collection
collection = initialize_collection(MONGO_URI, DB_NAME, COLLECTION_NAME)
print(collection)

# Simple menu
def print_menu():
    print("\n--- Menu ---")
    print("1. Set Data")
    print("2. Get Data (Available)")
    print("3. Get All Data")
    print("4. Get Data by ID")
    print("5. Remove Data (Bool)")
    print("6. Remove Data")
    print("7. Update Data")
    print("8. Delete All Data")
    print("9. Count Data (Bool)")
    print("10. Count All Data")
    print("11. Search Data by Field")
    print("12. Upsert Data")
    print("13. Search Across Fields")
    print("14. Search All Fields")
    print("15. Generate UUID")
    print("16. Exit")

# Example usage of each function
def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            content = input("Enter content: ")
            id_tem = uuid_id()
            def data_r():
                data = {'_id': id_tem ,'title': title, 'content': content, 'available': True}
                return data
            data = data_r()
            set_data(collection, data)
            print("Data set successfully!")

        elif choice == '2':
            data = get_data(collection)
            for item in data:
                print(item)

        elif choice == '3':
            data = get_all_data(collection)
            for item in data:
                print(item)

        elif choice == '4':
            id_data = input("Enter ID: ")
            data = get_data_one(collection, id_data)
            if data:
                print("Data found:")
                print(data)
            else:
                print("Data not found.")

        elif choice == '5':
            id_data = input("Enter ID: ")
            result = remove_data_bool(collection, id_data)
            if result.modified_count > 0:
                print("Data removed successfully!")
            else:
                print("Data not found.")

        elif choice == '6':
            id_data = input("Enter ID: ")
            result = remove_data(collection, id_data)
            if result.deleted_count > 0:
                print("Data removed successfully!")
            else:
                print("Data not found.")

        elif choice == '7':
            id_data = input("Enter ID: ")
            title = input("Enter new title: ")
            content = input("Enter new content: ")
            data = {'title': title, 'content': content}
            update_data(collection, id_data, data)
            print("Data updated successfully!")

        elif choice == '8':
            result = delete_db(collection)
            print(f"{result.deleted_count} documents deleted.")

        elif choice == '9':
            count = count_db_bool(collection)
            print(f"Number of documents where 'available' is True: {count}")

        elif choice == '10':
            count = count_all_db(collection)
            print(f"Total number of documents: {count}")

        elif choice == '11':
            field_name = input("Enter field name: ")
            field_value = input("Enter field value: ")
            data = search_data_by_field(collection, field_name, field_value)
            for item in data:
                print(item)

        elif choice == '12':
            id_data = input("Enter ID: ")
            title = input("Enter title: ")
            content = input("Enter content: ")
            data = {'title': title, 'content': content, 'available': True}
            query = {'_id': id_data}
            upsert_data(collection, query, data)
            print("Data upserted successfully!")

        elif choice == '13':
            search_query = input("Enter search query: ")
            data = search_across_fields(collection, search_query)
            for item in data:
                print(item)

        elif choice == '14':
            search_term = input("Enter search term: ")
            data = search_all_fields(collection, search_term)
            for item in data:
                print(item)

        elif choice == '15':
            id_tem = uuid_id()
            print(f"Generated UUID: {id_tem}")

        elif choice == '16':
            print("Exiting...")
            close_connection(collection)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
