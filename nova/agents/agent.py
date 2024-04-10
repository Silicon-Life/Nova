import asyncio
from abc import ABC, abstractmethod
from typing import Dict, Any, Callable

class Agent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.skills: Dict[str, Callable] = {}
        self.state: Dict[str, Any] = {}
        self.communicator = None
        self.environment = None
        self.plugins: Dict[str, Any] = {}
    
    @abstractmethod
    async def perceive(self):
        pass

    @abstractmethod
    async def decide(self):
        pass

    @abstractmethod
    async def act(self):
        pass

    async def learn(self, feedback: Any):
        pass

    def communicate(self, message: Any):
        if self.communicator:
            self.communicator.send(message)

    def add_skill(self, skill_name: str, skill_func: Callable):
        self.skills[skill_name] = skill_func

    def use_plugin(self, plugin_name: str, **kwargs):
        if plugin_name in self.plugins:
            self.plugins[plugin_name](**kwargs)
        else:
            print(f"Plugin {plugin_name} not found.")

    def update_state(self, new_state: Dict[str, Any]):
        self.state.update(new_state)

    async def run(self):
        while True:
            await self.perceive()
            await self.decide()
            await self.act()
            await asyncio.sleep(1)

    def register_plugin(self, plugin_name: str, plugin_func: Callable):
        self.plugins[plugin_name] = plugin_func

    def setup_communicator(self, communicator: Any):
        self.communicator = communicator

    def setup_environment(self, environment: Any):
        self.environment = environment

