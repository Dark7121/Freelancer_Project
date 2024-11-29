    const ctx = document.getElementById('abacusGraph').getContext('2d');

    // Custom plugin to draw background bars
    const backgroundPlugin = {
        id: 'backgroundPlugin',
        beforeDatasetsDraw(chart, args, options) {
            const { ctx, chartArea: { left, right, top, bottom }, scales: { x, y } } = chart;
            ctx.save();
            ctx.fillStyle = options.color || '#F2F7FF';
            chart.data.datasets[0].data.forEach((value, index) => {
                const xPos = x.getPixelForValue(index);
                const yPos = y.getPixelForValue(400); // Max value for background bars
                const height = y.getPixelForValue(0) - yPos;
                ctx.fillRect(xPos - 2.5, yPos, 5, height); // 5px bar width
            });
            ctx.restore();
        }
    };

    const data = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Monthly Analytics',
            data: [320, 290, 30, 50, 20, 230, 120, 190, 30, 50, 20, 30],
            backgroundColor: '#1B59F8', // Solid blue color
            borderColor: '#1B59F8',
            borderWidth: 1,
            barThickness: 5, // Set bar width to 5px
            borderRadius: 60,
            borderSkipped: false
        }]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {
            scales: {
                x: {
                    grid: {
                        display: false // Remove x-axis grid lines
                    },
                    ticks: {
                        maxRotation: 0, // Prevent tilting
                        minRotation: 0, // Prevent tilting
                        font: {
                            size: 10 // Adjust font size to fit all labels
                        }
                    },
                    border: {
                        display: false // Remove x-axis border line
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        display: false // Remove y-axis grid lines
                    },
                    ticks: {
                        stepSize: 100, // Set the interval for the y-axis
                        padding:5,
                        callback: function(value) {
                            if ([0, 100, 200, 300, 400].includes(value)) {
                                return value; // Only show specific values
                            }
                            return '';
                        },
                        font: {
                            size: 10 // Adjust font size if needed
                        }
                    },
                    border: {
                        display: false // Remove y-axis border line
                    }
                }
            },
            elements: {
                bar: {
                    borderRadius: 60
                }
            },
            plugins: {
                title: {
                    display: false
                }
            }
        },
        plugins: [backgroundPlugin]
    };
    Chart.defaults.font.family = 'DM Sans'; // Set global default font to DM Sans

    new Chart(ctx, config);