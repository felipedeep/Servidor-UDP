tomada de importação

localIP = "127,0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = ":)"
bytesToSend = str. encode (msgFromServer)

# Tomada criado unidade de transferência básica.

UDPServerSocket = soquete. soquete (família=soquete. AF_INET, tipo=soquete. SOCK_DGRAM)

# Vincular ao endereço IP do servidor.

UDPServersocket. bind(localIP, localPort))

imprimir("Servidor UDP está funcionando corretamente!")

# Lista de unidade de transferência(datagrama).

enquanto (Verdadeiro):

    bytesAddressPair = UDPServerSocket. recvfrom (bufferSize)

    mensagem = bytesAddressPair[0]
    endereço = bytesAddressPair[1]
    
    clienteMsg = "Mensagem do Cliente:{}". formato (mensagem)
    clientIP = "Endereço IP do Cliente:{}". formato (endereço)
    
    impressão (clientMsg)
    impressão (clientIP)

    Enviando uma resposta ao cliente.

    UDPServersocket. sendto(bytesToSend, endereço)
