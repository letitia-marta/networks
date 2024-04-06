import socket

def deznodamant (alegere1, alegere2):
        if alegere1 == alegere2:
                return "Remiza"
        elif (alegere1 == "piatra" and alegere2 == "foarfeca") or (alegere1 == "foarfeca" and alegere2 == "hartie") or (alegere1 == "hartie" and alegere2 == "piatra"):
                return "Jucator1 a castigat"
        else:
                return "Jucator2 a castigat"

def main():
        host = "127.0.0.1"
        port = 9999

        s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        s.bind ((host, port))
        s.listen(2)

        conn1, addr1 = s.accept()
        print ("Jucator1 s-a conectat.")
        conn1.send ("Esti Jucator1.".encode())

        conn2, addr2 = s.accept()
        print ("Jucator2 s-a conectat.")
        conn2.send ("Esti Jucator2.".encode())

        while True:
                alegere1 = conn1.recv(1024).decode().lower()
                alegere2 = conn2.recv(1024).decode().lower()

                if alegere1 and alegere2:
                        dezn = deznodamant (alegere1, alegere2)
                        if dezn == "Remiza":
                                conn1.send("Remiza".encode())
                                conn2.send("Remiza".encode())
                                continue
                        else:
                                rez = "Deznodamant: " + dezn
                                conn1.send (rez.encode())
                                conn2.send (rez.encode())
                
                joc_nou1 = conn1.recv(1024).decode().lower()
                joc_nou2 = conn2.recv(1024).decode().lower()
                if joc_nou1 == "nu" or joc_nou2 == "nu":
                        conn1.send ("Game over".encode())
                        conn2.send ("Game over".encode())
                        break

        conn1.close()
        conn2.close()
        s.close()

if __name__ == "__main__":
        main()
