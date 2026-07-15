import re
import screen_brightness_control as sbc
from speaker import speak


def set_brightness(level):
    level = max(0, min(int(level), 100))
    sbc.fade_brightness(level)


def handle_brightness(command):
    cmd = command.lower()

    current = sbc.get_brightness()[0]

    val = re.findall(r"\d+", cmd)
    num = int(val[0]) if val else None

    if num is not None:
        num = max(0, min(num, 100))

    # ---------------- GET BRIGHTNESS ----------------
    if (
        "get brightness" in cmd
        or "current brightness" in cmd
        or "what is the brightness" in cmd
    ):
        speak(f"The current brightness is {current} percent")
        return

    # ---------------- SET BRIGHTNESS ----------------
    elif "set brightness" in cmd and num is not None:
        set_brightness(num)
        speak(f"Brightness set to {num} percent")
        return

    # ---------------- MAX BRIGHTNESS ----------------
    elif "maximum brightness" in cmd or "max brightness" in cmd:
        set_brightness(100)
        speak("Maximum brightness")
        return

    # ---------------- MIN BRIGHTNESS ----------------
    elif "minimum brightness" in cmd or "min brightness" in cmd:
        set_brightness(0)
        speak("Minimum brightness")
        return

    # ---------------- INCREASE ----------------
    elif (
        "increase brightness" in cmd
        or "brightness up" in cmd
        or "raise brightness" in cmd
    ):

        if num is not None:
            if "%" in cmd or "percent" in cmd:
                current += current * (num / 100)
            else:
                current += num
        else:
            current += 10

        current = max(0, min(current, 100))

        set_brightness(current)
        speak(f"Brightness is now {round(current, 1)} percent")
        return

    # ---------------- DECREASE ----------------
    elif (
        "decrease brightness" in cmd
        or "brightness down" in cmd
        or "lower brightness" in cmd
    ):

        if num is not None:
            if "%" in cmd or "percent" in cmd:
                current -= current * (num / 100)
            else:
                current -= num
        else:
            current -= 10

        current = max(0, min(current, 100))

        set_brightness(current)
        speak(f"Brightness is now {round(current, 1)} percent")
        return