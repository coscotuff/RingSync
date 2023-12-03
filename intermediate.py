from flask import Flask, request, jsonify
import logging
import mmh3
import sys
import requests
from time import sleep
import grpc
import ring_pb2
import ring_pb2_grpc

# Create the shell script files to run all the files in the correct order

# Need to add a couple of things: On the end server side of things, there needs to be locking

app = Flask(__name__)


def Hash64(key):
    # Perform hashing computations on the key
    # Return a list of computed hashes
    hashes = []
    data = key
    for i in range(0, N):
        data = mmh3.hash64(str(data).encode("utf-8"))[0] % ceiling
        hashes.append(data)
    print("Hashes: ", hashes)
    return hashes


def GetServers(hashes):
    # Perform computations to determine the set of servers to send the API call to
    # Return a set of servers
    servers = set()
    for h64 in hashes:
        servers.add(nodes.FindServer(h64))
    return servers


def AddServerToRing(server):
    global serverCount
    # Add server to the ring
    # Return the hash of the server
    tempChain = LinkedList()
    h64 = mmh3.hash64(server.encode("utf-8"))[0] % ceiling

    for i in range(virtualNodeCount):
        tempChain.InsertInPosition(h64, serverCount)
        h64 = (h64 + stepSize) % ceiling

    nodes.MergeLists(tempChain.head)
    # nodes.PrintLL()
    # print("Server added to ring successfully.\n")
    serverCount += 1


@app.post("/")
def Entry():
    return "Hello, World!"


@app.post("/delete")
def Delete():
    if len(serverList) == 0:
        print("Error: No servers registered, can't service request. \n")
        return (
            jsonify({"update": "No servers registered.", "key": "No"}),
            500,
        )
    hashes = Hash64(request.json["key"])
    servers = GetServers(hashes)

    print("Servers: ", servers)
    print("Hashes: ", hashes)

    vector = []

    for server in servers:
        # Make an gRPC call to the end server
        # print("Server: " + serverList[server])
        with grpc.insecure_channel(serverList[server]) as channel:
            stub = ring_pb2_grpc.AlertStub(channel)
            response = stub.Delete(ring_pb2.keyValue(key=request.json["key"]))
            vector.append(response.timestamp)

            logger.debug(
                "Delete request for key serviced: "
                + response.key
                + " with timestamp "
                + str(response.timestamp)
            )

    print(
        "Delete request for key serviced: "
        + response.key
        + " with timestamp "
        + str(response.timestamp)
        + "\n"
    )

    return (
        jsonify(
            {
                "update": response.updated,
                "key": response.key,
                "vector": vector,
                "hashes": hashes,
                "servers": list(servers),
            }
        ),
        200,
    )


@app.post("/read")
def Read():
    if len(serverList) == 0:
        print("Error: No servers registered, can't service request. \n")
        return (
            jsonify({"update": "No servers registered.", "key": "No"}),
            500,
        )
    hashes = Hash64(request.json["key"])
    servers = GetServers(hashes)

    print("Servers: ", servers)
    print("Hashes: ", hashes)

    vector = []

    for server in servers:
        # Make a gRPC call to the end server
        # print("Server: " + serverList[server])
        with grpc.insecure_channel(serverList[server]) as channel:
            stub = ring_pb2_grpc.AlertStub(channel)
            response = stub.Read(ring_pb2.keyValue(key=request.json["key"]))
            vector.append(response.timestamp)

            logger.debug(
                "Read request for key serviced:"
                + request.json["key"]
                + ": "
                + response.key
                + " with timestamp "
                + str(response.timestamp)
            )

    print(
        "Read request for key serviced:"
        + request.json["key"]
        + ": "
        + response.key
        + " with timestamp "
        + str(response.timestamp)
        + "\n"
    )

    return (
        jsonify(
            {
                "update": response.updated,
                "key": response.key,
                "vector": vector,
                "hashes": hashes,
                "servers": list(servers),
            }
        ),
        200,
    )


@app.post("/create")
def Create():
    if len(serverList) == 0:
        print("Error: No servers registered, can't service request. \n")
        return (
            jsonify({"status": "No servers registered."}),
            500,
        )
    hashes = Hash64(request.json["key"])
    logger.debug("Hashing done.")
    servers = GetServers(hashes)
    logger.debug("Servers retrieved.")

    print("Servers: ", servers)
    print("Hashes: ", hashes)

    vector = []

    for server in servers:
        # Make an gRPC call to the end server
        # print("Server: " + serverList[server])
        with grpc.insecure_channel(serverList[server]) as channel:
            stub = ring_pb2_grpc.AlertStub(channel)
            response = stub.Add(
                ring_pb2.keyValue(key=request.json["key"], value=request.json["value"])
            )

            logger.debug(
                "Key-value pair added successfully: "
                + response.key
                + " "
                + response.value
                + " with timestamp "
                + str(response.timestamp)
            )
            vector.append(response.timestamp)

    print(
        "Key-value pair added successfully: "
        + response.key
        + " "
        + response.value
        + " with timestamp "
        + str(response.timestamp)
        + "\n"
    )

    return (
        jsonify(
            {
                "update": response.updated,
                "key": response.key,
                "value": response.value,
                "vector": vector,
                "hashes": hashes,
                "servers": list(servers),
            }
        ),
        200,
    )


@app.post("/update")
def Update():
    if len(serverList) == 0:
        print("Error: No servers registered, can't service request. \n")
        return (
            jsonify({"status": "No servers registered."}),
            500,
        )
    hashes = Hash64(request.json["key"])
    logger.debug("Hashing done.")
    servers = GetServers(hashes)
    logger.debug("Servers retrieved.")

    print("Servers: ", servers)
    print("Hashes: ", hashes)

    vector = []

    for server in servers:
        # Make an gRPC call to the end server
        # print("Server: " + serverList[server])
        with grpc.insecure_channel(serverList[server]) as channel:
            stub = ring_pb2_grpc.AlertStub(channel)
            response = stub.Update(
                ring_pb2.keyValue(key=request.json["key"], value=request.json["value"])
            )

            logger.debug(
                "Updation request processed: "
                + response.key
                + " "
                + response.value
                + " with timestamp "
                + str(response.timestamp)
            )
            vector.append(response.timestamp)

    print(
        "Updation request processed: "
        + response.key
        + " "
        + response.value
        + " with timestamp "
        + str(response.timestamp)
        + "\n"
    )

    return (
        jsonify(
            {
                "update": response.updated,
                "key": response.key,
                "value": response.value,
                "vector": vector,
                "hashes": hashes,
                "servers": list(servers),
            }
        ),
        200,
    )


@app.post("/register")
def RegisterServer():
    # Register server to the list of servers
    serverList.append(request.json["ip"] + ":" + request.json["port"])
    AddServerToRing(serverList[-1])
    return (
        jsonify({"status": "Successfully registered server.", "Added": serverList[-1]}),
        200,
    )


class Node:
    def __init__(self, data, server):
        self.data = data
        self.server = server
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at any index
    # Indexing starts from 0.
    def MergeLists(self, head):
        # A dummy node to store the result
        temp = Node(0, -1)
        tail = temp
        while True:
            # If any of the list gets completely empty
            # directly join all the elements of the other list
            if self.head is None:
                tail.next = head
                break
            if head is None:
                tail.next = self.head
                break

            # Compare the data of the lists and whichever is smaller is
            # appended to the last of the merged list and the head is changed
            if self.head.data <= head.data:
                tail.next = self.head
                self.head = self.head.next
            else:
                tail.next = head
                head = head.next

            # Advance the tail
            tail = tail.next

        # Returns the head of the merged list
        self.head = temp.next
        return

    # Method to add a node at correct position of LL
    def InsertInPosition(self, data, server):
        new_node = Node(data, server)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next and current_node.next.data < data:
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def FindServer(self, data):
        current_node = self.head
        while current_node.next and current_node.next.data < data:
            current_node = current_node.next
        if self.head != None:
            return (
                current_node.server
                if current_node.next == None
                else current_node.server
            )
        else:
            return -1

    # print method for the linked list
    def PrintLL(self):
        current_node = self.head
        while current_node:
            print(str(current_node.data) + " " + str(current_node.server))
            current_node = current_node.next


# main:
if __name__ == "__main__":
    logging.basicConfig(
        filename="intermediate.log",
        format="%(asctime)s %(message)s",
        filemode="w",
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Starting the intermediate server")

    # Configure the number of virtual nodes
    virtualNodeCount = 20

    # Configure the number of times data is to be replicated
    N = 4
    serverList = []
    serverCount = 0
    ceiling = 2**64
    stepSize = int(ceiling / virtualNodeCount)
    nodes = LinkedList()

    app.run(debug=True, port=6000)
