class PresenceDetector:
    """
    外出中か判定するクラス
    """
    def __init__(self, method="wifi"):
        self.method = method

    def is_user_home(self) -> bool:
        return True
