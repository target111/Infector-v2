import socket

class Filter(object):
    def __init__(self, input_ip, input_password, input_threads):
        self.input_ip       = input_ip
        self.input_threads  = input_threads
        self.input_password = input_password

    def ip(self):
        try:
            socket.inet_aton(self.input_ip)
            if self.input_ip.count(".") == 2 or self.input_ip.count(".") == 1:
                return True
            else:
                return False
                print("Invalid ip range!")

        except:
            print("Invalid ip range!")
            return False

    def threads(self):
        try:
            if int(self.input_threads) > 256:
                print("Max is of 256 threads!")
                return False
            else:
                return True

        except:
            print("Threads number must be an integer!")
            return False

    def password(self):
        try:
            if len(self.input_password.split(":")) == 2:
                return True
            else:
                print("Incorrect password format! (valid ex: root:root)")
                return False

        except:
            print("Incorrect password format! (valid ex: root:root)")
            return False
