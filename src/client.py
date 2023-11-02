# client.py
import asyncio
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory

# class MyClientProtocol(WebSocketClientProtocol):
#     async def onConnect(self, response):
#         print(f"Server connected: {response.peer}")
#         self.sendMessage(b"Hello, server!")  # You can send a message when connected

#     def onOpen(self):
#         print("WebSocket connection open.")

#     def onMessage(self, payload, isBinary):
#         if not isBinary:
#             message = payload.decode("utf8")
#             print(f"Text message received: {message}")

#     def onClose(self, wasClean, code, reason):
#         print(f"WebSocket connection closed: {reason}")

# async def run_client():
#     factory = WebSocketClientFactory("ws://127.0.0.1:9000")
#     factory.protocol = MyClientProtocol

#     loop = asyncio.get_event_loop()
#     coro = loop.create_connection(factory, "127.0.0.1", 9000)
#     transport, protocol = await coro  # Get the protocol instance

#     while True:
#         message = input("Enter a message: ")
#         if message.lower() == "exit":
#             break
#         protocol.sendMessage(message.encode("utf8"))  # Send the message through the protocol

# if __name__ == "__main__":
#     try:
#         asyncio.run(run_client())
#     except KeyboardInterrupt:
#         pass

#!/usr/bin/python

# from websockets import create_connection
# ws = create_connection("ws://127.0.0.1:9000")
# print ("Sending 'Hello, World'...")
# ws.send("Hello, World")
# print ("Sent")
# print ("Receiving...")
# result =  ws.recv()
# print ("Received '%s'" % result)
# ws.close()

# client.py
import asyncio
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory

class MyClientProtocol(WebSocketClientProtocol):
    async def onConnect(self, response):
        print(f"Server connected: {response.peer}")
        self.sendMessage(b"Hello, server!")  # You can send a message when connected

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if not isBinary:
            message = payload.decode("utf8")
            print(f"Text message received: {message}")

    def onClose(self, wasClean, code, reason):
        print(f"WebSocket connection closed: {reason}")

async def run_client():
    factory = WebSocketClientFactory("ws://127.0.0.1:9000", protocols=["wamp.2.json"])  # Specify the subprotocol here
    factory.protocol = MyClientProtocol
    # factory.setProtocolOptions(subprotocol="wamp.2.json")

    loop = asyncio.get_event_loop()
    transport, protocol = await loop.create_connection(factory, "127.0.0.1", 9000)  # Get the protocol instance

    while True:
        message = input("Enter a message: ")
        if message.lower() == "exit":
            break
        try:
            factory.protocol.sendMessage(message.encode("utf8"))  # Send the message through the protocol

        except Exception as e:
            print(f"Error sending message: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(run_client())
    except KeyboardInterrupt:
        pass

