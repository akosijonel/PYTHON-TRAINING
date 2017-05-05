import os
hostname1 = "google.com"
host1_stat = ""
host2_stat = ""
hostname2 = "192.168.1.1"

response = os.system("ping -c 1 " + hostname1)
if response == 0:
     host1_stat = "Reachable"
 else:
     host1_stat = "Unreachable"


response = os.system("ping -c 1 " + hostname2)
if response == 0:
     host2_stat = "Reachable"
 else:
     host2_stat = "Unreachable"