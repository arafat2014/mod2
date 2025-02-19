import time
print(4)
time.sleep(3)
print("This line print after 3 sec")

import time
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%D %H %M %S", t)

print(formatted_time)
