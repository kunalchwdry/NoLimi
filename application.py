import subprocess
def application(c):
    if "open notepad" in c.lower():
        subprocess.Popen("notepad.exe")
        return True
    elif "open calculator" in c.lower():
        subprocess.Popen("calc.exe")
        return True
    elif "open paint" in c.lower():
        subprocess.Popen("mspaint.exe")
        return True
    elif "open command prompt" in c.lower():
        subprocess.Popen("cmd.exe")
        return True
    elif "open wordpad" in c.lower():
        subprocess.Popen("write.exe")
        return True
    elif "open task manager" in c.lower():
        subprocess.Popen("taskmgr.exe")
        return True
    elif "open control panel" in c.lower():
        subprocess.Popen("control.exe")
        return True
    elif "open camera" in c.lower():
        subprocess.run("start microsoft.windows.camera:", shell=True)
        return True
    return False
    exit()