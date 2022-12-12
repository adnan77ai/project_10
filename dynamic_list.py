import os, time
listOfEmail = []
def prettyPrint():
  os.system("clear")
  print("listofEmail") 
  print()
  for email in range (len(listOfEmail)): 
    print(listOfEmail[email])
    time.sleep(1)
while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
   prettyPrint()
  elif menu == "4":
    print("SPAMMING:", time.ctime())
    print("SPAMMING:", time.ctime())
  time.sleep(1)
  os.system("clear")