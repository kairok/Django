$(document).ready(function() {
    // when page is loaded, remove the loading
    $('.loading').remove();

    // tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // overall analysis
$('.round-chart').easyPieChart({
    'scaleColor': false,
    'lineWidth': 20,
    'lineCap': 'butt',
    'barColor': '#6d5cae',
    'trackColor': '#e5e9ec',
    'size': 190
});

    // performance evaluation
$('#performance-eval .spider-chart').highcharts({

    chart: {
        polar: true,
        type: 'area'
    },

    title: {
        text: ''
    },

    xAxis: {
        categories: ['Taming', 'Acessory', 'Development', 'Grooming', 'Awareness', 'Ration'],
        tickmarkPlacement: 'on',
        lineWidth: 0
    },

    yAxis: {
        gridLineInterpolation: 'polygon',
        lineWidth: 0,
        min: 0
    },

    tooltip: {
        shared: true,
        pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
    },

    legend: {
        align: 'right',
        verticalAlign: 'top',
        y: 70,
        layout: 'vertical'
    },

    series: [{
        name: 'Allocated resources',
        data: [45000, 39000, 58000, 63000, 38000, 93000],
        pointPlacement: 'on',
        color: '#676F84'
    },
    {
        name: 'Spent resources',
        data: [83000, 49000, 60000, 35000, 77000, 90000],
        pointPlacement: 'on',
        color: '#f35958'
    }]

});

    // custom checkboxes
    var elems, switcheryOpts;

    elems = Array.prototype.slice.call(document.querySelectorAll('.switchery'))

    switcheryOpts = {
        color: '#1bc98e'
    };

    elems.forEach(function(el) {
        var switchery = new Switchery(el, switcheryOpts);
    });




    // ration stock stacked area
    $('#ration-stock .stacked-area').highcharts({
        chart: {
            type: 'area'
        },
        title: {
            text: ''
        },
        xAxis: {
            allowDecimals: false,
            labels: {
                formatter: function () {
                    return this.value; // clean, unformatted number for year
                }
            }
        },
        yAxis: {
            title: {
                text: 'Кол-во'
            },
            labels: {
                formatter: function () {
                    return this.value / 1000 + 'k';
                }
            }
        },
        tooltip: {
            pointFormat: '{series.name} produced <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
        },
        plotOptions: {
            area: {
                pointStart: 2012,
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 1,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },
        series: [{
            name: 'ПКО онлайн',
            data: [20000, 0, 3000, 600, 800, 6, 11, 32, 110, 235, 369, 640,
                1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468, 20434, 24126,
                27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342, 26662,
                26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
                24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586,
                22380, 21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950,
                10871, 10824, 10577, 10527, 10475, 10421, 10358, 10295, 10104],
            color: '#1bc98e'
        },
        {
            name: 'ПКО ',
            data: [3000, 4000, 5000, 9, 0, 70000, 500, 2000, 5000, 7000,
                5000, 25, 50, 120, 150, 200, 426, 660, 869, 1060, 1605, 2471, 3322,
                4238, 5221, 70000, 7089, 8339, 9399, 10538, 11643, 13092, 14478,
                15915, 17385, 19055, 21205, 23044, 25393, 27935, 30062, 32049,
                33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000, 37000,
                35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
                21000, 20000, 19000, 18000, 18000, 17000, 16000],
            color: '#676F84'
        }]
    });

// Monitoring stacked area
    $('#ration-stock .ver-column').highcharts({
        chart: {
        type: 'bar'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: ''
    },
    xAxis: {
        categories: ['ЦОН', 'eGOV', 'Homebank', 'Казпочта', 'Офис', 'Портал', 'Мобильное приложение', 'МИФ' ],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'выдано ПКО',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ' millions'
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 80,
        floating: true,
        borderWidth: 1,
        backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
        shadow: true
    },
    credits: {
        enabled: false
    },
    series: [{
        name: '2015',
        data: [107, 31, 635, 203, 150, 130, 50, 2]
    }, {
        name: '2016',
        data: [133, 156, 947, 408, 350, 300, 250, 6]
    }, {
        name: '2017',
        data: [1052, 954, 1250, 740, 600, 500, 300, 38]
    }]
    });

    // Combination-chart
 /*   $('#combo-channels .combo-area').highcharts({
         title: {
        text: ''
    },
    xAxis: {
        categories: ['01.2017', '02.2017', '03.2017', '04.2017', '05.2017', '06.2017', '07.2017', '08.2017']
    },
    labels: {
        items: [{
            html: 'Выдачи ПКО',
            style: {
                left: '50px',
                top: '18px',
                color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
            }
        }]
    },
    series: [{
        type: 'column',
        name: 'Онлайн',
        data: [3, 2, 1, 3, 4, 8, 5, 4]
    }, {
        type: 'column',
        name: 'Оффлайн',
        data: [2, 3, 5, 7, 6, 5, 7, 4]
    }, {
        type: 'spline',
        name: 'Average',
        data: [3, 2.67, 3, 6.33, 3.33, 3, 5, 5],
        marker: {
            lineWidth: 2,
            lineColor: Highcharts.getOptions().colors[3],
            fillColor: 'white'
        }
    }, {
        type: 'pie',
        name: 'Total consumption',
        data: [{
            name: 'Онлайн',
            y: 13,
            color: Highcharts.getOptions().colors[0] // Jane's color
        }, {
            name: 'Оффлайн',
            y: 23,
            color: Highcharts.getOptions().colors[1] // John's color
        }],
        center: [100, 80],
        size: 100,
        showInLegend: false,
        dataLabels: {
            enabled: false
        }
    }]
});*/

    // inverted regions area
    $('#inverted-regions .inverted-area').highcharts({
        chart: {
            type: 'area',
        inverted: true
    },
    title: {
        text: ''
    },
    subtitle: {
        style: {
            position: 'absolute',
            right: '0px',
            bottom: '10px'
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Акмолинская',
            'Актюбинская ',
            'Алматинская',
            'Атырауская',
            'ЗКО',
            'Жамбылская',
            'Карагандинская',
            'Кызылординская',
            'Мангистауская',
            'ЮКО',
            'Павлодарская',
            'СКО',
            'ВКО',
            'Астана',
            'Алматы',
            'н.д',

        ]
    },
    yAxis: {
        title: {
            text: 'Number of units'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        },
        min: 0
    },
    plotOptions: {
        area: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Август',
        data: [3, 4, 3, 5, 4, 10, 12, 11, 8, 5, 3, 12, 5, 6, 14, 15, 1]
    }, {
        name: 'Июль',
        data: [1, 3, 4, 3, 3, 5, 4, 5, 7, 9, 4, 6, 12, 11, 14, 11, 2]
    }]
});

    // daily usage
    $('#daily-usage .area-chart').highcharts({
        title: {
            text: '',
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                dataLabels: {
                    enabled: true,
                    style: {
                        fontWeight: '500'
                    }
                }
            }
        },
        series: [{
            type: 'pie',
            name: 'Time share',
            data: [
                ['Онлайн', 86],
                ['Оффлайн', 14]
                ]
        }]
    });
});

    // Region stacked-chart
$('#stacked-channels .inverted-channels').highcharts({
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Stacked bar chart'
    },
    xAxis: {
        categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Total fruit consumption'
        }
    },
    legend: {
        reversed: true
    },
    plotOptions: {
        series: {
            stacking: 'normal'
        }
    },
    series: [{
        name: 'John',
        data: [2, 3, 4, 2, 2]
    }, {
        name: 'Jane',
        data: [2, 2, 3, 2, 1]
    }, {
        name: 'Joe',
        data: [3, 4, 4, 2, 2]
    }]
});