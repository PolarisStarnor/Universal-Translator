import socket
import speech_to_text
import text_cleanup
import translation
import pathlib
import asyncio
from concurrent.futures import ThreadPoolExecutor
# import text_to_speech

def server_program():
    host = ""
    port = 14000

    server_socket = socket.socket()
    # bind the socket to the port
    server_socket.bind((host, port))

    server_socket.listen(2) #2 listeners at once
    # Accepting new connection
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))
    try:
        connect(conn)
    except KeyboardInterrupt:
        conn.close()
        exit()

    conn.close()

def connect(conn):
    while True:
        # recieve the data
        filename = "audio.mp3"
        with conn, open(filename, 'wb') as mp3:
            while True:
                data = conn.recv(2048)
                if not data: break
                mp3.write(data)

        filepath = pathlib.Path(filename)
        text = speech_to_text.transcribe(filepath)

        text = text_cleanup.eliminate_repetitions(text)
        text = text_cleanup.clean(text)
        # text = text_cleanup.rephrase(text)

        cleanup(filepath)

        print(text)

        conn.detach()

        # conn.send(text.encode())

def decode_to_mp3(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    return pathlib.Path(filename)

def cleanup(name: str):
   path = pathlib.Path(name)
   path.unlink()

if __name__ == '__main__':
    while True:
        server_program()
