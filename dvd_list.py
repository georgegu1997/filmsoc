#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Disk, Log

list = Disk.select().where(Disk.id >= 1559, Disk.avail_type != "Draft")

print "<Table>"
print "<tr>\
        <th>#</th>\
        <th>Call Number</th>\
        <th>Title</th>\
        <th>Price(HKD)</th>\
        <th>Purchase Date</th>\
        </tr>"
counter = 1

for disk in list:
    print "<tr>\
           <td>%d</td>\
           <td>%s</td>\
           <td>%s/%s<\td>\
           <td></td>\
           <td>%s</td>\
           <tr>"%(
           counter,
           disk.get_callnumber(),
           disk.title_en,
           disk.title_ch,
           Log.select().where(
             Log.log_type == 'create',
             Log.model == "Disk",
             Log.model_refer == disk.id
           )[0].created_at.date().isoformat()
           )
    counter ++
print "</table>"
