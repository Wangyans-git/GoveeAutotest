import threading


def thread_scan_display():
    thread = threading.Thread(target=scan_display,name="线程1")
    thread.start()


def scan_display():
    thread = threading.Thread(target=display)
    thread.start()


def display():
    print("1111")

thread_scan_display()