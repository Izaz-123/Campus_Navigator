document.getElementById('navigator-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    let start = document.getElementById('start').value;
    let end = document.getElementById('end').value;

    try {
        const response = await fetch('/find-path/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() // Needed for security
            },
            body: JSON.stringify({ start, end })
        });

        const data = await response.json();

        if (data.path) {
            document.getElementById('result').innerHTML = `
                <h5>Shortest Path:</h5>
                <p>${data.path.join(' ➡️ ')}</p>
                <p><strong>Distance:</strong> ${data.distance} meters</p>
            `;

            drawPathOnMap(data.path);
        } else {
            document.getElementById('result').innerHTML = `<p class="text-danger">No path found.</p>`;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

function getCSRFToken() {
    let name = 'csrftoken';
    let cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
        }
    }
    return '';
}

// Example D3 path drawing
function drawPathOnMap(path) {
    let mapDiv = d3.select("#map");
    mapDiv.html(""); // Clear old map

    let svg = mapDiv.append("svg")
        .attr("width", "100%")
        .attr("height", 400);

    let nodes = path.map((block, i) => ({ name: block, x: 100 + i * 150, y: 200 }));

    svg.selectAll("circle")
        .data(nodes)
        .enter()
        .append("circle")
        .attr("cx", d => d.x)
        .attr("cy", d => d.y)
        .attr("r", 25)
        .attr("fill", "skyblue")
        .attr("stroke", "black");

    svg.selectAll("text")
        .data(nodes)
        .enter()
        .append("text")
        .attr("x", d => d.x)
        .attr("y", d => d.y + 5)
        .attr("text-anchor", "middle")
        .attr("font-size", "12px")
        .text(d => d.name);

    // Draw lines between nodes
    svg.selectAll("line")
        .data(d3.pairs(nodes))
        .enter()
        .append("line")
        .attr("x1", d => d[0].x)
        .attr("y1", d => d[0].y)
        .attr("x2", d => d[1].x)
        .attr("y2", d => d[1].y)
        .attr("stroke", "black")
        .attr("stroke-width", 2);
}

