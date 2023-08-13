from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ( <!DOCTYPE html>
<html lang="ua">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Русин Василь Іванович</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #e6e6e6;
        }
        .container {
            background-color: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Русин Василь Іванович</h1>
        <p>Професія: Геодезист</p>
        <p>Ласкаво просимо до мого веб-сайту. Я тут, щоб поділитися своїм досвідом і знаннями в галузі геодезії.</p>
    </div>
</body>
</html>)