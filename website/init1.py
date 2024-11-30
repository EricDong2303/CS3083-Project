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
        session['airline_name'] = airline_name
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


# Created a function to query the customer's name, need to get name when resubmitting the page after success/fail
def query_customer_name():
    email = session['email']
    cursor = conn.cursor()
    query = 'SELECT first_name FROM customer WHERE email = %s'
    cursor.execute(query, (email,))
    customer_data = cursor.fetchone()
    name = customer_data['first_name']
    cursor.close()
    return name


# Route for the customer home page
@app.route('/home')
def home():
    if 'email' in session:
        name = query_customer_name()
        return render_template('homeCustomer.html', name=name)
    else:
        return render_template('loginCustomer.html')
    

# Route for the staff's home page
@app.route('/staffHome')
def staffHome():
    if 'username' in session:
        username = session['username']
        airline_name = session['airline_name']
        return render_template('homeStaff.html', username=username, airline_name=airline_name)
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
        name = query_customer_name()
        return render_template('homeCustomer.html', name=name, cancel_error="Invalid ticket ID or ticket not found. Can not cancel.")
    # query to delete the ticket
    query = '''
            DELETE FROM ticket 
            WHERE ticket_id = %s 
            AND departure_date > CURDATE() 
            OR (departure_date = CURDATE() AND departure_time > CURTIME())'''
    cursor.execute(query, (ticket_id))
    conn.commit()
    cursor.close()
    name = query_customer_name()
    return render_template('homeCustomer.html', name=name, cancel_message="Your flight has been canceled!")
    

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
        name = query_customer_name()
        return render_template('homeCustomer.html', name=name, rating_error="Invalid ticket ID or ticket not found.")
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
    name = query_customer_name()
    return render_template('homeCustomer.html', name=name, rating_message="Your review has been submitted!")


# Route for showing the amount of money the customer has spent. Customer will enter a date range and result will be shown
@app.route('/trackSpending', methods=['POST'])
def trackSpending():
    pass


# Route to let the airline staff see how much revenue was earned in the last month/year. 
@app.route('/viewRevenue', methods=['POST'])
def viewRevenue():
    # The staff just has to press the button, so we need to get their airline
    airline_name = session['airline_name']
    cursor = conn.cursor()
    # Query for the last month. First get number of days currently, substract to get the first of the month,
    # then subtract 1 whole month to get previous month. Then filter from that date to end of month
    last_month_query = '''
        SELECT SUM(ticket_price) AS total_revenue
        FROM ticket
        WHERE airline_name = %s
        AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL DAYOFMONTH(CURDATE()) - 1 DAY) - INTERVAL 1 MONTH
        AND purchase_date < DATE_SUB(CURDATE(), INTERVAL DAYOFMONTH(CURDATE()) - 1 DAY);
    '''
    cursor.execute(last_month_query, (airline_name,))
    last_month_rev = cursor.fetchone()['total_revenue'] or 0
    # Query to get revenue from the last year.
    last_year_query = '''
        SELECT SUM(ticket_price) AS total_revenue
        FROM ticket
        WHERE airline_name = %s
        AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
        AND purchase_date < CURDATE();
    '''
    cursor.execute(last_year_query, (airline_name,))
    last_year_rev = cursor.fetchone()['total_revenue'] or 0
    cursor.close()
    # Displays a new page to the staff with the revenue
    return render_template('viewRevenue.html', last_month_rev=last_month_rev, last_year_rev=last_year_rev)


# Route to add airport into the database system, does not change the page for staff but updates the database
@app.route('/addAirport', methods=['POST'])
def addAirport():
    # Get the info that the staff enters
    code = request.form['airport_code']
    name = request.form['name']
    city = request.form['city']
    country = request.form['country']
    number_of_terminals = request.form['terminals']
    type = request.form['type']
    # Do the query
    cursor = conn.cursor()
    query = '''
        INSERT INTO airport VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (code, name, city, country, number_of_terminals, type))
    conn.commit()
    cursor.close()
    return redirect(url_for('staffHome'))


# Route for staff to be able to add an airplane into the system, does not change the page for staff but updates the database
@app.route('/addAirplane', methods=['POST'])
def addAirplane():
    # Gets the info the staff enters
    airplane_id = request.form['airplane_id']
    seats = request.form['seats']
    company = request.form['company']
    model_number = request.form['model']
    manufacture_date = request.form['manufacture_date']
    airline_name = session['airline_name']
    # Do the query
    cursor = conn.cursor()
    query = '''
        INSERT INTO airplane (id, airline_name, seats, company, model_number, manufacture_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(query, (airplane_id, airline_name, seats, company, model_number, manufacture_date))
    conn.commit()
    cursor.close()
    return redirect(url_for('staffHome'))


# Route for the customer to be able to view their upcoming flights, to click the button, it should bring them to the next page
@app.route('/viewFlight', methods=['POST'])
def viewFlight():
    pass


# Route for the airline staff to see who the most frequent customer is
@app.route('/viewFrequentCustomer', methods=['POST'])
def viewFrequentCustomer():
    # When the staff presses on the button, it should bring them to a new page that shows who the most frequent customer is
    airline_name = session['airline_name']
    cursor = conn.cursor()
    query = '''
        SELECT c.first_name, c.last_name, COUNT(*) AS number_of_flights
        FROM customer c
        JOIN purchase p ON c.email = p.email
        JOIN ticket t ON p.ticket_id = t.ticket_id
        JOIN flight f ON t.flight_number = f.flight_number AND t.airline_name = f.airline_name
        WHERE f.airline_name = %s AND t.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
        GROUP BY c.first_name, c.last_name
        ORDER BY number_of_flights DESC
        LIMIT 1
    '''
    cursor.execute(query, (airline_name,))
    result = cursor.fetchone()
    cursor.close()
    # Put the result into a list, then the next page will extract the info and display it
    if not result:
        frequent_customer = None
    else:
        frequent_customer = {
            'first_name': result['first_name'],
            'last_name': result['last_name'],
            'num_flights': result['number_of_flights']
        }
    # The result will be shown on the new page
    return render_template('frequentCustomer.html', frequent_customer=frequent_customer)


# Route for the staff to change the status of a flight, does not change the page for staff but updates the database
@app.route('/changeFlightStatus', methods=['POST'])
def changeFlightStatus():
    # Bring the info the staff enters
    flight_number = request.form['flight_number']
    new_status = request.form['status']
    airline_name = session['airline_name']
    cursor = conn.cursor()
    # Do the query where it updates the status of the speciifc flight
    query = '''
        UPDATE flight
        SET flight_status = %s
        WHERE flight_number = %s AND airline_name = %s
    '''
    cursor.execute(query, (new_status, flight_number, airline_name))
    conn.commit()
    cursor.close()
    return redirect(url_for('staffHome'))


# Route for airline staff to see the average rating and all comments given for a specific flight
@app.route('/viewFlightRatings', methods=['POST'])
def viewFlightRatings():
    # Get the flight number and airline_name that will be used to query
    flight_number = request.form['flight_number']
    airline_name = session['airline_name']
    cursor = conn.cursor()
    # Query for average rating of the specific flight number
    avg_rating_query = '''
        SELECT AVG(rating) AS average_rating
        FROM review
        WHERE flight_number = %s AND airline_name = %s
    '''
    cursor.execute(avg_rating_query, (flight_number, airline_name))
    avg_rating = cursor.fetchone()['average_rating']
    # Query for all the comments made about this flight
    comments_query = '''
        SELECT comment
        FROM review
        WHERE flight_number = %s AND airline_name = %s
    '''
    cursor.execute(comments_query, (flight_number, airline_name))
    comments = cursor.fetchall()
    cursor.close()
    # Go to the new page where it displays all this info
    return render_template('flightRatings.html', flight_number=flight_number, average_rating=avg_rating, comments=comments)




# To Do
# Customer:
# 1) View flights that customer has purchased
# 2) Being able to purchase tickets
# 3) Track customer spend
# Airline Staff
# 1) View flights for the airline that staff works for
# 2) Create new flights for airline that staff works for
# 3) Schedule maintence, planes under maintenance cant be assigned to flight
# 4) Customer Search: Should also be able to see what flights the customer has taken on the staff airline




app.secret_key = 'some key that you will never guess'

# Run the app on localhost port 5000
debug = True  # -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)