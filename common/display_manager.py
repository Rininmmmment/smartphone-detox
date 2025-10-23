from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import sys
sys.path.append('/home/rininmmmment/e-Paper/RaspberryPi_JetsonNano/python/lib')
from waveshare_epd import epd2in13_V3

class DisplayManager:
    def __init__(self):
        self.epd = epd2in13_V3.EPD()
        self.epd.init()
        self.epd.Clear()
        self.font = ImageFont.truetype(
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 
            18
        )

    def update_status(self, detox_time: float, smartphone_count: int, icon_path):
        """
        detox_time・smartphone_count を画面に描画して更新する
        """
        # 新しい白背景の画像を作成
        image = Image.new('1', (self.epd.height, self.epd.width), 255)
        draw = ImageDraw.Draw(image)
        
        # 左側に画像を貼る
        icon = Image.open(icon_path).convert('1')
        icon = icon.resize((90, 90))
        image.paste(icon, (0, 25))  # 左上に配置（x=0, y=0）

        # テキスト描画
        draw.text(
            (10, 0), 
            datetime.now().strftime("%Y/%m/%d %H:%M"), 
            font=self.font, 
            fill=0
        )
        draw.text(
            (100, 30), 
            f"Not Using Time", 
            font=self.font, 
            fill=0
        )
        draw.text(
            (100, 50), 
            f"▶︎ ▶︎ {int(detox_time)} s", 
            font=self.font, 
            fill=0
        )
        draw.text(
            (100, 80), 
            f"Using Count", 
            font=self.font, 
            fill=0
        )
        draw.text(
            (100, 100), 
            f"▶︎ ▶︎ {smartphone_count}", 
            font=self.font, 
            fill=0
        )

        # 表示
        self.epd.display(self.epd.getbuffer(image))

    def clear(self):
        """画面をクリア"""
        self.epd.Clear()

    def sleep(self):
        """低電力モードへ移行"""
        self.epd.sleep()
