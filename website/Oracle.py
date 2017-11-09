#!/usr/bin/python
# -*- coding: utf-8 -*-


import cx_Oracle
import codecs
import os

os.environ["NLS_LANG"] = ".AL32UTF8"


try:
    #connection=cx_Oracle.connect('srez/srezPKB2013@PKB_SREZ')
    #connection = cx_Oracle.connect('nbk/nbk123@srez1')

    #connection = cx_Oracle.connect(user='rep', password='rep', dsn='172.28.5.181:1521/SREZ1')
    connection = cx_Oracle.connect('rep/rep@172.28.5.181/srez1')
except:
            print ("Logon  Error:")
            exit(0)
#connection.outputtypehandler = OutputTypeHandler

my_cursor=connection.cursor()
try:
            my_cursor.execute("""
            select period, area, periodicity, channel, Distribution_Option, Section_Name, Report_Type, Is_Subject_Found, Is_Free, Subproduct_Name, Cnt  from PKO_KKO_PERIOD t
            where t.periodicity=3
              """)
except:
    print ("")
    exit(0)

title_mask=('%-16s','%-16s','%-16s','%-16s','%-16s','%-16s','%-16s','%-16s','%-16s','%-16s','%-16s',)
i=0
row_mask='%-16s %-16s %-16s %-16s %-16s %-16s %-16s %-16s %-16s %-16s %-16s %-16s '
i=1
for period, area, periodicity, channel, Distribution_Option, Section_Name, Report_Type, Is_Subject_Found, Is_Free, Subproduct_Name, Cnt  in my_cursor:    #.fetchall():
            #txt=product.decode(connection.nencoding)
            print (u"Привет!: ", i, period, area, periodicity, channel, Distribution_Option, Section_Name, Report_Type, Is_Subject_Found, Is_Free, Subproduct_Name, Cnt)
            i+=1
            #if i>10:
            #    break
            #print str(creditpurpose2)+' '+product.encode('utf-8')


my_cursor.close()
connection.close()
