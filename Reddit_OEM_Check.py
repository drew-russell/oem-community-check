#Reddit OEM Coummnity Check
#Author: Drew Russell

import praw
import webbrowser
import time

class color:
   purple = '\033[95m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'

r = praw.Reddit(user_agent='User-Agent: python:com.datacenterhandbook.Reddit OEM Community Check:v1.0 (by /u/drew_russell)')
netapp = r.get_subreddit('netapp').get_new(limit=5)
vmware = r.get_subreddit('vmware').get_new(limit=5)
cisco = r.get_subreddit('cisco').get_new(limit=5)


def new_posts(sub_reddit):
    print('')
    for x in sub_reddit:
        print x
    print ''

def header(oem):
    print(color.red + oem + color.end)

print('')
header('NetApp')
new_posts(netapp)

header('VMware')
new_posts(vmware)

header('Cisco')
new_posts(cisco)

#Manually defined webbrowswer due to Chrome not being supported until 3.3
browser = webbrowser.get('safari')

#Ask user if they want to go direclty to a subreddit from the terminal
number_to_open = raw_input('Enter the ' + color.bold + 'number ' + color.end + 'of subreddits you would like to visit: ').lower()
print('')

#Verify that number to open is a number
while number_to_open.isdigit() == False:
    print('')
    print('**** Error: Please enter a valid number ****')
    print('')
    number_to_open = raw_input('Enter the ' + color.bold + 'number ' + color.end + 'of subreddits you would like to visit: ').lower()
    print('')

#If the user selects 0 close the application
if number_to_open == '0':
    print('You have chosen not to visit any subreddits.')
    print('')
    exit()

elif number_to_open == '3':
    browser.open_new_tab('https://www.reddit.com/r/netapp/new')
    browser.open_new_tab('https://www.reddit.com/r/vmware/new')
    browser.open_new_tab('https://www.reddit.com/r/cisco/new')

else:

    #Create list to house which OEM subreddits the user would like to visit
    oem_list = []

    #prompt user to enter which specific subreddits they'd like to open
    for x in range(0, int(number_to_open)):
        open = raw_input('OEM ' + str(x+1)+ ': ')
        oem_list.append(open)

    if 'netapp' in oem_list:
        browser.open_new_tab('https://www.reddit.com/r/netapp/new')

    if 'vmware' in oem_list:
         browser.open_new_tab('https://www.reddit.com/r/vmware/new')

    if 'cisco' in oem_list:
        browser.open_new_tab('https://www.reddit.com/r/cisco/new')



















