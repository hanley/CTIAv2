import pandas as pd
from datetime import datetime, timedelta
#Simulated login data (replace with your real data source)
data = [ 
	{'username': 'analyst', 'timestamp': '2023-10-01 08:00:00'},
	{'username': 'analyst', 'timestamp': '2023-10-01 08:30:00'},
	{'username': 'sam', 'timestamp': '2023-10-01 09:15:00'},
	{'username': 'sam', 'timestamp': '2023-10-01 09:16:00'},
	{'username': 'sam', 'timestamp': '2023-10-01 09:17:00'},
	{'username': 'sam', 'timestamp': '2023-10-01 09:18:00'},
	{'username': 'sam', 'timestamp': '2023-10-01 09:19:00'},
	#add more login data
]
#Create a Dataframe from the data
df = pd.DataFrame(data)
#Convert the 'timestamp' column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])
#Sort the DataFrame by timestamp
df = df.sort_values(by='timestamp')
#Define a time window for behavior analysis (e.g., 1 hour)
time_window = timedelta(hours=1)
#Create a dictionary to store login counts per user within the time window
login_counts =  {}
#Set the threshold for suspicious login counts
threshold = 3
#Iterate through the Dataframe to detect suspicious behavior
for index, row in df.iterrows():
	username = row['username']
	timestamp = row['timestamp']
	if username not in login_counts:
		login_counts[username] = []
	#Remove login timestamps that are outside the time window
	login_counts[username] = [t for t in login_counts[username] if timestamp - t <= time_window]
	login_counts[username].append(timestamp)

	if len(login_counts[username]) >= threshold:
		print(f"Suspicious behavior detected for user {username} at {timestamp}")
