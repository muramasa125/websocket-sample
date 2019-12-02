import asyncio
import websockets
import io

class WebSockets_Server:

    def __init__(self, loop, address , port, text):
        self.loop = loop
        self.address = address
        self.port = port
        self.text = text

    async def _handler(self, websocket, text):
        while True:
          recv_data = await websocket.recv()
          send_message = text + ':' + recv_data
          await websocket.send(send_message)
          print(send_message)

    def run(self):
        self._server = websockets.serve(self._handler, self.address, self.port)
        print('websocket-server start...')
        self.loop.run_until_complete(self._server)
        self.loop.run_forever()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    wss = WebSockets_Server(loop, '127.0.0.1', 60000, 'websocket-server通信成功!!')
    wss.run()