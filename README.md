<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NoLimi v2.0</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Segoe UI,Arial,sans-serif;
        }

        body{
            background:#0f172a;
            color:white;
        }

        header{
            text-align:center;
            padding:80px 20px;
            background:linear-gradient(135deg,#2563eb,#0f172a);
        }

        h1{
            font-size:60px;
        }

        h2{
            color:#60a5fa;
            margin-bottom:20px;
        }

        p{
            line-height:1.8;
            color:#d1d5db;
        }

        section{
            width:90%;
            max-width:1100px;
            margin:auto;
            padding:60px 0;
        }

        .grid{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:25px;
        }

        .card{
            background:#1e293b;
            padding:25px;
            border-radius:15px;
            transition:.3s;
        }

        .card:hover{
            transform:translateY(-8px);
            box-shadow:0 15px 30px rgba(0,0,0,.3);
        }

        ul{
            padding-left:20px;
            line-height:2;
        }

        pre{
            background:#111827;
            padding:20px;
            border-radius:10px;
            overflow:auto;
        }

        footer{
            text-align:center;
            padding:30px;
            color:#9ca3af;
            border-top:1px solid #334155;
        }

        .btn{
            display:inline-block;
            margin-top:30px;
            padding:15px 35px;
            background:#2563eb;
            color:white;
            text-decoration:none;
            border-radius:10px;
            font-weight:bold;
        }

        .btn:hover{
            background:#1d4ed8;
        }

    </style>

</head>
<body>

<header>

<h1>🚀 NoLimi v2.0</h1>

<p>
AI Powered Desktop Voice Assistant
</p>

<a href="https://github.com/kunalchwdry/NoLimi" class="btn">
View on GitHub
</a>

</header>

<section>

<h2>✨ Features</h2>

<div class="grid">

<div class="card">
<h3>🤖 AI Assistant</h3>

<ul>
<li>AI Conversations</li>
<li>Natural Language Commands</li>
<li>Modular AI Integration</li>
</ul>

</div>

<div class="card">

<h3>🌐 Browser</h3>

<ul>
<li>Open Websites</li>
<li>DuckDuckGo Search</li>
<li>YouTube Search</li>
<li>Smart Search</li>
</ul>

</div>

<div class="card">

<h3>💻 Applications</h3>

<ul>
<li>Launch Installed Apps</li>
<li>Windows Utilities</li>
<li>Browser Launcher</li>
</ul>

</div>

<div class="card">

<h3>🔊 System Controls</h3>

<ul>
<li>Volume Control</li>
<li>Brightness Control</li>
<li>Percentage Commands</li>
<li>Voice Automation</li>
</ul>

</div>

</div>

</section>

<section>

<h2>📂 Project Structure</h2>

<pre>
NoLimi/

│

├── main.py

├── AI/
│   └── AI.py

├── System/
│   ├── process.py
│   ├── application.py
│   ├── Browser.py
│   ├── volume.py
│   └── Brightness.py

├── speaker/
│   └── speaker.py

└── README.md
</pre>

</section>

<section>

<h2>🛠 Tech Stack</h2>

<div class="grid">

<div class="card">
Python 3.11
</div>

<div class="card">
SpeechRecognition
</div>

<div class="card">
Gemini API
</div>

<div class="card">
DuckDuckGo Search
</div>

<div class="card">
PyCAW
</div>

<div class="card">
Screen Brightness Control
</div>

<div class="card">
Pygame
</div>

<div class="card">
dotenv
</div>

</div>

</section>

<section>

<h2>🚀 Roadmap</h2>

<ul>

<li>📂 File Management</li>

<li>📸 Screenshot Commands</li>

<li>📋 Clipboard Manager</li>

<li>🔒 Lock PC</li>

<li>🌙 Sleep Mode</li>

<li>📶 WiFi & Bluetooth Control</li>

<li>🧠 Memory System</li>

<li>📅 Calendar Integration</li>

<li>📑 OCR</li>

<li>🔌 Plugin System</li>

</ul>

</section>

<section>

<h2>🎙 Example Commands</h2>

<pre>
Open YouTube

Increase Volume

Decrease Brightness

Open Chrome

Search Python

What is AI?

Open GitHub

Increase Volume by 20 Percent
</pre>

</section>

<footer>

<p>

Made with ❤️ by <b>Kunal Choudhary</b>

<br><br>

NoLimi v2.0

</p>

</footer>

</body>
</html>