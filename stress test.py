import httpx
import random
from threading import Thread

count = int(input("Thread count: "))

def stress(drug):
    while True:
        req = httpx.request('SMOKE', url = f'http://127.0.0.1:42000/api/v1/smoke/{drug}')
        if req.status_code != 200:
            print(req.status_code)
        httpx.request('HOWMANYNIGGASSMOKIN', url = f'http://127.0.0.1:42000/api/v1/drugs')

print('Running on ', count, ' threads')
for i in range(count):
    Thread(target=stress,args=(random.choice(['cocaine', 'meth']),)).start()
    print(i)