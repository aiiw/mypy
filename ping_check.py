import pathlib
a=pathlib.Path("1.txt")
a.write_text("bbbb")
import os
a=os.system("ping 192.168.0.101 -n 1")
print(a)
