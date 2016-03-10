#!/usr/bin/env python
"""Application for creating and provisioning DigitalOcean instances
By Jeremy Plack, 2015-11-22
"""
import json
import requests
import argparse
parser = argparse.ArgumentParser()

def main():
    return

def droplet_create():
    return

# Returns the list of droplets(instances) on the account.
def list_droplets():
     token = "4e8073041c5811735cf470f95e8778e145eaa4515fe8cdb6ed15315be948ed8e"
     droplets = requests.get("https://api.digitalocean.com/v2/droplets", auth=(token, ""))
     if droplets.status_code == 200:
         do_droplets = droplets.json()
         print "DROPLETS:"
         do_droplets = do_droplets["droplets"]

         for i, droplet in enumerate(do_droplets):
             print(do_droplets[i]["name"])
         return do_droplets
     return droplets.status_code



if __name__ == "__main__":
    print """


***************************************************
***************************************************
   __________   ___    ____  ____
  / ____/  _/  /   |  / __ \/ __ \.
 / /    / /   / /| | / /_/ / /_/ /
/ /____/ /   / ___ |/ ____/ ____/
\____/___/  /_/  |_/_/   /_/

This program provides methods for calling
the DigitalOcean API to create and manage
droplets (cloud compute instances).

***************************************************
***************************************************
    """
    ans=True
    while ans:
        print ("""
        1. List Droplets
        2. Create Droplet
        3. Exit/Quit
        """)
        ans=raw_input("What would you like to do? ")
        if ans=="1":
          list_droplets()
        elif ans=="2":
          create_droplet()
        elif ans=="3":
            print("\n Goodbye")
            break
        elif ans !="":
          print("\n Not Valid Choice Try again")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
