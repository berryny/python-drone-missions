import socket
import threading
import time

tello_address = ('', 8889)
local_address = ('', 9000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(local_address)


def send(message, delay):
    try:
        sock.sendto(message.encode(), tello_address)
        print("Sending message: " + message)
    except Exception as e:
        print("Error sending: " + str(e))

    time.sleep(delay)


def receive():
    while True:
        try:
            response, ip_address = sock.recvfrom(128)
            print("Received message: " + response.decode(encoding='utf-8'))
        except Exception as e:
            sock.close
            print("Error receiving: " + str(e))
            break


receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start

#Box Mission
box_leg_distance = 100
yaw_angle = 90
yaw_direction = "cw"
send("command", 3)
send("takeoff", 5)
for i in range(4):
    send("forward " + str(box_leg_distance), 4)
    send("cw " + str(yaw_angle), 3)
send("land", 5)
sock.close()

#Backflip Mission
send("command", 3)
send("takeoff", 5)
send("flib b", 4)
send("land", 5)
sock.close()

#Door mission
doorlength = 127
doorwidth = 91.44
send("command", 3)
send("takeoff", 5)
send("up" + str(doorlength / 2), 4)
send("right" + str(doorwidth), 4)
send("down" + str(doorlength), 4)
send("left" + str(doorwidth), 4)
send("up" + str(doorlength / 2), 4)
send("land", 5)
sock.close()

#Window Mission
windowLength = 127
windowWidth = 91.44
send("command", 3)
send("takeoff", 5)
send("left" + str(windowLength / 2), 4)
send("up" + str(windowWidth), 4)
send("right" + str(windowLength), 4)
send("down" + str(windowWidth), 4)
send("left" + str(windowLength / 2), 4)
send("land", 5)
sock.close()

#Turning Door Mission
doorlength = 127
doorwidth = 91.44
yawangle = 90
send("command", 3)
send("takeoff", 5)
send("up" + str(doorlength / 2), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(doorwidth), 4)
send("cw " + str(yawangle), 3)
#send(___, 5)
send("down" + str(doorlength), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(doorwidth), 4)
send("cw " + str(yawangle), 3)
#send(___, 5)
send("up" + str(doorlength / 2), 4)
send("land", 5)
sock.close()

#Turning Window Mission
windowLength = 127
windowWidth = 91.44
yawangle = 90
send("command", 3)
send("takeoff", 5)
send("left" + str(windowLength / 2), 4)
send("cw " + str(yawangle), 3)
send("up" + str(windowWidth), 4)
send("cw " + str(yawangle), 3)
send("right" + str(windowLength), 4)
send("cw " + str(yawangle), 3)
send("down" + str(windowWidth), 4)
send("cw " + str(yawangle), 3)
send("left" + str(windowLength / 2), 4)
send("land", 5)
sock.close()

#Coded Landing Mission
flightdistance = input("Enter flight distance in inches ")
send("command", 3)
send("takeoff", 5)
send("forward" + str(flightdistance * 2.54), 4)
send("land", 5)
sock.close()

#Equilateral Triangle Mission
trianglelength = 91.44
yawangle = 120
send("command", 3)
send("takeoff", 5)
send("forward " + str(trianglelength), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(trianglelength), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(trianglelength), 4)
send("land", 5)
sock.close()

#Star Mission
forwardlength = 127
yawangle = 144
send("command", 3)
send("takeoff", 5)
for i in range(5):
    send("forward " + str(forwardlength), 4)
    send("cw " + str(yawangle), 3)
send("land", 5)
sock.close()

#Turning Box Mission
boxlength = 76.2
yawangle = 90
send("command", 3)
send("takeoff", 5)
send("forward " + str(boxlength), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(boxlength), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(boxlength), 4)
send("cw " + str(yawangle), 3)
send("forward " + str(boxlength), 4)
send("cw " + str(yawangle), 3)
send("land", 5)
sock.close()

#Loop Box Mission
boxlength = 76.2
yawangle = 90
send("command", 3)
send("takeoff", 5)
for i in range(4):
    send("forward " + str(boxlength), 4)
    send("cw " + str(yawangle), 3)
send("land", 5)
sock.close()
