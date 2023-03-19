#!/usr/bin/python3
# List every state from the database hbtn_0e_0_usa
# Script takes 3 arguments: mysql username,password and databas
# Usage ./0-select_states.py [mysql username] [password] [database name]

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY states.id ASC")
    [print(state) for state in c.fetchall()]
