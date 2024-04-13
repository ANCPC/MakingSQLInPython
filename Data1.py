import csv
filename = "file.csv"
def show():
     with open(filename, 'r', newline='') as file:
         reader=csv.reader(file)
         for i in reader:
             print(i)
def new():
   
    name = input("Enter name: ")
    fname = input("Enter father's name: ")
    class_ = input("Enter class: ")
    number = input("Enter number: ")
    etc = input("Enter etc: ")

    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, fname, class_, number, etc])

import csv

def delete_row(csv_file, row_index):
    # Read the CSV file and store its data
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Delete the specified row
    if 0 <= row_index < len(data):
        del data[row_index]
        print("Row deleted successfully.")
    else:
        print("Invalid row index. No row deleted.")

    # Write the modified data back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)








def edit():
    l=[]
    L=[]
    a=0
    ind=0
    with open(filename, 'r', newline='') as file:
        reader=csv.reader(file)
        for i in reader:
            l.append(i)
           
        print(l)
        se=input("search for :")
        for ii , j in enumerate(l):
            for k in j:
                #print(k)
                if k==se:
                    L=j
                    ind=ii
        if L:
               #print(L,ind)
               print("edit values :")

               name = input("Enter name: ") or L[0]
               fname = input("Enter father's name: ") or L[1]
               class_ = input("Enter class: ") or L[2]
               number = input("Enter number: ")or L[3]
               etc = input("Enter etc: ") or L[4]

               for index, row in enumerate(reader):
                    if row == search_values:
                         ind=index
                   

               newL=[name,fname,class_,number,etc]
               delete_row(filename, ind)
               print(a)
               with open(filename, 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([name, fname, class_, number, etc])
        else:
             print("Not found")

while True:
    print("SELECT AN OPTION:\n")
    print("1. SHOW\n")
    print("2. NEW\n")
    print("3. EDIT\n")
    print("4. DELETE\n")
    print("5. EXIT\n")
    
    choice = input("Enter your choice (1/2/3/4/5): ").strip().lower()
    if choice == "show":
        show()
    elif choice == "new":
        new()
    elif choice == "edit":
        edit()
    elif choice == "delete":
        filename = input("Enter CSV filename: ")
        try:
            row_index = int(input("Enter the row index to delete: "))
            delete_row(filename, row_index)
        except ValueError:
            print("Invalid input. Row index must be an integer.")
    elif choice == "exit":
        confirm = input("Are you sure you want to exit? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Exiting the program.")
            break
        elif confirm == "no":
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Invalid option. Please select from (show, new, edit, delete, exit).")     



      
        




  
    
