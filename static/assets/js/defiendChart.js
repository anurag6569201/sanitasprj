const ctx4 = document.getElementById('firstChart').getContext('2d');
const firstChart = new Chart(ctx4, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Monthly Cases',
            data: [120, 190, 30, 50, 20, 30, 80, 100, 70, 40, 60, 90],
            borderWidth: 1
        }, {
            label: 'Weekly Cases',
            data: [50, 70, 20, 30, 10, 15, 40, 50, 35, 25, 30, 45],
            borderWidth: 1
        }, {
            label: 'Daily Cases',
            data: [5, 8, 2, 3, 1, 2, 6, 7, 5, 3, 4, 6],
            borderWidth: 1
        }, {
            label: 'Yearly Cases',
            data: [800, 1200, 300, 500, 200, 300, 800, 1000, 700, 400, 600, 900],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ctx = document.getElementById('horizontalChart').getContext('2d');
let horizontalChart;

function updateChart() {
    const selectedDisease = document.getElementById('diseaseSelect').value;
    const data = getDataForDisease(selectedDisease);

    if (horizontalChart) {
        horizontalChart.destroy();
    }

    horizontalChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Andhra Pradesh (' + data[0] + ')', 'Arunachal Pradesh (' + data[1] + ')', 'Assam (' + data[2] + ')', 'Bihar (' + data[3] + ')', 'Chhattisgarh (' + data[4] + ')', 'Goa (' + data[5] + ')', 'Gujarat (' + data[6] + ')', 'Haryana (' + data[7] + ')', 'Himachal Pradesh (' + data[8] + ')', 'Jharkhand (' + data[9] + ')', 'Karnataka (' + data[10] + ')', 'Kerala (' + data[11] + ')', 'Madhya Pradesh (' + data[12] + ')', 'Maharashtra (' + data[13] + ')', 'Manipur (' + data[14] + ')', 'Meghalaya (' + data[15] + ')', 'Mizoram (' + data[16] + ')', 'Nagaland (' + data[17] + ')', 'Odisha (' + data[18] + ')', 'Punjab (' + data[19] + ')', 'Rajasthan (' + data[20] + ')', 'Sikkim (' + data[21] + ')', 'Tamil Nadu (' + data[22] + ')', 'Telangana (' + data[23] + ')', 'Tripura (' + data[24] + ')', 'Uttar Pradesh (' + data[25] + ')'],
            datasets: [{
                label: selectedDisease.charAt(0).toUpperCase() + selectedDisease.slice(1) + ' Cases',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            scales: {
                x: {
                    beginAtZero: true
                }
            }
        }
    });
}

function getDataForDisease(disease) {
    if (disease === 'dengue') {
        return [100, 150, 80, 120, 200, 90, 140, 70, 110, 180, 95, 130, 170, 60, 100, 150, 80, 120, 200, 90, 140, 70, 110, 180, 95, 130, 170, 60]; // Update with actual data
    } else if (disease === 'malaria') {
        return [50, 70, 40, 90, 60, 30, 60, 35, 80, 45, 70, 55, 75, 40, 50, 70, 40, 90, 60, 30, 60, 35, 80, 45, 70, 55, 75, 40]; // Update with actual data
    } else if (disease === 'chikungunya') {
        return [30, 40, 20, 50, 35, 15, 25, 10, 30, 20, 40, 30, 45, 20, 30, 40, 20, 50, 35, 15, 25, 10, 30, 20, 40, 30, 45, 20]; // Update with actual data
    } else {
        return Array(29).fill(0); // Update with actual data for all 29 states
    }
}

updateChart();