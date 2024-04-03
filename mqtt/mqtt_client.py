# Importeer de paho.mqtt.client module die MQTT-client functionaliteiten biedt.
import paho.mqtt.client as mqtt

def create_client(client_id, on_connect, on_message, broker="localhost", port=1883):
    """
    Creëert en configureert een MQTT-client.

    Deze functie initialiseert een MQTT-client met een unieke client_id, 
    definieert callback functies voor connect- en message-events, en 
    maakt vervolgens verbinding met de MQTT-broker.

    Parameters:
        client_id (str): Een unieke identifier voor de MQTT-client.
        on_connect (function): Callback functie die wordt aangeroepen 
            wanneer de client verbinding maakt met de broker.
        on_message (function): Callback functie die wordt aangeroepen 
            wanneer een bericht wordt ontvangen.
        broker (str, optional): Het adres van de MQTT-broker. 
            Standaard is dit "localhost".
        port (int, optional): De poort waarop de MQTT-broker luistert. 
            Standaard is dit 1883.

    Returns:
        mqtt.Client: Een geconfigureerde MQTT-clientobject.
    """
    # Initialiseert een MQTT-client met de opgegeven client_id.
    client = mqtt.Client(client_id)
    
    # Stelt de callback functies in voor connect- en message-events.
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Maakt verbinding met de opgegeven MQTT-broker en poort.
    client.connect(broker, port, 60)  # De keepalive is ingesteld op 60 seconden.
    
    # Retourneert het geïnitialiseerde en geconfigureerde client-object.
    return client

def start_loop(client):
    """
    Start de netwerkloop van de MQTT-client.

    Deze functie start de oneindige loop van de client, waardoor deze
    continu luistert naar berichten van de broker. De loop wordt onderbroken
    bij het ontvangen van een KeyboardInterrupt (Ctrl+C).

    Parameters:
        client (mqtt.Client): De MQTT-client die de loop zal uitvoeren.

    Returns:
        None
    """
    try:
        # Start de oneindige loop die berichten verwerkt.
        client.loop_forever()
    except KeyboardInterrupt:
        # Print een bericht en maakt de verbinding met de broker los 
        # als de gebruiker de loop onderbreekt.
        print("Disconnecting from broker")
