from ipaddress import IPv4Address
from operator import itemgetter


def _next():
    with open('../db/ESM.txt', mode='r', encoding='utf-8', newline="\r\n") as f:
        while True:
            l = f.readline()
            if not l:
                break
            host, ip = l.split()[1:3]
            yield (host, IPv4Address(ip), )

for host, ip in sorted((_ for _ in _next()), key=itemgetter(1)):
    print(f'{ip} {host}')
