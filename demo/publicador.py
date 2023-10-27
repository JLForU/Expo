
# IMPORTS
import paho.mqtt.client as mqtt



# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n\n\n")


    client = mqtt.Client()
    client.connect("localhost", 1883)
    
    # Publish a message to a topic
    client.publish("mytopic", "Hello, MQTT!")
    client.disconnect()
    
    function_01()


    print ("\n\n\n\n")


# OTHER FUNCTIONS
def function_01 ( ) :

    print ("# CODE")



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       