import flask
from flask import Flask, render_template,url_for,request,send_file
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
file = pd.read_csv('2019.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Analysis')
def Analysis():
    return render_template('detail.html')

@app.route('/gdp')
def gdp():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on GDP per capita')
    y=file['GDP per capita']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.plot(x,y,color='orange')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('gdp.png')

@app.route('/score')
def score():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on Score')
    y=file['Score']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.scatter(x,y,color='orange')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('score.png')


@app.route('/freedom')
def freedom():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on freedom to make life choices')
    y=file['Freedom to make life choices']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.bar(x,y,color='red')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('freedom.png')
    
@app.route('/generosity')
def generosity():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on generosity')
    y=file['Generosity']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.bar(x,y,color='blue')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('generosity.png')


@app.route('/perceptions')
def perceptions():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on Perceptions of corruption')
    y=file['Perceptions of corruption']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.scatter(x,y,color='yellow')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('perceptions.png')

@app.route('/social')
def social():
    file = pd.read_csv('2019.csv')
    plt.title('World happiness report 2019 based on Social support')
    y=file['Social support']
    x=file['Country or region']
    N=len(x)

    plt.xticks(np.arange(0,N,2))    
    plt.scatter(x,y,color='green')

    plt.setp(plt.gca().get_xticklabels(),
         rotation=90,
         horizontalalignment='right',
         fontsize=10)
    return send_file('social.png')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
