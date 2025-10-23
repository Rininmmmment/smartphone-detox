from flask import Flask
import os

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>スマホデトックス操作パネル</title>
  <style>
    #status {
      margin-top: 20px;
      font-weight: bold;
      color: green;
    }
  </style>
  <script>
    async function sendAction(url) {
      try {
        const res = await fetch(url, { method: 'POST' });
        const text = await res.text();
        const statusDiv = document.getElementById('status');
        statusDiv.textContent = text;
        setTimeout(() => { statusDiv.textContent = ''; }, 3000); // 3秒後に消える
      } catch (e) {
        const statusDiv = document.getElementById('status');
        statusDiv.textContent = '通信エラー';
        setTimeout(() => { statusDiv.textContent = ''; }, 3000);
        console.error(e);
      }
    }
  </script>
</head>
<body>
  <h1>スマホデトックス操作</h1>
  <button onclick="sendAction('/camera_on')">カメラON</button>
  <button onclick="sendAction('/camera_off')">カメラOFF</button>
  <button onclick="sendAction('/switchbot_on')">SwitchBot ON</button>
  <button onclick="sendAction('/switchbot_off')">SwitchBot OFF</button>

  <div id="status"></div>
</body>
</html>
"""

@app.route("/")
def index():
    return html

@app.post("/camera_on")
def camera_on():
    os.system("python3 ../device/main.py &")
    return "カメラ起動中"

@app.post("/camera_off")
def camera_off():
    os.system("pkill -f main.py")
    return "カメラ停止"

@app.post("/switchbot_on")
def switchbot_on():
    os.system("python3 utils/switchbot.py on")
    return "SwitchBot ON"

@app.post("/switchbot_off")
def switchbot_off():
    os.system("python3 utils/switchbot.py off")
    return "SwitchBot OFF"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
