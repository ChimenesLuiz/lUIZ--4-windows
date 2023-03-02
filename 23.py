note = int(input("NOTES INITIAL QTD: "))
pen = int(input("PEN INITIAL QTD: "))
pencil = int(input("PENCIL INITIAL QTD: "))
eraser = int(input("ERASER INITIAL QTD: "))
ruler = int(input("RULER INITIAL QTD: "))
while True:
    choice = int(input("1-NOTEBOOK \n2-PEN \n3-PENCIL \n4-ERASER \n5-RULER \nChoise the code(NUMBER): "))
    if (choice == 1):
        choice = input("E-Enter item \nS-Withdraw item \nR-Show qtd \nX-Exit \nChoise the code(NUMBER): ")
        if (choice in "eE"):
            choice = int(input("Amount to add: "))
            note += choice
        elif (choice in "sS"):
                choice = int(input("Amount to remove: "))
                if (choice > note): print("insufficient items")
                else:   note -= choice
        elif (choice in "rR"):
            print(note)
        elif (choice in "xX"):
            break
    elif (choice == 2):
        choice = input("E-Enter item \nS-Withdraw item \nR-Show qtd \nX-Exit \nChoise the code(NUMBER): ")
        if (choice in "eE"):
            choice = int(input("Amount to add: "))
            pen += choice
        elif (choice in "sS"):
                choice = int(input("Amount to remove: "))
                if (choice > pen): print("insufficient items")
                else:   pen -= choice
        elif (choice in "rR"):
            print(pen)
        elif (choice in "xX"):
            break
    elif (choice == 3):
        choice = input("E-Enter item \nS-Withdraw item \nR-Show qtd \nX-Exit \nChoise the code(NUMBER): ")
        if (choice in "eE"):
            choice = int(input("Amount to add: "))
            pencil += choice
        elif (choice in "sS"):
                choice = int(input("Amount to remove: "))
                if (choice > pencil): print("insufficient items")
                else:   pencil -= choice
        elif (choice in "rR"):  print(pencil)
        elif (choice in "xX"):  break
    elif (choice == 4):
        choice = input("E-Enter item \nS-Withdraw item \nR-Show qtd \nX-Exit \nChoise the code(NUMBER): ")
        if (choice in "eE"):
            choice = int(input("Amount to add: "))
            eraser += choice
        elif (choice in "sS"):
                choice = int(input("Amount to remove: "))
                if (choice > eraser): print("insufficient items")
                else:   eraser -= choice
        elif (choice in "rR"):  print(eraser)
        elif (choice in "xX"):  break
    elif (choice == 5):
        choice = input("E-Enter item \nS-Withdraw item \nR-Show qtd \nX-Exit \nChoise the code(NUMBER): ")
        if (choice in "eE"):
            choice = int(input("Amount to add: "))
            ruler += choice
        elif (choice in "sS"):
                choice = int(input("Amount to remove: "))
                if (choice > ruler): print("insufficient items")
                else:   ruler -= choice
        elif (choice in "rR"):  print(ruler)
        elif (choice in "xX"):  break
    else:   print("Invalid choice")
