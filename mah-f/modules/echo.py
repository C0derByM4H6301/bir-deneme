import os

def main():
    ip = input("IP adresini girin: ")
    os.system("ping {} -c 4".format(ip))
