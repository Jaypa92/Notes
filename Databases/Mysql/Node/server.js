const express= require("express");
const pool = require("./db");

const app = express();
app.use(express.json());

app.get("/", async (req, res) => {
    try {
        const [rows] =await pool.query("SELECT NOW() As current_time");
        res.json({message: "Mysql Connection Successful!", time: rows[0].current_time});
    } catch(err) {
        console.error("Database Connection Error:", err);
        res.status(500).json({error: "Database connection failed"});
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server Running on Port ${PORT}`));