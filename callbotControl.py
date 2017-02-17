import ConfigParser
from callbot.callbot import * #import call bot python
import random
import subprocess
import os
import sys
import socket

def countdown(t):
    import time
    print('More trolling in...')
    while t >= 0:
        if t < 10:
            sys.stdout.write("Trolling In: " + str(t) +"\n")
            sys.stdout.flush()
            time.sleep(1)
            t -= 1
        else:
            sys.stdout.write("Trolling In: " + str(t) +"\n")
            sys.stdout.flush()
            time.sleep(20)
            t -= 20
    print('Troll comencing! \n \n \n \n \n')


class CallbotServer:
    def __init__ (self, host="localhost", port=60001, masterHost = "localhost", masterPort=60000 ) :
        self.host = host
        self.port = port
        self.masterHost = masterHost
        self.masterPort = masterPort


        try:
            self.callbotServer = self.startServer(self.host, self.port)

        except Exception:
            self.callbotServer = None
            #print "Socket Error"

        try:
            self.masterServer = self.connectToSever(self.masterHost, self.masterPort)

        except Exception:
            self.masterServer = None
            #print "Couldn't Connect to master Server"
            try:
                self.receiveData()
            except Exception:
                print ""

    def startServer ( self, host, port ):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind ( (host, port) )
            #print "created Socket"
            return serverSocket #serverSocket = self.socket
        except Exception:
            #print "Couldn't start socket"
            return None

    #for client connections
    def connectToSever(self, host, port):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.connect(  (host, port) )
            #print "connected to server: " + host +  port
            return serverSocket

        except Exception:
            #print "Could not connect to the server"
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

    # pass message to master
    def sendMessageToMaster(self, message):
        self.masterServer.send(message)

    def __del__(self):
        if self.masterServer != None:
            self.masterServer.close()

        if self.callbotServer != None:
            self.callbotServer.close()


class configSetup:

    configFile = "config.txt" #static

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.configFile)

    def readValue(self):
        self.config.read(self.configFile)
        numbers = self.config.get('callbot','numbers').split()
        visibleBrowser = self.config.get("callbot", "visibleBrowser")
        self.callbot = callbotConfig (numbers, visibleBrowser)
        self.masterHost = self.config.get('server', 'masterHost')
        self.masterPort = self.config.get('server', 'masterPort')
        self.callbotHost = self.config.get('server', 'callbotHost')
        self.callbotPort = self.config.get('server', 'callbotPort')

class CallingBot:

    def __init__ (self, numbers, visibility):
        self.numbers = numbers
        self.visibility = visibility

    def CallPeople(self):
        victim = random.choice(self.numbers)
        if len(self.numbers) ==2:
            self.n1 = self.numbers[0]
            self.id1 = self.numbers[0]
            self.n2 = self.numbers[1]
            self.id2 = self.numbers[1]

        elif len(self.numbers) <2:
            self.n1 = self.numbers[0]
            self.id1 = self.numbers[0]
            self.id2 = self.numbers[0]
            self.n2 = self.numbers[0]
        else:
            self.n1 = random.choice(self.numbers)
            self.numbers.remove(self.n1)
            self.n2 = random.choice(self.numbers)
            self.numbers.remove(self.n2)
            self.id1 = random.choice(self.numbers)
            self.id2 = random.choice(self.numbers)

        cmdArguments = self.call()
        return cmdArguments

    def CallThemselves(self):
        victim = random.choice(self.numbers)
        self.n1 = victim
        self.n2 = victim
        self.id1 = random.choice(self.numbers)
        self.id2 = random.choice(self.numbers)
        cmdArguments = self.call()
        return cmdArguments


    def call(self):
        cmdArguments = "python"
        cmdArguments += " callbot.py"
        cmdArguments += ' -n1 ' + str(self.n1)
        cmdArguments +=  " -id1 " + str(self.id1)
        cmdArguments += " -n2 " + str(self.n2)
        cmdArguments +=  " -id2 " + str(self.id2)
        cmdArguments +=  " -v " + str(self.visibility)
        cmdArguments = list( cmdArguments.split() )

        return cmdArguments



def callbotWrapper(config, callbotServer):
    config.readValue()
    relativePath ="callbot"
    counter = 0
    callbot =  CallingBot(config.callbot.numbers, config.callbot.visibleBrowser)
    #get working directory
    origWD = os.getcwd()
    #change directory
    os.chdir(os.path.join(os.path.abspath(origWD),relativePath))

    while counter < 5 :
        cmdArguments = callbot.CallPeople()
        p1 = subprocess.Popen(cmdArguments)
        #callbotServer.sendMessageToMaster(message)
        counter += 1

    os.chdir (origWD )


if __name__ == "__main__":
    secondsInDay = 86400
    config = configSetup()
    #passes ports and server information to the callbot server
    callbotServer = CallbotServer()
    callbotWrapper(config, callbotServer)
