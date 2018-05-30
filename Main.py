from ParsingSQL import parseSQLTable
from ExportSQL import *
import sys

# Link to the github: https://github.com/cw1753/SQL_Data_Generator

if __name__ == '__main__':
    # Fix the encoding for the files
    reload(sys)
    sys.setdefaultencoding('utf8')

    # Open file and Parse SQL table Code
    tableFile = open("Data\SQLTableCode.sql", "r")
    # Split the whole file by space into a List of words and import the table into our data structure.
    wordList = tableFile.read().replace('(', ' ').split()
    tableList = parseSQLTable(wordList)  # This list contain a list of table object
    for i in tableList:
        print i

    # Close file
    tableFile.close()

    # Import the data from the data files into the Attribute data list
    setDataToAttribute(tableList)

    # Write the data in SQL insert format
    writeToSQL(tableList)
