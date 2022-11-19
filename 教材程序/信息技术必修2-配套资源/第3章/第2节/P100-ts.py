#code=utf-8
import asyncio
import websockets

cs = set()
async def talk(websocket, path):
    try:
        while True:
            if (not websocket in cs):
                cs.add(websocket)
                msg='欢迎:'+str(websocket.remote_address);
            else:
                msg = str(websocket.remote_address)+'说:'+str(await websocket.recv());
            await asyncio.wait([ws.send(msg) for ws in cs])
    except Exception as err:
        cs.remove(websocket);




start_server = websockets.serve(talk, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
