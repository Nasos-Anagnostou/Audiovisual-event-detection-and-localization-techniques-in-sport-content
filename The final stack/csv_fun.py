# author: Nasos Anagnostou 
# Diploma Thesis "Semantic event analysis in sports Video using webcast Text"
# script for csv file preprocessing adding event_id column and changing column names

import pandas as pd
import csv
from pandasgui import show

def csv_editor (filename):

	# root path of csv files
	mypath = r"E:/Career files/Degree Thesis/2. Dataset/play by play text"

	# read csv file and create dataframe
	df = pd.read_csv(filename) #,index_col ="event_id")
	rows,cols  = df.shape

	#rename columns
	df.columns = ['Quarter', 'Clock time', 'Score', 'Event']

	#Create event_ids and place them as first column
	event_ids = list(range(1,rows+1))
	df.insert(loc=0, column='Event_Id', value=event_ids)
	print(df.columns)

	# display to user the events of play by play text to choose which event to watch
	show(df)

	# ask user to choose which event_id he wants to watch
	myevid = int(input("Give me the event_id you want to watch:"))
	# future use of the quarter for now not in use
	myquart = "2nd Quarter"

	# create a filter for the specific event id, quarter(not used currently)
	filt_1 = (df['Event_Id'] == myevid)
	filt_2 = (df['Quarter'] == myquart)

	# apply filter to get timetag, quarter(not used
	myttag = df.loc[filt_1, 'Clock time']
	myevent = df.loc[filt_2]  # , 'Clock time']

	# convert timetag,quarter to string
	myevent = myevent.to_string(index=False).strip()
	myttag = myttag.to_string(index=False).strip()

	df.to_csv(mypath+"/sample1.csv", index=False)

	return myttag


