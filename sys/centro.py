
# IMPORTACIONES #
import paho.mqtt.client as mqtt



#
# DECLARACIÓN DE CENTRO DE COMANDO #
#
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    client = mqtt.Client()
    client.connect ( "localhost", 1883)

    # Recibir mensaje, especificando un tópico.
    client.subscribe("entrada")
    client.subscribe("salida")
    client.on_message = on_message

    # Esperar más mensajes.
    try :
        client.loop_forever()
    except KeyboardInterrupt :
        pass

    # Establecer desconexión.
    client.disconnect()


    # MENSAJE DE EJECUCIÓN EXITOSA.
    function_01()


    print ("\n\n\n\n")



# OTRAS FUNCIONES #
def on_message ( client , userdata , message ) :

    print ( f"Mensaje: '{message.payload.decode()}' desde '{message.topic}'." )


def function_01 ( ) :

    print ("\n\nCentro de comando.")



# IMPLEMENTACIÓN DE FUNCIÓN MAIN #
if __name__ == "__main__" :
    main()




# To rest -->       
