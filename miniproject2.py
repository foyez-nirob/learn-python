import random
import string 

pass_len = 8

rng = string.ascii_letters+string.digits+string.punctuation

password = "".join([random.choice(rng) for i in range(pass_len)])

# password = ""
# for i in range(pass_len):
#     password += random.choice(rng)

print("you random password is :",password)