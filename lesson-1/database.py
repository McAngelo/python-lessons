import sqlite3
# creating a database
conn = sqlite3.connect('crop_guide.sqlite')
cur = conn.cursor()
try:
    # create a table in the database named crop
    cur.execute('CREATE TABLE crop(season VARCHAR, nh VARCHAR, nl VARCHAR, sh VARCHAR, sl VARCHAR, northern VARCHAR, southern VARCHAR)')
except:
    print("An error occured while creating the table")

# insert values to the table crop
cur.execute('INSERT INTO crop (season,nh,nl,sh,sl) values ("Kharif","Sugarcane","Rice","Cotton","Maize")')
cur.execute('INSERT INTO crop (season,nh,nl,sh,sl) values ("Rabi","Wheat","Mustard","Banana","Mango")')
cur.execute('INSERT INTO crop (season,nh,nl,sh,sl) values ("Zaid","Cucumber","Jute","Pumpkin","Tomato")')
cur.execute('INSERT INTO crop (northern) values ("Chandigarh  Delhi  Haryana  Himachal Pradesh  Jammu  Kashmir  Ladakh  Punjab  Rajasthan  Uttarakhand  Uttar Pradesh  Madhya Pradesh  West Bengal  Bihar  Gujarat  ")')
cur.execute('INSERT INTO crop (southern) values ("Andhra Pradesh  Karnataka  Kerala  Lakshadweep  Puducherry  Tamil Nadu  Telangana  Chennai  Bengaluru  Hyderabad  Kochi  Warangal  Thiruvananthapuram  Coimbatore  Visakhapatanam  Mysuru  Madurai  Vijayawada Kozhikode")')
#to commit the changes 
conn.commit()