from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import os
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")