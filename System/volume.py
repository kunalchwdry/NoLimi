import re
from pycaw.pycaw import AudioUtilities


def handle_volume(command, speak):
    cmd = command.lower()

    device = AudioUtilities.GetSpeakers()
    volume = device.EndpointVolume

    current = volume.GetMasterVolumeLevelScalar()

    val = re.findall(r"\d+", cmd)
    num = int(val[0]) if val else None

    if num is not None:
        num = max(0, min(100, num))

    # ---------------- MUTE ----------------
    if "mute" in cmd:
        volume.SetMasterVolumeLevelScalar(0, None)
        speak("Volume muted")
        return

    # ---------------- UNMUTE ----------------
    elif "unmute" in cmd:
        volume.SetMasterVolumeLevelScalar(0.5, None)
        speak("Volume restored")
        return

    # ---------------- GET VOLUME ----------------
    elif (
        "getvolume" in cmd
        or "current volume" in cmd
        or "what is the volume" in cmd
    ):
        speak(f"The current volume is {int(current * 100)} percent")
        return

    # ---------------- SET VOLUME ----------------
    elif "set volume" in cmd and num is not None:
        volume.SetMasterVolumeLevelScalar(num / 100, None)
        speak(f"Volume set to {num} percent")
        return

    # ---------------- MAX VOLUME ----------------
    elif "maximum volume" in cmd or "max volume" in cmd:
        volume.SetMasterVolumeLevelScalar(1, None)
        speak("Maximum volume")
        return

    # ---------------- MIN VOLUME ----------------
    elif "minimum volume" in cmd or "min volume" in cmd:
        volume.SetMasterVolumeLevelScalar(0, None)
        speak("Minimum volume")
        return

    # ---------------- INCREASE ----------------
    elif (
        "increase volume" in cmd
        or "volume up" in cmd
        or "raise volume" in cmd
    ):

        if num is not None:
            if "%" in cmd or "percent" in cmd:
                current += current * (num / 100)
            else:
                current += num / 100
        else:
            current += 0.1

        current = min(current, 1)

        volume.SetMasterVolumeLevelScalar(current, None)
        speak(f"Volume is now {round(current * 100, 1)} percent")
        return

    # ---------------- DECREASE ----------------
    elif (
        "decrease volume" in cmd
        or "volume down" in cmd
        or "lower volume" in cmd
    ):

        if num is not None:
            current -= num / 100
        else:
            current -= 0.1

        current = max(current, 0)

        volume.SetMasterVolumeLevelScalar(current, None)
        speak(f"Volume is now {int(current * 100)} percent")
        return