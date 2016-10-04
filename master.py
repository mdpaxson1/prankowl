import subprocess
import socket
import time
import console
class MasterServer:
    # eventually will use some type of socket connection for remote master server
    def __init__ (self, host="localhost", port=60000 ):
        self.host = host
        self.port = port

        try:
            self.spinUpCallbotController()
        except Exception:
            print "Couldn't start Subprocess callbot control"
            self.callbot_process = None

        try:
            self.socket = self.startServer()
        except Exception:
            self.socket = None
            #print "Socket Error"

        self.receiveData()


    #the subproceses can communicate with the master through this
    def startServer ( self ):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind ( (self.host, self.port) )
            #print "created Socket"
            return serverSocket #serverSocket = self.socket
        except Exception:
            #print "Couldn't start socket"
            return None

    def receiveData(self):
        #if there was no error  in creating the socket
        if self.socket != None:
            self.socket.listen(1)
            conn, addr = self.socket.accept()
            #print 'Connected by', addr
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
            conn.close()



    #if arguments takes some type of command line arguments, these arguments can also be sent through the socket
    def spinUpCallbotController(self, arguments=None):
        cmdArgumnents = ("python", "callbotControl.py")
        self.callbot_process = subprocess.Popen(cmdArgumnents)

    def __del__(self):
        #checks to see if the callbot process hasn't been closed, and then closes it

        if self.callbot_process != None:
            try:
                self.callbot_process.kill()
                self.callbot_process = None
                self.serverS
            except Exception:
                    #print "error"
                    return None




if __name__ == "__main__":
    secondsInDay = 86400
    while True:
        print ("\n=============================")
        print ("I reckon I'll troll someone now\n")

        masterServer = MasterServer()
        time.sleep(secondsInDay)
