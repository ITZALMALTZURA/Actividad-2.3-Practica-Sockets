import socket
BUFFER_SIZE = 4096
#Establecemos el tipo de conexion,ip y puerto
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Realizamos la conexion al la IP y puerto
mi_socket.connect(('127.0.0.1',9000))
data = mi_socket.recv(BUFFER_SIZE)

# Cerramos el socket
mi_socket.close()

# Mostramos los datos recibidos
print(data.decode())
