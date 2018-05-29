from SQLTable import *


# Clean the string of brackets and commas
def cleanStr(m):
    return m.replace('(', '').replace(')', '').replace(',', '')


# Return the table the FK is referencing to
def findReferenceTable(tbList, tbName):
    for i in tbList:
        if i.tableName == tbName:
            return i


# Parse the list of words from the SQL Code
# Return a List of SQLTable Objects
def parseSQLTable(wordsLst):
    tableLst = []
    # Runs through the whole word list and create data structure base on SQL KEY WORDS
    for i in range(len(wordsLst)):
        # CREATE TABLE Check
        if wordsLst[i] == "CREATE" and wordsLst[i+1] == "TABLE":
            table = SQLTable(cleanStr(wordsLst[i+2]))
            tableLst.append(table)
            i += 3
            while i < len(wordsLst):
                # End of Creating Table
                if wordsLst[i] == ')':
                    i += 1
                    break

                # Primary Key Check
                if wordsLst[i] == "PRIMARY" and wordsLst[i + 1] == "KEY":
                    i += 2
                    while i < len(wordsLst):
                        pk = cleanStr(wordsLst[i])
                        table.primaryKey.append(pk)
                        if wordsLst[i].find(')') != -1:  # Reaches the end of the Primary Key list
                            i += 1
                            break
                        i += 1

                # Foreign Key Check
                elif wordsLst[i] == "FOREIGN" and wordsLst[i + 1] == "KEY":
                    i += 2
                    # Count FK from the same table
                    fkCounter = 0
                    # In FK line
                    while i < len(wordsLst):
                        if wordsLst[i] == "REFERENCES":
                            if fkCounter > 1:
                                lst = []
                                for ct in range(fkCounter):  # Add more than one FK from the same table to the FK list
                                    lst.append(cleanStr(wordsLst[i+ct-fkCounter]))
                                table.foreignKey.forKeys.append(lst)
                            else:
                                # Add one FK to FK list
                                table.foreignKey.forKeys.append(cleanStr(wordsLst[i-1]))

                            tb = findReferenceTable(tableLst, wordsLst[i+1])  # The table it references to
                            i += 2
                            # After References
                            while i < len(wordsLst):
                                if fkCounter > 1:
                                    lst = []
                                    for ct in range(fkCounter):
                                        lst.append(cleanStr(wordsLst[i + ct]))
                                    table.appendAttribute2(tb, lst) # Add a list of Attr from referenced the same table
                                    i += fkCounter - 1
                                else:
                                    table.appendAttribute(tb, cleanStr(wordsLst[i]))  # Add Attr from referenced table
                                # Last FK to add
                                if wordsLst[i].find(')') != -1:
                                    i += 1
                                    break
                                i += 1
                            break
                        fkCounter += 1
                        i += 1

                # Adding Attributes
                else:
                        # Check for End line with a comma ( , )
                        if wordsLst[i+1].find(',') != -1:  # Has no limit restriction
                            attr = table.Attribute(table.tableName, wordsLst[i], cleanStr(wordsLst[i+1]))
                            table.tableAttributes.append(attr)
                            i += 2
                        else:  # Has a limit restriction
                            attr = table.Attribute(table.tableName, wordsLst[i], wordsLst[i + 1], cleanStr(wordsLst[i + 2]))
                            table.tableAttributes.append(attr)
                            i += 3
    return tableLst
