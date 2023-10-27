
# IMPORTS
import paho.mqtt.client as mqtt



# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n\n\n")


    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost", 1883)
    client.subscribe("mytopic")
    client.loop_forever()

    function_01()


    print ("\n\n\n\n")


# OTHER FUNCTIONS
def function_01 ( ) :

    print ("# CODE")


def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       