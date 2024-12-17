import socket

host = 'localhost'
port = 5000
udp_client = socket.socket( type = socket.SOCK_DGRAM )

while True :
    data = input( 'Enter message to send : ' )
    if not data :
        break
    udp_client.sendto( data.encode() , ( host , port ) )
    print( 'Ready to recieve data' )
    data , addr = udp_client.recvfrom( 1024 )
    if not data :
        break
    print( 'Received message : ' , data.decode() )
udp_client.close()