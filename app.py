from flask import Flask, render_template, request
import json, random

app = Flask(__name__)

with open('moods.json', 'r') as f:
  mood_d = json.load(f)

@app.route('/')
def home():
  return render_template('index.html')

@pp.route('/results', methods=['POST'])
def result():
  mood = request.form['mood']
  quotes = mood_d.get(mood,"Stay Blessed and Be You, Always!"])
  quote = random.choice(quotes)
  return render_template('result.html', mood = mood, quote = quote)

if __name__ == '__main__':
  app.run(debug=True)
