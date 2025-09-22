document.addEventListener('DOMContentLoaded', () => {
    const tripForm = document.getElementById('trip-form');
    const resultsContent = document.getElementById('results-content');
    const submitButton = document.getElementById('submit-button');

    tripForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(tripForm);
        const data = {
            destination: formData.get('destination'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date'),
        };

        // Basic validation
        if (!data.destination || !data.start_date || !data.end_date) {
            resultsContent.innerHTML = '<p style="color: red;">Please fill out all fields.</p>';
            return;
        }

        resultsContent.innerHTML = '<p>Planning your trip...</p>';
        submitButton.disabled = true;
        submitButton.textContent = 'Planning...';

        try {
            const response = await fetch('/api/v1/plan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const tripPlan = await response.json();
            displayResults(tripPlan);

        } catch (error) {
            console.error('Error planning trip:', error);
            resultsContent.innerHTML = `<p style="color: red;">An error occurred while planning your trip. Please check the console for details.</p>`;
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Plan Trip';
        }
    });

    function displayResults(plan) {
        let html = '<h3>Flights</h3>';
        if (plan.flights && plan.flights.length > 0) {
            html += '<ul>';
            plan.flights.forEach(flight => {
                html += `<li>${flight.airline} - $${flight.price} (Departs: ${flight.departure_time})</li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>No flights found.</p>';
        }

        html += '<h3>Hotels</h3>';
        if (plan.hotels && plan.hotels.length > 0) {
            html += '<ul>';
            plan.hotels.forEach(hotel => {
                html += `<li>${hotel.name} - $${hotel.price_per_night}/night (Rating: ${hotel.rating})</li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>No hotels found.</p>';
        }

        resultsContent.innerHTML = html;
    }
});
