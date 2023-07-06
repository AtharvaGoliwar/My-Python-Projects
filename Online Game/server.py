import socket
from _thread import *
import pickle
from game import Game

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

games = {}
idCount = 0 #NOT NEEDED FOR NOW


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))       #SENDING PLAYER NUMBER , LIKE FOR CHESS GAME, 0 WILL BE FOR WHITE AND 1 WILL BE FOR BLACK

    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)           #DATA FOR CHESS GAME WILL BE THE SELF.COORDS LIST (FOR THAT I WILL HAVE TO CREATE A NEW FUNCTION WHICH WILL RETURN THE SELF.COORDS LIST)

                    conn.sendall(pickle.dumps(game))      #SENDS ALL THE DATA TO THE CLIENT
            else:
                break
        except:
            break

    print("Lost connection")
    #HERE WRITE A FUNCTION WHERE THE CHESS GAME WINDOW WILL CLOSE AND THE INITIAL WINDOW OF WAITING FOR GAMES WINDOW WILL OPEN UP ONCE AGAIN
    try: #THIS TRY AND EXCEPT NOT NEEDED FOR THR CHESS GAME
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))





    ### DIRECTIONS OF WHAT ALL HAPPENS IN THE COMPLETE PROCESS
    # 1. FIRST BOTH THE CLIENTS CONNECT AND THE MATCH BEGINS
    # 2. THE P0 WILL PLAY A MOVE AND SEND THE NEW SELF.COORDS TO THE SERVER
    # 3. THEN SERVER WILL SEND THAT SELF.COORDS TO BOTH CLIENTS
    # 4. THEN THE NEW ACCEPTED SELF.COORDS WILL BE CHANGED TO THE NEW ONE AND THIS WILL BE RECEIVED AND WILL BE UPDATED AGAIN IN THE CLIENT ITSELF
    # AND MOST IMPORTANT CHANGE THAT HAS TO BE MADE IN THE CHESS GAME FILE
    # THAT ALONG WITH THEN NUMBER OF MOVES THING, ADD A NEW VARIABLE OF PLAYER OR THE CLIENT LIKE FIGURE OUT SOMETHING