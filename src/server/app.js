const express = require('express');
const mysql = require('mysql');
const app = express();
app.use(express.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'admin',
    database: 'msme'
});

app.post('/check-msme', (req, res) => {
    const regNumber = req.body.msmeRegNumber;
    const query = 'SELECT * FROM msme WHERE reg_number = ?';

    db.query(query, [regNumber], (error, results) => {
        if (error) {
            return res.status(500).json({ error: 'Internal Server Error' });
        }

        const isValid = results.length > 0;
        res.json({ isValid });
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});