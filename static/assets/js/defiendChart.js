let firstChartInstance;
let horizontalChart;
const ctx4 = document.getElementById('firstChart').getContext('2d');
const ctx = document.getElementById('horizontalChart').getContext('2d');

async function updateChart() {
    const selectedDisease = document.getElementById('diseaseSelect').value;
    
    // Fetch dynamic data
    const { monthlyData, weeklyData, dailyData, yearlyTotal, stateData } = await getDataForDisease(selectedDisease);

    // Destroy previous chart instances
    if (firstChartInstance) firstChartInstance.destroy();
    if (horizontalChart) horizontalChart.destroy();

    // Time-based Chart (Monthly, Weekly, Daily)
    firstChartInstance = new Chart(ctx4, {
        type: 'line',
        data: {
            datasets: [
                { label: `${selectedDisease.toUpperCase()} Monthly Cases`, data: monthlyData, borderColor: 'blue', borderWidth: 2, fill: false },
                { label: `${selectedDisease.toUpperCase()} Weekly Avg Cases`, data: weeklyData, borderColor: 'green', borderWidth: 2, fill: false },
            ]
        },
        options: {
            scales: { y: { beginAtZero: true } },
            plugins: {
                annotation: {
                    annotations: [{
                        type: 'line',
                        mode: 'horizontal',
                        scaleID: 'y',
                        value: yearlyTotal / 12,
                        borderColor: 'purple',
                        borderWidth: 2,
                        label: {
                            content: 'Yearly Avg',
                            enabled: true,
                            position: 'center'
                        }
                    }]
                }
            }
        }
    });

    // State-wise Cases Chart
    horizontalChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: stateData.states,
            datasets: [{
                label: `${selectedDisease.toUpperCase()} Cases`,
                data: stateData.cases,
                backgroundColor: stateData.cases.map(c => `rgba(255, 99, 132, ${c / Math.max(...stateData.cases)})`),
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            scales: { x: { beginAtZero: true } }
        }
    });
}


async function getDataForDisease(disease) {
    try {
        const response = await fetch(`testing?disease=${disease}`);
        const data = await response.json();

        return {
            monthlyData: data.timeData.monthly,
            weeklyData: data.timeData.weekly,
            dailyData: data.timeData.daily,
            yearlyTotal: data.timeData.yearly,
            stateData: {
                states: data.stateData.states,
                cases: data.stateData.cases
            }
        };
    } catch (error) {
        console.error('Error fetching data:', error);
        return { monthlyData: [], weeklyData: [], dailyData: [], yearlyTotal: 0, stateData: { states: [], cases: [] } };
    }
}

document.getElementById('diseaseSelect').addEventListener('change', updateChart);
updateChart();  // Initial call to load the first chart

