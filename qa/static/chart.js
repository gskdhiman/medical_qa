function get_bar_config(label_txt, dataset_label, data_labels, data_values) {
    // configurations for the bar chart
    return {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: data_labels,
            datasets: [
                {
                    label: dataset_label,
                    backgroundColor: Array(56).fill('rgba(255, 99, 132, 0.5)'),
                    //backgroundColor: data_colors,
                    // borderColor: data_colors,
                    borderColor: Array(data_values.length).fill('rgba(255, 99, 132, 1)'),
                    data: data_values,
                    fill: true,
                },
            ]
        },

        // Configuration options go here
        options: {
            responsive: true,
            title: {
                display: true,
                text: label_txt
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            legend: {
                display: false,
                position: 'top',
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: false,
                        labelString: 'Tokens'
                    },
                    ticks: {
                        autoSkip: false,
                        fontSize: 10,
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Probability'
                    },
                    ticks: {
                        autoSkip: false,
                        fontSize: 10,
                        beginAtZero: true,
                        callback: function (value, index, values) {
                            return value;
                        }
                    }
                }]
            }
        }
    }
}

function returnCharts(tokens, start, end) {

    // bar charts
    const bar = document.getElementById('start').getContext('2d');
    const bar_config = get_bar_config('start', 'Confidence', tokens, start );
    const Bar =  new Chart(bar, bar_config);

    const bar2 = document.getElementById('end').getContext('2d');
    const bar_config2 = get_bar_config('end', 'Confidence', tokens, end);
    const Bar2 =  new Chart(bar2, bar_config2);

    return [Bar,Bar2]

}

function showCharts(Bar,Bar2) {
    window.myLine = Bar;
    window.myLine = Bar2;
}