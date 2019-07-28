import asyncio
import json
from aio_pika import connect_robust


async def consume_qq(channel):
    qq = await channel.declare_queue("qq")
    async with qq.iterator() as queue_iter:
        async for message in queue_iter:
            await kek(message=message)


async def queues_consuming_app():
    connection = await connect_robust(host="localhost")
    channel = await connection.channel()
    print(f"Got connection {connection}")
    print(f"Got channel {channel}")

    # Consumer-level error-handling
    while True:
        try:
            print("Starting to consume QQ")
            await consume_qq(channel=channel)
        except Exception as e:
            print(f"CRITICAL ERROR IN CUNSUMER OF QQ: [ {e} ]")
            await asyncio.sleep(7)


async def kek(message=None, text=None):
    await asyncio.sleep(3)
    if message:
        async with message.process(requeue=True, reject_on_redelivered=True):
            print(f'Got message: {json.loads(getattr(message, "body", b"{}").decode())}')
    else:
        print(f"No messege, text is {text}")


all_consumers = (
    queues_consuming_app(),
    kek(text="lol"),
)
