import pandas as pd
import socks
import socket
import stem.process
from igramscraper.instagram import Instagram


def get_handles():
    instagram = Instagram()
    instagram.with_credentials('USERNAME', 'PASSWORD')
    instagram.login()

    data = pd.read_csv('C:\\Users\\sligh\\PycharmProjects\\test\\test-sheet.csv',
                       usecols=['handle'], skip_blank_lines=True)
    dataframe = pd.DataFrame(data=data)

    for row in dataframe.itertuples(index=False, name=None):
        handle = str(row)
        translation_table = dict.fromkeys(map(ord, '(\'),'), None)
        handle = handle.translate(translation_table)
        print(handle)
        account = instagram.get_account(handle)
        print(handle + ': ', account.identifier)
        time.sleep(10)

# to get tor working, navigate to process.py in the stem library
# go to line 204 and enter tor path in tor_cmd = '[your path]'
# ex. tor_cmd = r"C:\Users\sligh\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe"


if __name__ == "__main__":
    # You can change the port number
    # if error: Process terminated: Failed to bind one of the listener ports.
    # make sure to kill tor process in task man, process didn't die properly last execution
    SOCKS_PORT = 7000
    tor_process = stem.process.launch_tor_with_config(
        config={
            'SocksPort': str(SOCKS_PORT),
        },
    )
    socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=SOCKS_PORT)
    socket.socket = socks.socksocket
    print("tor takeoff 🚀➡️🌑")
    get_handles()
    tor_process.kill()
