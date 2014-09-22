# Create a CAR DB with a table called inventory



import sqlite3

with sqlite3.connect("car.db") as connection:
    c = connection.cursor()
    
    # update data
    #c.execute("CREATE table orders(Make TEXT, Model TEXT, Order_Date TEXT)")
    
    
    # update data
    #c.execute("UPDATE inventory SET Quantity = 10 WHERE Model = 'Focus'")
    #c.execute("UPDATE inventory SET Quantity = 40 WHERE Model = 'FX'")
    
    #list to hold the records to be added to the inventory table
    cars = [ 
            
            ('Ford', 'Focus', '2014-01-01'),
            ('Ford', 'Exodus','2014-02-01'),
            ('Ford', 'Sapphire','2014-03-01'),
            ('Honda', 'Accord', '2014-04-01'),
            ('Honda', 'FX', '2014-05-01'),
            ('Ford', 'Focus', '2014-06-01'),
            ('Ford', 'Exodus','2014-07-01'),
            ('Ford', 'Sapphire','2014-08-01'),
            ('Honda', 'Accord', '2014-09-01'),
            ('Honda', 'FX', '2014-10-01'),
            ('Ford', 'Focus', '2014-06-02'),
            ('Ford', 'Exodus','2014-07-03'),
            ('Ford', 'Sapphire','2014-08-04'),
            ('Honda', 'Accord', '2014-09-05'),
            ('Honda', 'FX', '2014-10-06')
           ]
    
    # insert data
    #c.executemany('INSERT INTO orders VALUES(?, ?, ? )', cars)
    
    #print "\nNEW DATA: \n"
    
    c.execute("SELECT DISTINCT inventory.Make, inventory.Model, inventory.Quantity, orders.Order_Date FROM inventory, orders WHERE inventory.Make = orders.Make and inventory.Model = orders.Model")
    
    
    rows = c.fetchall()
    
    
    
    for r in rows: 
        print "Make: {} Model:{}".format(r[0], r[1])
        print "Quantity: {}".format(str(r[2]))
        print "Order Date: {}".format(r[3])