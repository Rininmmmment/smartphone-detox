import asyncio
from bleak import BleakClient

class SwitchBot:
    CHARACTERISTIC = "cba20002-224d-11e6-9fb8-0002a5d5c51b"

    def __init__(self, mac_address: str):
        self.mac_address = mac_address

    async def _send_command(self, command_bytes: bytes):
        async with BleakClient(self.mac_address) as client:
            await client.write_gatt_char(self.CHARACTERISTIC, command_bytes)

    async def turn_on(self):
        """SwitchBot を ON にする"""
        await self._send_command(bytes([0x57, 0x01, 0x00]))
        print("SwitchBot ON")
