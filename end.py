from concurrent import futures
import logging
import csv
import grpc
import threading
import ring_pb2
import ring_pb2_grpc


class Server(ring_pb2_grpc.AlertServicer):
    def __init__(self):
        self.data = True

    def Delete(self, request, context):
        lock.acquire()

        if request.key not in vector:
            vector[request.key] = 0
        vector[request.key] += 1

        status = "False"
        data = []
        # Add key-value pair to csv database. Check if there is a entry for the key, if so, update it, else append.
        with open("database.csv", "r", newline="") as r:
            read = csv.reader(r)
            data = list(read)

        for row in data:
            if row[0] == request.key:
                data.remove(row)
                status = "True"
                break

        with open("database.csv", "w", newline="") as w:
            write = csv.writer(w)
            write.writerows(data)

        lock.release()
        return ring_pb2.returnValue(
            updated=status,
            key=request.key,
            timestamp=vector[request.key],
        )

    def Read(self, request, context):
        lock.acquire()

        if request.key not in vector:
            vector[request.key] = 0
        vector[request.key] += 1

        status = "False"
        data = []
        # Add key-value pair to csv database. Check if there is a entry for the key, if so, update it, else append.
        with open("database.csv", "r", newline="") as r:
            read = csv.reader(r)
            data = list(read)

        value = ""
        for row in data:
            if row[0] == request.key:
                value = row[1]
                status = "True"
                break

        lock.release()
        return ring_pb2.returnValue(
            updated=status,
            key=value,
            timestamp=vector[request.key],
        )

    def Add(self, request, context):
        lock.acquire()

        if request.key not in vector:
            vector[request.key] = 0
        vector[request.key] += 1

        status = "False"
        data = []
        # Add key-value pair to csv database. Check if there is a entry for the key, if so, update it, else append.
        with open("database.csv", "r", newline="") as r:
            read = csv.reader(r)
            data = list(read)
            r.close()

        for row in data:
            print(row)
            if row[0] == request.key:
                row[1] = request.value
                status = "True"
                break

        if status == "False":
            data.append([request.key, request.value])
            print("Data after update/append: ", data)

        with open("database.csv", "w", newline="") as w:
            write = csv.writer(w)
            write.writerows(data)
            w.close()

        lock.release()
        return ring_pb2.returnValue(
            updated=status,
            key=request.key,
            value=request.value,
            timestamp=vector[request.key],
        )

    def Update(self, request, context):
        lock.acquire()

        if request.key not in vector:
            vector[request.key] = 0
        vector[request.key] += 1

        status = "False"
        data = []
        # Add key-value pair to csv database. Check if there is a entry for the key, if so, update it, else append.
        with open("database.csv", "r", newline="") as r:
            read = csv.reader(r)
            data = list(read)
            r.close()

        for row in data:
            print(row)
            if row[0] == request.key:
                row[1] = request.value
                status = "True"
                break

        with open("database.csv", "w", newline="") as w:
            write = csv.writer(w)
            write.writerows(data)
            w.close()

        lock.release()
        return ring_pb2.returnValue(
            updated=status,
            key=request.key,
            value=request.value,
            timestamp=vector[request.key],
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ring_pb2_grpc.add_AlertServicer_to_server(Server(), server)
    server.add_insecure_port("[::]:5000")
    server.start()
    print("Server started listening on port 5000")
    server.wait_for_termination()


# main:
if __name__ == "__main__":
    logging.basicConfig(
        filename="end.log",
        format="%(asctime)s %(message)s",
        filemode="w",
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.debug("Starting the end server")
    f = open("database.csv", "w", newline="")
    f.close()

    # Locking for serialising access to the database
    lock = threading.Lock()

    vector = {}

    # Start the server
    serve()
