const express = require("express");
const mongoose = require("mongoose");

const app = express();
app.use(express.json());

mongoose.connect("mongodb://mongo:27017/testdb", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log("Connected to MongoDB"))
.catch(err => console.log("Mongo connection error: ", err));

const UserSchema = new mongoose.Schema({
    name: String,
});
const User = mongoose.model("User", UserSchema);

app.get("/", (req, res) => {
    res.send("Node.js + MongoDB App running in Docker Compose!");
});

app.post("/user", async (req, res) => {
    const user = await User.create({ name: req.body.name });
    res.send(user);
});

app.get("/users", async (req, res) => {
    const users = await User.find();
    res.send(users);
});

app.listen(3000, () => console.log("Server running on port 3000"));
