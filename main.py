import flask
from flask import Flask, render_template,url_for,request,send_file
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
app = Flask(__name__)
file = pd.read_csv('2019.csv')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Analysis')
def Analysis():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on score')
    y=file['Score']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.scatter(x,y,color='yellow')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('analysis.png')
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)

