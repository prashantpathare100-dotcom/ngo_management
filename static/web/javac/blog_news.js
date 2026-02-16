const express = require("express");
const app = express();
app.use(express.static("public"));

app.set("view engine", "ejs");
app.set('views','views');

app.get("/", (req, res) => {
  res.render("home");
});

app.get("/a", (req, res) => {
  res.render("a");
});

app.get("/b", (req, res) => {
  res.render("b");   // a.ejs open होईल
});

app.get("/c", (req, res) => {
  res.render("c");   // c.ejs open होईल
});








app.listen(2000, () => {
  console.log("Server running on http://localhost:800");
});