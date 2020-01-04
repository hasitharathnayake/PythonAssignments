import sqlite3

connection=sqlite3.connect('Ages.sqlite')
cur=connection.cursor()

#if the db exists then override
#then create a table and 2 columns name and age
cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

#Entering data
data='''DELETE FROM Ages;INSERT INTO Ages (name, age) VALUES ('Naomie', 13);
INSERT INTO Ages (name, age) VALUES ('Raonaid', 20);
INSERT INTO Ages (name, age) VALUES ('Kellsey', 20);
INSERT INTO Ages (name, age) VALUES ('Youer', 22);
INSERT INTO Ages (name, age) VALUES ('Elody', 25);'''

#Format data to avoid seperate entry
sqlcmds=data.split(';')
cleanSqlcmds=list()
for item in sqlcmds[1:-1]:
    item=item.strip('\n')
    cur.execute(item)
#commit to disk not needed only use in intervals
connection.commit()

#view db
for row in cur.execute('SELECT name, age FROM Ages ORDER BY age'):
    print(str(row[0]), row[1])
#for getting marks
for row in cur.execute('SELECT hex(name||age) AS X FROM Ages ORDER BY X'):
    print(str(row[0]))
    break #print just one
