Amazon A to Z Shift Finder
A Python script that automatically monitors and claims available VET/MET shifts on Amazon's A to Z portal based on your preferences.
⚠️ Important Note

Features:  

Auto-login to A to Z portal
Configurable shift preferences (days, times, shift length)
Smart filtering based on your criteria
Cookie persistence to avoid frequent re-authentication

Requirements

Python 3.7+
Chrome browser

Installation Steps  
1. Install Python  

Download Python from https://www.python.org/  
Run the installer  
Make sure to check "Add Python to PATH" during installation  

2. Download Required Libraries

Make a new text file on your desktop  
Copy and paste these package names, each on a new line:  


selenium  
undetected-chromedriver  
setuptools  

Save it as requirements.txt  
Right-click the file and select "Open in Terminal" or "Open PowerShell window here"  
Type: pip install -r requirements.txt  
Press Enter and wait for installation to complete  

If you get any errors, try running these commands in the terminal one at a time:  
pip install selenium  
pip install undetected-chromedriver  
pip install setuptools  

3. Download the script and save it somewhere easy to find  
Open it with Notepad or any text editor  
Find these settings near the top and change them to match your preferences:  

USERNAME = "your_username"     # Your A to Z login  
PASSWORD = "your_password"     # Your A to Z password  
EARLIEST_TIME = "10:00"       # Earliest shift you'll take  
LATEST_TIME = "18:00"         # Latest shift you'll take  
LONGEST_SHIFT = 8             # Max hours you'll work  
WEEKDAYS = [                  # Days you want to work  
"Monday",  
"Tuesday",  
"Wednesday",  
"Thursday",  
"Friday"  
]
HOURS_TO_RUN = 3             # How many hours to run the script  

4. Create the Chrome Profile Directory Folder  
Create a new folder anywhere.  
Copy the directory of that folder on this line of the code: CHROME_PROFILE_DIRECTORY_PATH = r"Chrome Profile Directory goes here"  

5. Run the Script  

Double-click the Python file  
A Chrome window will open and log into A to Z  
If asked to verify your identity:  

Click the verification option  
Enter the code sent to you  
Check "Remember this device"  


The script will start looking for shifts that match your settings  


Need Help?
Feel free to open an issue on GitHub if you run into problems!  
