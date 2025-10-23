import sqlite3

class DataLogger:
    """
    データをDBに書き込むクラス
    """
    def __init__(self, db_path="usage.db"):
        self.conn = sqlite3.connect(db_path)

    def log_event(self, event_type, qr_id, ts, meta=None):
        pass

    def query_usage(self, range_start, range_end):
        pass
