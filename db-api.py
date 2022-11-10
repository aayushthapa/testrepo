#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# py database api provides common interface for various database engines to the extent that it's possible to do so
# dbapi is a consolidated interface for a number of database systems
# Every database has its own requirement, interface, paradigm; no single interface will serve all of them equally
# Like many scripting languages, python ships with sqlite - good for online and mobile applications

# sqlite - database will be fully contained in 1 file and this file is portable, can be used in different OS
# can be interfaced with any sqlite driver in any language and we can use that database that's all in one file
# run this to program to create a file named 'dp-api.db'

import sqlite3

def main():
    print('connect')   
    db = sqlite3.connect('db-api.db')   # connecting to database; calling connect on sqlite3 object which will return database handle, from that database handle in turn we can use to interface with database
    cur = db.cursor()    # grabbing a cursor from database handle to be able to keep track where we are in the database as we run database commands
    print('create')
    cur.execute("DROP TABLE IF EXISTS test")  # to exeute SQL
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    db.commit()
    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]   #fetchone from the cursor after we execute the previous command which will return a row with one element in it that will have the count of # of rows in the table
    print(f'there are {count} rows in the table.')
    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)
    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()

if __name__ == '__main__': main()
