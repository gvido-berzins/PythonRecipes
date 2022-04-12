import sys
import time

path = sys.path[1]
print(f"Processing data: {path}")
for _ in range(5):
    print("[*] Processing...")
    time.sleep(1)
print("DONE!")
