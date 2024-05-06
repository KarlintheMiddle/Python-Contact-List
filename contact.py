contactList = []


def AddContact():
    while True:
        
        contact = {}
        contact["First Name"] = input("First Name: ")
        contact["Middle Name"] = input("Middle Name: ")
        contact["Last Name"] = input("Last Name: ")
        contact["Age"] = input("Age: ")
        contact["Contact Number"] = input("Contact Number: ")

        contactList.append(contact)

        addMore = input("Add more? ( yes/no ): ")
        if addMore.lower() != "yes":
            FunctionSelect()

def ShowContact():
    for idx, contact in enumerate(contactList,1):
        print(f"Contact {idx} : {contact['Last Name']}, {contact['First Name']} {contact['Middle Name']} - {contact['Age']} - {contact['Contact Number']}")

def DeleteContact():
    ShowContact()
    if len(contactList) > 0:
        while True:
            contactID = input("Select the contact number to delete: ")

            contactList.pop(int(contactID)-1)

            delMore = input("Delete more? ( yes/no ): ")
            if delMore.lower() != "yes":
                FunctionSelect()
            if delMore.lower() == "yes" and len(contactList) == 0:
                print("Contact List is Empty")
                FunctionSelect()
    else:
        print("Contact List is Empty")
        FunctionSelect()

def UpdateContact():
    ShowContact()

    if len(contactList) > 0:
        while True:
            contactID = input("Select the contact number to update: ")

            newFirstName = input("First Name: ")
            newMiddleName = input("Middle Name: ")
            newLastName = input("Last Name: ")
            newAge = input("Age: ")
            newContactNumber = input("Contact Number: ")

            contactList[int(contactID)-1]["First Name"] = newFirstName
            contactList[int(contactID)-1]["Middle Name"] = newMiddleName
            contactList[int(contactID)-1]["Last Name"] = newLastName
            contactList[int(contactID)-1]["Age"] = newAge
            contactList[int(contactID)-1]["Contact Number"] = newContactNumber
        
            upMore = input("Update more? ( yes/no ): ")
            if upMore.lower() != "yes":
                FunctionSelect()
            if upMore.lower() == "yes" and len(contactList) == 0:
                print("Contact List is Empty")
                FunctionSelect()

    else:
        print("Contact List is Empty")
        FunctionSelect()


def FunctionSelect ():
    while True:
        x = input("What can I do for you? (Add, Update, Delete, Show, Cancel): ")
        if x.lower() == "add":
            AddContact()
        elif x.lower() == "show":
            ShowContact()
        elif x.lower() == "delete":
            DeleteContact()
        elif x.lower() == "update":
            UpdateContact()
        elif x.lower() == "cancel":
            break
        else:
            print("Make sure your input is spelled correctly")


FunctionSelect()

