import * as d3 from "d3";
import { Chart } from "chart.js";
import { registerables } from "chart.js";
Chart.register(...registerables);

// --- Sound Manager ---
// Sound functionality removed as per user request.
// const SoundManager = {
//     audioContext: null,
//     sounds: {},
//     isMuted: false, // Could be controlled by a UI element later

//     init() {
//         try {
//             this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
//         } catch (e) {
//             console.warn("Web Audio API is not supported in this browser.");
//         }
//     },

//     async loadSound(name, url) {
//         if (!this.audioContext) return;
//         if (this.sounds[name]) return this.sounds[name];
//         try {
//             const response = await fetch(url);
//             const arrayBuffer = await response.arrayBuffer();
//             const audioBuffer = await this.audioContext.decodeAudioData(arrayBuffer);
//             this.sounds[name] = audioBuffer;
//             return audioBuffer;
//         } catch (e) {
//             console.error(`Failed to load sound: ${name}`, e);
//         }
//     },

//     playSound(name) {
//         if (!this.audioContext || !this.sounds[name] || this.isMuted) return;
//         const source = this.audioContext.createBufferSource();
//         source.buffer = this.sounds[name];
//         source.connect(this.audioContext.destination);
//         source.start(0);
//     }
// };

document.addEventListener('DOMContentLoaded', async function () {
    // --- Initialize Sound Manager and Load Sounds ---
    // Sound functionality removed as per user request.
    // SoundManager.init();
    // await Promise.all([
    //     SoundManager.loadSound('hover', 'hover-sound.mp3'),
    //     SoundManager.loadSound('click', 'click-sound.mp3')
    // ]);

    // Add sound to interactive elements
    // Sound functionality removed as per user request.
    // document.querySelectorAll('.interactive-element, .scroll-button, .nav-link').forEach(el => {
    //     el.addEventListener('mouseenter', () => SoundManager.playSound('hover'));
    //     el.addEventListener('click', () => SoundManager.playSound('click'));
    // });

    // Smooth scroll for the "Explorar datos" button and nav links
    const scrollLinks = document.querySelectorAll('.scroll-button, .nav-link[href^="#"]');

    for (const scrollLink of scrollLinks) {
        scrollLink.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            // Check if it's a real anchor link
            if (href && href.startsWith('#') && href.length > 1) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    }

    // --- API Configuration ---
    const API_BASE_URL = window.location.origin + '/api/v1';
    
    // Global variable to store crime data
    let crimeData = [];
    let isLoading = false;

    // --- API Functions ---
    async function fetchCrimeData() {
        try {
            showLoadingState(true);
            console.log('🔄 Fetching crime data from API...');
            
            const response = await fetch(`${API_BASE_URL}/crime-data`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const result = await response.json();
            
            if (result.status === 'success') {
                crimeData = result.data || [];
                console.log(`✅ Loaded ${crimeData.length} crime records from API`);
                return crimeData;
            } else {
                throw new Error(result.message || 'Error fetching data');
            }
        } catch (error) {
            console.error('❌ Error fetching crime data:', error);
            // Fallback to demo data if API fails
            crimeData = getDemoData();
            showErrorMessage('Error al cargar datos. Mostrando datos de demostración.');
            return crimeData;
        } finally {
            showLoadingState(false);
        }
    }

    async function fetchStatistics() {
        try {
            const response = await fetch(`${API_BASE_URL}/statistics`);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const result = await response.json();
            
            if (result.status === 'success') {
                return result.data;
            } else {
                throw new Error(result.message || 'Error fetching statistics');
            }
        } catch (error) {
            console.error('❌ Error fetching statistics:', error);
            return null;
        }
    }

    // --- Demo Data Fallback ---
    function getDemoData() {
        return [
            { state: "Edo. de México", crimes: 28500, incidence: 8.5, types: { Homicidio: 2200, Robo: 15000, Otros: 11300 } },
            { state: "Ciudad de México", crimes: 21000, incidence: 7.2, types: { Homicidio: 1100, Robo: 12000, Otros: 7900 } },
            { state: "Jalisco", crimes: 15000, incidence: 6.5, types: { Homicidio: 1800, Robo: 8000, Otros: 5200 } },
            { state: "Guanajuato", crimes: 12500, incidence: 7.8, types: { Homicidio: 2500, Robo: 5000, Otros: 5000 } },
            { state: "Baja California", crimes: 11800, incidence: 9.1, types: { Homicidio: 2800, Robo: 6000, Otros: 3000 } },
            { state: "Veracruz", crimes: 9200, incidence: 5.5, types: { Homicidio: 900, Robo: 4000, Otros: 4300 } },
            { state: "Nuevo León", crimes: 8500, incidence: 4.9, types: { Homicidio: 700, Robo: 5500, Otros: 2300 } },
            { state: "Puebla", crimes: 7800, incidence: 5.8, types: { Homicidio: 650, Robo: 3500, Otros: 3650 } },
            { state: "Sonora", crimes: 6500, incidence: 6.2, types: { Homicidio: 1200, Robo: 2800, Otros: 2500 } },
            { state: "Chihuahua", crimes: 6200, incidence: 7.0, types: { Homicidio: 1500, Robo: 2500, Otros: 2200 } },
            { state: "Michoacán", crimes: 5900, incidence: 8.2, types: { Homicidio: 1900, Robo: 2000, Otros: 2000 } },
            { state: "Tamaulipas", crimes: 4800, incidence: 6.8, types: { Homicidio: 800, Robo: 2200, Otros: 1800 } },
            { state: "Guerrero", crimes: 4500, incidence: 8.9, types: { Homicidio: 1600, Robo: 1500, Otros: 1400 } },
            { state: "Sinaloa", crimes: 3200, incidence: 5.1, types: { Homicidio: 500, Robo: 1800, Otros: 900 } },
            { state: "Oaxaca", crimes: 2800, incidence: 3.4, types: { Homicidio: 300, Robo: 1000, Otros: 1500 } }
        ];
    }

    // --- UI Helper Functions ---
    function showLoadingState(show) {
        isLoading = show;
        const loadingElements = document.querySelectorAll('.loading-indicator');
        
        if (show) {
            // Add loading indicators if they don't exist
            if (loadingElements.length === 0) {
                const dashboardSection = document.getElementById('dashboard');
                if (dashboardSection) {
                    const loadingDiv = document.createElement('div');
                    loadingDiv.className = 'loading-indicator alert alert-info text-center';
                    loadingDiv.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Cargando datos...';
                    dashboardSection.insertBefore(loadingDiv, dashboardSection.firstChild);
                }
            }
        } else {
            // Remove loading indicators
            loadingElements.forEach(el => el.remove());
        }
    }

    function showErrorMessage(message) {
        const dashboardSection = document.getElementById('dashboard');
        if (dashboardSection) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'alert alert-warning alert-dismissible fade show';
            errorDiv.innerHTML = `
                <i class="fas fa-exclamation-triangle me-2"></i>${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            `;
            dashboardSection.insertBefore(errorDiv, dashboardSection.firstChild);
            
            // Auto-remove after 5 seconds
            setTimeout(() => {
                if (errorDiv.parentNode) {
                    errorDiv.remove();
                }
            }, 5000);
        }
    }

    // --- Counter Animation ---
    function animateCountUp(element, endValue, isPercentage = false) {
        let start = 0;
        const duration = 2000; // 2 seconds
        const range = endValue - start;
        let current = start;
        const increment = endValue > start ? 1 : -1;
        const stepTime = Math.abs(Math.floor(duration / range));
        
        const timer = setInterval(() => {
            current += increment * Math.max(1, Math.floor(range/100)); // Make smaller numbers animate slower
             if ((increment > 0 && current >= endValue) || (increment < 0 && current <= endValue)) {
                current = endValue;
                clearInterval(timer);
            }
            if (isPercentage) {
                 element.innerText = current.toFixed(1) + '%';
            } else {
                 element.innerText = Math.floor(current).toLocaleString();
            }
        }, 10);
    }

    // --- Update Key Stats ---
    async function updateStats(data) {
        try {
            // Try to get real statistics from API first
            const apiStats = await fetchStatistics();
            
            if (apiStats) {
                // Use API statistics
                const totalCrimesEl = document.getElementById('total-crimes-stat');
                totalCrimesEl.dataset.count = apiStats.total_crimes || 0;
                
                document.getElementById('top-state-stat').innerText = 
                    apiStats.top_crime_state?.state || 'N/A';
                
                const avgIncidenceEl = document.getElementById('avg-incidence-stat');
                avgIncidenceEl.dataset.count = apiStats.avg_incidence || 0;
                
                // For homicide rate, calculate from data
                if (data.length > 0) {
                    const sortedByHomicide = [...data].sort((a, b) => {
                        const aRate = (a.types?.Homicidio || 0) / (a.crimes || 1);
                        const bRate = (b.types?.Homicidio || 0) / (b.crimes || 1);
                        return bRate - aRate;
                    });
                    document.getElementById('top-homicide-stat').innerText = 
                        sortedByHomicide[0]?.state || 'N/A';
                }
            } else {
                // Fallback to client-side calculation
                updateStatsFromData(data);
            }
        } catch (error) {
            console.error('Error updating stats:', error);
            updateStatsFromData(data);
        }
    }

    function updateStatsFromData(data) {
        const totalCrimes = data.reduce((sum, item) => sum + (item.crimes || 0), 0);
        const totalCrimesEl = document.getElementById('total-crimes-stat');
        totalCrimesEl.dataset.count = totalCrimes;
        
        if (data.length > 0) {
            const sortedByCrimes = [...data].sort((a, b) => (b.crimes || 0) - (a.crimes || 0));
            document.getElementById('top-state-stat').innerText = 
                sortedByCrimes[0]?.state || 'N/A';

            const totalIncidence = data.reduce((sum, item) => sum + (item.incidence || 0), 0);
            const avgIncidence = data.length > 0 ? (totalIncidence / data.length) : 0;
            const avgIncidenceEl = document.getElementById('avg-incidence-stat');
            avgIncidenceEl.dataset.count = avgIncidence.toFixed(1);

            const sortedByHomicide = [...data].sort((a, b) => {
                const aHomicides = a.types?.Homicidio || 0;
                const bHomicides = b.types?.Homicidio || 0;
                const aRate = a.crimes > 0 ? aHomicides / a.crimes : 0;
                const bRate = b.crimes > 0 ? bHomicides / b.crimes : 0;
                return bRate - aRate;
            });
            document.getElementById('top-homicide-stat').innerText = 
                sortedByHomicide[0]?.state || 'N/A';
        } else {
            document.getElementById('total-crimes-stat').innerText = '0';
            document.getElementById('top-state-stat').innerText = 'N/A';
            document.getElementById('avg-incidence-stat').innerText = '0%';
            document.getElementById('top-homicide-stat').innerText = 'N/A';
        }
    }

    // --- D3.js Bubble Chart ---
    const bubbleSvg = d3.select("#crime-bubble-chart-svg");
    const bubbleContainer = document.getElementById('bubble-chart-container');
    const bubbleTooltip = d3.select("body").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

    const bubbleIncidenceColorScale = d3.scaleSequential(d3.interpolateRgb("#0dcaf0", "#e94560")) // Info to Danger color
        .domain(d3.extent(crimeData, d => d.incidence));

    function renderBubbleChart(filteredData = crimeData) {
        const width = bubbleContainer.clientWidth;
        const height = bubbleContainer.clientHeight;
        bubbleSvg.selectAll("*").remove(); // Clear previous elements
        
        if (filteredData.length === 0) return;

        const root = d3.hierarchy({ children: filteredData })
            .sum(d => d.crimes);

        const pack = d3.pack()
            .size([width - 2, height - 2])
            .padding(5);

        const nodes = pack(root).leaves();

        const node = bubbleSvg.selectAll("g")
            .data(nodes)
            .enter().append("g")
            .attr("transform", d => `translate(${d.x},${d.y})`);

        node.append("circle")
            .attr("r", d => d.r)
            .attr("class", "bubble")
            .attr("fill", d => bubbleIncidenceColorScale(d.data.incidence))
            .on("mouseover", function(event, d) {
                // SoundManager.playSound('hover'); // Sound functionality removed
                bubbleTooltip.transition().duration(200).style("opacity", .9);
                bubbleTooltip.html(`<strong>${d.data.state}</strong><br/>Crímenes: ${d.data.crimes.toLocaleString()}<br/>Incidencia: ${d.data.incidence}%`)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY - 28) + "px");
            })
            .on("mouseout", function(d) {
                bubbleTooltip.transition().duration(500).style("opacity", 0);
            });

        node.append("text")
            .attr("class", "bubble-label")
            .attr("dy", "0.3em")
            .text(d => d.r > 20 ? d.data.state.substring(0, 3) + "." : "")
            .style("font-size", d => Math.max(8, d.r / 4) + "px");
    }

    // --- Chart.js Horizontal Bar Chart ---
    const barCtx = document.getElementById('crime-bar-chart').getContext('2d');
    let crimeBarChart; 

    function renderBarChart(dataToDisplay = crimeData) {
        const topData = [...dataToDisplay]
            .sort((a, b) => b.crimes - a.crimes)
            .slice(0, 10)
            .reverse(); // Reverse for horizontal chart display

        const labels = topData.map(d => d.state);
        const crimeCounts = topData.map(d => d.crimes);

        if (crimeBarChart) {
            crimeBarChart.destroy();
        }

        // Set Chart.js defaults for dark mode
        Chart.defaults.color = 'rgba(255, 255, 255, 0.7)';
        Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.2)';

        crimeBarChart = new Chart(barCtx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Número de Delitos',
                    data: crimeCounts,
                    backgroundColor: 'rgba(13, 110, 253, 0.7)',
                    borderColor: 'rgba(13, 110, 253, 1)',
                    borderWidth: 1,
                    borderRadius: 5,
                }]
            },
            options: {
                indexAxis: 'y', // This makes the bar chart horizontal
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true,
                        title: { display: true, text: 'Número de Delitos' },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' }
                    },
                    y: {
                        grid: { display: false }
                    }
                },
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: context => ` ${context.raw.toLocaleString()} delitos`
                        }
                    }
                }
            }
        });
    }

    // --- Chart.js Doughnut Chart ---
    const doughnutCtx = document.getElementById('crime-doughnut-chart').getContext('2d');
    let crimeDoughnutChart;

    function renderDoughnutChart(dataToDisplay = crimeData) {
        const top5Data = [...dataToDisplay]
            .sort((a, b) => b.crimes - a.crimes)
            .slice(0, 5);

        const labels = top5Data.map(d => d.state);
        const crimeCounts = top5Data.map(d => d.crimes);

        if (crimeDoughnutChart) {
            crimeDoughnutChart.destroy();
        }

        crimeDoughnutChart = new Chart(doughnutCtx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Delitos',
                    data: crimeCounts,
                    backgroundColor: [
                        '#e94560', // danger
                        '#0d6efd', // primary
                        '#ffc107', // warning
                        '#0dcaf0', // info
                        '#6f42c1'  // purple
                    ],
                    borderColor: '#16213e', // Card background color
                    borderWidth: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: 'rgba(255, 255, 255, 0.9)'
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: context => ` ${context.label}: ${context.raw.toLocaleString()} delitos`
                        }
                    }
                }
            }
        });
    }

    // --- Initialize Dashboard ---
    async function initializeDashboard() {
        try {
            console.log('🚀 Initializing dashboard...');
            
            // Fetch real data from API
            const data = await fetchCrimeData();
            
            // Update statistics
            await updateStats(data);
            
            // Render all charts
            renderBubbleChart(data);
            renderBarChart(data);
            renderDoughnutChart(data);
            
            console.log('✅ Dashboard initialized successfully');
            
        } catch (error) {
            console.error('❌ Error initializing dashboard:', error);
            showErrorMessage('Error al inicializar el dashboard. Usando datos de demostración.');
            
            // Fallback to demo data
            const demoData = getDemoData();
            await updateStats(demoData);
            renderBubbleChart(demoData);
            renderBarChart(demoData);
            renderDoughnutChart(demoData);
        }
    }

    // Initialize dashboard when DOM is loaded
    initializeDashboard();

    // --- Dashboard Update Logic ---
    const locationFilterInput = document.getElementById('filter-location');
    let debounceTimeout;

    if (locationFilterInput) {
        locationFilterInput.addEventListener('input', () => {
            clearTimeout(debounceTimeout);
            debounceTimeout = setTimeout(async () => {
                const searchTerm = locationFilterInput.value.toLowerCase();
                
                if (isLoading) {
                    console.log('⏳ Still loading data, skipping filter update');
                    return;
                }
                
                const filteredData = crimeData.filter(d => 
                    d.state && d.state.toLowerCase().includes(searchTerm)
                );
                
                console.log(`🔍 Filtering by "${searchTerm}": ${filteredData.length} results`);
                
                // Update all components with filtered data
                updateStatsFromData(filteredData); // Use client-side calculation for filters
                renderBubbleChart(filteredData);
                renderBarChart(filteredData);
                renderDoughnutChart(filteredData);

                // When filtering, we don't re-animate the counters, just update simple text
                const totalCrimes = filteredData.reduce((s,i) => s + (i.crimes || 0), 0);
                document.getElementById('total-crimes-stat').innerText = totalCrimes.toLocaleString();
                
                const totalIncidence = filteredData.reduce((s,i) => s + (i.incidence || 0), 0);
                const newAvg = filteredData.length > 0 ? (totalIncidence / filteredData.length).toFixed(1) : 0;
                document.getElementById('avg-incidence-stat').innerText = `${newAvg}%`;

                console.log("✅ Dashboard updated with filter:", searchTerm);
            }, 300); // Debounce for 300ms
        });
    }

    // --- Add Refresh Button Functionality ---
    function addRefreshButton() {
        const statsSection = document.getElementById('stats-cards');
        if (statsSection && !document.getElementById('refresh-btn')) {
            const refreshBtn = document.createElement('button');
            refreshBtn.id = 'refresh-btn';
            refreshBtn.className = 'btn btn-outline-primary btn-sm mb-3';
            refreshBtn.innerHTML = '<i class="fas fa-sync-alt me-2"></i>Actualizar Datos';
            refreshBtn.onclick = async () => {
                refreshBtn.disabled = true;
                refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Actualizando...';
                
                try {
                    await initializeDashboard();
                    showErrorMessage('Datos actualizados correctamente.');
                } catch (error) {
                    showErrorMessage('Error al actualizar los datos.');
                } finally {
                    refreshBtn.disabled = false;
                    refreshBtn.innerHTML = '<i class="fas fa-sync-alt me-2"></i>Actualizar Datos';
                }
            };
            
            statsSection.parentNode.insertBefore(refreshBtn, statsSection);
        }
    }

    // Add refresh button after DOM is loaded
    setTimeout(addRefreshButton, 1000);

    // Re-render charts on window resize
    window.addEventListener('resize', () => {
        clearTimeout(debounceTimeout);
        debounceTimeout = setTimeout(() => {
            if (isLoading || !crimeData.length) return;
            
            const searchTerm = locationFilterInput?.value?.toLowerCase() || '';
            const filteredData = crimeData.filter(d => 
                d.state && d.state.toLowerCase().includes(searchTerm)
            );
            renderBubbleChart(filteredData);
            // No need to re-render Chart.js charts as they are responsive by default
        }, 300);
    });

    // --- Intersection Observer for animations ---
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');

                // If the stats cards section is visible, trigger the count-up
                if (entry.target.id === 'stats-cards') {
                    const totalCrimesEl = document.getElementById('total-crimes-stat');
                    const avgIncidenceEl = document.getElementById('avg-incidence-stat');
                    animateCountUp(totalCrimesEl, parseFloat(totalCrimesEl.dataset.count));
                    animateCountUp(avgIncidenceEl, parseFloat(avgIncidenceEl.dataset.count), true);
                    // We only want this to run once, so we can unobserve.
                    observer.unobserve(entry.target);
                }
            }
        });
    }, {
        threshold: 0.1 // Trigger when 10% of the element is visible
    });

    animatedElements.forEach(el => observer.observe(el));
});