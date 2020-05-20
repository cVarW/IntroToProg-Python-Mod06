# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# RRoot,1.1.2030,Fixed bug by clearing the list before it was refilled
# CWei,05.17.2020,Modified code to complete assignment 6
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection


# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """ Processing the data to and from a text file """

    @staticmethod
    def ReadFileDataToList(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def WriteListDataToFile(file_name, list_of_rows):
        # pass  # TODO: Add code Here
        """
        Desc -Reads data from th list of dictionaries into a file

        :param file_name:
        :param list_of_rows:
        :return:
        """
        file = open(file_name, "w")
        for dicR in list_of_rows:
            file.write(dicR["Task"] + "," + dicR["Priority"] + "\n")
        file.close()

    # TODO: Create more functions that perform various Processing task as needed
    @staticmethod
    def AddNewItem(v1, v2):
        """
        Add new item to lstTable

        :param v1: (string)
        :param v2: (string)
        :return: lstTable
        """
        dicRow = {"Task": v1, "Priority": v2}
        lstTable.append(dicRow)
        return lstTable

    @staticmethod
    def RemoveItemFromList(vKey,vLnItm):
        """
        If Item is found in current list, lstTable. 1st matching
            item will be removed. Else, return 'Item not found'

        :param vKey: (string)
        :param vLnItm: (string)
        :return: lstTable
        """
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(vKey == str(list(dict(lstTable[intRowNumber]).values())[0])):
                del lstTable[intRowNumber]  # Delete the row if a match is found
                vLnItm = True   # Set the flag so the loop stops
            intRowNumber += 1   # Increment counter to get next row
        return vLnItm



# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for perform Input and Output """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Create more functions that perform various IO tasks as needed
    @staticmethod
    def InputNewItem():
        """
        Ask user for new task and priority
        :param v1: (string)
        :param v2: (string)
        :return: string
        """
        v1 = str(input("What is the task? - ")).strip()  # Get task from user
        v2 = str(input("What is the priority? [high|low] - ")).strip()  # Get priority from user
        print()  # Add an extra line for looks
        return v1, v2


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
FileProcessor.ReadFileDataToList(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.2 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        # Step 3.2.a - Ask user for new task and priority
        # ToDo: Place IO code in a new function
        # strTask = str(input("What is the task? - ")).strip()  # Get task from user
        # strPriority = str(input("What is the priority? [high|low] - ")).strip()  # Get priority from user
        # print()  # Add an extra line for looks
        (strTask, strPriority) = IO.InputNewItem()  # Assign arguments to strTask & strPriority

        # Step 3.2.b  Add item to the List/Table
        # ToDo: Place processing code in a new function
        # dicRow = {"Task": strTask, "Priority": strPriority}  # Create a new dictionary row
        # lstTable.append(dicRow)  # Add the new row to the list/table
        lstTable = FileProcessor.AddNewItem(strTask, strPriority)
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.3 - Remove a new item to the list/Table
    elif (strChoice == '3'):

        # Step 3.3.a - Ask user for item and prepare searching while loop
        strKeyToRemove = input("Which TASK would you like removed? - ")  # get task user wants deleted
        blnItemRemoved = False  # Create a boolean Flag for loop

        # ToDo: Place processing code in a new function
        # intRowNumber = 0  # Create a counter to identify the current dictionary row in the loop

        # Step 3.3.b - Search though the table or rows for a match to the user's input
        # while (intRowNumber < len(lstTable)):
        #    if (strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):  # Search current row column 0
        #        del lstTable[intRowNumber]  # Delete the row if a match is found
        #        blnItemRemoved = True  # Set the flag so the loop stops
        #    intRowNumber += 1  # Increase counter to get next row
        blnItemR = FileProcessor.RemoveItemFromList(strKeyToRemove, blnItemRemoved)

        # Step 3.3.c - Update user on the status of the search
        if (blnItemR == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print()  # Add an extra line for looks

        # Step 3.3.d - Show the current items in the table
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.4 - Save tasks to the ToDoFile.txt file
    elif (strChoice == '4'):

        # Step 3.4.a - Show the current items in the table
        IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table

        # Step 3.4.b - Ask if user if they want save that data
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            # ToDo: Place processing code in a New function
            FileProcessor.WriteListDataToFile(strFileName, lstTable)
            # objFile = open(strFileName, "w")
            # for dicRow in lstTable:  # Write each row of data to the file
            #    objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            # objFile.close()

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu

    # Step 3.5 - Reload data from the ToDoFile.txt file (clears the current data from the list/table)
    elif (strChoice == '5'):
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss
        strYesOrNo = input("Reload file data without saving? [y/n] - ")  # Double-check with user
        if (strYesOrNo.lower() == 'y'):
            lstTable.clear()  # Added to fix bug 1.1.2030
            FileProcessor.ReadFileDataToList(strFileName, lstTable)  # Replace the current list data with file data
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        else:
            input("File data was NOT reloaded! Press the [Enter] key to return to menu.")
            IO.ShowCurrentItemsInList(lstTable)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.6 - Exit the program
    elif (strChoice == '6'):
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #
