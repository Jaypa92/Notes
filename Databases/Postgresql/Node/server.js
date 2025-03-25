const express = require("express");
const pool = require("./db");

const app = express();
app.use(express.json());

app.get("/", async (req, res) => {
    try{
        const result = await pool.query("SELECT NOW()");
        res.json({ success: true, timestamp: result.rows[0]});
    } catch (err) {
        console.error(err);
        res.status(500).send("Database Connection Error");
    }
});

app.listen(5000, () => console.log("Server Running on Port 5000"));