"""
    Listens on a socket and speaks received messages
    through a text-to-speech interface.
"""

import socket
import selectors
import types

import fire

from tts import DummyVoice

def accept_wrapper(sock, selector):
    conn, addr = sock.accept()
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, msg='')
    selector.register(conn, selectors.EVENT_READ, data=data)

def service_connection(key, mask, selector, separator, voice):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            msg = recv_data.decode('utf-8')
            sep_idx = msg.find(separator)
            if sep_idx == -1:
                data.msg += msg
            else:
                voice.speak(msg[:sep_idx])
                print('>{}<'.format(msg[:sep_idx]))
                data.msg += msg[sep_idx:]
        else:
            print('closing connection to', data.addr)
            selector.unregister(sock)
            sock.close()

def main(host='', port=4444, sep='\n', lang='cs-CZ', rate=100):
    voice = DummyVoice(lang=lang, rate=rate)
    sel = selectors.DefaultSelector()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, data=None)

    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj, sel)
            else:
                service_connection(key, mask, sel, sep, voice)

if __name__ == "__main__":
    fire.Fire(main)