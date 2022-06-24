
import signal
import sys
import os
import ctypes
import datetime
import pkg_resources


try:
    # name of console
    ctypes.windll.kernel32.SetConsoleTitleW("Consola CheLang")
except:
    pass

from fulvo.basic import run  


# ctrl + c function
def signal_handler(sig, frame):
    print('Se metio el enano de ANVISA. Se suspende el partido')
    sys.exit(0)

# set ctrl + c function
signal.signal(signal.SIGINT, signal_handler)

try:
    dist = pkg_resources.get_distribution('playsound').version("1.2.2")
    print("La cancha esta lista para jugar".format(dist.key, dist.version))
except pkg_resources.DistributionNotFound:
    print('Las condiciones no permiten jugar el partido. Instala {}'.format('playsound'))
    sys.exit(0)

def export():
    for arg in sys.argv:
        if arg[0] == "-":
            sys.argv.remove(arg)
    # if 1 argument open console
    if len(sys.argv) == 1:
        while True:
            folder = os.path.basename(os.getcwd())
            inputText = input("/"+ folder + " < Fulvo > ")
            inputText = inputText.replace("\\","\\\\")
            if inputText.strip() == "": continue
            result, error = run(__file__,inputText)

            if error: print(error.as_string())

            elif result: 
                for programReturn in result.elements:
                    print(repr(programReturn))

                    
    # if 2 argument open file
    else:
        uri = sys.argv[1]
        uri = uri.replace("\\","\\\\")
        result, error = run(__file__, f'Correme("{uri}")')

        if error: print(error.as_string())

        elif result: 
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            elif len(result.elements) > 1:
                print(repr(result))

        folder = os.path.basename(os.getcwd())
        input("/"+ folder + " Fulvo > Apreta enter y terminalo juez")
        sys.exit(0)

now = datetime.datetime.now()
