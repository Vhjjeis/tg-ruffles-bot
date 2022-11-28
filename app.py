from handlers import dp
from loader import bot, executor
import logger
from loops import thread_ruffles
import asyncio


ruffles_loop = asyncio.get_event_loop()
ruffles_loop.create_task(thread_ruffles())

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
