import sqlite3

con = sqlite3.connect('school.db')

def sql_insert(con, entities):

    cursorObj = con.cursor()
    
    cursorObj.execute('INSERT INTO stu(id, name, regNumber, accommodationType, course) VALUES(?, ?, ?, ?, ?)', entities)
    
    con.commit()

entities = (1, 'Rehema', 147620, 'full-board', 'Computer Science')

sql_insert(con, entities)