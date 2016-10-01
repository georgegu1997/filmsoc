#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A script to clean the files not in use in the ihome server.
# The script should be run when you find the storage in the FTP server is almost full.

from datetime import date
from models import User
from helpers import delete_file

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

if __name__ == '__main__':
    main()
