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

    file_in_use = Exco.select()
    for file in file_in_use:
        if file.img_url_id != None:
            file_id_in_use.append(file.img_url_id)

    file_in_use = Disk.select()
    for file in file_in_use:
        if file.cover_url_id != None:
            file_id_in_use.append(file.cover_url_id)

    file_in_use = Document.select()
    for file in file_in_use:
        if file.doc_url_id != None:
            file_id_in_use.append(file.doc_url_id)

    file_in_use = PreviewShowTicket.select()
    for file in file_in_use:
        if file.cover_url_id != None:
            file_id_in_use.append(file.cover_url_id)

    file_in_use = Publication.select()
    for file in file_in_use:
        if file.cover_url_id != None:
            file_id_in_use.append(file.cover_url_id)

    file_in_use = Publication.select()
    for file in file_in_use:
        if file.doc_url_id != None:
            file_id_in_use.append(file.doc_url_id)

    file_in_use = Sponsor.select()
    for file in file_in_use:
        if file.img_url_id != None:
            file_id_in_use.append(file.img_url_id)
            
    file_in_use = SiteSettings.select()
    for setting in SiteSettings:
        if setting.key == "header_image":
            file_id_in_use.append(int(setting.value))

    file_id_in_use.sort()
    #print file_id_in_use

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
        print file.id
        print file.url
        
    answer = raw_input("These files will be deleted from the ihome server, are you sure?(Y/N)")
    if answer == "Y" or answer == "y":
        #delete_file(obs_file_url)
        print "Deletion finished!"
    else:
        print "Deletion cancelled!"


"""
def main():
    user_sq = User.select().where(
    	User.member_type != 'Expired',
    	User.expire_at <= date.today()
    )
    for user in user_sq:
        user.member_type = 'Expired'
        user.save()

    update_mailing_list(
        [x.itsc for x in User.select(User.itsc).where(
            User.member_type != 'Expired')])
"""
if __name__ == '__main__':
    main()
