from flask import Flask, request, render_template_string, jsonify
import subprocess
import sys
import os
import json

app = Flask(__name__)

# HTML template for the web interface
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube to IPTV</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: 50px auto; padding: 20px; background: #f0f4f8; }
        h1 { color: #1a73e8; }
        .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input, button { padding: 12px; font-size: 16px; margin: 5px 0; width: 100%; box-sizing: border-box; border-radius: 5px; }
        input { border: 1px solid #ddd; }
        button { background: #1a73e8; color: white; border: none; cursor: pointer; }
        button:hover { background: #1557b0; }
        .result { background: #e8f0fe; padding: 15px; border-radius: 5px; margin-top: 20px; border-left: 4px solid #1a73e8; }
        .error { background: #fce8e6; border-left-color: #d93025; }
        a { color: #1a73e8; word-break: break-all; }
        .badge { display: inline-block; background: #34a853; color: white; padding: 3px 10px; border-radius: 15px; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎬 YouTube to IPTV</h1>
        <p>Convert YouTube channels to IPTV streams</p>
        <form method="POST">
            <input type="text" name="channel" placeholder="Enter YouTube Channel Name (e.g., Citizen TV)" required>
            <button type="submit">Generate IPTV Link</button>
        </form>
        {% if result %}
            <div class="result">
                <h3>✅ IPTV URL Generated:</h3>
                <p><a href="{{ result }}" target="_blank">{{ result }}</a></p>
                <p><small>📺 Copy this URL and paste it in your IPTV player</small></p>
            </div>
        {% endif %}
        {% if error %}
            <div class="result error">
                <h3>⚠️ Error:</h3>
                <p>{{ error }}</p>
            </div>
        {% endif %}
        <p style="margin-top: 20px; font-size: 14px; color: #666;">
            📂 <a href="https://github.com/odenzel-art/project-1">View on GitHub</a>
        </p>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    if request.method == 'POST':
        channel = request.form.get('channel')
        if channel:
            try:
                # Here you can call your project_1.py logic
                # For now, generating a sample IPTV URL
                result = f"https://iptv-odenzel.onrender.com/playlist.m3u?channel={channel.replace(' ', '_')}"
            except Exception as e:
                error = str(e)
    
    return render_template_string(HTML, result=result, error=error)

# Health check endpoint for Render
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)