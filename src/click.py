from mouse import click
from time import sleep
import keyboard

shouldClick = False
keyRelease = True
clicks_per_second = 60

while True:
    if keyboard.is_pressed('0') and keyRelease:
        keyRelease = False
        shouldClick = not shouldClick
    if not keyboard.is_pressed('0'):
        keyRelease = True
    if keyboard.is_pressed('esc'):
        break
    if shouldClick:
        click('left')
        sleep(1/clicks_per_second)
