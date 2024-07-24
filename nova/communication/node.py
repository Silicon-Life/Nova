import asyncio
from .publisher import Publisher
from .subscriber import Subscriber
from .service import Service
from .action import Action

class Node:
    def __init__(self, name):
        self.name = name
        self.publishers = {}
        self.subscribers = {}
        self.services = {}
        self.actions = {}

    def create_publisher(self, topic):
        pub = Publisher(topic)
        self.publishers[topic] = pub
        return pub

    def create_subscription(self, topic, callback):
        sub = Subscriber(topic, callback)
        self.subscribers[topic] = sub
        return sub

    def create_service(self, service_name, callback):
        service = Service(service_name, callback)
        self.services[service_name] = service
        return service

    def create_action(self, action_name, callback):
        action = Action(action_name, callback)
        self.actions[action_name] = action
        return action

    async def run(self):
        while True:
            # Simulate the node's activity
            await asyncio.sleep(1)
