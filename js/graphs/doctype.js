$(function () {
    var chart;
    
    $(document).ready(function () {
    	
    	// Build the chart
        chart = new Highcharts.Chart({
            chart: {
                renderTo: 'doctype',
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: ''
            },
            tooltip: {
        	    pointFormat: '{series.name}: <b>{point.percentage}%</b>',
            	percentageDecimals: 1
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                type: 'pie',
                name: 'Server',
                data: [
			["null", 19],
       			["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">", 3],
        ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">", 1],
        ["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">", 1],
        ["<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\" \"http://www.w3.org/TR/html4/loose.dtd\">", 4],
        ["<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\"[]>", 2],
        ["<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml2/DTD/xhtml1-strict.dtd\">", 1],
        ["HTML 4.0 (loose)", 1],
        ["HTML 4.01 (loose)", 2],
        ["HTML 4.01 (strict)", 1],
        ["HTML 5", 20],
        ["XHTML 1.0 (loose)", 70],
        ["XHTML 1.0 (strict)", 27],
        ["XHTML 1.1", 12],
        ["XHTML+RDFA 1.0", 1]
                ]
            }]
        });
    });
    
});
