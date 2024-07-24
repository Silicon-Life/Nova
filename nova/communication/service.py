class Service:
    def __init__(self, service_name, callback):
        self.service_name = service_name
        self.callback = callback

    async def call(self, request):
        return await self.callback(request)
