print("dP                dP                 .d888888   888888ba\n"+
      "88                88                d8'    88   88    `8b\n"+
      "88d888b. .d8888b. 88d888b. .d8888b. 88aaaaa88a a88aaaa8P'\n"+
      "88'  `88 88'  `88 88'  `88 88'  `88 88     88   88\n"+
      "88.  .88 88.  .88 88.  .88 88.  .88 88     88   88\n"+
      "88Y8888' `88888P8 88Y8888' `88888P8 88     88   dP\n"+
      "                                         by Diego Jenzer\n\n")

print("[?] What do you want to do?\n"+
      "    1. Start new AP.\n"+
      "    2. Stop AP.\n"+
      "    3. See stats.\n")

while True:
      first_question = input("Your selection: ")

      if first_question == "1" or first_question == "2" or first_question == "3":
            break
      else:
            print("[!] Please select an option.")


if first_question == "1":
      print("[1]")
elif first_question == "2":
      print("[2]")
else:
      print("[3]")
