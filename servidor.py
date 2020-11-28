#Se importa la libreria
import socket

#Establecemos el tipo de conexion,ip y puerto
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_socket.bind(('127.0.0.1',9000)) 

#Se manda mensaje para la espera de una conexion del cliente
print ("Esperando conexiones")
mi_socket.listen(5)

con, addr = mi_socket.accept()
print("Cliente conectado")
message = "Hola, soy el servidor!" 
con.send(message.encode()) 


con.close() # Cerramos la conexion
mi_socket.close() # Cerramos el socket
print("Cliente desconectado")#Mensaje en donde el cliente se desconecta
