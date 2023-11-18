import requests
import docker
import socket
import logging


def GetIP():
    try:
        # Create a socket object and connect to a remote host (e.g., Google's DNS server)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        # Get the local IP address
        self_ip = s.getsockname()[0]
        return self_ip
    except socket.error as e:
        print(f"Error: {e}")
        return None
    finally:
        s.close()


def RemoveContainers():
    docker_client = docker.from_env()
    containers = docker_client.containers.list()
    for container in containers:
        container.remove(force=True)


def AddContainers(N):
    RemoveContainers()
    logger.debug("Removed all containers")
    docker_client = docker.from_env()
    logger.debug("Fetched docker env information...")
    for i in range(1, N + 1):
        docker_client.containers.run(
            "endServer",
            name="endServer" + str(i),
            detach=True,
            ports={"5000/tcp": str(5000 + i)},
        )

        logger.debug("Started container " + str(i))

        response = requests.post(
            "http://" + intermediateIP + "/register",
            json={"IP": ip, "port": str(5000 + i)},
        )

        # Check the response status code
        if response.status_code == 200:
            print("Registered" + str(i) + " successfully!")
        else:
            print(response)
            print(response.json)
            print("Request failed")


if __name__ == "__main__":
    logging.basicConfig(
        filename="initialiser.log",
        format="%(asctime)s %(message)s",
        filemode="w",
    )
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    ip = GetIP()
    intermediateIP = "127.0.0.1:5000"
    containerCount = 3

    logger.debug(
        "Starting registration process for the " + str(containerCount) + " containers"
    )
    AddContainers(containerCount)
