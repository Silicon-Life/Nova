import asyncio

class Publisher:
    def __init__(self, topic):
        self.topic = topic
        self.subscribers = []

    def publish(self, message):
        for subscriber in self.subscribers:
            asyncio.create_task(subscriber.receive(message))

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)
