#Reddit OEM Coummnity Check
#Author: Drew Russell

import praw
import webbrowser

class color:
   purple = '\033[95m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'

r = praw.Reddit(user_agent='Reddit OEM Community Posts')
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
open = raw_input('Which subreddit would you like to visit? ').lower()

if open == 'netapp':
    browser.open('https://www.reddit.com/r/netapp')

elif open == 'vmware':
 browser.open('https://www.reddit.com/r/vmware')

elif open == 'cisco':
 browser.open('https://www.reddit.com/r/cisco')

else:
    print("Successfully checked all OEM subreddit's")


print('')
print('')
print('')















