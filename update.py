import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="7668",
    database="sway-db"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Clubs (PlayerID VARCHAR (255), PlayerName VARCHAR(255), JerseyNumber VARCHAR(255), ClubName VARCHAR(255), SigningAmount VARCHAR(255), Country VARCHAR(255))")

sql = "INSERT INTO Clubs (PlayerID, PlayerName, JerseyNumber, ClubName, SigningAmount, Country) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    # ("01", "Cristiano Ronaldo", "07", "Manchester United", "445000 $", "Portugal"),
    # ("02", "Leoniel Messi", "30", "PSG", "348000 $", "Argentina"),
    # ("03", "Paul Pogba", "10", "Manchester United", "310000 $", "France"),
    # ("04", "Serigo Ramos", "04", "PSG", "326000 $", "Spain"),
    # ("05", "Kevin Bruyne", "25", "Manchester City", "290000 $", "Germany"),
    # ("06", "Luis Suarez", "10", "ATK Madrid", "257000 $", "Uruguay"),
    # ("07", "Mohamed Salah", "75", "Liverpool F.C.", "287500 $", "Egypt"),
]
mycursor.executemany(sql, val)
mydb.commit()
