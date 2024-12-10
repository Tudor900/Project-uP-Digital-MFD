import os
os.system("bluetoothctl pair 00:10:CC:4F:36:03")
os.system("bluetoothctl trust 00:10:CC:4F:36:03")
os.system("bluetoothctl connect 00:10:CC:4F:36:03")
os.system("sudo rfcomm bind rfcomm0 00:10:CC:4F:36:03")
