document.getElementById("loadData").addEventListener("click", () => {
  fetch("/data?limit=50")
    .then((res) => res.json())
    .then((data) => {
      const tbody = document.querySelector("#data-table tbody");
      tbody.innerHTML = "";

      data.forEach((row) => {
        const tr = document.createElement("tr");

        tr.innerHTML = `
                    <td>${formatDate(row.Start)}</td>
                    <td>${formatNumber(row.Open)}</td>
                    <td>${formatNumber(row.High)}</td>
                    <td>${formatNumber(row.Low)}</td>
                    <td>${formatNumber(row.Close)}</td>
                    <td>${formatBig(row.Volume)}</td>
                    <td>${formatBig(row.MarketCap)}</td>
                `;

        tbody.appendChild(tr);
      });
    })
    .catch((err) => console.error(err));
});

function formatNumber(num) {
  return Number(num).toFixed(2);
}

function formatBig(num) {
  return Number(num).toLocaleString();
}

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString();
}
