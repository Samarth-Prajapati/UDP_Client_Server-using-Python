import socket

host = 'localhost'
port = 5000
udp_server = socket.socket( type = socket.SOCK_DGRAM )
udp_server.bind( ( host , port ) )

while True :
    print( 'Waiting for message : ' )
    data , addr = udp_server.recvfrom( 1024 )
    print( 'Received message : ' , data.decode() , ' from ' , addr )
    msg = input( 'Enter message to send : ' )
    udp_server.sendto( msg.encode() , addr )
    
udp_server.close()