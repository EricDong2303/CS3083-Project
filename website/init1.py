# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL, port 3307 is my MariaDB
conn = pymysql.connect(host='localhost',
                       port=3307,
                       user='root',
                       password='',
                       db='air_ticket_reservation_system',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


# Define a route to index
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


# Route for the search flight
@app.route('/searchFlight')
def searchFlight():
    return render_template('searchFlight.html')


# Define route for customer register
@app.route('/registerCustomer')
def registerCustomer():
    return render_template('registerCustomer.html')


# Define route for staff register
@app.route('/registerStaff')
def registerStaff():
    return render_template('registerStaff.html')


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
        session['username'] = username
        return redirect(url_for('staffHome'))
    else:
        # returns an error message to the html page
        error = 'Invalid airline, username, or password'
        return render_template('loginStaff.html', error=error)


# Authenticates the register for customer
@app.route('/registerAuthCustomer', methods=['GET', 'POST'])
def registerAuthCustomer():
    # Gets all the info the customer entered
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
        # Redirect to home page after successful registration, customer will now log in using their login credentials
        return render_template('loginCustomer.html')


# Authenticates the register for staff
@app.route('/registerAuthStaff', methods=['GET', 'POST'])
def registerAuthStaff():
    # grabs information from the forms
    username = request.form['username']
    airline_name = request.form['airline_name']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date_of_birth = request.form['date_of_birth']
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM airline_staff WHERE username = %s'
    cursor.execute(query, (username))
    data = cursor.fetchone()
    error = None
    if (data):
        # If the previous query returns data, then user exists and show error
        error = "This user already exists"
        return render_template('registerStaff.html', error=error)
    else:
        ins = 'INSERT INTO airline_staff VALUES (%s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (username, airline_name, password,
                       first_name, last_name, date_of_birth))
        conn.commit()
        cursor.close()
        return render_template('loginStaff.html')


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


# Route for searching the flights
@app.route('/searchFlights', methods=['POST'])
def searchFlights():
    # Gets the info for the flight the customer wants to search for
    source = request.form['source']
    destination = request.form['destination']
    departure_date = request.form['departure_date']
    return_date = request.form.get('return_date', None)  # Optional for round trips
    # query to fetch flights based on input
    cursor = conn.cursor()
    query = '''
        SELECT flight_number, airline_name, departure_date, departure_time, arrival_date, arrival_time, base_price
        FROM flight
        WHERE arrival_code = %s AND departure_code = %s AND departure_date = %s;
    '''
    params = (source, destination, departure_date)
    # return_date if it's provided
    if return_date:
        query += " AND arrival_date = %s"
        params += (return_date,)

    cursor.execute(query, params)
    flights = cursor.fetchall()
    cursor.close()
    # Brings the customer to this page where it will show results
    return render_template('searchFlightResults.html', flights=flights, source=source, destination=destination)


# Route for the customer home page
@app.route('/home')
def home():
    if 'email' not in session:
        return render_template('loginCustomer.html')
    email = session['email']
    cursor = conn.cursor()
    query = 'SELECT first_name FROM customer WHERE email = %s'
    cursor.execute(query, (email,))
    customer_data = cursor.fetchone()
    name = customer_data['first_name']
    cursor.close()
    return render_template('homeCustomer.html', name=name)


# Route for the staff's home page
@app.route('/staffHome')
def staffHome():
    if 'username' in session:
        username = session['username']
        return render_template('homeStaff.html', username=username)
    else:
        return redirect(url_for('loginStaff'))


# Route for canceling a trip, customer will enter ticketID and it will unlink the ticket from the customer
@app.route('/cancelTrip', methods=['POST'])
def cancelTrip():
    # Get the info
    ticket_id = request.form['ticket_id']
    cursor = conn.cursor()
    # Query to make sure the ticket is after current time
    query = '''
            DELETE FROM purchase 
            WHERE ticket_id = %s AND
            ticket_id IN (
                SELECT ticket_id 
                FROM ticket
                WHERE ticket_id = %s 
                AND departure_date > CURDATE()
                OR (departure_date = CURDATE() AND departure_time > CURTIME())
            )
        '''
    cursor.execute(query, (ticket_id, ticket_id))
    conn.commit()
    check = cursor.fetchone()
    # Shows error if customer does not have the ticket
    if not check:
        cursor.close()
        return render_template('homeCustomer.html', cancel_error="Invalid ticket ID or ticket not found. Can not cancel.")
    # query to delete the ticket
    query = '''
            DELETE FROM ticket 
            WHERE ticket_id = %s 
            AND departure_date > CURDATE() 
            OR (departure_date = CURDATE() AND departure_time > CURTIME())'''
    cursor.execute(query, (ticket_id))
    conn.commit()
    cursor.close()
    return render_template('homeCustomer.html', cancel_message="Your flight has been canceled!")
    

# Route for the customer rating the flights, the customer should have a ticket for the flight they want to review
@app.route('/rateFlight', methods=['POST'])
def rateFlight():
    # Get the info from what the customer entered
    email = session['email']
    rating = request.form['rating']
    comment = request.form['comment']
    ticket_id = request.form['ticket_id']
    cursor = conn.cursor()
    # Need to query to get info from the ticket
    ticket_find = '''SELECT * 
    		FROM ticket
    		WHERE ticket_id = %s'''
    cursor.execute(ticket_find, (ticket_id,))
    ticket = cursor.fetchone()
    # If no ticket or invalid ticket, show an error
    if not ticket:
        cursor.close()
        return render_template('homeCustomer.html', rating_error="Invalid ticket ID or ticket not found.")
	# Get the info from ticket that was queried
    airline_name = ticket['airline_name']
    flight_number = ticket['flight_number']
    departure_date = ticket['departure_date']
    departure_time = ticket['departure_time']
    # Insert into review table after info was retrieved
    review_post = '''INSERT INTO review VALUES(%s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(review_post, (email, flight_number, airline_name, departure_date, departure_time, rating, comment))
    conn.commit()
    cursor.close()
    return render_template('homeCustomer.html', rating_message="Your review has been submitted!")


# Route for showing the amount of money the customer has spent. Customer will enter a date range and result will be shown
@app.route('/trackSpending', methods=['POST'])
def track_spending():
    pass



app.secret_key = 'some key that you will never guess'

# Run the app on localhost port 5000
debug = True  # -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)