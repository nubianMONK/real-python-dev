# Create a CAR DB with a table called inventory



import sqlite3

with sqlite3.connect("car.db") as connection:
    c = connection.cursor()
    
    # update data
    #c.execute("CREATE table inventory(Make TEXT, Model TEXT, Quantity INT)")
    
    
    # update data
    c.execute("UPDATE inventory SET Quantity = 10 WHERE Model = 'Focus'")
    c.execute("UPDATE inventory SET Quantity = 40 WHERE Model = 'FX'")
    
    #list to hold the records to be added to the inventory table
    cars = [ 
            
            ('Ford', 'Focus', 5),
            ('Ford', 'Exodus', 10),
            ('Ford', 'Sapphire',15),
            ('Honda', 'Accord', 25),
            ('Honda', 'FX', 30)
           ]
    
    # delete data
    #c.executemany('INSERT INTO inventory VALUES(?, ?, ? )', cars)
    
    print "\nNEW DATA: \n"
    
    c.execute("SELECT * FROM inventory WHERE Make='Ford'")
    
    
    rows = c.fetchall()
    
    
    
    for r in rows: 
        print r[0], r[1], r[2]