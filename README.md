#Parsing SQL table Definition

The Program consist of a SQL table definition parser. It takes a SQL table definition file, (ex: SQLTableCode.sql)
The table definition should follow this format:

    CREATE TABLE Person(
      username VARCHAR (50),
      password VARCHAR (50),
      first_name VARCHAR (50),
      last_name VARCHAR (50),
      PRIMARY KEY (username)
    )

    CREATE TABLE Content(
      id INT AUTO_INCREMENT,
      username VARCHAR (50),
      timest TIMESTAMP,
      file_path VARCHAR (100),
      content_name VARCHAR (50),
      public BOOLEAN,
      PRIMARY KEY (id),
      FOREIGN KEY (username) REFERENCES Person (username)
    )

The Parser parses the definition using these keywords and all keywords need to be CAPITAPZED.

    CREATE TABLE
    PRIMARY KEY
    FOREIGN KEY
    REFERENCES
    INT
    TIMESTAMP
    BOOLEAN



#How to use

After parsing the SQL table definition into the correct data structure, data from CSV data files (ex: Comment.csv, Firstname.csv, Password.csv). Each data file contains potential data that can be used for a specific attribute in the database. The user must know which attribute requires data to be generated and which attributes are foreign keys, which will get data from the attribute it is referencing. The data file is a single column csv file.

*** Make sure that the data file is in CSV format and there are no extra row in the front or the end of the file***

When using the program with new SQL table definition, the only thing that news to be change is the ExportSQL.py file, setDataToAttribute function. Just need to open new data file using the readDataFile function. Then just create new elif statement for new attributes that is not listed in the program. Get data for that attribute from the data file that matches that attribute.

![alt tag](https://raw.github.com/cw1753/SQL_Data_Generator/Example Picture/Import data.JPG)
