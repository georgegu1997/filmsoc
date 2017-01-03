#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script to clean the files not in use in the ihome server.
# The script should be run when you find the storage in the FTP server is almost full.

from models import *
from helpers import delete_file

# Exco -> img_url_id
# Disk -> cover_url_id
# Document -> doc_url_id
# PreviewShowTicket -> cover_url_id
# Publication -> cover_url_id doc_url_id
# Sponsor -> img_url_id
# SiteSettings -> header_image

def main():

    file_id_in_use = []
    counter = 0

    file_in_use = Exco.select()
    counter = 0
    for file in file_in_use:
        if file.img_url_id != None:
            counter ++
            file_id_in_use.append(file.img_url_id)
    print "file used in Exco:", counter

    file_in_use = Disk.select()
    counter = 0
    for file in file_in_use:
        if file.cover_url_id != None:
            counter ++
            file_id_in_use.append(file.cover_url_id)
    print "file used in Disk:", counter

    file_in_use = Document.select()
    counter = 0
    for file in file_in_use:
        if file.doc_url_id != None:
            counter ++
            file_id_in_use.append(file.doc_url_id)
    print "file used in Document:", counter

    file_in_use = PreviewShowTicket.select()
    counter = 0
    for file in file_in_use:
        if file.cover_url_id != None:
            counter ++
            file_id_in_use.append(file.cover_url_id)
    print "file used in PreviewShowTicket:", counter

    file_in_use = Publication.select()
    counter = 0
    for file in file_in_use:
        if file.cover_url_id != None:
            counter ++
            file_id_in_use.append(file.cover_url_id)
        if file.doc_url_id != None:
            counter ++
            file_id_in_use.append(file.doc_url_id)
    print "file used in Publication:", counter

    file_in_use = Sponsor.select()
    counter = 0
    for file in file_in_use:
        if file.img_url_id != None:
            counter ++
            file_id_in_use.append(file.img_url_id)
    print "file used in Sponsor:", counter

    file_in_use = SiteSettings.select()
    counter = 0
    for setting in SiteSettings:
        if setting.key == "header_image":
            counter ++
            file_id_in_use.append(int(setting.value))
    print "file used in SiteSettings:", counter

    file_id_in_use.sort()
    #print file_id_in_use
    print "Total number of files in use:", len(file_id_in_use)

    all_file = File.select()
    obs_file = []
    obs_file_url = []
    obs_file_id = []
    for file in all_file:
        if file.id not in file_id_in_use:
            obs_file.append(file)
            obs_file_url.append(file.url)
            obs_file_id.append(file.id)

    #print obs_file_id
    for file in obs_file:
        print file.id,"\t",file.name,"\t",file.url
    print "total:", len(obs_file)

    answer = raw_input("These files will be deleted from the ihome server, are you sure?(Y/N)")
    if answer == "Y" or answer == "y":
        #delete_file(obs_file_url)
        print "Deletion finished!"
    else:
        print "Deletion cancelled!"

if __name__ == '__main__':
    main()
