from flask import Flask, render_template_string
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SERVERX OPTION</title>
    <style>
        body {
            font-family: sans-serif; /* Use a generic sans-serif font */
            background-color: #1e1e1e; /* Dark background */
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center; /* Center horizontally */
            justify-content: center; /* Center vertically */
            min-height: 100vh; /* Ensure full viewport height */
            margin: 0; /* Remove default margins */
        }

      .container {
            display: flex;
            flex-direction: column;
            gap: 20px; /* Spacing between the boxes */
        }

      .box {
            background-color: #282828; /* Darker box background */
            padding: 20px;
            border-radius: 10px; /* Rounded corners */
            text-align: center; /* Center text within the box */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
        }

      .image-container {
            width: 200px; /* Set a specific width for the image */
            margin: 0 auto 10px; /* Center the image and add margin below */
        }

      .image-container img {
            max-width: 100%; /* Make image responsive */
            height: auto;
            display: block; /* Prevents a small space below image */
            border-radius: 5px; /* Image border radius */
        }

      .server-title {
            font-weight: bold;
            margin-bottom: 10px;
        }

      .visit-button {
            display: inline-block;
            background-color: #f0ad4e; /* Orange button */
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease; /* Smooth transition */
        }

      .visit-button:hover {
            background-color: #e09d3e; /* Darker orange on hover */
        }
    </style>
</head>
<body>

<div class="container">
    <div class="box">
        <div class="image-container">
            <img src="https://i.ibb.co/93VC3jbM/20250214-212537.jpg" alt="">
        </div>
        <div class="server-title">SERVICES<br></div>
        <a href="https://main-e27b.onrender.com" class="visit-button">Visit</a>
    </div>

    <div class="box">
        <div class="image-container">
            <img src="https://i.ibb.co/6RRkf4bD/20250214-212224.jpg" alt="All in One Tool Image 2">
        </div>
        <div class="server-title">ABOUT<br></div>
        <a href="https://about-ypme.onrender.com" class="visit-button">Visit</a>
    </div>

    <div class="container">
    <div class="box">
        <div class="image-container">
            <img src="https://i.ibb.co/27J5BSNM/20250215-001929.jpg" alt="">
        </div>
        <div class="server-title">STUTAS<br></div>
        <a href="https://stutas.onrender.com" class="visit-button">Visit</a>
    </div>
    <a href="https://wa.me/+9779844298980" target="_blank" style="position: fixed; bottom: 400px; left: 50%; transform: translateX(-50%); display: flex; flex-direction: column; align-items: center; z-index: 100;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/2048px-WhatsApp.svg.png" alt="WhatsApp" style="width: 300px; height: 300px;">  <span style="margin-top: 10px; background-color: rgba(0, 0, 0, 0.5); color: white; padding: 8px 16px; border-radius: 8px; font-size: 40px;">Contact</span> </a>

</div>

</body>
</html>'''

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
