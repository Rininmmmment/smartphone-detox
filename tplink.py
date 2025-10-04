from tapo import ApiClient
import asyncio
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("TPLINK_USERNAME")
PASSWORD = os.getenv("TPLINK_PASSWORD")
IP_ADDRESS = os.getenv("TPLINK_IP")

async def main():
    client = ApiClient(USERNAME, PASSWORD)
    device = await client.p110(IP_ADDRESS)
    await device.on()   # デバイスをONにする
    sleep(10)
    await device.off()

asyncio.run(main())
