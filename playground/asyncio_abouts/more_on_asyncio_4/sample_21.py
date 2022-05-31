import asyncio
import concurrent.futures
import logging
import queue
import random
import string
import time
import uuid

import attr

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s,%(msecs)s %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)


@attr.s
class PubSubMessage:
    instance_name = attr.ib()
    message_id = attr.ib(repr=False)
    hostname = attr.ib(repr=False, init=False)

    def __attrs_post_init__(self):
        self.hostname = f"{self.instance_name}.example.net"


def publish_sync(q):
    choices = string.ascii_lowercase + string.digits

    while True:
        msg_id = str(uuid.uuid4())
        host_id = "".join(random.choices(choices, k=4))
        instance_name = f"cattle-{host_id}"
        msg = PubSubMessage(message_id=msg_id, instance_name=instance_name)
        # publish an item
        q.put(msg)
        logging.info(f"published {msg}")
        # simulate randomness of publishing messages
        time.sleep(random.random())


def consume_sync(q):
    while True:
        # wait for an item from the publisher
        msg = q.get()
        # process the message
        logging.info(f"consumed {msg}")
        # substitute for handling a message
        time.sleep(random.random())


async def publish(executor, q):
    logging.info("starting publisher")
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(executor, publish_sync, q) for i in range(5)]
    asyncio.ensure_future(asyncio.gather(*futures, return_exceptions=True))


async def consume(executor, q):
    logging.info("starting consumer")
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(executor, consume_sync, q) for i in range(5)]
    asyncio.ensure_future(asyncio.gather(*futures, return_exceptions=True))


def main():
    executor = concurrent.futures.ThreadPoolExecutor()
    loop = asyncio.get_event_loop()
    q = queue.Queue()

    try:
        loop.create_task(publish(executor, q))
        loop.create_task(consume(executor, q))
        loop.run_forever()
    finally:
        loop.close()
        logging.info("successfully shutdown the Mayhem service.")


if __name__ == "__main__":
    main()
