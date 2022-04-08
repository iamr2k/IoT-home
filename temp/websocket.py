import time
import json
from api.check import check
async def websocket_application(scope, receive, send):
    while True:
        
        event = await receive()

        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept',
            })

        if event['type'] == 'websocket.disconnect':
            break

        if event['type'] == 'websocket.receive':
            result = check()
            temp = result.get("temperature")
            humidity= result.get("humidity")
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': json.dumps({"temp": temp, "humidity": humidity})

                })
            