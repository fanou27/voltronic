import sys

from wksSendCommand import wksProtocol

port = sys.argv[1]
command = "POP02"
wks = wksProtocol(port, command)
wks.send()
if wks.isFrameOk():
   print("true")
else:
   print("false")

