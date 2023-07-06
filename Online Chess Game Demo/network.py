import socket
import pickle
#from game import demo

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname())
        self.port = 5555
        self.addr = (self.server,self.port)
        #self.p = self.connect()
        self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self,data):
        try:
            self.client.send(data)
            #self.receive()
            #return pickle.loads(self.client.recv(2048*2))
            #pickle.loads(self.client.recv(2048))
            '''while True:
                self.recv_dic = self.client.recv(4096).decode()
                if self.recv_dic != "":
                    break'''
        except socket.error as e:
            print(e)

    def receive(self):
        #return pickle.loads(self.client.recv(2048))
        #while True:
        data = self.client.recv(4096)
        try:
            print("Receiving")
            self.recv_data = pickle.loads(data)
            print(self.recv_data)
        except:
            self.recv_data = data.decode()
            print(self.recv_data)
         #   if len(self.recv_data)!=0:
                #self.client.send("Message Received".encode())
          #      break
        #print("broke successfully")
        return self.recv_data