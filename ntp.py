import subprocess
import struct

p = subprocess.Popen('ntpd -q', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
res = p.stdout.readline()
skew = res.split(" ")[-1]
sign = skew[0]
skew = int(float(skew[1:-2]) * 1000000)

if sign == "-":
    skew *= (-1)

print skew
with open("/var/run/blkin/skew", 'w') as f:
    f.write(struct.pack('i', skew))
p.wait()
