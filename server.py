from flask import Flask, flash, redirect, render_template, request, session, abort
import random
import sys
sys.path.insert(0, 'py/')
from run import run

app = Flask(__name__)
 
@app.route("/")
def index():
#    return name    
	return render_template(
		'index.html',**locals())

@app.route("/pick/", methods=['GET', 'POST'])
def pick():
	if request.method == 'POST':
		f1 = request.form['submit']
		print f1
		f2 = request.form['submit2']
		print f2
		f3 = int(request.form['fight'])
		if f3 is not None:
			print "Running Simulation..."
			victor = run("predict", f1, f2)
			return redirect(url_for('fight'))
	return render_template('pick.html',**locals())

@app.route("/fight/")
def fight():
	return render_template('fight.html')

@app.route("/about/")
def about():
#    return name    
        return render_template(
                'about.html',**locals())

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "3000")
