# FullThrottle
assignment 

FRAMEWORK : Django
	
DATABASE : Sqlite3
	
HOST : PythonAnywhere

------------------------------------------------------------------------------------------------------------------------------------------------------

DATABASE:

	DataBase contain 2 table's

	1st table contain 'User Information' (name, id, tz)

	2nd table contaion 'Activity Periods' Information(start time, end time) with 'id' as 'Forgein Key'

------------------------------------------------------------------------------------------------------------------------------------------------------
COMMAND:

	this command is use to upload json file which contain User's data into Database
	>>> py -3.8 manage.py insert 'file_path'
	exmple:
		py -3.8 manage.py insert C:\Users\Rupali\Documents\ankit\FullThrottle\myApp\FullThrottle\test.json
	
------------------------------------------------------------------------------------------------------------------------------------------------------

HTML TEMPLATE:

	Easyly download the data present in "DATABASE" in required json fromat
	
	templates location : 'myApp/FullThrottle/templates/personal'

------------------------------------------------------------------------------------------------------------------------------------------------------

APP WORKING	:
	
	At each load of template all data from DataBase is featched and converted into JSON format and store that JSON file at location 'myApp/json/out.json'
	
------------------------------------------------------------------------------------------------------------------------------------------------------

SAMPLE JSON FORMAT :


	{
	  "ok": true,
	  "members": [
		{
		  "id": "W012A3CDE",
		  "real_name": "Egon Spengler",
		  "tz": "America/Los_Angeles",
		  "activity_periods": [
			{
			  "start_time": "Feb 1 2020  1:33PM",
			  "end_time": "Feb 1 2020 1:54PM"
			},
			{
			  "start_time": "Mar 1 2020  11:11AM",
			  "end_time": "Mar 1 2020 2:00PM"
			},
			{
			  "start_time": "Mar 16 2020  5:33PM",
			  "end_time": "Mar 16 2020 8:02PM"
			}
		  ]
		},
	  ]
	}
	
	JSON LOCATION : myApp/FullThrottle/test.json
	
------------------------------------------------------------------------------------------------------------------------------------------------------

	