import pyautogui
import time
import sys

# ================= CONFIG =================

FILE_PATH = r"C:/path/to/txt/file/containing/links"
SONG_COUNT = 12 #how many songs in this album
START_DELAY = 3
KEY_DELAY = 0.25

FIRST_SONG_X, FIRST_SONG_Y = 545, 555 #screen coordinates of first song 

# =========================================


def wait(t=KEY_DELAY):
    check_kill_switch()
    time.sleep(t)


def check_kill_switch():
    if pyautogui.position() == (0, 0):
        print("KILL SWITCH ACTIVATED")
        sys.exit(0)


def focus_first_song():
    check_kill_switch()
    pyautogui.moveTo(FIRST_SONG_X, FIRST_SONG_Y, duration=0.1)
    wait()
    pyautogui.click()
    wait()


def copy_selected_song_link():
    check_kill_switch()

    pyautogui.press(['right'] * 4, interval=0.05)
    wait()

    pyautogui.press(['enter', 'up', 'enter', 'enter'], interval=0.25)
    wait()


def append_clipboard_to_file():
    check_kill_switch()

    pyautogui.hotkey('win', 'r')
    wait()
    pyautogui.typewrite(f'notepad "{FILE_PATH}"\n', interval=0.01)
    wait(0.6)

    pyautogui.hotkey('ctrl', 'end')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    wait()
    pyautogui.hotkey('ctrl', 'w')
    wait()
    pyautogui.press('enter')
    wait()


def move_to_next_song():
    check_kill_switch()
    pyautogui.press('down')
    wait()


def copy_album(song_count):
    for i in range(song_count):
        print(f"Song {i + 1}/{song_count}")
        copy_selected_song_link()
        append_clipboard_to_file()
        move_to_next_song()


# ================= RUN =================

time.sleep(START_DELAY)
focus_first_song()
copy_album(SONG_COUNT)
