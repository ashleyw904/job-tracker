window.onload = function () {
    const ctx = document.getElementById('statusChart').getContext('2d');

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Applied', 'Interviewing', 'Offer', 'Rejected'],
            datasets: [{
                data: window.chartData,
                backgroundColor: ['#007bff', '#ff9800', '#28a745', '#dc3545']
            }]
        }
    });
};