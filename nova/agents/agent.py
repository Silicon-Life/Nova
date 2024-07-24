import asyncio
from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, name, role, communication_manager):
        self.name = name
        self.role = role
        self.communication_manager = communication_manager
        self.skills = {}
        self.state = {}
        self.plugins = {}

    @abstractmethod
    async def perceive(self):
        pass

    @abstractmethod
    async def decide(self):
        pass

    @abstractmethod
    async def act(self):
        pass

    async def learn(self, feedback):
        pass

    def communicate(self, topic, message):
        publisher = self.communication_manager.create_publisher(self.name, topic)
        publisher.publish(message)

    def add_skill(self, skill_name, skill_func):
        self.skills[skill_name] = skill_func

    def use_plugin(self, plugin_name, **kwargs):
        if plugin_name in self.plugins:
            self.plugins[plugin_name](**kwargs)
        else:
            print(f"Plugin {plugin_name} not found.")

    def update_state(self, new_state):
        self.state.update(new_state)

    async def run(self):
        while True:
            await self.perceive()
            await self.decide()
            await self.act()
            await asyncio.sleep(1)

    def register_plugin(self, plugin_name, plugin_func):
        self.plugins[plugin_name] = plugin_func

    def setup_communicator(self, communicator):
        self.communication_manager = communicator
