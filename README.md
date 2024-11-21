Amazon A to Z Shift Finder
A Python script that automatically monitors and claims available VET/Flex shifts on Amazon's A to Z portal based on your preferences.  

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

   Run these commands in the terminal one at a time:  
   pip install selenium  
   pip install undetected-chromedriver  
   pip install setuptools  

3. Download the script and save it somewhere easy to find  
   Open it/edit it with Notepad or any text editor  
   Find these settings near the top and change them to match your preferences:  

STALL_AFTER_LOGIN = 10

NUMBER_OF_DAYS = 7   

EARLIEST_TIME = "00:00"   

LATEST_TIME = "00:00"   

LONGEST_SHIFT = 8   

WEEKDAYS = [   
"Monday",   
"Tuesday",   
"Wednesday",   
"Thursday",   
"Friday",   
"Saturday",   
"Sunday"   
]   


CHROME_PROFILE_DIRECTORY_PATH = r"Chrome Profile Directory Goes Here"   

Amazon_Login = "AtoZ Username Here"   

USERNAME = "AtoZ Username Here"   

PASSWORD = "Atoz Password Here"   

HOURS_TO_RUN = 3   

SECONDS_BETWEEN_CHECKS = 5   

4. Create the Chrome Profile Directory Folder  
   Create a new folder anywhere.  
   Copy the directory of that folder on this line of the code: CHROME_PROFILE_DIRECTORY_PATH = r"Chrome Profile Directory goes here"
   Save changes

6. Run the Script  

   Double-click the Python file  
   A Chrome window will open and log into A to Z  
   If asked to verify your identity:  

Click the verification option  
Enter the code sent to you  
Check "Remember this device"  


The script will start looking for shifts that match your settings  


Need Help?
Feel free to open an issue on GitHub if you run into problems!  
