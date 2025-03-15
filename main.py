import feepaid
import feepending
import otp
from dotenv import load_dotenv
import os

# load_dotenv()
load_dotenv(dotenv_path=".env")  # Explicitly specify the file

print("DEBUG: EMAIL_USER =", os.getenv("EMAIL_USER"))  # Debugging
print("DEBUG: EMAIL_PASSWORD =", os.getenv("EMAIL_PASSWORD"))

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()
admin_username = input("Enter username: ")
if admin_username != "admin":
    print("Invalid Username")
    exit()

admin_email = os.getenv("EMAIL_USER")
print(f"DEBUG: Admin email loaded = {admin_email}")
otp_code = otp.send_otp(admin_email)
# print(f"DEBUG: OTP sent is {otp_code}")
# entered_otp = int(input("Enter OTP:"))
# if entered_otp != otp_code:
#     print("Login Failed!")
#     exit()
if otp_code is None:
        print("Failed to generate OTP. Try again.")
        exit()

entered_otp = int(input("Enter OTP: "))
print(f"DEBUG: Expected OTP = {otp_code}, Entered OTP = {entered_otp}")
if entered_otp !=otp_code:
    print("Login Failed!")
    exit()

print(f"{admin_username} logged in successfully!")
input("\nPress Enter to continue...") 
clear_screen()

user_records = {
    1001: ["Jayalakshmi", "mantrijayalakshmi5518@gmail.com", True],
    1002: ["Murthy", "mantrijayalakshmi796@gmail.com", False],
    1003: ["Nagamani", "20u41a4208@diet.edu.in", True],
    1004: ["Joshita","mantrijayalakshmi5518@gmail.com", True ],
    1005: ["Mokshit", "mantrijayalakshmi796@gmail.com", False]
}

# def update_user_fee_status(user_id,status):
#     if user_id in user_records:
#         user_records[user_id][2] = status
#         print(f"{user_records[user_id][0]}'s fee status updated to {status}")

while True:
    print("\nWelcome Admin!"
    "\n1. Update User Fee Status"
    "\n2. Notify users with pending fee"
    "\n3. notify users with cleared fee"
    "\n4. Exit")

    try:
        choice = int(input("Enter option: "))
    except Exception as e:
        print("Invalid input. Please enter a number")
        continue

    if choice == 1:
        for user_id in user_records:
            status = input(f"Enter the fee status of {user_records[user_id][0]} (true/false): ").strip().lower() == "true"
            user_records[user_id][2] = status
            print(f"{user_records[user_id][0]}'s Data Updated!")

    elif choice == 2:
        pending_users = [[user_records[user_id][0], user_records[user_id][1]] for user_id in user_records if not user_records[user_id][2]]
        for name, email in pending_users:
            feepending.send_mail(email, name)
        print("Fee pending notification sent!")

    elif choice == 3:
        cleared_status = [[user_records[user_id][0], user_records[user_id][1]] for user_id in user_records if user_records[user_id][2]]
        for name, email in cleared_status:
            feepaid.send_mail(email,name)
        print("Fee cleared notification sent!")
    elif choice == 4:
        print("Thankyou! Visit again.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4..")
    input("\nPress Enter to continue...") 
