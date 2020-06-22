import asyncio

from confluent_kafka import Consumer


async def consume(topic_name):
    c = Consumer({"bootstrap.servers": "localhost:19092", "group.id": "0"})
    c.subscribe(["com.luka.project2"])
    
    while True:
        messages = c.consume(5, timeout=1.0)
        
        for msg in messages:
            if msg is None:
                print('no msg')
            elif msg.error() in not None:
                print(f'Error: {msg.error()}')
            else:
                print(f'{msg.value()}\n')


def run_consumer():
    try:
        asyncio.run(consume("com.luka.project2"))
        
    except KeyboardInterrupt as e:
        print("Shutting down...")

if __name__ == '__main__':
    run_consumer()