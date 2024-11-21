#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='air_ticket_reservation_system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

#Define a route to hello function
@app.route('/')
def hello():
	return render_template('index.html')

#Define route for customer login
@app.route('/loginCustomer')
def loginCustomer():
	return render_template('loginCustomer.html')

#Define route for staff login
@app.route('/loginStaff')
def loginStaff():
	return render_template('loginStaff.html')


# Gotta differentiate for staff and customer as well but need to deal with staff's foreign keys aka airline
#Define route for customer register
@app.route('/registerCustomer')
def registerCustomer():
	return render_template('registerCustomer.html')

#Define route for staff register
@app.route('/registerStaff')
def registerStaff():
	return render_template('registerStaff.html')



##################################################################
##################################################################
################               TODO               ################
##################################################################
##################################################################

# Fix the login so that either we can differentiate between staff
# and customer logins

#Authenticates the login FOR CUSTOMER
@app.route('/loginAuthCustomer', methods=['GET', 'POST'])
def loginAuthCustomer():
	#grabs information from the forms
	email = request.form['email']
	password = request.form['password']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM customer WHERE email = %s and password = %s'
	cursor.execute(query, (email, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['email'] = email
		return redirect(url_for('home'))
	else:
		#returns an error message to the html page
		error = 'Invalid email or password'
		return render_template('loginCustomer.html', error=error)

#Authenticates the login FOR STAFF
@app.route('/loginAuthStaff', methods=['GET', 'POST'])
def loginAuthStaff():
	#grabs information from the forms
	airline_name = request.form['airline_name']
	username = request.form['username']
	password = request.form['password']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM airline_staff WHERE airline_name = %s and username = %s and password = %s'
	cursor.execute(query, (airline_name, username, password))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	cursor.close()
	error = None
	if(data):
		#creates a session for the the user
		#session is a built in
		session['username'] = username
		return redirect(url_for('home'))
	else:
		#returns an error message to the html page
		error = 'Invalid airline, username, or password'
		return render_template('loginStaff.html', error=error)

# Make register for both customers and staff
# and also just fix what it generally does

#Authenticates the register for customer
@app.route('/registerAuthCustomer', methods=['GET', 'POST'])
def registerAuthCustomer():
	#grabs information from the forms
	username = request.form['username']
	password = request.form['password']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM user WHERE username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = 'INSERT INTO user VALUES(%s, %s)'
		cursor.execute(ins, (username, password))
		conn.commit()
		cursor.close()
		return render_template('index.html')


#Authenticates the register for staff
# This needs some extra logic for if the airline exists or not methinks
@app.route('/registerAuthStaff', methods=['GET', 'POST'])
def registerAuthStaff():
	#grabs information from the forms
	airline_name = request.form['airline_name']
	username = request.form['username']
	password = request.form['password']
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	date_of_birth = request.form['date_of_birth']
	#cursor used to send queries
	cursor = conn.cursor()
	#executes query
	query = 'SELECT * FROM user WHERE username = %s'
	cursor.execute(query, (username))
	#stores the results in a variable
	data = cursor.fetchone()
	#use fetchall() if you are expecting more than 1 data row
	error = None
	if(data):
		#If the previous query returns data, then user exists
		error = "This user already exists"
		return render_template('register.html', error = error)
	else:
		ins = '''INSERT INTO user (airline_name, username, password, first_name, last_name, date_of_birth)
        VALUES (%s, %s, %s, %s, %s, %s)'''
		cursor.execute(ins, (airline_name, username, password, first_name, last_name, date_of_birth))
		conn.commit()
		cursor.close()
		return render_template('index.html')

# Might need to change this? Customer uses email but staff uses username
@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')

app.secret_key = 'some key that you will never guess'

#Run the app on localhost port 5000
debug = True # -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
	app.run('127.0.0.1', 5000, debug = True)

# Need to revamp stuff from here on down because we aren't doing a blog

@app.route('/home')
def home():

    username = session['username']
    cursor = conn.cursor();
    query = 'SELECT ts, blog_post FROM blog WHERE username = %s ORDER BY ts DESC'
    cursor.execute(query, (username))
    data1 = cursor.fetchall() 
    for each in data1:
        print(each['blog_post'])
    cursor.close()
    return render_template('home.html', username=username, posts=data1)

@app.route('/post', methods=['GET', 'POST'])
def post():
	username = session['username']
	cursor = conn.cursor();
	blog = request.form['blog']
	query = 'INSERT INTO blog (blog_post, username) VALUES(%s, %s)'
	cursor.execute(query, (blog, username))
	conn.commit()
	cursor.close()
	return redirect(url_for('home'))
