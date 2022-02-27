import mysql.connector

try:
    employeeDB = mysql.connector.connect(       
        host = "localhost",              
        user = "",                     
        passwd = "",
        database = "SalaryManagementSystem"
    )
except:
    print("Please enter your MySQL Username and Password in line code 6 and 7 please.")


mycursor = employeeDB.cursor()

try:
    mycursor.execute("CREATE DATABASE SalaryManagementSystem")

    
except:
    pass

try:

    mycursor.execute("""CREATE TABLE Departments (
                     DepartmentID INT NOT NULL,
                     DepartmentName VARCHAR(100) NOT NULL,
                   Manager VARCHAR(100) NOT NULL,
                   EmployeeSize INT NOT NULL,
                  Location VARCHAR(100) NOT NULL,
                   PRIMARY KEY (DepartmentID)
                )""")

    mycursor.execute("""CREATE TABLE Employees (
                  EmployeeID INT AUTO_INCREMENT UNIQUE,
                  DepartmentID INT NOT NULL,
               Name VARCHAR(100) NOT NULL,
                 Degree VARCHAR(100) NOT NULL,
                   Years INT DEFAULT 0,
                  Salary INT NOT NULL,
                PRIMARY KEY (EmployeeID),
                FOREIGN KEY(DepartmentID) REFERENCES Departments(DepartmentID)               
             )""")
except:
    pass

#[===] MENU [===] #
class MenuSystem():
    def Talk(self):
        print("""Hello!
This is my first Database Management System, so excuse the rough edges.

This is an employee salary database management system, where you're able to input the employee's details alongside their salary in the employee table.
This is also linked (through an one to many relationship) with the departments table.
The department table is utilised to store information about the department, and thus, which employee is in which department.

Other features is that you're able to remove content from the table.
Able to see attributes of the table.
Able to see what's inside of the table.
And much more!
""")

        menu.Choices()
              
    def Choices(self):
        print("""
Please choose a number to do a certain command for the employee salary database management system.

1 - Add content into the tables
2 - Remove content from the tables
3 - See the attributes of the tables
4 - Update details of the tables
5 - Salary actions
6 - Find manager/employee name
7 - Go through salaries
8 - Check what departments there are
9 - View the content within the tables
10 - Reset all of the table content
11 - Quit

""")

        try:
            option = int(input(""))

            if option == 1:
                add.Adding()

            elif option == 2:
                remov.Removing()

            elif option == 3:
                attr.Attributes()

            elif option == 4:
                sense.Details()

            elif option == 5:
                salary.Salary()

            elif option == 6:
                find.Finding()

            elif option == 7:
                going.Through()

            elif option == 8:
                departCheck.DepartmentChecks()

            elif option == 9:
                view.ViewTables()

            elif option == 10:
                reset.Reset()

            elif option == 11:
                quit()

            else:
                raise


        except:
            print("That wasn't a valid option")
            menu.Choices()
#[===] MENU [===] #

#[===] RESETTING TABLE CONTENT [===]#
class ResettingTable():
    def Reset(self):
        Correct = False

        while Correct != True:
            try:
                print("""Are you sure you want to erase all of the table's content?
Please input Y for Yes or N for No.""")

                option = str(input(""))

                if option == "Y":
                    mycursor.execute("DROP TABLE Employees")
                    employeeDB.commit()
                    mycursor.execute("DROP TABLE Departments")
                    employeeDB.commit()
                    
                    mycursor.execute("""CREATE TABLE Departments (
                                        DepartmentID INT NOT NULL,
                                        DepartmentName VARCHAR(100) NOT NULL,
                                        Manager VARCHAR(100) NOT NULL,
                                        EmployeeSize INT NOT NULL,
                                        Location VARCHAR(100) NOT NULL,
                                        PRIMARY KEY (DepartmentID)
                                        )""")

                    mycursor.execute("""CREATE TABLE Employees (
                                        EmployeeID INT AUTO_INCREMENT UNIQUE,
                                        DepartmentID INT NOT NULL,
                                        Name VARCHAR(100) NOT NULL,
                                        Degree VARCHAR(100) NOT NULL,
                                        Years INT DEFAULT 0,
                                        Salary INT NOT NULL,
                                        PRIMARY KEY (EmployeeID),
                                        FOREIGN KEY(DepartmentID) REFERENCES Departments(DepartmentID)               
                                        )""")
                    
                    print("Everything has been erased.")
                    menu.Choices()

                elif option == "N":
                    print("Very well then.")
                    menu.Choices()

                else:
                    raise

            except:
                print("That wasn't a valid option")
                reset.Reset()
#[===] RESETTING TABLE CONTENT [===]#

#[===] GOING THROUGH THE TABLE CONTENTS [===]#
class ViewTableContents():
    def ViewTables(self):
        print("""Please choose an option that best suits you.

1 - Employees table
2 - Departments table
3 - Employees joined with departments table
4 - Departments joined with employees table

""")
        try:
            option = int(input(""))

            if option == 1:
                mycursor.execute("SELECT * FROM Employees")
                for x in mycursor:
                    print(x)

                print("That is all of the content within the employees table.")
                menu.Choices()

            elif option == 2:
                mycursor.execute("SELECT * FROM Departments")
                for x in mycursor:
                    print(x)

                print("That is all of the content within the departments table.")
                menu.Choices()

            elif option == 3:
                mycursor.execute("SELECT * FROM Employees INNER JOIN Departments ON Employees.DepartmentID=Departments.DepartmentID")
                for x in mycursor:
                    print(x)

                print("That is the content of the Employees table merged with the Departments table.")
                menu.Choices()
                

            elif option == 4:
                mycursor.execute("SELECT * FROM Departments INNER JOIN Employees ON Departments.DepartmentID=Employees.DepartmentID")
                for x in mycursor:
                    print(x)

                print("That is the content of the Departments table merged with the Employees table.")
                menu.Choices()
                
                

            else:
                raise

        except:
            print("That wasn't a valid option")
            view.ViewTables()
            
#[===] GOING THROUGH THE TABLE CONTENTS [===]#
            
#[===] CHECKING DEPARTMENTS [===]#
class DepartmentChecking():
    def DepartmentChecks(self):
        print("""Please choose an option that best suits you.

1 - See the departments in lowercase
2 - See the departments in uppercase

""")
        try:
            option = int(input(""))

            if option == 1:
                mycursor.execute("SELECT LOWER(DepartmentName) FROM Departments")
                for x in mycursor:
                    print(x)

                print("These are all of the departments registered so far.")
                menu.Choices()

            elif option == 2:
                mycursor.execute("SELECT UPPER(DepartmentName) FROM Departments")
                for x in mycursor:
                    print(x)

                print("These are all of the departments registered so far.")
                menu.Choices()

            else:
                raise

        except:
            print("That wasn't a valid option")
            departCheck.DepartmentChecks()
            
#[===] CHECKING DEPARTMENTS [===]#
            
#[===] GOING THROUGH SALARIES [===]#
class GoingThrough():
    def Through(self):
        print("""Please choose an option that best suits you.

1 - See the salaries in ascending order
2 - See the salaries in descending order
3 - Limit of how many salaries that can be seen
4 - Diffrentiated salaries

""")

        try:
            option = int(input(""))

            if option == 1:
                mycursor.execute("SELECT Salary FROM Employees ORDER BY Salary ASC")
                for x in mycursor:
                    print(x)

                print("These are all of the salaries inputted in ascending order")
                menu.Choices()

            elif option == 2:
                mycursor.execute("SELECT Salary FROM Employees ORDER BY Salary DESC")
                for x in mycursor:
                    print(x)

                print("These are all of the salaries inputted in descending order")
                menu.Choices()

            elif option == 3:
                Correct = False

                while Correct != True:
                    try:
                        print("How many people salaries do you wish to see?")

                        numberPeople = int(input(""))

                        countPeople = 0

                        mycursor.execute("SELECT * FROM Employees")
                        for x in mycursor:
                            countPeople += 1

                        if numberPeople > countPeople:
                            raise

                        else:
                            Correct = True

                    except:
                        print("That is an invalid data type or your input exceeds the amount of employees in the table.")

                mycursor.execute("SELECT Salary FROM Employees LIMIT %s" %(numberPeople))
                for x in mycursor:
                    print(x)

                numberPeople = str(numberPeople)
                print("This is " + numberPeople + " employees salaries")
                menu.Choices()

            elif option == 4:
                mycursor.execute("SELECT DISTINCT Salary FROM Employees")
                for x in mycursor:
                    print(x)

                print("These are all of the salaries which are diffrentiated to each other.")
                menu.Choices()

            else:
                raise

        except:
            print("That wasn't a valid option")
            going.Through()

            
#[===] GOING THROUGH SALARIES [===]#
            
#[===] FINDING EMPLOYEE OR MANAGER NAME [===]#
class FindName():
    def Finding(self):
        print("""Please choose an option that best suits you.

1 - Employee
2 - Manager

""")
        try:
            option = int(input(""))

            if option == 1:
                print("What is the name of the employee or start of the name of the employee that you're trying to look for?")
                nameSearch = str(input(""))

                mycursor.execute("SELECT Name FROM Employees WHERE Name LIKE '" + nameSearch + "%'")
                for x in mycursor:
                    print(x)

                print("These are the search results")
                menu.Choices()

            elif option == 2:
                print("What is the name of the manager or start of the name of the manager that you're trying to look for?")
                nameSearch = str(input(""))

                mycursor.execute("SELECT Manager FROM Departments WHERE Manager LIKE '" + nameSearch + "%'")
                for x in mycursor:
                    print(x)

                print("These are the search results")
                menu.Choices()

            else:
                raise

        except:
            print("That wasn't a valid option")
            find.Finding()
            
#[===] FINDING EMPLOYEE OR MANAGER NAME [===]#
            
#[===] SALARY ACTIONS [===]#
class SalaryActions():
    def Salary(self):
        print("""Please choose an option that best suits your needs.

1 - Find the average salary
2 - Find the total of all salaries
3 - Increase or decrease salaries
4 - List of employees who have X minimum salary
5 - Find the minimum salary of the employees

""")

        try:
            option = int(input(""))

            if option == 1:
                mycursor.execute("SELECT AVG(Salary) FROM Employees WHERE Salary > 0")
                for x in mycursor:
                    x = str(x)
                
                print(x + " this is the average salary of all of the employees")

                menu.Choices()

            elif option == 2:
                mycursor.execute("SELECT SUM(Salary) FROM Employees WHERE Salary > 0")
                for x in mycursor:
                    x = str(x)
                
                print(x + " is the total salary of all of the employees")

                menu.Choices()

            elif option == 3:
                Correct = False

                while Correct != True:
                    try:
                        ListOfEmployeeID = []
                        EmplID = int(input("Please enter the Employee ID for who you wish to change their salary"))

                        mycursor.execute("SELECT EmployeeID FROM Employees")
                        for x in mycursor:
                            x = str(x)
                            ListOfEmployeeID.append(x)

                        NewEmplID = str(EmplID)
                        NewEmplID = ("(" + NewEmplID + ",)")

                        if NewEmplID in ListOfEmployeeID:
                            Correct = True

                        else:
                            print("This Employee ID doesn't exist.")
                            ListOfEmployeeID.clear()

                    except:
                        print("That was the wrong data type.")
                        ListOfEmployeeID.clear()

                SalaryChanges = False

                mycursor.execute("SELECT Salary FROM Employees WHERE EmployeeID = %s" %(EmplID))
                for x in mycursor:
                    x = str(x)
                    oldSalary = x

                oldSalary = int(oldSalary)

            

                while SalaryChanges == False:
                    try:
                        print("Please enter how much you wish to add or take away from the salary of this employee. When you are taking away, ensure it's a minus sign")
                        SalaryDifference = int(input(""))

                        newSalary = oldSalary + SalaryDifference
                        newSalary = int(newSalary)

                        mycursor.execute("UPDATE Employees SET Salary = %s WHERE EmployeeID = %s" %(newSalary, EmplID))
                        employeeDB.commit()

                        SalaryChanges = True


                    except:
                        print("That was the wrong data type.")

                mycursor.execute("SELECT Salary FROM Employees WHERE EmployeeID = %s" %(EmplID))
                for x in mycursor:
                    newSalary = x

                mycursor.execute("SELECT Name FROM Employees WHERE EmployeeID = %s" %(EmplID))
                for x in mycursor:
                    employeeName = x

                EmplID = str(EmplID)
                oldSalary = str(oldSalary)
                newSalary = str(newSalary)
                employeeName = str(employeeName)

                print(employeeName + " salary has went from " + oldSalary + " to " + newSalary)

                menu.Choices()

            elif option == 4:
                Correct = False

                while Correct != True:
                    try:
                        print("What minimum salary must the employees have to be viewed?")
                        minimumSalary = int(input(""))

                        if minimumSalary < 0:
                            print("The minimum salary can't be below 0")
                            raise
                        else:
                            Correct = True

                    except:
                        print("That was the wrong data type.")

                mycursor.execute("SELECT Name FROM Employees WHERE Salary >= %s" %(minimumSalary))
                for x in mycursor:
                    print(x)

                minimumSalary = str(minimumSalary)

                print("These are the employees who have minimum " + minimumSalary + " as their salary")
                menu.Choices()

            elif option == 5:
                mycursor.execute("SELECT Min(Salary) FROM Employees")
                for x in mycursor:
                    x = str(x)

                print(x + " is the minimum salary of the employees")
                menu.Choices()
    

            else:
                raise

        except:
            print("That wasn't a valid option")
            salary.Salary()
#[===] SALARY ACTIONS [===]#

# [===] TABLE SENSITIVE DETAILS [===]#
class SensitiveDetails():
    def Details(self):
        print("""Please choose a number to update a specific table.

1 - Employees
2 - Departments


""")
        try:
            option = int(input(""))

            if option == 1: #employee choice
                Correct = False

                while Correct != True: #getting correct employee id
                    try:
                        ListOfEmployeeID = []
                        EmplID = int(input("Please enter the Employee ID"))

                        mycursor.execute("SELECT EmployeeID FROM Employees")
                        for x in mycursor:
                            x = str(x)
                            ListOfEmployeeID.append(x)

                        NewEmplID = str(EmplID)
                        NewEmplID = ("(" + NewEmplID + ",)")

                        if NewEmplID in ListOfEmployeeID:
                            Correct = True

                        else:
                            print("This Employee ID doesn't exist.")
                            ListOfEmployeeID.clear()

                    except:
                        print("That was the wrong data type.")
                        ListOfEmployeeID.clear()

                mycursor.execute("SELECT Years, DepartmentID FROM Employees WHERE EmployeeID = %s" %(EmplID))
                for x in mycursor:
                    oldValues = x

                ListOfEmployeeID.clear()

                YearChoice = False
                DepartmentChoice = False

                while YearChoice != True: #changing employee years
                    try:
                        print("""Please choose the option that suits you best.

1 - Change the employee number of working years
2 - No change of working years

""")

                        option = int(input(""))

                        if option == 1:
                            YearCorrect = False

                            while YearCorrect != True:
                                try:
                                    NewYear = int(input("How long have they been working for now in years?"))
                                    mycursor.execute("UPDATE Employees SET Years = %s WHERE EmployeeID = %s" %(NewYear, EmplID))
                                    employeeDB.commit()
                                    YearCorrect = True

                                except:
                                    print("That was the wrong data type.")

                            YearChoice = True

                        elif option == 2:
                            YearChoice = True

                        else:
                            raise

                    except:
                        print("That was the wrong data type or out of bounds")

                while DepartmentChoice != True: # changing department id
                    try:
                        print("""Please choose the option that suits you best.

1 - Change the employee Department ID
2 - No change of Department ID

""")
                        option = int(input(""))

                        if option == 1:
                            DepartmentDetail = False

                            while DepartmentDetail != True:
                                try:
                                    mycursor.execute("SELECT DepartmentID, DepartmentName FROM Departments")
                                    for x in mycursor:
                                        print(x)

                                    print("\n")
                                    NewDepartmentIDDetail = int(input("What is the new department that they belong to?"))
                                    mycursor.execute("UPDATE Employees SET DepartmentID = %s WHERE EmployeeID = %s" %(NewDepartmentIDDetail, EmplID))
                                    employeeDB.commit()
                                    DepartmentDetail = True

                                except:
                                    print("Wrong data type or that department doesn't exist.")

                            DepartmentChoice = True

                        elif option == 2:
                            DepartmentChoice = True

                        else:
                            raise

                    except:
                        print("That was the wrong data type or out of bounds")

                print(oldValues)

                mycursor.execute("SELECT Years, DepartmentID FROM Employees WHERE EmployeeID = %s" %(EmplID))
                for x in mycursor:
                    print(x)

                print("\nNew changes are implemented")
                menu.Choices()
                
# change content of department/employees, department -> ID, ask if it's manager or employee count or both
            elif option == 2:
                Correct = False

                while Correct != True:
                    try:
                        ListOfDepartmentID = []
                        DepartID = int(input("Please enter the Department ID"))

                        mycursor.execute("SELECT DepartmentID FROM Departments")
                        for x in mycursor:
                            x = str(x)
                            ListOfDepartmentID.append(x)

                        NewDepartID = str(DepartID)
                        NewDepartID = ("(" + NewDepartID + ",)")

                        if NewDepartID in ListOfDepartmentID:
                            Correct = True

                        else:
                            print("This Department ID doesn't exist.")

                    except:
                        print("That was the wrong data type.")

                # ask if they wanna get rid of manager, employee count

                ManagerChoice = False
                EmployeeChoice = False

                mycursor.execute("SELECT Manager, EmployeeSize FROM Departments WHERE DepartmentID = %s" %(DepartID))
                for x in mycursor:
                    oldValue = x

                while ManagerChoice != True:
                    try:
                        print("""Please choose the option that suits you best.

1 - Change the manager name of the department
2 - No change of the manager name

""")

                        option = int(input(""))

                        if option == 1:
                            ManagerDetail = False

                            while ManagerDetail != True:
                                try:
                                    NewManagerName = str(input("What is the new name of the manager?"))
                                    print(NewManagerName)
                                    print(DepartID)

                                    mycursor.execute("UPDATE Departments SET Manager = '" + NewManagerName + "' WHERE DepartmentID = %s" %(DepartID))
                                    employeeDB.commit()
                                    
                                    ManagerDetail = True

                                except:
                                    print("Wrong data type")

                            ManagerChoice = True

                        elif option == 2:
                            ManagerChoice = True

                        else:
                            raise

                    except:
                        print("That was the wrong data type or out of bounds")


                while EmployeeChoice != True:
                    try:
                        print("""Please choose the option that suits you best.

1 - Change the employee count of the department
2 - No change to the employee count

""")
                        option = int(input(""))

                        if option == 1:
                            EmployeeCount = False

                            while EmployeeCount != True:
                                try:
                                    NewEmployeeCountDetail = int(input("What is the new employee size of this department?"))

                                    mycursor.execute("UPDATE Departments SET EmployeeSize = %s WHERE DepartmentID = %s" %(NewEmployeeCountDetail, DepartID))
                                    employeeDB.commit()

                                    EmployeeCount = True

                                except:
                                    print("Wrong data type")

                            EmployeeChoice = True

                        elif option == 2:
                            EmployeeChoice = True

                        else:
                            raise

                    except:
                        print("That was the wrong data type or out of bounds")

                print(oldValue)

                mycursor.execute("SELECT Manager, EmployeeSize FROM Departments WHERE DepartmentID = %s" %(DepartID))
                for x in mycursor:
                    print(x)

                print("\nNew changes are implemented")
                menu.Choices()             


            # THIS AREA IS FOR DEPARTMENTS


            else:
                raise

        except:
            print("That wasn't a valid option")
            sense.Details()
            
# [===] TABLE SENSITIVE DETAILS [===]#

#[===] TABLE ATTRIBUTES [===]#
class TableAttributes():
    def Attributes(self):
        print("""Please choose a number to see a specific table attributes.

1 - Employees
2 - Departments
3 - Both

""")

        try:
            option = int(input(""))

            if option == 1:
                mycursor.execute("DESCRIBE Employees")
                for x in mycursor:
                    print(x)

                print("Here lies the attributes for the table Employees")
                menu.Choices()
                
            elif option == 2:
                mycursor.execute("DESCRIBE Departments")
                for x in mycursor:
                    print(x)

                print("Here lies the attributes for the table Departments")
                menu.Choices()

            elif option == 3:
                mycursor.execute("DESCRIBE Employees")
                for x in mycursor:
                    print(x)

                print("\n")

                mycursor.execute("DESCRIBE Departments")
                for x in mycursor:
                    print(x)

                print("Here lies the attributes for the table Employees and Departments")
                menu.Choices()

            else:
                raise

        except:
            print("That wasn't a valid option")
            attr.Attributes()
#[===] TABLE ATTRIBUTES [===]#
            
#[===] REMOVING CONTENT [===]#
class RemovingContent():
    def Removing(self):
        print("""Please choose a number to remove data to a specific table.

1 - Employees
2 - Departments

""")
        Accurate = False

        try:
            option = int(input(""))

            if option == 1:
                while Accurate != True:
                    try:
                        EmplID = int(input("\nWhat is the ID of the employee you wish to remove?"))
                        Accurate = True

                    except:
                        print("That was of the invalid data type. Restarting the data process")

                mycursor.execute("DELETE FROM Employees WHERE EmployeeID = %s" %(EmplID))
                employeeDB.commit()

                mycursor.execute("SELECT * FROM Employees")
                for x in mycursor:
                    print(x)

                print("The content is now removed from the table Employees")
                menu.Choices()

            if option == 2:
                while Accurate != True:
                    try:
                        DepartID = int(input("\nWhat is the department ID?"))
                        Accurate = True

                    except:
                        print("That was of the invalid data type. Restarting the data process")

                mycursor.execute("DELETE FROM Departments WHERE DepartmentID = %s" %(DepartID))
                employeeDB.commit()

                mycursor.execute("SELECT * FROM Departments")
                for x in mycursor:
                    print(x)

                print("The content is now removed from the table Departments")
                menu.Choices()

            else:
                raise

        except:
            print("That wasn't a valid option")
            remov.Removing()
            
#[===] REMOVING CONTENT [===]#

#[===] ADDING CONTENT [===] #
class AddingContent():
    def Adding(self):
        print("""Please choose a number to add data to a specific table.

1 - Employees
2 - Departments

""")
        Accurate = False
        
        try:
            option = int(input(""))

            if option == 1:
                while Accurate != True:
                    try:

                        EmplID = int(input("\nWhat is the employee's ID?"))
                        
                        mycursor.execute("SELECT DepartmentID, DepartmentName FROM Departments")
                        for x in mycursor:
                           print(x)
                        
                        DepartmentID = int(input("\nWhich department does the employee belong to?"))
                        EmployeeName = str(input("\nWhat is the name of the employee?"))
                        DegreeName = str(input("\nWhat Degree does the employee has?"))
                        EmployeeYears = int(input("\nHow many years has the employee been with the company?"))
                        EmployeeSalary = int(input("\nWhat is the yearly salary of the employee?"))
                        mycursor.execute("INSERT INTO Employees (EmployeeID, DepartmentID, Name, Degree, Years, Salary) VALUES (%s, %s, %s, %s, %s, %s)", (EmplID, DepartmentID, EmployeeName, DegreeName, EmployeeYears, EmployeeSalary))
                        employeeDB.commit()
                        Accurate = True

                    except:
                        print("That was of the invalid data type. Restarting the data process")

                mycursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s" %(EmplID))
                for x in mycursor:
                    print(x)

                print("This is the new data added into the table Employees")
                menu.Choices()

            if option == 2:
                while Accurate != True:
                    try:
                        DepartID = int(input("\nWhat is the department ID?"))
                        DepartName = str(input("\nWhat is the name of this department?"))
                        ManagerName = str(input("\nWho is the manager of this department?"))
                        EmployeeCount = int(input("\nHow many employees are in this department?"))
                        DepartLocation = str(input("\nWhere is this department located?"))

                        mycursor.execute("INSERT INTO Departments (DepartmentID, DepartmentName, Manager, EmployeeSize, Location) VALUES (%s, %s, %s, %s, %s)", (DepartID, DepartName, ManagerName, EmployeeCount, DepartLocation))
                        employeeDB.commit()

                        Accurate = True

                    except:
                        print("That was of the invalid data type. Restarting the data process")

                mycursor.execute("SELECT * FROM Departments WHERE DepartmentID = %s" %(DepartID))
                for x in mycursor:
                    print(x)



                print("This is the new data added into the table Departments")
                menu.Choices()

            else:
                raise

        except:
            print("That wasn't a valid option")
            add.Adding()

        menu.Choices()
#[===] ADDING CONTENT [===] #

#[===] ADMIN [===] #
add=AddingContent()
remov=RemovingContent()
attr=TableAttributes()
sense=SensitiveDetails()
salary=SalaryActions()
find=FindName()
going=GoingThrough()
departCheck=DepartmentChecking()
view=ViewTableContents()
menu=MenuSystem()
reset=ResettingTable()
menu.Talk()
#[===] ADMIN [===] #
