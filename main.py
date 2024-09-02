import subprocess
import os
with open(os.devnull, "wb") as limbo:
        subnet = 4
        for n in range(0, 255):
                ip="192.168.{}.{}".format(subnet, n)
                result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        print (ip, "Down")
                else:
                        print (ip, "Up")
