
# IMPORTACIONES #
import paho.mqtt.client as mqtt



# VARIABLES GLOBALES #
cliente = mqtt.Client()
TOOPICO = "salida"


#
# DECLARACIÓN DE SENSOR DE ENTRADA #
#
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    cliente.connect ( "localhost" , 1883 )

    # Enviar mensajes.
    try :
        while ( True ) :
            funcioon_publicar()
    except KeyboardInterrupt :
        pass

    # Establecer desconexión.
    cliente.disconnect()

    # MENSAJE DE EJECUCIÓN EXITOSA.
    function_01()


    print ("\n\n\n\n")



# OTRAS FUNCIONES #
def funcioon_publicar ( ) :

    pregunta = input ( f"{TOOPICO}: " )

    if pregunta == "1" :
        # Enviar mensaje por medio de un tópico.
        cliente.publish ( TOOPICO , f"Sensor de {TOOPICO}." )


def function_01 ( ) :

    print ( "\n\nSensor de entrada." )



# IMPLEMENTACIÓN DE FUNCIÓN MAIN #
if __name__ == "__main__" :
    main()




# To rest -->       
