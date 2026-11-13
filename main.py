

import urllib.request
import urllib.parse
import json
import time

TOKEN = "1475791054:S-EFQv7FkTtSnnK4sB3ZX2MPNracyi1qeSg"
API = f"https://tapi.bale.ai/bot{TOKEN}"

offset = 0

while True:
    try:
        url = f"{API}/getUpdates?offset={offset}&timeout=30"

        with urllib.request.urlopen(url, timeout=40) as response:
            data = json.loads(response.read().decode("utf-8"))

        if data.get("ok"):
            for update in data.get("result", []):
                offset = update["update_id"] + 1

                message = update.get("message")

                if message:
                    chat_id = message["chat"]["id"]

                    payload = json.dumps({
                        "chat_id": chat_id,
                        "text": "خوبم"
                    }).encode("utf-8")

                    req = urllib.request.Request(
                        f"{API}/sendMessage",
                        data=payload,
                        headers={"Content-Type": "application/json"}
                    )

                    urllib.request.urlopen(req, timeout=30)

    except Exception as e:
        print("Error:", e)
        time.sleep(3)
