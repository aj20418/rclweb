const express = require('express');
const app = express();

app.use(express.static('public'));

app.get("/", function (req, res) {
  res.sendFile(__dirname + '/src/index.html');
});

app.get("/test", function (req, res) {
  res.send(__dirname + '/src/data.html');
});

const listener = app.listen(8080, function () {
  console.log('Listening on port ' + listener.address().port);
});
