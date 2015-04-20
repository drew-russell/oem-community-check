#Reddit OEM Coummnity Check
#Author: Drew Russell

import praw, webbrowser, sys, requests
from bs4 import BeautifulSoup



class color:
   purple = '\033[95m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'

print('')
print(color.bold + 'Executing Script. Please standby...' + color.end)

#Reddit Variables
r = praw.Reddit(user_agent='User-Agent: python:com.datacenterhandbook.Reddit OEM Community Check:v1.0 (by /u/drew_russell)')

def new_posts(sub_reddit):
    print('')
    for x in sub_reddit:
        print str(x).lstrip('0123456789:: ')
    print ''

def header(oem):
    print(color.bold + color.underline + oem + color.end)
    print('')

def reddit():
    print(color.blue + 'Reddit' + color.end)

def oem_community():
    print(color.blue + 'OEM Community' + color.end)
    print('')

#region NetApp
print('')
header('NetApp')
reddit()

#Subreddit Posts
netapp = r.get_subreddit('netapp').get_new(limit=5)
new_posts(netapp)

#NetApp OEM Community Variables
oem_community()
Community_NetApp = "https://community.netapp.com/t5/Forums/ct-p/forums"
HTML_NetApp = requests.get(Community_NetApp)
Soup_NetApp = BeautifulSoup(HTML_NetApp.content)
Post_NetApp = Soup_NetApp.find_all("div", {"class": "custom-subject"})
for post in Post_NetApp:
    print post.contents[0].text
print('')

#endregion

#region VMware
header('VMware')
reddit()
vmware = r.get_subreddit('vmware').get_new(limit=5)
new_posts(vmware)
oem_community()
#endregion

#region Cisco
header('Cisco')
reddit()

#Subreddit
cisco = r.get_subreddit('cisco').get_new(limit=5)
new_posts(cisco)

#Cisco Owned Community
oem_community()
Community_Cisco = "https://communities.cisco.com/community/technology/datacenter"
HTML_Cisco = requests.get(Community_Cisco)
Soup_Cisco = BeautifulSoup(HTML_Cisco.content)
Post_Cisco = Soup_Cisco.find_all("td", 'jive-table-cell-title', limit=5)
for post in Post_Cisco:
    print post.contents[1].text.strip()
print('')
#endregion

#region Open in Browser

#Define which browswer to open
if sys.platform == 'darwin':
    browser = webbrowser.get('macosx')
elif sys.platform == 'win32':
    browser = webbrowser.get('windows-default')

#Ask user if they want to go direclty to a subreddit from the terminal
number_to_open = raw_input('Enter the ' + color.bold + 'number ' + color.end + 'of OEMs you would like to visit: ').lower()
print('')

#Verify that number to open is a number
while number_to_open.isdigit() == False:
    print('')
    print('**** Error: Please enter a valid number ****')
    print('')
    number_to_open = raw_input('Enter the ' + color.bold + 'number ' + color.end + 'of OEMs you would like to visit: ').lower()
    print('')

#If the user selects 0 close the application
if number_to_open == '0':
    print('You have chosen not to visit any OEM Communities.')
    print('')
    exit()

elif number_to_open == '3':
    browser.open_new_tab('https://www.reddit.com/r/netapp/new')
    browser.open_new_tab('https://www.reddit.com/r/vmware/new')
    browser.open_new_tab('https://www.reddit.com/r/cisco/new')
    browser.open_new_tab('https://community.netapp.com/t5/Forums/ct-p/forums')
    browser.open_new_tab('https://www.reddit.com/r/cisco/new')

else:

    #Create list to house which OEM subreddits the user would like to visit
    oem_list = []

    #prompt user to enter which specific subreddits they'd like to open
    for x in range(0, int(number_to_open)):
        open = raw_input('OEM ' + str(x+1)+ ': ')
        while open not in ['vmware','cisco','netapp']:
            print('')
            print('**** Error: The OEM must be Cisco, NetApp, or VMware ****')
            print('')
            open = raw_input('OEM ' + str(x+1)+': ')
        oem_list.append(open)



    if 'netapp' in oem_list:
        browser.open_new_tab('https://www.reddit.com/r/netapp/new')
        browser.open_new_tab('https://community.netapp.com/t5/Forums/ct-p/forums')

    if 'vmware' in oem_list:
         browser.open_new_tab('https://www.reddit.com/r/vmware/new')

    if 'cisco' in oem_list:
        browser.open_new_tab('https://www.reddit.com/r/cisco/new')
        browser.open_new_tab('https://communities.cisco.com/community/technology/datacenter')

#endregion






















