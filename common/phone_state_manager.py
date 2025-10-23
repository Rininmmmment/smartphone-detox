from datetime import datetime
from enum import Enum
import time

class PhoneState(Enum):
    UNKNOWN = 0  # 不明
    NOT_USING = 1  # 使っていない
    USING = 2    # 使用中

class PhoneStateManager:
    def __init__(self):
        self.state_data = []
        self.current_state = PhoneState.UNKNOWN
        self.detox_time = 0  # 使用していない時間の累計
        self.last_change_time = time.time()
        self.smartphone_count = 0 # 使用回数

    def set_state(self, new_state):
        self.current_state = new_state
        
        if self.current_state == PhoneState.USING:
            self.smartphone_count += 1
        
        # detox_time の更新
        if self.current_state == PhoneState.NOT_USING:
            self.detox_time += time.time() - self.last_change_time
        
        # タイムスタンプ更新
        self.last_change_time = time.time()
        
        self.state_data.append({
            'state': self.current_state,
            'detox_time': self.detox_time,
            'time': datetime.fromtimestamp(self.last_change_time),
            'count': self.smartphone_count
        })