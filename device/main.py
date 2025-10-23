import cv2, time, asyncio, random
from datetime import datetime
from picamera2 import Picamera2
from pyzbar.pyzbar import decode
from common.date_checker import DateChecker
from common.display_manager import DisplayManager
from common.phone_state_manager import PhoneState, PhoneStateManager
from common.switchbot import SwitchBot
from dotenv import load_dotenv
import os
from common.const import Const
from common.sound_controller import SoundController

load_dotenv()

interval = random.randint(90, 900)

async def main():
	"""
	初期設定
	"""
	# カメラ
	picam2 = Picamera2()
	picam2.start()

    # アラーム音
	sound_controller = SoundController()

    # SwitchBot
	bot = SwitchBot(os.getenv("MAC_ADDRESS"))
	
	display = DisplayManager()
	
	"""
	監視するかチェック
	"""
	# 土日か祝日か判定
	if DateChecker.is_holiday():
		print("Holiday!!!")
		return

	"""
	監視処理
	"""
	# スマホ使用回数
	smartphone_count = 0
	phone_state = PhoneStateManager()
 
	while True:
		frame = picam2.capture_array()
		codes = decode(frame)
		# cv2.imshow("frame", frame)

		print('----------------------------')
		print('detox_time: ', str(phone_state.detox_time) + ' s')
		print('smartphone_count: ', phone_state.smartphone_count)
		print('----------------------------')
  
		display.update_status(
      		phone_state.detox_time, 
        	phone_state.smartphone_count,
			Const.PIYO_IMAGE_NAME
    	)
		
		time.sleep(Const.INTERVAL_SEC)
		
		# 正しいQRコードがある
		if codes:
			text = codes[0].data.decode("utf-8")
			if text == Const.QRCODE_TEXT:
				print("Correct QR!!!!")
				sound_controller.stop_mos()
				phone_state.set_state(PhoneState.NOT_USING)
				
		# 正しくないQRコードがある or 何もない
		else:
			print("NO QR CODE!!")
			# await bot.turn_on()
			smartphone_count += 1
			phone_state.set_state(PhoneState.USING)
			if not sound_controller.is_mos_playing():
				sound_controller.play_mos()

	cv2.destroyAllWindows()

asyncio.run(main())
