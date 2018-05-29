class SQLTable:
    class Attribute:
        def __init__(self, tName, aName, aType, aLimit=None,):
            self.attName = aName
            self.attType = aType
            self.attLimit = aLimit
            self.tbName = tName
            self.attData = []

        def __str__(self):
            if self.attLimit is not None:
                return "\n  " + self.attName + " " + self.attType + " " + self.attLimit
            return "\n  " + self.attName + " " + self.attType

    class ForeignKey:
        def __init__(self):
            self.forKeys = []  # Stores the name of the attributes of its own table. Store a list of attribute name if it references multiple foreign key reference to the same table
            self.attrPointer = []  # Points to the attr object that is reference to. This list holds the object and a list of objects if there are more than one foreign key reference the same table.

        def __str__(self):
            st = ""
            if len(self.forKeys) != 0:
                for i in range(len(self.attrPointer)):
                    if not isinstance(self.attrPointer[i], list):
                        st += "\n     FOREIGN KEY (" + self.forKeys[i] + ")"
                        st += " REFERENCES " + self.attrPointer[i].tbName + "(" + self.attrPointer[i]. attName + ")"
                    else:
                        st += "\n     FOREIGN KEY (" + ", ".join(self.forKeys[i]) + ")"
                        st += " REFERENCES " + self.attrPointer[i][0].tbName + "(" + ", ".join(attr.attName for attr in self.attrPointer[i]) + ")"
            return st

    def __init__(self, tName):
        self.tableName = tName
        self.tableAttributes = []  # List of attributes
        self.primaryKey = []
        self.foreignKey = self.ForeignKey()

    # Find and append the attribute object from this table to the FK attr list
    def appendAttribute(self, rTable, attr):
        for i in rTable.tableAttributes:
            if i.attName == attr:
                self.foreignKey.attrPointer.append(i)
                return

    # Find and append the attribute object list from this table to the FK attr list
    def appendAttribute2(self, rTable, attrLst):
        lst = []
        for i in rTable.tableAttributes:
            for attr in attrLst:
                if i.attName == attr:
                    lst.append(i)
        self.foreignKey.attrPointer.append(lst)

    def __repr__(self):
        st = self.tableName
        st += ",".join(str(attr) for attr in self.tableAttributes)
        st += "\n     PRIMARY KEY" + " (" + ", ".join(self.primaryKey) + ")"
        st += str(self.foreignKey)
        return st + "\n"
