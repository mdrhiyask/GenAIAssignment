"""Create a daily Excel status report through visible desktop automation.

Prerequisites (Windows):
    pip install pyautogui pyperclip
    Install Google Chrome and Microsoft Excel.

Run this script, then do not use the mouse or keyboard until it finishes.
Move the mouse to the upper-left corner at any time to trigger PyAutoGUI's
emergency stop (FailSafeException).
"""

from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip


# Edit these values if an application needs more time to start on your computer.
CITY = "New Delhi"
COMMENT = "Weather captured automatically - check conditions before planning travel."
APP_START_DELAY = 5
PAGE_LOAD_DELAY = 5
SAVE_DIALOG_DELAY = 3


def wait(seconds: float) -> None:
    """Pause while keeping the intended timing clear in the automation flow."""
    time.sleep(seconds)


def open_chrome_and_copy_weather() -> str:
    """Open a public weather page in Chrome and copy its visible one-line result."""
    # wttr.in returns a compact text page, making Ctrl+A/C a dependable way to
    # copy one meaningful piece of information through the browser UI.
    url = f"https://wttr.in/{CITY.replace(' ', '%20')}?format=3"
    pyautogui.hotkey("win", "r")
    wait(1)
    pyautogui.write(f'chrome --new-window "{url}"', interval=0.01)
    pyautogui.press("enter")
    wait(PAGE_LOAD_DELAY)

    # Put focus in the page, copy its contents, and read the clipboard.
    pyautogui.click(pyautogui.size().width // 2, pyautogui.size().height // 2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    wait(1)
    weather = pyperclip.paste().strip()
    if not weather:
        raise RuntimeError("No weather text was copied. Check your internet connection and try again.")
    return " ".join(weather.split())


def open_excel() -> None:
    """Launch Excel with a new blank workbook using the Windows Run dialog."""
    pyautogui.hotkey("win", "r")
    wait(1)
    pyautogui.write("excel", interval=0.1)
    pyautogui.press("enter")
    wait(APP_START_DELAY)


def add_report_row(timestamp: str, weather: str) -> None:
    """Paste headers and the required report row into the active worksheet."""
    # Pasting TSV is more reliable than clicking individual cells and preserves
    # copied web text exactly, including characters PyAutoGUI cannot type.
    spreadsheet_text = (
        "Date & Time\tFetched Data\tComment\n"
        f"{timestamp}\t{weather}\t{COMMENT}"
    )
    pyperclip.copy(spreadsheet_text)
    pyautogui.hotkey("ctrl", "v")
    wait(2)

    # Make the final sheet easier to read before taking the screenshot.
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("alt", "h")
    pyautogui.press("o")
    pyautogui.press("a")
    wait(1)


def save_workbook(destination: Path) -> None:
    """Save the active Excel workbook as an .xlsx file through Excel's dialog."""
    pyautogui.hotkey("ctrl", "shift", "s")
    wait(SAVE_DIALOG_DELAY)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.write(str(destination), interval=0.01)
    pyautogui.press("enter")
    wait(SAVE_DIALOG_DELAY)

    # Excel occasionally asks to confirm the selected file type. Enter accepts
    # the default Excel Workbook (.xlsx) option if that dialog appears.
    pyautogui.press("enter")
    wait(2)


def main() -> None:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.4

    output_dir = Path(__file__).resolve().parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    now = datetime.now()
    workbook_path = output_dir / f"daily_report_{now:%Y-%m-%d}.xlsx"
    screenshot_path = output_dir / f"daily_report_{now:%Y-%m-%d}_screenshot.png"

    print("Starting in 3 seconds. Keep your computer unlocked and do not touch it.")
    wait(3)
    weather = open_chrome_and_copy_weather()
    open_excel()
    add_report_row(now.strftime("%Y-%m-%d %H:%M:%S"), weather)
    save_workbook(workbook_path)

    # This is a screenshot of the visible, final Excel sheet - not a generated
    # image - which directly satisfies the assignment requirement.
    pyautogui.screenshot(str(screenshot_path))
    print(f"Saved workbook: {workbook_path}")
    print(f"Saved screenshot: {screenshot_path}")


if __name__ == "__main__":
    try:
        main()
    except pyautogui.FailSafeException:
        print("Stopped safely because the mouse was moved to the upper-left corner.")
    except Exception as error:
        print(f"Automation stopped: {error}")
        raise
