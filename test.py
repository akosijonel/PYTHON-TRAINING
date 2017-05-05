import pexpect

child = pexpect.spawn ('telnet 52.79.200.113 32773')
child.logfile = sys.stdout
child.expect(">")
child.sendline("en")