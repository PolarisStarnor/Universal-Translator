import socket
import speech_to_text
import text_cleanup
import translation
import pathlib
import asyncio
import time
import re
from concurrent.futures import ThreadPoolExecutor
import text_to_speech

def server_program(sending : bool = False):
    conn, address = connect()
    try:
        connect_recieve(conn)
    except KeyboardInterrupt:
        conn.close()
        exit()


def connect_recieve(conn):
    while True:
        # recieve the data
        filename = "audio.mp3"
        # i = 0;
        with conn, open(filename, 'wb') as mp3:
            while True:
                # i += 1
                try:
                    # print("iteration")
                    data = conn.recv(2048)
                    if not data: break
                    mp3.write(data)
                except:
                    break

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
        to_language = 'de'
        from_language = 'en'
        text = translation.translate(text, from_language, to_language)
        print(text)
        # text = text_cleanup.clean(text)
        # print(text)
        # text = text_cleanup.rephrase(text)
        # print(text)

        # print(''.join(text))
        print("--------- Final Output ---------")
        print(text)
        print("--------- ------------ ---------")

        filename = text_to_speech.google_tts(text, to_language)

        # send_data(conn, text)
        conn.close()
        # conn.send(text.encode())

def decode_to_mp3(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    return pathlib.Path(filename)

def cleanup(name: str):
   path = pathlib.Path(name)
   path.unlink()

def send_data(conn, text: str):
    try:
        send_me(text, conn)
    except KeyboardInterrupt:
        conn.close()
        exit()

def send_me(text: str):
    i = 0;
    while i < 4096:
        i += 1
        conn.send(text.encode(encoding='utf-8'))
    conn.close()

def connect():
    host = ""
    port = 14000

    server_socket = socket.socket()
    # bind the socket to the port
    server_socket.bind((host, port))

    server_socket.listen(2) #2 listeners at once
    # Accepting new connection
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))

    return conn, address

if __name__ == '__main__':
    while True:
        server_program()
