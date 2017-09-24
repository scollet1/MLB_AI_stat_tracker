from flask import Flask, flash, redirect, render_template, request, session, abort
import random
 
app = Flask(__name__)
 
@app.route("/")
def index():
#    return name    
	return render_template(
		'index.html',**locals())

@app.route("/FighterOne/")
def f1():
	return render_template(
		'FighterOne.html',**locals())

@app.route("/FighterTwo/")
def f2():
	return render_template(
		'FighterTwo.html',**locals())

@app.route("/fight/")
def fight():
	return render_template(
		'FighterTwo.html',**locals())

@app.route("/about/")
def pick(options):
#    return name    
        return render_template(
                'about.html',**locals())

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "3000")
