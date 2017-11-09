# -*- coding: utf-8 -*-

# conn=cx_Oracle.connect('rep/rep@172.28.5.181/srez1')
# cursor=conn.cursor()

from django.shortcuts import render
from django import forms

from fusioncharts import FusionCharts

import datetime
import time

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

areas = 'almaty'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def webapp(request):
    return render(request, 'webapp.html')

def settings(request):
    return render(request, 'settings.html')

def geo(request):
    return render(request, 'geo.html')

def test(request):
    return render(request, 'test.html')

def region(request):
    return render(request, 'region.html')

def quick(request):
    ok = 1
    my_cursor.execute("""
             SELECT
  PERIOD,
  DISTRIBUTION_OPTION,
  sum(PKO_KKO_PERIOD.CNT) sm
FROM
  PKO_KKO_PERIOD
WHERE
  (
   PKO_KKO_PERIOD.REPORT_TYPE  In  ( 'ПКО'  )
   AND
   PKO_KKO_PERIOD.PERIODICITY  In  ( 1  )
  )
GROUP BY
  PKO_KKO_PERIOD.PERIOD, 
  PKO_KKO_PERIOD.DISTRIBUTION_OPTION
  order by period asc
                """)
    period = []
    online=[]
    avg=[]
    offline=[]
    ons=0
    ofs=0
    onlinesm=0
    oflinesm=0

    for PERIOD,DISTRIBUTION_OPTION, sm in my_cursor:

        if u'Онлайн' in DISTRIBUTION_OPTION:
            online.append(sm)
            ons=sm
            onlinesm+=sm
        if u'Оффлайн' in DISTRIBUTION_OPTION:
            offline.append(sm)
            ofs=sm
            oflinesm+=sm
        if PERIOD not in period:
            period.append(PERIOD)
            avg.append((ons+ofs)/2)

    return render(request, 'quick.html',{ 'online':online, 'offline':offline, 'period':period, 'avg':avg, 'onlinesum':onlinesm, 'oflinesum':oflinesm})

def channel(request):
    ok=1
    my_cursor.execute("""
           select   
             PKO_KKO_DAILY.PERIOD,
             sum(PKO_KKO_DAILY.CNT) sm
             FROM
             PKO_KKO_DAILY
             WHERE
             (
             PKO_KKO_DAILY.PERIOD  >= to_date('04-09-2017', 'DD.MM.YYYY')
             AND 
             PKO_KKO_DAILY.PERIOD <= to_date('17-09-2017', 'DD.MM.YYYY')
             AND
             PKO_KKO_DAILY.REPORT_TYPE  In  ( 'ПКО'  )
             )
             GROUP BY
             PKO_KKO_DAILY.PERIOD
             """)
    pkosum = []
    pkoperiod = []

    for PERIOD, sm in my_cursor:
        pkosum.append(sm)
        dt=PERIOD.strftime('%m/%d/%Y')
        if dt not in pkoperiod:
            pkoperiod.append(dt)
            # print(pkosum)

    return render(request, 'Channel.html',{'pkoperiod':pkoperiod,'pkosum':pkosum})

def monitoring(request):
    # def form_view(request):
    #     context = {
    #         'areas': area.objects.all()
    #     }
    #
    #     if request.POST:
    #         area_pk_list = request.POST.getlist('area', None)
    #         print(request.POST.getlist('area', None))
    #
    #         selected_area_obj_list = area.objects.filter(pk__in=area_pk_list)
    #         print(selected_area_obj_list)

    region =u'Алматы'.encode('utf-8')
    line=u'Онлайн'.encode('utf-8')
    free=u'Платно и Бесплатно'.encode('utf-8')
    found=u'Найден и Не найден'.encode('utf-8')
    try:
        if request.GET[u'areas'] != '':
            region=request.GET[u'areas'].encode('utf-8')
    except:
        pass
    try:
        if request.GET[u'line'] != '':
            line=request.GET[u'line'].encode('utf-8')
    except:
        pass

    try:
        if request.GET[u'found'] != '':
            found=request.GET[u'found'].encode('utf-8')
    except:
        pass

    try:
        if request.GET[u'pay'] != '':
            free=request.GET[u'pay'].encode('utf-8')
    except:
        pass



    # Grafik for month
    my_cursor.execute("""
                             SELECT
              PKO_KKO_PERIOD.PERIOD,
              PKO_KKO_PERIOD.AREA,
              sum(PKO_KKO_PERIOD.CNT) sm
            FROM
              PKO_KKO_PERIOD
            WHERE
              (
               PKO_KKO_PERIOD.PERIODICITY  In  ( 1  )
               AND
               PKO_KKO_PERIOD.REPORT_TYPE  In  ( 'ПКО'  )
               AND
               PKO_KKO_PERIOD.CHANNEL  In  ( 'ЦОН'  )
               AND
               PKO_KKO_PERIOD.PERIOD  In  ( '2017-08','2017-07'  )
              )
            GROUP BY
              PKO_KKO_PERIOD.PERIOD, 
              PKO_KKO_PERIOD.AREA
            order by period asc
                    """)
    area = []
    date1 = []
    date2 = []
    avg = []
    d2s = 0
    d1s = 0
    date1sm = 0
    date2sm = 0

    for PERIOD, AREA, sm in my_cursor:

        if u'2017-07' in PERIOD:
            date2.append(sm)
            d2s = sm
            date2sm += sm
        if u'2017-08' in PERIOD:
            date1.append(sm)
            d1s = sm
            date1sm += sm
        if AREA not in area:
            area.append(AREA)
            avg.append((d2s + d1s) / 2)

    sql="SELECT PERIOD, SECTION_NAME, sum(PKO_KKO_PERIOD.CNT) sm FROM PKO_KKO_PERIOD  WHERE (PERIODICITY In (1) AND PERIOD In ('2017-08','2017-07') " \
        "AND CHANNEL  In  ( 'ЦОН'  ) AND REPORT_TYPE In ('ПКО') AND AREA  In  ('" + region + "'))  GROUP BY PERIOD, SECTION_NAME order by PERIOD"
    my_cursor.execute(sql)
    section_name = []
    sectiondate1 = []
    sectiondate2 = []

    for PERIOD, SECTION_NAME, sm in my_cursor:

        if u'2017-07' in PERIOD:
            sectiondate2.append(sm)

        if u'2017-08' in PERIOD:
            sectiondate1.append(sm)

        if SECTION_NAME not in section_name:
            section_name.append(SECTION_NAME)




    #  Grafik for week
    if free.decode('utf-8') == u'Платно и Бесплатно':
        sql = "select PERIOD, AREA, sum(CNT) sm FROM PKO_KKO_DAILY  WHERE PERIOD >= to_date('28-08-2017', 'DD.MM.YYYY')" \
              " AND PERIOD <= to_date('10-09-2017', 'DD.MM.YYYY')  AND CHANNEL In ('ЦОН') AND REPORT_TYPE In ('ПКО') AND PERIODICITY In (4)    "

    else:
        sql="select PERIOD, AREA, sum(CNT) sm FROM PKO_KKO_DAILY  WHERE PERIOD >= to_date('28-08-2017', 'DD.MM.YYYY')  AND PERIOD <= to_date('10-09-2017', 'DD.MM.YYYY')  AND CHANNEL In ('ЦОН') AND REPORT_TYPE In ('ПКО') AND PERIODICITY In (4) AND is_free  In  ('" + free + "')   "


    if found.decode('utf-8') != u'Найден и Не найден':
        sql+=" AND is_subject_found  In  ('" + found + "')"

    sql+="  group by PERIOD,  AREA order by PERIOD"
    my_cursor.execute(sql)

    # datefrom = '2017-06-01'
    # dateto = '2017-07-01'
    # request.session["datefrom"] = datefrom
    # request.session["dateto"] = dateto
    daily_area = []
    daily_date1 = []
    daily_date2 = []
    daily_avg = []
    daily_d2s = 0
    daily_d1s = 0
    daily_date1sm = 0
    daily_date2sm = 0
    week1 = {}
    week2 = {}
    nomweek = 1
    ok = 0

    for PERIOD, AREA, sm in my_cursor:

        if PERIOD.weekday()==6 or PERIOD.weekday()==5 or PERIOD.weekday()==4 or PERIOD.weekday()==3 or PERIOD.weekday()==2:
            ok=1
        if ok==1 and PERIOD.weekday()==0:
            nomweek=2
        if nomweek==2:
            #daily_date1.append(daily_date1sm)
            week2.setdefault(AREA, 0)
            week2[AREA] += sm
            daily_d2s = sm
            daily_date2sm += sm
        if nomweek==1:
            week1.setdefault(AREA, 0)
            week1[AREA] +=sm
            daily_d1s = sm
            daily_date1sm += sm
        if AREA not in daily_area:
            daily_area.append(AREA)
            #daily_avg.append((daily_d2s + daily_d1s) / 2)


    for dn in daily_area:
        try:
            daily_date2.append(week2[dn])
        except:
            daily_date2.append(0)
        try:
            daily_date1.append(week1[dn])
        except:
            daily_date1.append(0)

    '''
    for item, value in week1.items():
        if item != None:
            if u'Актюбинская' in item.decode('utf-8'):
                ok=1

        daily_date1.append(value)
        daily_date2.append(week2[item])
        if item not in daily_area:
            daily_area.append(item)

    txt=''
    for item, value in week1.items():
        if item==None:
            item='None'
        txt+=item+' '
    print txt
    txt = ''
    for item, value in week1.items():
        if item == None:
            item = 'None'
        txt += item + ' '
    print txt
    txt = ''
    for it in daily_date1:
        txt += str(it) + ' '
    print txt
    '''


    #   REGIONs  for week
    if free.decode('utf-8') == u'Платно и Бесплатно':
        sql = "SELECT PERIOD, SECTION_NAME, sum(CNT) sm FROM PKO_KKO_DAILY  WHERE PERIODICITY In (4) AND PERIOD >= to_date('28-08-2017', 'DD.MM.YYYY') and PERIOD <= to_date('10-09-2017', 'DD.MM.YYYY') " \
              " AND CHANNEL  In  ( 'ЦОН'  ) AND REPORT_TYPE In ('ПКО') AND AREA  In  ('" + region + "')    "
    else:
        sql = "SELECT PERIOD, SECTION_NAME, sum(CNT) sm FROM PKO_KKO_DAILY  WHERE PERIODICITY In (4) AND PERIOD >= to_date('28-08-2017', 'DD.MM.YYYY') and PERIOD <= to_date('10-09-2017', 'DD.MM.YYYY') " \
              " AND CHANNEL  In  ( 'ЦОН'  ) AND REPORT_TYPE In ('ПКО') AND AREA  In  ('" + region + "') AND is_free  In  ('" + free + "')     "



    if found.decode('utf-8') != u'Найден и Не найден':
        sql+=" AND is_subject_found  In  ('" + found + "')"
    sql += "  GROUP BY PERIOD, SECTION_NAME order by PERIOD"

    my_cursor.execute(sql)
    w_section_name = []
    w_sectiondate1 = []
    w_sectiondate2 = []
    week1 = {}
    week2 = {}
    nomweek = 1
    ok = 0

    for PERIOD, SECTION_NAME, sm in my_cursor:

        if PERIOD.weekday()==6 or PERIOD.weekday()==5 or PERIOD.weekday()==4 or PERIOD.weekday()==3 or PERIOD.weekday()==2:
            ok=1
        if ok==1 and PERIOD.weekday()==0:
            nomweek=2
        if nomweek==2:
            week2.setdefault(SECTION_NAME, 0)
            week2[SECTION_NAME] += sm
        if nomweek==1:
            week1.setdefault(SECTION_NAME, 0)
            week1[SECTION_NAME] +=sm
        if SECTION_NAME not in w_section_name:
            w_section_name.append(SECTION_NAME)

    for nm in w_section_name:
        try:
            w_sectiondate2.append(week2[nm])
        except:
            w_sectiondate2.append(0)
        try:
            w_sectiondate1.append(week1[nm])
        except:
            w_sectiondate1.append(0)

    #for item, value in week1.items():
    #    w_sectiondate1.append(value)
    #    w_sectiondate2.append(week2[item])

    # request.session["areas"] = 'almaty'
    # areas = request.session["areas"]
    #
    # areas=[]
    #
    # areas.append(value)
    #
    # if AREA == 'Алматы':
    #     mestype = u'Алматы'
    #
    # if u'Алматы' in AREA:



    return render(request, 'monitoring.html', {'date2': date2, 'date1': date1, 'area': area, 'avg': avg, 'date2sm': date2sm, 'date1sm': date1sm,
                                               'section_name': section_name, 'sectiondate2': sectiondate2, 'sectiondate1': sectiondate1,
                                               'daily_date2': daily_date2, 'daily_date1': daily_date1,
                                               'daily_area': daily_area, 'daily_avg': daily_avg, 'daily_date2sm': daily_date2sm, 'daily_date1sm': daily_date1sm,
                                               'w_section_name': w_section_name, 'w_sectiondate2': w_sectiondate2,
                                               'w_sectiondate1': w_sectiondate1,
                                               'selected':region.decode('utf-8'), 'line':line.decode('utf-8'), 'pay':free.decode('utf-8'), 'found':found.decode('utf-8')})

def region2(request):
    bar2d = FusionCharts("bar2d", "ex1" , "400", "400", "bar2d1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    """{
    "chart": {
        "caption": "",
        "subcaption": "Based on % MoM",
        "yaxisname": "change",
        "plotgradientcolor": "",
        "rotatevalues": "0",
        "divlinecolor": "#CCCCCC",
        "showvalues": "1",
        "valuefontbold": "1",
        "yaxisnamefontsize": "12",
        "labelsepchar": ": ",
        "labeldisplay": "AUTO",
        "numberscalevalue": "1000,1000,1000",
        "numberscaleunit": "K,M,B",
        "animation": "0",
        "theme": "zune"
    },
    "data": [
        {
            "label": "Almaty",
            "value": "3800000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}Americas"
        },
        {
            "label": "Astana",
            "value": "3300000000",
            "tooltext": "Popular in: {br}Asia{br}UK{br}Australia"
        },
        {
            "label": "VKO",
            "value": "3000000000",
            "tooltext": "Popular in: {br}Asia{br}Europe{br}Africa{br}Australia"
        },
        {
            "label": "Zhambyl obl",
            "value": "3000000000",
            "tooltext": "Popular in: {br}Europe{br}America{br}Asia"
        },
        {
            "label": "Kyzylorda obl",
            "value": "1900000000",
            "tooltext": "Popular in: {br}Asia{br}Europe{br}America{br}Australia"
        },
        {
            "label": "Mangystau obl",
            "value": "1850000000",
            "tooltext": "Popular in: {br}Asia{br}Europe{br}Africa{br}Americas"
        },
        {
            "label": "Qaraganda  obl",
            "value": "1500000000",
            "tooltext": "Popular in: {br}America{br}Japan"
        },
        {
            "label": "SKO",
            "value": "1450000000",
            "tooltext": "Popular in: {br}America{br}Asia{br}Canada{br}Europe"
        },
        {
            "label": "Pavlodar obl",
            "value": "1400000000",
            "tooltext": "Popular in: {br}America"
        },
        {
            "label": "UKO",
            "value": "1300000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        }, 
        {
            "label": "Atyrau obl",
            "value": "1350000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        }, 
        {
            "label": "Aktobe obl",
            "value": "1330000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        },
        {
            "label": "ZKO",
            "value": "1300000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        },
        {
            "label": "Almaty obl",
            "value": "1290000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        },
        {
            "label": "Kostanay obl",
            "value": "1280000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        }, 
        {
            "label": "Akmola obl",
            "value": "1260000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        },
        {
            "label": "N/D",
            "value": "1200000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        }
    ]
}""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
    return render(request, 'region2.html', {'output': bar2d.render()})

def manual(request):
    return render(request, 'manual.html')

    # return render(request, 'region2.html')
