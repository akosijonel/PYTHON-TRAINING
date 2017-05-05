import pexpect
import sys
import time
child = pexpect.spawn('telnet 52.79.200.113 32773')
child.logfile = sys.stdout
child.expect("#")
child.sendline("show ip int brief")
child.expect("#")
child.sendline("exit")
child.expect("#")