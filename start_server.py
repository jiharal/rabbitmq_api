
import os, uuid, json
from dotenv import load_dotenv
from kombu import Connection, Exchange, Producer
import sys

load_dotenv()

def publishStatus(jsonData, paramQueue):
    print("publish status", jsonData)

    queueName = paramQueue
    exchange = Exchange(queueName, type="direct")
    with Connection(os.getenv("RABBITMQ_HOST")) as connection:
        producer = Producer(connection)
        producer.publish(
            json.dumps(jsonData),
            exchange=exchange,
            routing_key=queueName,
            serializer="json",
            compression="zlib",
        )

if __name__ == "__main__":
    print("API Started")
    coreID = str(uuid.uuid4())
    callbackQueue =  "/mining/inference/v1/status/reply"
    status = ' '.join(sys.argv[1:]) or "online"
    resp = {
        "correlation_id": coreID,
        "success": bool(True),
        "message": "success",
        "data": {"status": "ONLINE"},
    }
    resp = {
        "correlation_id": coreID,
        "success": bool(True),
        "message": "success",
        "data": {"status": "ONLINE"},
    }
    if status == "online":
        publishStatus(resp, callbackQueue)
    elif status == "offline":
        resp["data"] = {"status": "OFFLINE"}
        publishStatus(resp, callbackQueue)
    else:
        resp["success"] = bool(False)
        resp["message"] = "Server is down"
        resp["data"] = {}
        publishStatus(resp, callbackQueue)
