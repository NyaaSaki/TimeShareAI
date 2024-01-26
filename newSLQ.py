import sqlite3 as sq
connect = sq.connect("ownership.db")
cursor = connect.cursor()

#cursor.execute("""CREATE TABLE ResortOwnership (
#    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#   Name TEXT,
#    Address TEXT,
#    MembershipTier TEXT,
#    ResortName TEXT,
#    OwnershipDays INTEGER
#);""")
"""










INSERT INTO ResortOwnership (Name, Address, MembershipTier, ResortName, OwnershipDays) VALUES
('Alexander Moore', '111 Elm Street, San Diego, 92101', 'Platinum Premier', 'Lavish Lair', 21);




"""

cursor.execute("""
INSERT INTO ResortOwnership (Name, Address, MembershipTier, ResortName, OwnershipDays) VALUES
('Alexander Moore', '111 Elm Street, San Diego, 92101', 'Platinum Premier', 'Lavish Lair', 21);

""")

cursor.close()