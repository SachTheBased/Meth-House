import json
import asyncio
import websockets

clients = set()
secret_key = "METH_HOUSE-9999"

print("starting")

async def echo(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            if message['secret_key'] == secret_key:
                message = json.loads(message)
                if message['type'] == 'grow':
                    msg = json.dumps({'type': 'grow', 'drug': message['drug']})
                elif message['type'] == 'smoke':
                    msg = json.dumps({'type': 'smoke', 'drug': message['drug']})
                for client in clients:
                    await client.send(msg)
    except websockets.exceptions.ConnectionClosed as e:
        clients.remove(websocket)

start_server = websockets.serve(echo, "0.0.0.0", 9999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()