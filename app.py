from flask import Flask, render_template, request
import json
import os
import random

app = Flask(__name__)

# Load moods.json relative to the app root and handle errors gracefully
moods_path = os.path.join(app.root_path, 'moods.json')
try:
    with open(moods_path, 'r', encoding='utf-8') as f:
        mood_d = json.load(f)
        if not isinstance(mood_d, dict):
            mood_d = {}
except (FileNotFoundError, json.JSONDecodeError):
    mood_d = {}

@app.route('/')
def home():
    return render_template('template/index.html')

@app.route('template/results', methods=['POST'])
def result():
    mood = request.form.get('mood', '').strip()
    if not mood:
        return render_template('template/results.html', mood='Unknown', quote='Please select a mood.')

    quotes = mood_d.get(mood, ["Stay Blessed and Be You, Always!"])
    quote = random.choice(quotes) if quotes else "Stay Blessed and Be You, Always!"
    return render_template('template/results.html', mood=mood, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
