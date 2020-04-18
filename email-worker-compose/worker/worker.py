import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
  r = redis.Redis(hots='queue', port=6379, db=0)
  while True:
    mensamge = json.loads(r.blpop('sender')[1])
    # Simulando envio de e-mail...
    print('Mandando a mensagem:', mensagem['assunto'])
    sleep(randint(15, 45))
    print('Mensagem', mensagem['assunto'], 'enviada')