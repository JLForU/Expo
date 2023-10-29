
# IMPORTS
import paho.mqtt.client as mqtt



# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    client = mqtt.Client()
    client.connect("localhost", 1883)
    
    # Enviar mensaje por medio de un tópico.
    client.publish("mytopic", "Hello, MQTT!")

    # Establecer desconexión.
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
