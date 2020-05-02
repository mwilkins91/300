const cron = require("node-cron");
const cronParser = require("cron-parser").parseExpression;
const CRON_TIME_SETTING = "* * * * *";
const { spawn } = require("child_process");
const PORT = process.env.PORT || 3000;
const fs = require("fs");
const path = require("path");

const onCron = () => {
  const python = spawn("python", ["main.py"]);
  python.stdout.on("data", (data) => {
    console.log(data.toString());
    fs.appendFile("convo.html", data.toString(), function (err) {
      if (err) console.error(err);
    });
  });
  python.stderr.on("data", (data) => console.error(data.toString()));
};

cron.schedule(
  CRON_TIME_SETTING,
  () => {
    onCron();
  },
  true
);

const express = require("express");
const bodyParser = require("body-parser");
const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

app.post("/", (req, res) => {
  const msg = req.body.Body;
  console.log("body: ", req.body);
  if (!msg || !isValid) {
    return res.status(400).send();
  }
  fs.appendFile(
    "convo.html",
    `<div style="border: 2px solid black; margin-top: 20px;"><p>Person:</p><p>${msg}</p></div>`,
    function (err) {
      if (err) console.error(err);
    }
  );
  res.status(200);
});

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "/convo.html"));
});

app.listen(PORT, () => {
  console.log(`Express server listening on port ${PORT}`);
});
