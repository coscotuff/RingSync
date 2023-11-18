import time
import ring_pb2
import ring_pb2_grpc
import grpc


with grpc.insecure_channel("localhost:5000") as channel:
    stub = ring_pb2_grpc.AlertStub(channel)
    response = stub.Add(ring_pb2.keyValue(key="134.lols", value="5180"))
print(response)
time.sleep(2)

with grpc.insecure_channel("localhost:5000") as channel:
    stub = ring_pb2_grpc.AlertStub(channel)
    response = stub.Delete(ring_pb2.keyValue(key="134.lols"))
print(response)
time.sleep(2)

with grpc.insecure_channel("localhost:5000") as channel:
    stub = ring_pb2_grpc.AlertStub(channel)
    response = stub.Add(ring_pb2.keyValue(key="134.lols", value="5120"))
print(response)
time.sleep(2)

with grpc.insecure_channel("localhost:5000") as channel:
    stub = ring_pb2_grpc.AlertStub(channel)
    response = stub.Delete(ring_pb2.keyValue(key="1345lols", value="5180"))
print(response)
time.sleep(2)

with grpc.insecure_channel("localhost:5000") as channel:
    stub = ring_pb2_grpc.AlertStub(channel)
    response = stub.Add(ring_pb2.keyValue(key="135.lols", value="5180"))
print(response)
time.sleep(2)

with grpc.insecure_channel("localhost:5000") as channel:
    stub = ring_pb2_grpc.AlertStub(channel)
    response = stub.Add(ring_pb2.keyValue(key="134.lols", value="5180"))
print(response)
time.sleep(2)
