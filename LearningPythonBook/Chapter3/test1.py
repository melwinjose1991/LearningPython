import sys
print(sys.platform)

x = 'test1'

import test2
print("=== import test2 ===")
print(x)
print(test2.x)
print("\n")


from test2 import x
print("=== from test2 import x ===")
print(x)
print(test2.x)
print("\n")


print("=== reload(test2) ===")
input("Press Enter to continue")
from imp import reload
reload(test2)
print(x)
print(test2.x)


print("=== reload(test2) ===")
input("Change x in test2.py and then press Enter to continue")
reload(test2)
print(x)
print(test2.x)