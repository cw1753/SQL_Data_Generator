from TimeStampGenerator import *
import random
import hashlib


# Read data file. Return list
def readDataFile(fileName):
    f = open(fileName, "r")
    lst = f.read().split('\n')
    f.close()
    # print lst
    return lst


# Set Data to table and attribute
def setDataToAttribute(tbList):
    # Number of rows for the initial or main table.
    numFirstSample = 16
    # Number of rows for the other table
    numSample = 8

    # Read Data file to lists
    firstnameList = readDataFile("Data\Firstname.csv")
    lastnameList = readDataFile("Data\Lastname.csv")
    passwordList = readDataFile("Data\Password.csv")
    contentList = readDataFile("Data\Content.csv")
    groupList = readDataFile("Data\Group.csv")
    descriptionList = readDataFile("Data\Description.csv")
    commentList = readDataFile("Data\Comment.csv")

    # Import data to each attribute's data list
    randLst = random.sample(xrange(0, len(firstnameList)), numFirstSample)
    for tb in tbList:
        # Check for foreign Key
        for fk in range(len(tb.foreignKey.forKeys)):
            fkAttr = tb.foreignKey.attrPointer[fk]
            if not isinstance(fkAttr, list):
                for attI in range(len(tb.tableAttributes)):
                    if tb.tableAttributes[attI].attName == tb.foreignKey.forKeys[fk]:
                        attrIndex = attI
                        break
                rdSample = random.sample(xrange(0, len(fkAttr.attData)), numSample)
                for sp in rdSample:
                    tb.tableAttributes[attrIndex].attData.append(fkAttr.attData[sp])
            else:
                index = []
                tempCount = 0
                for attI in range(len(tb.tableAttributes)):
                    if tb.tableAttributes[attI].attName == tb.foreignKey.forKeys[fk][tempCount]:
                        index.append(attI)
                        tempCount += 1
                rdSample = random.sample(xrange(0, len(fkAttr[0].attData)), numSample)
                for sp in rdSample:
                    for ind in range(len(index)):
                        tb.tableAttributes[index[ind]].attData.append(fkAttr[ind].attData[sp])

        # Goes through the list of attribute
        for att in tb.tableAttributes:
            # Add data only if the attribute data list is empty
            if len(att.attData) == 0:
                if att.attType == 'BOOLEAN':  # Randomly choose TRUE or FALSE
                    for i in range(numSample):
                        att.attData.append(random.randint(0, 1))
                elif att.attType == 'TIMESTAMP':  # Uses our TimeStampGenerator
                    for i in range(numSample):
                        att.attData.append(genTimeStamp())
                else:
                    if att.attName == "username":  # Automatically create username with User + incremented number
                        for i in range(numFirstSample):
                            att.attData.append('User' + str(i + 1))
                    elif att.attName == 'password':  # Uses the password in the password file
                        for i in range(numFirstSample):
                            att.attData.append(hashlib.md5(passwordList[0].encode('utf-8')).hexdigest())  # The password uses md5 encoding
                    elif att.attName == 'first_name':  # Uses first name from the firstname file
                        for i in randLst:
                            att.attData.append(firstnameList[i])
                    elif att.attName == 'last_name':  # Uses last name from the lastname file
                        for i in randLst:
                            att.attData.append(lastnameList[i])
                    elif att.attName == 'id': # Id is auto incremented
                        for i in range(numSample):
                            att.attData.append(i)
                    elif att.attName == 'file_path':  # Automatically create file path which is just a string and does not represent real file path
                        for i in range(numSample):
                            att.attData.append("file_path" + str(random.randint(0, len(contentList))))
                    elif att.attName == 'content_name':  # Uses the content name in the content file
                        for i in range(numSample):
                            att.attData.append(contentList[random.randint(0, len(contentList)-1)])
                    elif att.attName == 'comment_text':  # Uses the comment in the comment file
                        for i in range(numSample):
                            att.attData.append(commentList[random.randint(0, len(commentList)-1)])
                    elif att.attName == 'group_name':  # Uses the group name in the group file
                        for i in range(numSample):
                            att.attData.append(groupList[random.randint(0, len(groupList)-1)])
                    elif att.attName == 'description':  # Uses the description in the description file
                        for i in range(numSample):
                            att.attData.append(descriptionList[random.randint(0, len(descriptionList)-1)])

                    # Can add more data files base on the new attributes in a new set of tables.
                    # Can follow the same format as used above to import the data into teh attributes' data list.

    print("Finish importing the data into our data structure")


# Write to SQLData File. The SQL code will delete all data from the table then insert the new data for each table
def writeToSQL(tbList):
    outFile = open("Output_SQLDataCode.sql", 'w+')
    # Writing DELETE functions
    for tb in range(1, len(tbList)+1):
        outFile.write("DELETE FROM " + tbList[-tb].tableName + ";\n")
    # Writing INSERT functions for new data
    for tb in tbList:
        outFile.write("INSERT INTO " + tb.tableName + " (" + ", ".join(attr.attName for attr in tb.tableAttributes) + ") VALUES\n")
        for i in range(len(tb.tableAttributes[0].attData)):
            outFile.write("(")
            for k in range(len(tb.tableAttributes)):
                if tb.tableAttributes[k].attType == 'INT' or tb.tableAttributes[k].attType == 'BOOLEAN':
                    outFile.write(str(tb.tableAttributes[k].attData[i]))
                else:
                    outFile.write("'" + str(tb.tableAttributes[k].attData[i]) + "'")

                if k != len(tb.tableAttributes)-1:
                    outFile.write(",")
            outFile.write(")")
            if i != len(tb.tableAttributes[0].attData) - 1:
                outFile.write(",\n")
        outFile.write(";\n\n\n\n")
    print("Finish exporting the data into SQL format")

