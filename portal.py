import requests
import logging
import json
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
        print("Value: " + response.json()["value"])
        print("Vector clock across replicas: " + str(response.json()["vector"]))
        print("Added to servers: " + str(response.json()["servers"]))
        print(
            "Virtual node numbers of servers: " + str(response.json()["hashes"]) + "\n"
        )
        logger.debug("Key: " + response.json()["key"])
        logger.debug("Value: " + response.json()["value"])
    else:
        print("Failed to create key-value pair. Server error...\n")
        logger.debug("Failed to create key-value pair.")

    save_file = open("savedata.json", "a")
    json.dump(response.json(), save_file, indent=6)
    save_file.close()


def UpdateValue(key, value, IP):
    # Make a POST request to the server to create a key-value pair
    response = requests.post(
        "http://" + IP + ":6000/update", json={"key": key, "value": value}
    )
    # print(response)
    if response.status_code == 200:
        if response.json()["update"] == "True":
            print("Found value for the key in the database...")
            print("Updated the value to newly provided values... ")
            print("Key: " + response.json()["key"])
            print("Value: " + response.json()["value"])
            print("Vector clock across replicas: " + str(response.json()["vector"]))
            print("Added to servers: " + str(response.json()["servers"]))
            print(
                "Virtual node numbers of servers: "
                + str(response.json()["hashes"])
                + "\n"
            )
            logger.debug("Key-value pair updated successfully.")
        else:
            print("Key not found, nothing was updated.")
            logger.debug("Key not found, nothing was updated.")
        logger.debug("Key: " + response.json()["key"])
        logger.debug("Value: " + response.json()["value"])
    else:
        print("Failed to update key-value pair. Server error...\n")
        logger.debug("Failed to update key-value pair.")

    save_file = open("savedata.json", "a")
    json.dump(response.json(), save_file, indent=6)
    save_file.close()


def DeleteKey(key, IP):
    # Make a DELETE request to the server to delete a key
    response = requests.post("http://" + IP + ":6000/delete", json={"key": key})
    if response.status_code == 200:
        if response.json()["update"] == "True":
            print("Entry for key found...")
            print("Deleted from servers: " + str(response.json()["servers"]))
            print("Virtual node numbers of servers: " + str(response.json()["hashes"]))
            print("Vector clock across replicas: " + str(response.json()["vector"]))
            logger.debug("Key-value pair updated successfully.")
        else:
            print("Key not found, nothing was deleted.")
            logger.debug("Key not found, nothing was deleted.")
        print("Key: " + response.json()["key"] + "\n")
        logger.debug("Key: " + response.json()["key"])
    else:
        print(response)
        print("Failed to delete key. Server error...\n")
        logger.debug("Failed to delete key.")

    save_file = open("savedata.json", "a")
    json.dump(response.json(), save_file, indent=6)
    save_file.close()


def ReadKey(key, IP):
    # Make a READ request to the server to read a key
    response = requests.post("http://" + IP + ":6000/read", json={"key": key})
    if response.status_code == 200:
        if response.json()["update"] == "True":
            print("Entry for key found...")
            print("Value associated with key " + key + ": " + response.json()["key"])
            print(
                "Vector clock across replicas: " + str(response.json()["vector"]) + "\n"
            )
            logger.debug(
                "Value associated with key " + key + ": " + response.json()["key"]
            )
        else:
            print("Key not found.")
            logger.debug("Key not found.")
    else:
        print(response)
        print("Failed to retrieve value. Server error...\n")
        logger.debug("Failed to retrieve value.")

    save_file = open("savedata.json", "a")
    json.dump(response.json(), save_file, indent=6)
    save_file.close()


def main():
    # The IP address of the server is taken in as a command line argument
    serverIP = "127.0.0.1"

    while True:
        print("Menu:")
        print("1. Create key-value pair")
        print("2. Delete key")
        print("3. Read key")
        print("4. Update key-value pair")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            CreateKeyValue(key, value, serverIP)
        elif choice == "2":
            key = input("Enter the key to delete: ")
            DeleteKey(key, serverIP)
        elif choice == "3":
            key = input("Enter the key to read: ")
            ReadKey(key, serverIP)
        elif choice == "4":
            key = input("Enter the key to update: ")
            value = input("Enter the new value: ")
            UpdateValue(key, value, serverIP)
        elif choice == "5":
            sys.exit()
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
