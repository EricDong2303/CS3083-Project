# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL
conn = pymysql.connect(host='localhost',
                       port=3307,
                       user='root',
                       password='',
                       db='air_ticket_reservation_system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# Define a route to hello function


@app.route('/')
def hello():
    return render_template('index.html')

# Define route for customer login


@app.route('/loginCustomer')
def loginCustomer():
    return render_template('loginCustomer.html')

# Define route for staff login


@app.route('/loginStaff')
def loginStaff():
    return render_template('loginStaff.html')


@app.route('/searchFlight')
def searchFlight():
    return render_template('searchFlight.html')


# Gotta differentiate for staff and customer as well
# but need to deal with staff's foreign keys aka airline
# Define route for customer register
@app.route('/registerCustomer')
def registerCustomer():
    return render_template('registerCustomer.html')

# Define route for staff register


@app.route('/registerStaff')
def registerStaff():
    return render_template('registerStaff.html')

# Fix the login so that either we can differentiate between staff
# and customer logins

# Authenticates the login FOR CUSTOMER


@app.route('/loginAuthCustomer', methods=['GET', 'POST'])
def loginAuthCustomer():
    # grabs information from the forms
    email = request.form['email']
    password = request.form['password']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM customer WHERE email = %s and password = %s'
    cursor.execute(query, (email, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['email'] = email
        return redirect(url_for('home'))
    else:
        # returns an error message to the html page
        error = 'Invalid email or password'
        return render_template('loginCustomer.html', error=error)

# Authenticates the login FOR STAFF


@app.route('/loginAuthStaff', methods=['GET', 'POST'])
def loginAuthStaff():
    # grabs information from the forms
    airline_name = request.form['airline_name']
    username = request.form['username']
    password = request.form['password']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM airline_staff WHERE airline_name = %s \
             and username = %s and password = %s'
    cursor.execute(query, (airline_name, username, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        # session is a built in
        session['username'] = username
        return redirect(url_for('home'))
    else:
        # returns an error message to the html page
        error = 'Invalid airline, username, or password'
        return render_template('loginStaff.html', error=error)

# Make register for both customers and staff
# and also just fix what it generally does

# Authenticates the register for customer


@app.route('/registerAuthCustomer', methods=['GET', 'POST'])
def registerAuthCustomer():
    if request.method == 'POST':
        # Grab information from the forms
        email = request.form['email']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        building_number = request.form['building_number']
        street_name = request.form['street_name']
        apartment_number = request.form['apartment_number']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        passport_number = request.form['passport_number']
        passport_exp = request.form['passport_exp']
        passport_country = request.form['passport_country']
        date_of_birth = request.form['date_of_birth']
        
        # Cursor used to send queries
        cursor = conn.cursor()
        
        # Check if the user already exists
        query = 'SELECT * FROM customer WHERE email = %s'
        cursor.execute(query, (email))
        data = cursor.fetchone()
        error = None
        
        if data:
            # If the previous query returns data, then user exists
            error = "This email is already registered"
            return render_template('registerCustomer.html', error=error)
        else:
            # Insert the new user into the customer table
            insert_query = '''INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (email, password, first_name, last_name, 
                                          building_number, street_name, apartment_number, 
                                          city, state, zipcode, passport_number, passport_exp, 
                                          passport_country, date_of_birth))
            conn.commit()
            cursor.close()
            return render_template('index.html')  # Redirect to home page after successful registration
    else:
        return render_template('registerCustomer.html')


# Authenticates the register for staff
# This needs some extra logic for if the airline exists or not methinks
@app.route('/registerAuthStaff', methods=['GET', 'POST'])
def registerAuthStaff():
    # grabs information from the forms
    username = request.form['username']
    airline_name = request.form['airline_name']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('registerStaff.html', error=error)
    else:
        ins = 'INSERT INTO airline_staff VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (username, airline_name, password,
                       first_name, last_name, date_of_birth))
        conn.commit()
        cursor.close()
        return render_template('index.html')

# Might need to change this? Customer uses email but staff uses username


#Define route of customer logout
@app.route('/logoutCustomer')
def logoutCustomer():
    session.pop('email')
    return redirect('/loginCustomer')


#Define route for staff logout 
@app.route('/logoutStaff')
def logoutStaff():
	session.pop('username')
	return redirect('/loginStaff')



@app.route('/searchFlights', methods=['POST'])
def searchFlights():
    # Retrieve form data
    source = request.form['source']
    destination = request.form['destination']
    departure_date = request.form['departure_date']
    return_date = request.form.get('return_date', None)  # Optional for round trips

    # SQL query to fetch flights based on input
    cursor = conn.cursor()
    query = '''
        SELECT flight_number, airline_name, departure_date, departure_time, arrival_date, arrival_time, base_price
        FROM flight
        WHERE arrival_code = %s AND departure_code = %s AND departure_date = %s;
    '''
    params = (source, destination, departure_date)

    # Include return_date if it's provided
    if return_date:
        query += " AND arrival_date = %s"
        params += (return_date,)

    cursor.execute(query, params)
    flights = cursor.fetchall()
    cursor.close()

    # Pass the results to the results page
    return render_template('searchFlightResults.html', flights=flights, source=source, destination=destination)


@app.route('/home')
def home():
    if 'email' not in session:
        return render_template('loginCustomer.html')

    # Fetch email from the session
    email = session['email']
    cursor = conn.cursor()

    # Fetch customer name using email
    query = 'SELECT first_name FROM customer WHERE email = %s'
    cursor.execute(query, (email,))
    customer_data = cursor.fetchone()
    username = customer_data['first_name']
    
    cursor.close()

    return render_template('homeCustomer.html', username=username)


@app.route('/cancelTrip', methods=['POST'])
def cancelTrip():
    pass


@app.route('/rateFlight', methods=['POST'])
def rateFlight():
    pass


@app.route('/trackSpending', methods=['POST'])
def track_spending():
    pass



app.secret_key = 'some key that you will never guess'

# Run the app on localhost port 5000
debug = True  # -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)