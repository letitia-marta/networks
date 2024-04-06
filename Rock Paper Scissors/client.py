import socket

def main():
        host = "127.0.0.1"
        port = 9999

        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.connect ((host, port))

        jucator = s.recv(1024).decode()
        print (jucator)

        while True:
                alegere = input ("Alege (\"piatra\", \"foarfeca\", \"hartie\"): ").lower()
                s.send (alegere.encode())

                rez = s.recv(1024).decode()
                if rez == "Remiza":
                        print ("Remiza. Alege din nou")
                        continue

                print (rez)

                if rez.startswith ("Deznodamant"):
                        joc_nou = input ("Vrei sa joci din nou? (\"da\"/\"nu\") ").lower()
                        s.send(joc_nou.encode())
                        if joc_nou != "da":
                                go = s.recv(1024).decode()
                                print (go)
                                break

        s.close()

if __name__ == "__main__":
        main()
