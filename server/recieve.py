import socket
import speech_to_text
import text_cleanup
import translation
import pathlib
import asyncio
import re
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


def connect(conn):
    while True:
        # recieve the data
        filename = "audio.mp3"
        with conn, open(filename, 'wb') as mp3:
            while True:
                data = conn.recv(2048)
                if not data: break
                mp3.write(data)

        p = re.compile('After:.*?\n')

        filepath = pathlib.Path(filename)
        text = speech_to_text.transcribe(filepath)
        print(text)
        cleanup(filepath)

        try:
            text = p.findall(text_cleanup.eliminate_repetitions(text))[0][7:]
        except IndexError:
            continue
        print(text)
        text = translation.translate(text, 'en', 'de')
        print(text)
        # text = text_cleanup.clean(text)
        # print(text)
        # text = text_cleanup.rephrase(text)
        # print(text)

        # print(''.join(text))
        print("--------- Final Output ---------")
        print(text)
        print("--------- ------------ ---------")

        conn.send(bytes(text))

        conn.close()

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
