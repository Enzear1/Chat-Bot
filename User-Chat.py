
import requests
import json
import threading
import time

name = ''
server = ''

def getChat():
    global server
    response = requests.get(f'{server}/getChat')
    print('-------New-------')
    resp = response.text
    y = json.loads(resp)
    for item in y.values():
        print(str(list(item.keys())[0]) + ">> " + str(list(item.values())[0]))
    print('-------CHAT-------')
def main():
    global server
    server = input('Введите ip/port Сервера>> ')
    inpName = True
    while inpName:
        name = input('Введите своё имя: ')
        if(name == ''):
            print('Некорректное имя!')
        else:
            try:
                response = requests.get(f'{server}/usersEvent',params = {
                'eventName' : 'addUserName',
                'name' : name})
            except Exception:
                print(Exception)
            if(response.text == '301'):
                inpName = False
                break
            else:
                print('Это имя уже занято!')
    getChat()
    while True:
        msg = input('msg>> ')
        if(msg == ''):
            getChat()
        else:
            try:
                response = requests.get(f'{server}/usersEvent',params = {
                    'eventName' : 'sendMessage',
                    'name' : name,
                    'msg' : msg})
            except Exception:
                print(Exception)
            getChat()
        time.sleep(0.5)
if __name__ == '__main__':
    thmain = threading.Thread(target = main())
    thmain.run()
