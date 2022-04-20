"""
Summart:
    Connect to FTP and run commands using Python socket library
"""
import socket


def recv(s):
    while True:
        data = s.recv(4096)
        data = data.decode()
        print(data)
        print(f"data len: {len(data)}")
        if len(data) < 4096:
            break


def send(s, data):
    s.sendall(f"{data}\r\n".encode())
    recv(s)


def main():
    netloc = "ftp.vim.org"
    port = 21
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((netloc, port))

    recv(s)
    print("LOGGING IN".center(50, "-"))
    send(s, "USER anonymous")
    send(s, "PASS anonymous")
    print("LISTING".center(50, "-"))
    send(s, "HELP")
    send(s, "QUIT")
    s.close()


if __name__ == "__main__":
    main()
