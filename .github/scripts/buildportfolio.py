#!/usr/bin/env python3
import pymongo
import glob
import subprocess
import os


client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client["Portfolio"]

def getTechStack():
    Header = "### Technologies and tools 🛠"
    collection = db['teches'].find()
    toolt = "<img src='{logo}' alt='{slug}' width='40' height='40'/>"
    tools = []
    for tool in collection:
        tools.append(toolt.format(logo=tool['LogoUrl'],slug=tool['name']))
    if len(tools) == 0:
        return ""
    return Header + "\n" + " ".join(tools)

def connection_links():
    collection = db['connectionurls'].find()
    linkat = "<a href='{link}' target='blank'><img align='center' src='{Logo}' alt='{slug}' target='_blank' height='30' width='40' /></a>"
    links = []
    for link in collection:
        links.append(linkat.format(link=link['Link'],Logo=link['Logo'],slug=link['Slug']))
    if len(links) == 0:
        return ""
    return "\n".join(links)

def get_current_status():
    Header = "### Currently Learning 📚"
    collection = db['currents'].find({"finished":False})
    Currents = []
    for current in collection:
        dash = "-" + " " + current['name']
        Currents.append(dash)
    if len(Currents) == 0:
        return ""
    return Header + "\n" + " ".join(Currents)


if __name__ == "__main__":
    readme = eval(open(".github/scripts/README.tpml","r").read())
    cv = open("README.md","w")
    cv.write(readme)
    cv.close()
