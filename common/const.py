from pathlib import Path
from datetime import time

class Const:
    """
    QR
    """
    QRCODE_TEXT = "nekochan_on_the_roomba"

    """
    Sounds
    """
    AUDIO_FREQUENCY = 44100   
    AUDIO_SIZE = 16           
    AUDIO_CHANNELS = 2
    AUDIO_BUFFER = 4096
    ALARM_SOUND_NAME = Path(__file__).parent / "sounds" / "alarm.mp3"
    MOS_SOUND_NAME = Path(__file__).parent / "sounds" / "mos39.mp3"
    
    """
    Images
    """
    PIYO_IMAGE_NAME = Path(__file__).parent / "images" / "cat.jpg"

    """
    Fonts
    """
    FONT_NAME = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    FONT_SIZE = 18
    
    """
    e-Paper
    """
    E_PAPER_LIB_PATH = "/home/rininmmmment/e-Paper/RaspberryPi_JetsonNano/python/lib"
    
    """
    SwitchBot
    """
    CHARACTERISTIC = "cba20002-224d-11e6-9fb8-0002a5d5c51b"
    
    """
    判定処理
    """
    INTERVAL_SEC = 5
    
    """
    Work Time
    """
    WORK_START = time(9, 0)
    WORK_END = time(17, 0)

    # データログイベント
    EVENT_START = "start"
    EVENT_STOP = "stop"

    # LINE通知
    LINE_NOTIFY_COOLDOWN_SEC = 900  # 15分間隔で通知抑制

    # サウンド
    DEFAULT_VOLUME = 0.5  # 0.0～1.0

    # e-ink
    DISPLAY_WIDTH = 200
    DISPLAY_HEIGHT = 200

    # デバウンス
    DEFAULT_DEBOUNCE_MS = 3000

    # 外出判定方式
    PRESENCE_METHOD_WIFI = "wifi"
    PRESENCE_METHOD_BLE = "ble"
    PRESENCE_METHOD_MANUAL = "manual"
