from types import FunctionType
import keyboard
import mouse 
import time
import threading

def click(delay: time.time) -> None:
    while True:
        mouse.click()
        time.sleep(delay)

def wait_for_keypress(keypress: str) -> None:
    keyboard.wait(keypress)
    return

def run_script(func: FunctionType, key: str, *args) -> None:
    listener = threading.Thread(target=wait_for_keypress, args=(key,))
    trainer = threading.Thread(target=func, args=(args), daemon = True)#, lambda: stop_thread))
    listener.start()
    trainer.start()
    listener.join()
    return

if __name__=="__main__":
    run_script(click, "space")
    print("Done")
