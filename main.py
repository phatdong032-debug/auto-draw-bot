import asyncio
import os
import requests
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# 1. Tạo Web Server chạy ẩn để Render duy trì trạng thái LIVE 24/7
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Auto Spin Bot Status: OK")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()
def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

# 2. Cấu hình gửi Request rút thăm từ cURL
def trigger_lucky_draw():
    url = 'https://dkfsopp8.com/hall/api/active/redPackIndex'

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'vi',
        'appsystem': 'Windows 10',
        'appversion': 'v7.5.57',
        'browserfingerid': 'GEE3-01-3f6f71b93e7c24e73ec95b31b7be5e82a6ed5b9acd83bad88b241110eb6093ca',
        'browsertype': 'Mobile Chrome v147.0.0.0',
        'clienttimezone': '+7',
        'content-type': 'application/json',
        'currency': 'VND',
        'device': 'c0c19d9a-3a80-4537-ad4c-c06f1de0db75',
        'devicebrand': 'Google',
        'devicemodel': 'Google Pixel 7',
        'domain': 'ev88vip.com',
        'language': 'vi',
        'newjwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE4MTk5MDgyNjcsImV4dEluZm8iOnsiYnJvd3NlcmZpbmdlcmlkIjoiIiwiY2xpZW50aXAiOiIxNC4xOTEuMTgzLjMyIiwiZGV2aWNlIjoiYzBjMTlkOWEtM2E4MC00NTM3LWFkNGMtYzA2ZjFkZTBkYjc1IiwieC1kZXZpY2UiOiIxLTYifSwidSI6Ijc4NTM1MTUxNSIsInYiOiIxNzg4MzcyMjY3In0.fG-6RY-d1W5_aSb6U6K7TtN-JKPYnqPU9QPkxF0OJBs',
        'operatingsystem': 'Android',
        'origin': 'https://ev88vip.com',
        'physicaldevicemodel': 'Google Pixel 7',
        'platformtype': '5',
        'priority': 'u=1, i',
        'referer': 'https://ev88vip.com/',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sitecode': '178',
        'timestamp': str(int(datetime.now().timestamp())),
        'token': 'b3a7f9f9c6faf2b427931788372267213447045',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'webauthndomain': 'ev88vip.com',
        'x-custom-referer': 'https://ev88vip.com/home/event?fixed.isSaveShort=true&fixed.isHideDomain=1',
        'x-data-mode': 'plain',
        'x-device': '2-6',
        'x-object-id': '{"uid":785351515,"browserLanguage":"vi","init":{"device":"","created":1788372232027,"version":1788226611000}}',
        'x-request-id': '821e8119-8e60-47e6-a377-43381e76d867',
        'x-version': '7.5.57',
    }

    current_time = int(datetime.now().timestamp())
    json_data = {
        'robot': 0,
        'time': current_time,
    }

    try:
        response = requests.post(
            'https://dkfsopp8.com/hall/api/active/redPackIndex',
            headers=headers,
            json=json_data,
            timeout=15
        )
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Kết quả:", response.text)
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Lỗi kết nối:", e)

# 3. Vòng lặp chính - Chạy 1 tiếng (3600 giây) một lần
async def main():
    print("Bot rút thăm tự động đã khởi chạy thành công!")
    while True:
        trigger_lucky_draw()
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
