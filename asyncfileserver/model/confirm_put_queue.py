import asyncio


class ConfirmPutQueue(object):
    def __init__(self, arbiter, queue=asyncio.Queue()):
        self._arbiter = arbiter
        self._queue = queue

    async def get(self) -> bytes:
        item: bytearray = await self._queue.get()
        return bytes(item) if item != None else None

    def task_done(self):
        self._queue.task_done()

    async def put(self, item: bytearray):
        if await self._arbiter.process(item):
            await self._queue.put(item)
