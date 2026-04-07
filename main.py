import random

def main():
    generatorotp = random.randint(000000,100000)
    username = input("Username: ")
    print('Hello '+username+'!')
    print("Here is your OTP for login",generatorotp)
    password = input("Enter your OTP: ")

    if password == str(generatorotp):
        print('Login Successful!')
    else:
        print('Login Failed!')



if __name__ == "__main__":
    main()