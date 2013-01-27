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
			["Unknown / None / Other", 19 + 3 + 1 + 1 + 4 + 2 + 1],
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
