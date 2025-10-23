from typing import Optional
from collections import deque
import time

class QRDetector:
    # def __init__(self, stable_count=3, cache_ttl_sec=5):
    #     self.recent_ids = deque(maxlen=stable_count)
    #     self.stable_count = stable_count
    #     self.cache_ttl_sec = cache_ttl_sec

    # def detect(self, frame) -> Optional[str]:
    #     """フレームからQR抽出（pyzbarなどで実装）"""
    #     return None

    # def is_stable(self, qr_id: str) -> bool:
    #     """n回連続で検出されているか"""
    #     return self.recent_ids.count(qr_id) >= self.stable_count
