const express = require('express');
const app = express();
const http = require('http');

app.use(express.static(__dirname + '/final'));

app.get("/", function (req, res) {
  res.sendFile('index.html');
});

app.get("/test", function (req, res) {
  res.sendFile('stylesheet.css');
});

const listener = app.listen(8080, function () {
  console.log('Listening on port ' + listener.address().port);
});

setInterval(() => {
  http.get(`http://${process.env.PROJECT_DOMAIN}.glitch.me/`);
}, 280000);