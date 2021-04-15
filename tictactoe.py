import os
print(".,,.....Main Menu.....,,.")
print("1. Start 2 players game")
print("2. Contact the developer")
print("3. Update")
print("4. Quit")

choice=int(input("Enter your choice"))
if choice == 1:
 os.system("python3 main.py")
elif choice == 2:
 os.system("am start -a android.intent.action.VIEW -d http://https://bit.ly/3e7SfnR")
elif choice == 3:
 os.system("bash update.sh")
else:
 os.system("exit")
