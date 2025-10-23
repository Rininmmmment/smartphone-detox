import pygame
from common.const import Const

class SoundController:
    def __init__(self):
        pygame.mixer.pre_init(
            frequency=Const.AUDIO_FREQUENCY,
            size=-Const.AUDIO_SIZE, 
            channels=Const.AUDIO_CHANNELS,
            buffer=Const.AUDIO_BUFFER
        )
        pygame.mixer.init()
        
        # 音声オブジェクト
        self.mos_sound = pygame.mixer.Sound(str(Const.MOS_SOUND_NAME))
        self.alarm_sound = pygame.mixer.Sound(str(Const.ALARM_SOUND_NAME))
        
        # 専用チャンネル
        self.channel_mos = pygame.mixer.Channel(0)
        self.channel_alarm = pygame.mixer.Channel(1)
        
        # 再生状態フラグ
        self.playing_mos = False
        self.playing_alarm = False

    def play_mos(self):
        self.channel_mos.play(self.mos_sound, loops=-1)  # ループ再生
        self.playing_mos = True

    def stop_mos(self):
        self.channel_mos.stop()
        self.playing_mos = False

    def play_alarm(self):
        self.channel_alarm.play(self.alarm_sound, loops=-1)  # ループ再生
        self.playing_alarm = True

    def stop_alarm(self):
        self.channel_alarm.stop()
        self.playing_alarm = False

    def is_mos_playing(self):
        return self.playing_mos

    def is_alarm_playing(self):
        return self.playing_alarm
