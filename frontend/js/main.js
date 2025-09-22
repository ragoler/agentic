document.addEventListener('DOMContentLoaded', () => {
    const tripForm = document.getElementById('trip-form');
    const resultsContent = document.getElementById('results-content');
    const resultsContainer = document.getElementById('results-container');
    const submitButton = document.getElementById('submit-button');

    tripForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const formData = new FormData(tripForm);
        const data = {
            destination: formData.get('destination'),
            start_date: formData.get('start_date'),
            end_date: formData.get('end_date'),
        };

        if (!data.destination || !data.start_date || !data.end_date) {
            resultsContent.innerHTML = '<p class="error">Please fill out all fields.</p>';
            resultsContainer.style.display = 'block';
            return;
        }

        resultsContent.innerHTML = '<p class="loading">Searching for the best options...</p>';
        resultsContainer.style.display = 'block';
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
                const errorData = await response.json().catch(() => ({ detail: `HTTP error! status: ${response.status}` }));
                throw new Error(errorData.detail);
            }

            const tripPlan = await response.json();
            displayResults(tripPlan, data.destination);

        } catch (error) {
            console.error('Error planning trip:', error);
            resultsContent.innerHTML = `<p class="error">An error occurred: ${error.message}</p>`;
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = 'Plan Trip';
        }
    });

    function displayResults(plan, destination) {
        let html = `<h3>Live Flights Near ${destination}</h3>`;
        if (plan.live_flights_nearby && plan.live_flights_nearby.length > 0) {
            html += '<ul>';
            plan.live_flights_nearby.forEach(flight => {
                html += `<li><strong>${flight.callsign}</strong> (from ${flight.origin_country})</li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>No live flights found nearby.</p>';
        }

        html += '<h3>Hotel Options</h3>';
        if (plan.hotels && plan.hotels.length > 0) {
            html += '<ul>';
            plan.hotels.forEach(hotel => {
                html += `<li><strong>${hotel.name}</strong> - ${hotel.price_per_night}/night (Rating: ${hotel.rating})</li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>No hotels found.</p>';
        }

        resultsContent.innerHTML = html;
    }
});
