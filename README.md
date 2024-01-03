# RingSync
RingSync is a Python-based project that leverages user-friendly REST API, gRPC, protocol buffers, and Docker to ensure the seamless storage, retrieval, updation and deletion of objects while maintaining high availability, fault tolerance, and data consistency. 

This repository contains the codebase for a consistently hashed, ring topology based architecture with replication designed for a cloud-based object storage system built on the key principles of distributed computing as a part of the assignment from the Semester-I '23-24 offering of the CS G527 Cloud Computing course.

## Underlying System Architecture

![unnamed (1)](https://github.com/coscotuff/RingSync/assets/74728041/4c0e5f86-4d54-40af-a806-b6e41ccd7d68)

## Requirements

- Python 3.x
- gRPC (Google Remote Procedure Call): gRPC tools and gRPC Python Libraries
- Protobuf  ‘protoc’  compiler (for .proto files)
- Docker (code was run and tested on v4.24)
- docker Python Library
- mmh3 Python Library
- Flask Python Library

Please ensure that you have these dependencies installed and configured before running the scripts.

## Running Instructions
_Note:_
_1) The operating systems of the machines on which the files are to be run must be Linux-based._
_2) Ensure that all the required software and libraries are installed on your system. For more information on which libraries and software are needed, kindly go through technical design documentation._

1) Clone the repository.
2) Navigate to the directory of the repository. Create a Docker image named ‘ringserver’ via the following instruction:
```
docker build -t ringserver .
```
3) Run the intermediate server with the following instruction
```
python intermediate.py
```
4) Run the endserver initialiser script to register all N nodes (containers) with the intermediate server:
```
python endInitialiser.py
```
5) You should have N containers running the ringserver image now. Now, any client can perform the desired CRUD operations by accessing the portal
```
python portal.py
```

_Note: It might be needed to modify the IP addresses according to the necessities of the machines running this system on your end. Please do so accordingly before trying out the code._
