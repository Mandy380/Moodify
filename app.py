from flask import Flask, render_template, request
import json, random

app = Flask(__name__)

with open('moods.json', 'r') as f:
  mood_d = json.load(f)

@app.route('/')
def home():
  return render_template('inder.html')

@pp.route('/results', methods=['POST'])
