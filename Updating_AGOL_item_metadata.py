# ##### Import the GIS module and other needed Python modules
from arcgis.gis import GIS
from getpass import getpass

# ##### Create the GIS object and point it to AGOL
# Get username and password
username = input('Username: ')
password = getpass(prompt='Password: ')

# Connect to portal
gis = GIS("https://arcgis.com/", username, password)


# ##### Get the item that you want to update
title = input("Feature class to search for: ")

items = gis.content.search(query="title:'" + title + "' AND owner:" + username, item_type="Feature Service")
item = items[0]

# ##### Update the metadata
# First set up some variables for input ot the *update* method.
thumbnail_path = "c:/temp/Hospitals.JPG"
tags = list(item.tags)
tags.append("health")
item_properties = {"snippet": "Location of Cambridge hospitals.",
                   "title": "Cambridge Hospitals",
                   "tags": ','.join(tags),
                   "accessinformation": "City of Cambridge GIS",
                   "licenseInfo": "License Info"
}


# Then perform the update
item.update(item_properties, thumbnail=thumbnail_path)
