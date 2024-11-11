Amazon A to Z Shift Finder
A Python script that automatically monitors and claims available VET/MET shifts on Amazon's A to Z portal based on your preferences.
⚠️ Important Note
This tool is for educational purposes. Make sure using automated tools doesn't violate your workplace policies.
Features

Auto-login to A to Z portal
Configurable shift preferences (days, times, shift length)
Smart filtering based on your criteria
Cookie persistence to avoid frequent re-authentication
Random delays and human-like typing simulation to avoid detection

Requirements

Python 3.7+
Chrome browser
Windows (tested on Windows 10/11)

Setup Guide

1. Clone this repository: git clone <https://github.com/Amazon-Hate-it-But-Need-it/Amazon-AtoZ-VET-Flex-Bot>
cd to the directory of the python script

2. Install required packages:
pip install selenium undetected-chromedriver
pip install setuptools

3. Configure your settings in the script:

Set CHROME_PROFILE_DIRECTORY_PATH to your Chrome user data directory or create a new folder and set the directory of that folder as the CHROME_PROFILE_DIRECTORY_PATH
Update USERNAME and PASSWORD with your A to Z credentials
Adjust shift preferences:

NUMBER_OF_DAYS: How many days ahead to look for shifts (default: 8)
EARLIEST_TIME and LATEST_TIME: Your preferred shift time range (format: "HH:MM")
LONGEST_SHIFT: Maximum shift length in hours
WEEKDAYS: List of days you're willing to work. 
HOURS_TO_RUN: How long the script should run
SECONDS_BETWEEN_CHECKS: Delay between shift checks





Usage

1. Run the script
2. The script will:

Open Chrome and navigate to A to Z
Log in using your credentials
Handle any verification prompts
Start monitoring for shifts matching your criteria
Automatically attempt to claim matching shifts
Continue running for the specified duration



Customization Tips

Adjust STALL_AFTER_LOGIN if the page takes longer to load
Modify typing and click delays in delay_typing() and wait_and_click() methods
Add additional shift criteria by modifying the find_shifts() method

Troubleshooting

Chrome Won't Launch: Make sure your Chrome profile path is correct
Login Fails: Double-check credentials and watch for CAPTCHA/verification
Shifts Not Found: Verify your time preferences and ensure you're looking at the right days
Script Crashes: Check Chrome is updated and try clearing browser data

Contributing
Feel free to submit issues and pull requests for improvements!
