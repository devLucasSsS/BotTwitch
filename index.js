const tmi = require("tmi.js");

const client = new tmi.Client({
  options: { debug: true },
  identity: {
    username: "lucassss14",
    password: "oauth:o8gapeamhl62m8h2p1mivx3bshn84k",
  },
  channels: ["Mathi"],
});

client.connect();

client.on("message", (channel, tags, message, self) => {
  if (self) return;

  if (message.toLowerCase() === "!afk") {
    client.say(channel, `Mathi will be back in a few minutes.`);
  }
  if (message.toLowerCase() === "!ping") {
    client.say(channel, `pong`);
  }

  if (message.toLowerCase() === "!subathon") {
    client.say(
      channel,
      `1 Sub = +1 Min. | 100 Bits = +1 Min. | $3 Tip  = +1 Min | \n\nSub milestones and more info: https://twitter.com/Mathi501/status/1579241459038842881?t=gWlRLEPtvKPmpNzBaOmvqw&s=19`
    );
  }
});
