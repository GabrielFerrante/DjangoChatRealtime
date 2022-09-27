from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):

    #função assincrona
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['nome_sala']
        self.room_group_name = f'chat_{self.room_name}'

        #entrar na sala
        #await = Necessário para funções assincronas
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def desconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.room_name
        )

    
    #recebe mensagem do websocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        mensagem = text_data_json['mensagem']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message' : mensagem
            }
        )

    
    #recebe a mensagem da sala

    async def chat_message(self, event):
        mensagem = event['message']

        await self.send(text_data=json.dumps({
            'mensagem':mensagem
        }))

