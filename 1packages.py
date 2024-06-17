import cowsay
import sys
#packages are all useful and some are funny, like this one... named cowsay i just installed it in my terminal by triggering this command: pip install cowsay


if len(sys.argv)==2:
    cowsay.trex("hello, "+ sys.argv[1])

