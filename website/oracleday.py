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
            select PERIOD, AREA, sum(CNT) sm FROM PKO_KKO_DAILY 
            WHERE (PERIOD >= to_date('25-08-2017', 'DD.MM.YYYY') and PERIOD <= to_date('07-09-2017', 'DD.MM.YYYY')
            AND CHANNEL In ('ЦОН') AND REPORT_TYPE In ('ПКО') AND PERIODICITY In (4))
            group by PERIOD,  AREA  """)
except:
    print("")
    exit(0)

title_mask=('%-16s','%-16s','%-16s')
i=0
row_mask='%-16s %-16s %-16s %-16s'
i=1
for period, area, sm in my_cursor:    #.fetchall():
            #txt=product.decode(connection.nencoding)
            print (u"Привет!: ", i, period, area, sm)
            i+=1
            #if i>10:
            #    break
            #print str(creditpurpose2)+' '+product.encode('utf-8')

# select PKO_KKO_DAILY.PERIOD, PKO_KKO_DAILY.AREA, sum(PKO_KKO_DAILY.CNT) sm FROM   PKO_KKO_DAILY  WHERE   ( PKO_KKO_DAILY.PERIOD   >= to_date('25-08-2017', 'DD.MM.YYYY') and PKO_KKO_DAILY.PERIOD <= to_date('06-09-2017', 'DD.MM.YYYY')               AND   PKO_KKO_DAILY.CHANNEL  In  ( 'ЦОН'  )    AND    PKO_KKO_DAILY.REPORT_TYPE  In  ( 'ПКО'  )    AND    PKO_KKO_DAILY.PERIODICITY  In  ( 4 )) GROUP BY   PKO_KKO_DAILY.PERIOD,  PKO_KKO_DAILY.AREA=4  """)

my_cursor.close()
connection.close()
