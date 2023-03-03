import requests
import random
import os
import sys
import io

samples = 100
id_range = (1, 150000)

if len(sys.argv) >= 2:
    samples = int(sys.argv[1])

def rng():
    begin, end = id_range
    return random.randrange(begin, end)

for i in range(samples):
    while True:
        id = str(rng())
        filepath = 'out/album/' + id + '.json'
        if not os.path.exists(filepath):
            break
    try:
        r = requests.get('http://0.0.0.0:9990/album/' + id + '?foramt=json')
        with io.open(filepath, 'w', encoding='utf-8') as f:
            f.write(r.content.decode('utf-8'))
    except Exception as e:
        print('error at id ' + id + ':' + str(e))


