import subprocess
import os

with open(os.devnull, "wb") as out:
  for ip in range(1, 255):
    ip_address = "10.11.1.{0}".format(ip)
    result = subprocess.Popen(["ping", "-c", "1", ip_address],
                              stdout=out, stderr=out).wait()
    if result:
             continue
    else:
             print ip_address, "is alive and well!"
