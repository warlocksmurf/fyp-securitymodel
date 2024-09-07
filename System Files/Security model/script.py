#!/usr/bin/env python3

import pymysql
from asterisk.agi import AGI

# initialize AGI
agi = AGI()
agi.verbose("AGI STARTED")

caller_id = agi.env['agi_callerid']

try:
    # establish database connection and cursor
    db = pymysql.connect(host='localhost', user='asterisk', password='123', database='capstone')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM blacklist WHERE caller_id = %s", (caller_id,))
    result = cursor.fetchone()

    # check if caller is in the blacklist table
    if result:
        agi.set_variable("BLACKLIST", "TRUE")
        agi.verbose("Caller is blacklisted")
    else:
        agi.set_variable("BLACKLIST", "FALSE")
        agi.verbose("Caller is non-blacklisted")

except Exception as e:
    agi.verbose("Error: {}".format(e))

finally:
    db.close()  # close database connection
    