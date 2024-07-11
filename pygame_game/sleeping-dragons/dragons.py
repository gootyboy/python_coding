import time
import random

VIP_pass_authorization = input("swip card")


def check_VIP_pass(VIP_pass):
    if VIP_pass  == True:
        print("authorized")
    else:
        print("unauthorized, please try agian")

if VIP_pass_authorization == " ":
    VIP_pass = False
    VIP_pass_True_False = random.randint(1, 2)

    if VIP_pass_True_False == 2:
        VIP_pass = True

    print("authorizing...")
    time.sleep(10)
    check_VIP_pass(VIP_pass)