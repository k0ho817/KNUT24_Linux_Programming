import signal
import time

def signal_handler(signum, frame):
    print(f"Signal {signum} received. Exiting gracefully...")
    exit(0)

# SIGINT 신호에 대한 핸들러 설정
signal.signal(signal.SIGINT, signal_handler)

print("Press Ctrl+C to trigger the signal handler.")
while True:
    print("Running ...")
    time.sleep(1)