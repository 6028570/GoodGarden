/**
 * Class to handle the creation and manipulation of line charts on a canvas.
 */
class LineChart 
{
    /**
     * Creates an instance of LineChart.
     * @param {string} canvasId - The ID of the canvas element where the chart will be drawn.
     */
    constructor(canvasId) 
    {
        this.canvas = document.getElementById(canvasId);
        if (this.canvas) 
        {
            this.ctx = this.canvas.getContext("2d");
        }
        this.padding = 35; // Default padding around the graph
    }

    /**
     * Clears the entire canvas, preparing it for a new drawing.
     */
    clearCanvas() 
    {
        if (this.canvas) 
        {
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        }
    }

    /**
     * Draws a line chart on the canvas using the provided data.
     * @param {Array<string>} xLabels - Labels for the x-axis.
     * @param {Array<number>} data - Data points for the chart, one per x-label.
     * @param {Array<number|string>} [yLabels=["", 10, 15, 20, 25, 30, 35, 40]] - Labels for the y-axis.
     */
    drawChart(xLabels, data, yLabels = ["", 10, 15, 20, 25, 30, 35, 40]) 
    {
        if (!this.canvas) 
        {
            return; // Exit if canvas is not initialized
        }
        
        this.clearCanvas();
        const graphWidth = this.canvas.width - this.padding * 2;
        const graphHeight = this.canvas.height - this.padding * 2;

        // Draw the axes
        this.ctx.strokeStyle = "rgb(143, 188, 143)";
        this.ctx.beginPath();
        this.ctx.moveTo(this.padding, this.padding);
        this.ctx.lineTo(this.padding, this.canvas.height - this.padding);
        this.ctx.lineTo(this.canvas.width - this.padding, this.canvas.height - this.padding);
        this.ctx.stroke();

        // Calculate increments for plotting points
        const xIncrement = graphWidth / (xLabels.length - 1);
        const yIncrement = graphHeight / (yLabels.length - 1);
        
        // Plot the data points
        this.ctx.beginPath();
        this.ctx.moveTo(this.padding, this.canvas.height - this.padding - (data[0] / 100) * graphHeight);
        for (let i = 1; i < data.length; i++) 
        {
            const xPos = this.padding + i * xIncrement;
            const yPos = this.canvas.height - this.padding - (data[i] / 100) * graphHeight;
            this.ctx.lineTo(xPos, yPos);
        }
        this.ctx.stroke();
        
        // Draw y-axis labels
        this.ctx.fillStyle = "black";
        this.ctx.textAlign = "right";
        this.ctx.textBaseline = "middle";
        yLabels.forEach((label, i) => 
        {
            if (label !== "") 
            {
                const yPos = this.canvas.height - this.padding - i * yIncrement;
                this.ctx.fillText(label, this.padding - 10, yPos);
            }
        });

        // Draw x-axis labels
        this.ctx.textAlign = "center";
        xLabels.forEach((label, i) => 
        {
            if (label !== "") 
            {
                const xPos = this.padding + i * xIncrement;
                this.ctx.fillText(label, xPos, this.canvas.height - this.padding + 20);
            }
        });
    }
}

/**
 * Fetches weather data from an API and draws a line chart with the fetched data.
 * @param {LineChart} chart - The LineChart instance to draw on.
 * @param {string} apiUrl - The URL to fetch the weather data from.
 */
function fetchWeatherDataAndDrawChart(chart, apiUrl) 
{
    fetch(apiUrl)
        .then(response => response.ok ? response.json() : Promise.reject('Network response was not ok.'))
        .then(data => 
        {
            const dates = data.weather_forecast.map(day => day.dag);
            const temperatures = data.weather_forecast.map(day => day.max_temp);
            chart.drawChart(dates, temperatures);
        })
        .catch(error => console.error('There was a problem with the fetch operation:', error));
}

const myChart = new LineChart("myCanvas");
fetchWeatherDataAndDrawChart(myChart, "http://127.0.0.1:5000/weather");