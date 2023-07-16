import asyncio
import time

from app.pkg.kafka.producer import *
from app.pkg.kafkalogger.logger import *

logger = setup_custom_logger('root')


async def main():
    newKafkaClient = Kafka.NewProducer()
    await Kafka.Produce(newKafkaClient)


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
