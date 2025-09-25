from tapo import ApiClient
import asyncio
from time import sleep

async def main():
    client = ApiClient("rinr10693otes@gmail.com", "krukb8dog")
    device = await client.p110("192.168.11.7")
    await device.on()   # デバイスをONにする
    sleep(10)
    await device.off()

asyncio.run(main())
