import cv2, time, requests, asyncio, random
from datetime import datetime
from picamera2 import Picamera2
from pyzbar.pyzbar import decode
import pygame
import jpholiday
from switchbot import SwitchBot
from dotenv import load_dotenv
import os

load_dotenv()

QRCODE_TEXT = "nekochan_on_the_roomba"
MAC_ADDRESS = os.getenv("MAC_ADDRESS")
ALARM_SOUND_NAME = "/home/rininmmmment/smartphone-detox/alarm.mp3"
MOS_SOUND_NAME = "/home/rininmmmment/smartphone-detox/mos39.mp3"

interval = random.randint(90, 900)

async def main():
	"""
	初期設定
	"""
	# カメラ
	picam2 = Picamera2()
	picam2.start()

    # アラーム音
	pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
	pygame.mixer.init()
	mos = pygame.mixer.Sound(MOS_SOUND_NAME)
	channel_mos = pygame.mixer.Channel(0)
	alarm = pygame.mixer.Sound(ALARM_SOUND_NAME)
	channel_alarm = pygame.mixer.Channel(1)

    # SwitchBot
	bot = SwitchBot(MAC_ADDRESS)
	
	# 土日か祝日か判定
	today = datetime.today()
	is_weekend = today.weekday() >= 5  # 5=土曜, 6=日曜
	is_holiday = jpholiday.is_holiday(today.date())
	if is_weekend or is_holiday:
		print("Holiday!!!")
		return
	
	"""
	監視処理
	"""
	interval = 5
	# スマホ使用回数
	smartphone_count = 0
	# スマホ無しで過ごした時間(s)
	detox_time = 0
	
	while True:
		frame = picam2.capture_array()
		codes = decode(frame)
		# cv2.imshow("frame", frame)

		print('----------------------------')
		print(today)
		print('interval: ', interval)
		print('detox_time: ', detox_time)
		print('smartphone_count: ', smartphone_count)
		print('----------------------------')
		
		time.sleep(interval)
		
		# 正しいQRコードがある
		if codes:
			text = codes[0].data.decode("utf-8")
			if text == QRCODE_TEXT:
				print("Correct QR!!!!")
				channel_mos.stop()
				detox_time += interval
				interval = random.randint(90, 900)
				
		# 正しくないQRコードがある or 何もない
		else:
			print("NO QR CODE!!")
			# await bot.turn_on()
			smartphone_count += 1
			interval = 5
			if not channel_mos.get_busy():
				channel_mos.play(mos)

	cv2.destroyAllWindows()

asyncio.run(main())
