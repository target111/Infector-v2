version = "2.0"

import sys
from lib.scanner import Scanner
from lib.filter import Filter

def usage():
    if len(sys.argv) != 6:
        if len(sys.argv) == 2:
            if sys.argv[1] == "--help":
                print("Usage: %s <ip_range> <host> <binary_file> <creds> <threads>" % sys.argv[0])
                exit()

            else:
                print("Unknown command: '%s'\ntry: %s --help for more information." % (sys.argv[1], sys.argv[0]))
                exit()
        else:
            print("Usage: %s <ip_range> <host> <binary_file> <creds> <threads>" % sys.argv[0])
            exit()

def main():
    usage()

    valid = Filter(sys.argv[1], sys.argv[4], sys.argv[5])


    if valid.ip() and valid.threads() and valid.password():
        for i in range(int(sys.argv[5])):
            try:
                Scanner(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]).start()
            except:
                pass

        print("Started %d threads." % int(sys.argv[5]))

    else:
        exit()


if __name__ == "__main__":
    main()
