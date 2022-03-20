import requests
import json
import threading
import time

name = ''
server = ''

def getChat():
    response = requests.get(f'{server}/getChat')
    print('-------New-------')
    resp = response.text
    y = json.loads(resp)
    for i in range(1,int(y['total']) + 1):
        dat = y[str(i)]
        print(list(dat.keys())[0] + '>> ' + list(dat.values())[0])
    print('-------CHAT-------')
def main():
    server = input('Введите ip/port Сервера>> ')
    inpName = True
    while inpName:
        name = input('Введите своё имя: ')
        if(name == ''):
            print('Некорректное имя!')
        else:
            response = requests.get(f'{server}/usersEvent',params = {
                'eventName' : 'addUserName',
                'name' : name})
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
            response = requests.get(f'{server}/usersEvent',params = {
                'eventName' : 'sendMessage',
                'name' : name,
                'msg' : msg})
            getChat()
        time.sleep(0.5)
if __name__ == '__main__':
    thmain = threading.Thread(target = main())
    thmain.run()
