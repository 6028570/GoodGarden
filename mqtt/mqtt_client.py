import paho.mqtt.client as mqtt

def create_client(client_id, on_connect, on_message, broker="localhost", port=1883):
    client = mqtt.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(broker, port, 60)
    return client

def start_loop(client):
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("Disconnecting from broker")
