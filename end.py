from flask import Flask, request, jsonify
import logging
import csv

app = Flask(__name__)


@app.route("/")
def Entry():
    return "Hello, World!"


@app.post("/del")
def Del():
    status = "False"
    data = []
    # Add key-value pair to csv database. Check if there is a entry for the key, if so, update it, else append.
    with open("database.csv", "r", newline="") as r:
        read = csv.reader(r)
        data = list(read)

    for row in data:
        if row[0] == request.json["key"]:
            data.remove(row)
            status = "True"
            break

    with open("database.csv", "w", newline="") as w:
        write = csv.writer(w)
        write.writerows(data)

    return (
        jsonify(
            {
                "Operation": "Delete",
                "Updated": status,
                "key": request.json["key"],
                "value": request.json["value"],
            }
        ),
        200,
    )


@app.post("/add")
def Add():
    status = "False"
    data = []
    # Add key-value pair to csv database. Check if there is a entry for the key, if so, update it, else append.
    with open("database.csv", "r", newline="") as r:
        read = csv.reader(r)
        data = list(read)
        r.close()

    for row in data:
        print(row)
        if row[0] == request.json["key"]:
            row[1] = request.json["value"]
            status = "True"
            break

    if status == "False":
        data.append([request.json["key"], request.json["value"]])
        print("Data after update/append: ", data)

    with open("database.csv", "w", newline="") as w:
        write = csv.writer(w)
        write.writerows(data)
        w.close()

    return (
        jsonify(
            {
                "Operation": "Add",
                "Updated": status,
                "key": request.json["key"],
                "value": request.json["value"],
            }
        ),
        200,
    )


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
    app.run(debug=True)
