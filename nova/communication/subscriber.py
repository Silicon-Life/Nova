class Subscriber:
    def __init__(self, topic, callback):
        self.topic = topic
        self.callback = callback

    async def receive(self, message):
        await self.callback(message)
