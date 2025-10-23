from datetime import datetime
import jpholiday

class DateChecker:
    @staticmethod
    def is_holiday(today: datetime = None) -> bool:
        """
        今日が土日または祝日かどうか判定
        """
        if today is None:
            today = datetime.today()
        is_weekend = today.weekday() >= 5  # 5=土曜, 6=日曜
        is_holiday = jpholiday.is_holiday(today.date())
        return is_weekend or is_holiday
