import sqlite3 as sq

connect = sq.connect("booking.db")
cursor = connect.cursor()


#__________________________________ Generate Command __________________________________________
GENERATE_COMMAND = """
-- Create the table
CREATE TABLE ResortOwnership (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Address TEXT,
    MembershipTier TEXT,
    ResortName TEXT,
    OwnershipDays INTEGER
);

-- Function to generate random names
CREATE TABLE FirstNames (
    FirstName TEXT
);

INSERT INTO FirstNames (FirstName) VALUES 
('John'), ('Mary'), ('Michael'), ('Emma'), ('William'), ('Sophia'), ('James'), ('Olivia'), 
('Alexander'), ('Ava'), ('Ethan'), ('Isabella'), ('Liam'), ('Charlotte'), ('Noah'), ('Mia'), 
('Logan'), ('Amelia'), ('Benjamin'), ('Emily');

CREATE TABLE LastNames (
    LastName TEXT
);

INSERT INTO LastNames (LastName) VALUES 
('Smith'), ('Johnson'), ('Williams'), ('Jones'), ('Brown'), ('Davis'), ('Miller'), ('Wilson'), 
('Moore'), ('Taylor'), ('Anderson'), ('Thomas'), ('Jackson'), ('White'), ('Harris'), ('Martin'), 
('Thompson'), ('Garcia'), ('Martinez'), ('Robinson');

-- Function to generate random addresses
CREATE TABLE Streets (
    Street TEXT
);

INSERT INTO Streets (Street) VALUES 
('Main Street'), ('First Avenue'), ('Second Street'), ('Maple Avenue'), ('Oak Street'), 
('Park Avenue'), ('Washington Street'), ('Elm Street'), ('Center Street'), ('Church Street');

CREATE TABLE Cities (
    City TEXT
);

INSERT INTO Cities (City) VALUES 
('New York'), ('Los Angeles'), ('Chicago'), ('Houston'), ('Phoenix'), ('Philadelphia'), 
('San Antonio'), ('San Diego'), ('Dallas'), ('San Jose');

CREATE TABLE ZipCodes (
    ZipCode TEXT
);

INSERT INTO ZipCodes (ZipCode) VALUES 
('10001'), ('90001'), ('60601'), ('77001'), ('85001'), ('19101'), ('78201'), ('92101'), 
('75201'), ('95101');

-- Function to generate random membership tier
CREATE TABLE MembershipTiers (
    MembershipTier TEXT
);

INSERT INTO MembershipTiers (MembershipTier) VALUES 
('Gold Luxe'), ('Silver Prestige'), ('Diamond Elite Prestige'), ('Platinum Premier');

-- Function to generate random resort name
CREATE TABLE Resorts (
    ResortName TEXT
);

INSERT INTO Resorts (ResortName) VALUES 
('Classy Courts'), ('Fencing Fields'), ('Pleasant Piazza'), ('Snooty Steps'), 
('Ritzy Rivera'), ('The Other Other Windmill'), ('Grand Glacier'), ('Lavish Lair');

-- Insert random data into the table
WITH RandomData AS (
  SELECT
    (SELECT FirstName FROM FirstNames ORDER BY RANDOM() LIMIT 1) || ' ' || (SELECT LastName FROM LastNames ORDER BY RANDOM() LIMIT 1) AS Name,
    (SELECT Street FROM Streets ORDER BY RANDOM() LIMIT 1) || ', ' || (SELECT City FROM Cities ORDER BY RANDOM() LIMIT 1) || ', ' || (SELECT ZipCode FROM ZipCodes ORDER BY RANDOM() LIMIT 1) AS Address,
    (SELECT MembershipTier FROM MembershipTiers ORDER BY RANDOM() LIMIT 1) AS MembershipTier,
    (SELECT ResortName FROM Resorts ORDER BY RANDOM() LIMIT 1) AS ResortName,
    CAST((RANDOM() * 30) + 1 AS INTEGER) AS OwnershipDays
  FROM
    sqlite_master
  LIMIT 12
)
INSERT INTO ResortOwnership (Name, Address, MembershipTier, ResortName, OwnershipDays)
SELECT * FROM RandomData;

"""

#_________________________________create table_____________________________________________
cursor.execute("""CREATE TABLE ResortOwnership (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Address TEXT,
    MembershipTier TEXT,
    ResortName TEXT,
    OwnershipDays INTEGER
);""")




##________________________Function to generate random names_____________________

cursor.execute("""CREATE TABLE FirstNames (
    FirstName TEXT
);""")

cursor.execute("""INSERT INTO FirstNames (FirstName) VALUES
('John'), ('Mary'), ('Michael'), ('Emma'), ('William'), ('Sophia'), ('James'), ('Olivia'), 
('Alexander'), ('Ava'), ('Ethan'), ('Isabella'), ('Liam'), ('Charlotte'), ('Noah'), ('Mia'), 
('Logan'), ('Amelia'), ('Benjamin'), ('Emily');""")

print("im reaching here")

cursor.execute("""CREATE TABLE LastNames (
    LastName TEXT
);""")

cursor.execute("""INSERT INTO LastNames (LastName) VALUES 
('Smith'), ('Johnson'), ('Williams'), ('Jones'), ('Brown'), ('Davis'), ('Miller'), ('Wilson'), 
('Moore'), ('Taylor'), ('Anderson'), ('Thomas'), ('Jackson'), ('White'), ('Harris'), ('Martin'), 
('Thompson'), ('Garcia'), ('Martinez'), ('Robinson');""")




#____________________Function to generate random addresses__________________

cursor.execute("""CREATE TABLE Streets (
    Street TEXT
);""")

cursor.execute("""INSERT INTO Streets (Street) VALUES 
('Main Street'), ('First Avenue'), ('Second Street'), ('Maple Avenue'), ('Oak Street'), 
('Park Avenue'), ('Washington Street'), ('Elm Street'), ('Center Street'), ('Church Street');""")

cursor.execute("""CREATE TABLE Cities (
    City TEXT
);""")

cursor.execute("""INSERT INTO Cities (City) VALUES 
('New York'), ('Los Angeles'), ('Chicago'), ('Houston'), ('Phoenix'), ('Philadelphia'), 
('San Antonio'), ('San Diego'), ('Dallas'), ('San Jose');""")

cursor.execute("""CREATE TABLE ZipCodes (
    ZipCode TEXT
);
""")

cursor.execute("""INSERT INTO ZipCodes (ZipCode) VALUES 
('10001'), ('90001'), ('60601'), ('77001'), ('85001'), ('19101'), ('78201'), ('92101'), 
('75201'), ('95101');""")

#_________________________Membership Tiers_________________________________________

cursor.execute("""CREATE TABLE MembershipTiers (
    MembershipTier TEXT
);""")

cursor.execute("""INSERT INTO MembershipTiers (MembershipTier) VALUES 
('Gold Luxe'), ('Silver Prestige'), ('Diamond Elite Prestige'), ('Platinum Premier');""")

#___________________________Resort Names____________________________________________
cursor.execute("""CREATE TABLE Resorts (
    ResortName TEXT
);""")

cursor.execute("""INSERT INTO Resorts (ResortName) VALUES 
('Classy Courts'), ('Fencing Fields'), ('Pleasant Piazza'), ('Snooty Steps'), 
('Ritzy Rivera'), ('The Other Other Windmill'), ('Grand Glacier'), ('Lavish Lair');""")

cursor.execute("""INSERT INTO ResortOwnership (Name, Address, MembershipTier, ResortName, OwnershipDays)
SELECT
    (SELECT FirstName FROM FirstNames ORDER BY RANDOM() LIMIT 1) || ' ' || (SELECT LastName FROM LastNames ORDER BY RANDOM() LIMIT 1),
    (SELECT Street FROM Streets ORDER BY RANDOM() LIMIT 1) || ', ' || (SELECT City FROM Cities ORDER BY RANDOM() LIMIT 1) || ', ' || (SELECT ZipCode FROM ZipCodes ORDER BY RANDOM() LIMIT 1),
    (SELECT MembershipTier FROM MembershipTiers ORDER BY RANDOM() LIMIT 1),
    (SELECT ResortName FROM Resorts ORDER BY RANDOM() LIMIT 1),
    CAST((RANDOM() * 30) + 1 AS INTEGER)
FROM
    sqlite_master
LIMIT 12;""")

#cursor.execute("""SELECT * FROM ResortOwnership;""")

#_____________________________ Post Command _________________________________________
connect.close()