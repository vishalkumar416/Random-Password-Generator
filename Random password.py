import random
import string
pass_len=8
val=string.ascii_letters + string.digits + string.punctuation
# print(val)
password = ""
for i in range(pass_len):
 password = password + random.choice(val)
print("Your 8-digit random password is : ",password) 