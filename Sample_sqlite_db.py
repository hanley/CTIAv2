import sqlite3
#Define the SQLite database file path
db_file = '/home/analyst/History'
try:
    # connect to the SQLite database
	conn = sqlite3.connect(db_file)
    #create a cursor object to interact with the database
	cursor = conn.cursor()
    # Define a SQLquery to retrieve data from a specific table
	query = "SELECT * FROM downloads"
    #execute the query
	cursor.execute(query)
    #fetch all the results
	data = cursor.fetchall()
    #Process and print the retrieved data
	for row in data:
		print(row)
except sqlite3.Error as e:
	print(f"An error occured: {e}")
finally:
    #Close the database connection
	if conn:
		conn.close()
