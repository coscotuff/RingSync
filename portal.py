import requests
import logging
import sys


def CreateKeyValue(key, value, IP):
    # Make a POST request to the server to create a key-value pair
    response = requests.post(
        "http://" + IP + ":6000/create", json={"key": key, "value": value}
    )
    # print(response)
    if response.status_code == 200:
        if response.json()["update"] == "True":
            print("A value for the key already exists in the database...")
            print("Updated the value to newly provided values... ")
            logger.debug("Key-value pair updated successfully.")
        else:
            print("Key-value pair added successfully...")
            logger.debug("Key-value pair added successfully.")
        print("Key: " + response.json()["key"])
        print("Value: " + response.json()["value"] + "\n")
    else:
        print("Failed to create key-value pair. \n")
        logger.debug("Failed to create key-value pair.")


def DeleteKey(key, IP):
    # Make a DELETE request to the server to delete a key
    response = requests.post("http://" + IP + ":6000/delete", json={"key": key})
    if response.status_code == 200:
        if response.json()["update"] == "True":
            print("Entry for key found...")
            print("Deleted!")
            logger.debug("Key-value pair updated successfully.")
        else:
            print("Key not found, nothing was deleted.")
            logger.debug("Key not found, nothing was deleted.")
        print("Key: " + response.json()["key"] + "\n")
        logger.debug("Key: " + response.json()["key"])
    else:
        print(response)
        print("Failed to delete key.\n")
        logger.debug("Failed to delete key.")


def main():
    # The IP address of the server is taken in as a command line argument
    serverIP = "127.0.0.1"

    while True:
        print("Menu:")
        print("1. Create key-value pair")
        print("2. Delete key")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            CreateKeyValue(key, value, serverIP)
        elif choice == "2":
            key = input("Enter the key to delete: ")
            DeleteKey(key, serverIP)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    logging.basicConfig(
        filename="client.log",
        format="%(asctime)s %(message)s",
        filemode="w",
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Starting the client application")
    main()
