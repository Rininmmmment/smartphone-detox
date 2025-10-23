import asyncio
from bleak import BleakClient
from common.const import Const

class SwitchBot:
    def __init__(self, mac_address: str):
        self.mac_address = mac_address

    async def _send_command(self, command_bytes: bytes):
        async with BleakClient(self.mac_address) as client:
            await client.write_gatt_char(Const.CHARACTERISTIC, command_bytes)

    async def turn_on(self):
        await self._send_command(bytes([0x57, 0x01, 0x00]))
        print("SwitchBot ON")
