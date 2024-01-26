import sqlite3 as sq




def execute(query):
    connect = sq.connect("booking.db")
    cursor = connect.cursor()
    cursor.execute(query)
    cursor.close()
    
connect = sq.connect("booking.db")
cursor = connect.cursor()
#cursor.execute("""INSERT INTO ResortOwnership (Name, Address, MembershipTier, ResortName, OwnershipDays) VALUES
#('John Smith', '123 Main Street, New York, 10001', 'Gold Luxe', 'Classy Courts', 7),
#('Emma Johnson', '456 Oak Avenue, Los Angeles, 90001', 'Silver Prestige', 'Fencing Fields', 14),
#('Michael Williams', '789 Elm Street, Chicago, 60601', 'Diamond Elite Prestige', 'Pleasant Piazza', 21),
#('Olivia Brown', '101 Park Avenue, Houston, 77001', 'Gold Luxe', 'Snooty Steps', 10),
#('William Davis', '234 Washington Street, Phoenix, 85001', 'Diamond Elite Prestige', 'Ritzy Rivera', 28),
#('Sophia Miller', '567 Center Street, Philadelphia, 19101', 'Platinum Premier', 'The Other Other Windmill', 7),
#('James Wilson', '890 Church Street, San Antonio, 78201', 'Gold Luxe', 'Grand Glacier', 14),
#('Alexander Moore', '111 Elm Street, San Diego, 92101', 'Platinum Premier', 'Lavish Lair', 21),
#('Ava Taylor', '222 Center Street, Dallas, 75201', 'Diamond Elite Prestige', 'Classy Courts', 10),
##('Ethan Anderson', '333 First Avenue, San Jose, 95101', 'Gold Luxe', 'Fencing Fields', 28),
#('Isabella Thomas', '444 Second Street, New York, 10001', 'Platinum Premier', 'Pleasant Piazza', 14),
#('Liam Jackson', '555 Maple Avenue, Los Angeles, 90001', 'Diamond Elite Prestige', 'Snooty Steps', 21);""")
cursor.close()