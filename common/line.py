import requests
from typing import Optional

class LineNotify:
    """
    LINE Notify で通知を送るユーティリティクラス
    """
    def __init__(self, token: str):
        """
        token: LINE Notify のアクセストークン
        """
        self.token = token
        self.api_url = "https://notify-api.line.me/api/notify"
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def send(self, message: str, image_path: Optional[str] = None) -> bool:
        """
         メッセージを送信する
        message: 送信するテキスト
        image_path: 送信したい画像ファイルのパス（任意）
        return: 成功なら True, 失敗なら False
        """
        data = {"message": message}
        files = None
        if image_path:
            try:
                files = {"imageFile": open(image_path, "rb")}
            except Exception as e:
                print(f"画像ファイルオープン失敗: {e}")
                return False

        try:
            r = requests.post(self.api_url, headers=self.headers, data=data, files=files)
            if files:
                files["imageFile"].close()
            return r.status_code == 200
        except Exception as e:
            print(f"送信エラー: {e}")
            return False
