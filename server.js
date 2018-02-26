const express = require('express');
const app = express();

app.use(express.static('public'));

app.get("/", function (request, response) {
  response.sendFile(__dirname + '/src/index.html');
});

const listener = app.listen(8080, function () {
  console.log('Listening on port ' + listener.address().port);
});
