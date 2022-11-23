

function padTo2Digits(num) {
  return num.toString().padStart(2, '0');
}

function formatDate(d) {
  const date = new Date(d);
  return [
      date.getFullYear(),
      padTo2Digits(date.getMonth() + 1),
      padTo2Digits(date.getDate()),
    ].join('-');
}

function createColumn(cat, data) {
  const table = document.querySelector(
    cat + ' > table'
  );

  Array.from(data).forEach(t => {
    const row = table.insertRow(table.rows.length);
    const link = row.insertCell(0);
    const size = row.insertCell(1);
    const date = row.insertCell(2);

    link.innerHTML = `<a href="${t.link}">${t.file}</a>`;
    date.innerHTML = formatDate(t.date);
    size.innerHTML = t.size;
  });
}

(async () => {

  const socket = io();

  let build = null;
  let dist = null;
  socket.once('columnCreate', data => {
    Object.keys(data).forEach(key => {
      switch (key) {
        case 'build': createColumn('#build', data[key]);
          break;
        case 'dist': createColumn('#dist', data[key]);
          break;
      }
    });
  });

})();
