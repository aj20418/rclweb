const express = require("express");
const exphbs = require("express-handlebars");

const app = express();

app.engine("handlebars", exphbs({
    defaultLayout: "main"
}));
app.set("view engine", "handlebars");

app.get("/", (req, res) => {
    res.render("index");
});

app.get("/signup", (req, res) => {
    res.redirect("https://docs.google.com/forms/d/e/1FAIpQLSd8zBqqJ4lPtTFSn0TbE_zyenUeh2k7PenefLocIu8xH5fXIw/viewform");
});

app.get("/teams", (req, res) => {
    res.render("teams");
});

const port = 5000

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});