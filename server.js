const cron = require("node-cron");
const cronParser = require("cron-parser").parseExpression;
const CRON_TIME_SETTING = "*/5 * * * *";
const { spawn } = require("child_process");
const PORT = process.env.PORT || 3000;

const onCron = () => {
  const python = spawn("python", ["main.py"]);
  python.stdout.on("data", (data) => console.log(data.toString()));
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
  res.status(200);
});

app.listen(PORT, () => {
  console.log(`Express server listening on port ${PORT}`);
});
