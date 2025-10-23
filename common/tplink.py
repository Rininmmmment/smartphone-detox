from tapo import ApiClient
import asyncio
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    client = ApiClient(
        os.getenv("TPLINK_USERNAME"), 
        os.getenv("TPLINK_PASSWORD")
    )
    device = await client.p110(os.getenv("TPLINK_IP"))
    await device.on()   # デバイスをONにする
    sleep(10)
    await device.off()

asyncio.run(main())
