
from mimetypes import init
from channels.consumer import AsyncConsumer


class BoardConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        board_room = "boardroom"
        self.board_room = board_room
        await self.channel_layer.group_add(
            board_room, self.channel_name
        )
        await self.send({
            "type" : "websocket.accept"
        })

    async def websocket_receive(self , event):
        initial_data = event.get("text" , None)

        await self.channel_layer.group_send(
            self.board_room,{
                "type": "board_message",
                "text" : initial_data

            }
        )

    async def board_message(self ,event):
        await self.send({
            "type" : "websocket.send",
            "text" : event['text0']
        })

    
    async def websocket_disconnect(self , event):
        print('Disconnect' , event)