import argparse
import socket
from datetime import datetime

def server(port):
    x = "Your choice was server and it will run on port " + str(port)
    return x

def client(port):
    x = "Your choice was client and it will run on port " + str(port)
    return x

if __name__ == "__main__":
    choices = {"client": client, "server" : server}
    parser = argparse.ArgumentParser(description="Send and recieve UDP locally")
    parser.add_argumnet("role", choices=choices, help="Which role to play")
    parser.ads_argument("-p", metavar="PORT", type=int, default=1060, help="UDP port (default 1060)")

args = parser.parse_args()
function = choices[args.role]
print(function(args.p))

