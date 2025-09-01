// document.addEventListener('DOMContentLoaded', async () => {
//   async function getData() {
//     try {
//       const response = await fetch("https://xpoint.ea-africaexchange.com/api/price_difference");
//       const data = await response.json();
//       return data;
//     } catch (error) {
//       console.error("Error:", error);
//     }
//   }

//   // Await the resolved data
//   const apiData = await getData();
//   console.log("API Data:", apiData);

//   // Function to populate a single <ul>
//   function populateStockTicker(ul, data) {
//     ul.innerHTML = ''; // Clear existing content

//     Object.entries(data).forEach(([commodity, [change, currentPrice]]) => {
//       const previousPrice = currentPrice - change;
//       const isIncrease = change >= 0;
//       const li = document.createElement('li');
//       li.className = isIncrease ? 'plus' : 'minus';

//       li.innerHTML = `
//         <span class="company">${commodity}</span>
//         <span class="change">${isIncrease ? '+' : ''}${change} (${((change / previousPrice) * 100).toFixed(2)}%)</span><br><br>
//         <span class="company">RWF</span>
//         <span class="price">${currentPrice.toFixed(2)}</span>
//       `;

//       ul.appendChild(li);
//     });
//   }

//   // Select both <ul> elements
//   const ul1 = document.querySelector('.stock-ticker ul:first-child');
//   const ul2 = document.querySelector('.stock-ticker ul:last-child');

//   // Populate both <ul> elements with the same data
//   populateStockTicker(ul1, apiData);
//   populateStockTicker(ul2, apiData);
// });

document.addEventListener('DOMContentLoaded', async () => {
const CACHE_EXPIRATION = 60 * 60 * 1000; // 1 hour in milliseconds

async function getData() {
  try {
    const cachedData = localStorage.getItem('apiData');
    const cachedTime = localStorage.getItem('apiDataTime');

    if (cachedData && cachedTime) {
      const age = Date.now() - parseInt(cachedTime, 10);
      if (age < CACHE_EXPIRATION) {
        console.log("Using cached data");
        return JSON.parse(cachedData);
      }
    }

    // Fetch new data if cache is expired or not available
    const response = await fetch("https://xpoint.ea-africaexchange.com/api/price_difference");
    const data = await response.json();

    // Cache the data and timestamp
    localStorage.setItem('apiData', JSON.stringify(data));
    localStorage.setItem('apiDataTime', Date.now().toString());
    console.log("Fetched and cached data");
    return data;
  } catch (error) {
    console.error("Error:", error);
  }
}
  // Await the resolved data
  const apiData = await getData();

  // Function to populate a single <ul>
  function populateStockTicker(ul, data) {
    ul.innerHTML = ''; // Clear existing content

    Object.entries(data).forEach(([commodity, [change, currentPrice]]) => {
      const previousPrice = currentPrice - change;
      const isIncrease = change >= 0;
      const li = document.createElement('li');
      li.className = isIncrease ? 'plus' : 'minus';

      li.innerHTML = `
        <br><span class="company">${commodity}</span>
        <span class="change">${isIncrease ? '+' : ''}${change} (${((change / previousPrice) * 100).toFixed(2)}%)</span><br>
        <span class="company">RWF</span>
        <span class="price">${currentPrice.toFixed(2)}</span>
      `;

      ul.appendChild(li);
    });
  }

  // Select both <ul> elements
  const ul1 = document.querySelector('.stock-ticker ul:first-child');
  const ul2 = document.querySelector('.stock-ticker ul:last-child');

  // Populate both <ul> elements with the same data
  populateStockTicker(ul1, apiData);
  populateStockTicker(ul2, apiData);
});