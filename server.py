import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None

CLIENTS = {}




def acceptConnections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
        playerName = player_socket.recv(2048).decode('utf-8').strip()
        if len(CLIENTS) == 0:
            CLIENTS[playerName] = {'Player_Type': 'Player 1'}
        else:
            CLIENTS[playerName] = {'Player_Type' : 'Player 2'}
        CLIENTS[playerName]['player_socket'] = player_socket 
        CLIENTS[playerName]['address'] = addr
        CLIENTS[playerName]['player_name'] = playerName
        CLIENTS[playerName]['turn'] = False

        print("Connected established with "+playerName)
        


def setup():
    print("\n")
    print('\n\t\t\t\t\t*** Welcome to Tambola Game ***')


    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup()