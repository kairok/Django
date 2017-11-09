from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from fusioncharts import FusionCharts

# Loading Data from a Static JSON String
# It is a example to show a Column 2D chart where data is passed as JSON string format.
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):
    # Create an object for the column2d chart using the FusionCharts class constructor
  bar2d = FusionCharts("bar2d", "ex1" , "600", "400", "bar2d1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
    """{
    "chart": {
        "caption": "Top 10 most popular sports in Web World",
        "subcaption": "Based on number of estimated fans - till last year",
        "yaxisname": "Estimated fans",
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
            "label": "Football",
            "value": "3500000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}Americas"
        },
        {
            "label": "Cricket",
            "value": "2500000000",
            "tooltext": "Popular in: {br}Asia{br}UK{br}Australia"
        },
        {
            "label": "Field Hockey",
            "value": "2000000000",
            "tooltext": "Popular in: {br}Asia{br}Europe{br}Africa{br}Australia"
        },
        {
            "label": "Tennis",
            "value": "1000000000",
            "tooltext": "Popular in: {br}Europe{br}America{br}Asia"
        },
        {
            "label": "Volleyball",
            "value": "900000000",
            "tooltext": "Popular in: {br}Asia{br}Europe{br}America{br}Australia"
        },
        {
            "label": "Table Tennis",
            "value": "850000000",
            "tooltext": "Popular in: {br}Asia{br}Europe{br}Africa{br}Americas"
        },
        {
            "label": "Baseball",
            "value": "500000000",
            "tooltext": "Popular in: {br}America{br}Japan"
        },
        {
            "label": "Golf",
            "value": "450000000",
            "tooltext": "Popular in: {br}America{br}Asia{br}Canada{br}Europe"
        },
        {
            "label": "Basketball",
            "value": "400000000",
            "tooltext": "Popular in: {br}America"
        },
        {
            "label": "American Football",
            "value": "400000000",
            "tooltext": "Popular in: {br}Europe{br}Africa{br}Asia{br}America{br}Australia."
        }
    ]
}""")

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
  return render(request, 'region2.html', {'output' : bar2d.render()})

