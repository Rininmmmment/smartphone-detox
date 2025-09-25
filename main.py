import cv2, time, requests, asyncio
from picamera2 import Picamera2
from pyzbar.pyzbar import decode
import pygame
from switchbot import SwitchBot

QRCODE_TEXT = "nekochan_on_the_roomba"
MAC_ADDRESS = "D0:35:33:34:14:67"
ALARM_SOUND_NAME = "alarm.mp3"

EXECUTE_INTERVAL_SEC = 10

async def main():
	"""
	初期設定
	"""
	# カメラ
	picam2 = Picamera2()
	picam2.start()

    # アラーム音
	pygame.mixer.init()
	pygame.mixer.music.load(ALARM_SOUND_NAME)

    # SwitchBot
	bot = SwitchBot(MAC_ADDRESS)
		
		
	"""
	監視処理
	"""
	while True:
		frame = picam2.capture_array()
		codes = decode(frame)
		
		# 正しいQRコードがある
		if codes:
			text = codes[0].data.decode("utf-8")
			if text == QRCODE_TEXT:
				print("Correct QR!!!!")
				pygame.mixer.music.stop()
				
		# 正しくないQRコードがある or 何もない
		else:
			print("NO QR CODE!!")
			await bot.turn_on()
			if not pygame.mixer.music.get_busy():
				pygame.mixer.music.play()
				
		time.sleep(EXECUTE_INTERVAL_SEC)

		cv2.imshow("frame", frame)

	cv2.destroyAllWindows()

asyncio.run(main())
