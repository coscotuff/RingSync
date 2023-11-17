import requests
import logging
import sys

# Need to later on add functionality to check if: The key does not exist, The key already exists and therefore the value has now been updated.


def CreateKeyValue(key, value, IP):
    # Make a POST request to the server to create a key-value pair
    response = requests.post(
        "http://" + IP + ":5000/create", json={"key": key, "value": value}
    )
    print(response)
    if response.status_code == 200:
        print("Key-value pair created successfully.")
        print(response.json())
        logger.debug("Key-value pair created successfully.")
    else:
        print("Failed to create key-value pair.")
        logger.debug("Failed to create key-value pair.")


def DeleteKey(key, IP):
    # Make a DELETE request to the server to delete a key
    response = requests.post("http://" + IP + ":5000/delete", json={"key": key})
    if response.status_code == 200:
        print("Key deleted successfully.")
        logger.debug("Key deleted successfully.")
    else:
        print("Failed to delete key.")
        logger.debug("Failed to delete key.")


def main():
    # The IP address of the server is taken in as a command line argument
    serverIP = "127.0.0.1"

    if len(sys.argv) == 2:
        serverIP = sys.argv[1]
    elif len(sys.argv) > 2:
        print("Invalid number of arguments. Please check the shell script.")

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
        # elif choice == "4":
        #     response = requests.post("http://" + serverIP + ":5000/register", json = {"IP": "127.lols", "port": "5069"})
        #     print(response)
        #     if response.status_code == 200:
        #         print("Retrieved IP: ")
        #         print(response.json())
        #         logger.debug("Key-value pair created successfully.")

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
