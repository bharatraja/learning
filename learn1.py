# import selectors
# import socket
# from selectors import SelectorKey
# from typing import List, Tuple
 
# selector = selectors.DefaultSelector()
 
# server_socket = socket.socket()
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
# server_address = ('127.0.0.1', 8000)
# server_socket.setblocking(False)
# server_socket.bind(server_address)
# server_socket.listen()
 
# selector.register(server_socket, selectors.EVENT_READ)
 
# while True:
#     events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)  
 
#     if len(events) == 0:                                                
#         #print('No events, waiting a bit more!')
#         pass
 
#     for event, _ in events:
#         event_socket = event.fileobj                                    
 
#         if event_socket == server_socket:                               
#             connection, address = server_socket.accept()
#             connection.setblocking(False)
#             print(f"I got a connection from {address}")
#             selector.register(connection, selectors.EVENT_READ)         
#         else:
#             data = event_socket.recv(1024)                              
#             print(f"I got some data: {data}")
#             #event_socket.send(data)
import asyncio
import socket
from asyncio import AbstractEventLoop
async def echo(connection: socket,
               loop: AbstractEventLoop) -> None:
    buffer=b''
    while data := await loop.sock_recv(connection, 1024):
        if data == b'boom\r\n':
            raise Exception("Unexpected network error")
        
        if data[-2:] != b'\r\n':
            buffer = buffer + data 
        await loop.sock_sendall(connection, buffer+ b'\r\n')
        buffer=b''                        
 
 
async def listen_for_connection(server_socket: socket,
                                loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Got a connection from {address}")
        asyncio.create_task(echo(connection, loop))                      
 
 
async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
 
    await listen_for_connection(server_socket, asyncio.get_event_loop()) 
 
asyncio.run(main())