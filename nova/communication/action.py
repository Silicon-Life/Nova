class Action:
    def __init__(self, action_name, callback):
        self.action_name = action_name
        self.callback = callback

    async def execute(self, goal):
        return await self.callback(goal)
