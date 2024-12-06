# Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
import datetime
import uuid

# Initialize the app from Flask
app = Flask(__name__)

# Configure MySQL, port 3307 is my MariaDB
conn = pymysql.connect(host='localhost',
                       port=3307, # 3307 or 3306 depending on who's using it
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
    query = '''SELECT * FROM customer WHERE email = %s and password = md5(%s)'''
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
    username = request.form['username']
    password = request.form['password']
    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = '''SELECT * FROM airline_staff WHERE \
            username = %s and password = md5(%s)'''
    cursor.execute(query, (username, password))
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if (data):
        # creates a session for the the user
        session['username'] = username
        session['airline_name'] = data["airline_name"]
        return redirect(url_for('staffHome'))
    else:
        # returns an error message to the html page
        error = 'Invalid username or password'
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
    query = '''SELECT * FROM customer WHERE email = %s'''
    cursor.execute(query, (email))
    data = cursor.fetchone()
    error = None
    if data:
        # If the previous query returns data, then user exists
        error = "This email is already registered"
        return render_template('registerCustomer.html', error=error)
    else:
        # Insert the new user into the customer table
        try:
            insert_query = '''INSERT INTO customer VALUES (%s, md5(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            cursor.execute(insert_query, (email, password, first_name, last_name,
                                      building_number, street_name,
                                      apartment_number, city, state, zipcode,
                                      passport_number, passport_exp,
                                      passport_country, date_of_birth))
            conn.commit()
            cursor.close()
            # Redirect to home page after successful registration, customer will now log in using their login credentials
            return render_template('loginCustomer.html')
        except:
            error = "One or more fields are incorrect. Please reenter your information"
            return render_template('registerCustomer.html', error=error)


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
    query = '''SELECT * FROM airline_staff WHERE username = %s'''
    cursor.execute(query, (username))
    data = cursor.fetchone()
    error = None
    if (data):
        # If the previous query returns data, then user exists and show error
        error = "This user already exists"
        return render_template('registerStaff.html', error=error)
    else:
        try:
            ins = '''INSERT INTO airline_staff VALUES (%s, %s, md5(%s), %s, %s, %s)'''
            cursor.execute(ins, (username, airline_name, password,
                        first_name, last_name, date_of_birth))
            conn.commit()
            cursor.close()
            return render_template('loginStaff.html')
        except:
            error = "One or more fields are incorrect. Please reenter your information"
            return render_template('registerStaff.html', error=error)


# Define route of customer logout
@app.route('/logoutCustomer')
def logoutCustomer():
    session.pop('email')
    return redirect('/loginCustomer')


# Define route for staff logout
@app.route('/logoutStaff')
def logoutStaff():
    session.pop('username')
    session.pop('airline_name')
    return redirect('/loginStaff')


# route for ticket purchase confirmation and collection
@app.route('/purchaseTicket', methods=['POST'])
def purchaseTicket():
    if 'email' not in session:
        return redirect(url_for('loginCustomer'))

    flight_number = request.form['flight_number']
    airline_name = request.form['airline_name']
    departure_date = request.form['departure_date']
    departure_time = request.form['departure_time']
    base_price = request.form['base_price']

    return render_template(
        'purchaseTicket.html',
        flight_number=flight_number,
        airline_name=airline_name,
        departure_date=departure_date,
        departure_time=departure_time,
        base_price=base_price
    )


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
    outbound_query = '''
        SELECT flight_number, airline_name, departure_date, departure_time, arrival_date, arrival_time, base_price
        FROM flight
        WHERE arrival_code = %s AND departure_code = %s AND departure_date = %s
    '''
    cursor.execute(outbound_query, (destination, source, departure_date))
    outbound_flights = cursor.fetchall()
    # return_date if it's provided
    return_flights = None
    if return_date:
        return_query = '''
            SELECT flight_number, airline_name, departure_date, departure_time, arrival_date, arrival_time, base_price
            FROM flight
            WHERE departure_code = %s AND arrival_code = %s AND departure_date = %s
        '''
        # for returns, the we're departing from the destination and returning to the source
        cursor.execute(return_query, (destination, source, return_date))
        return_flights = cursor.fetchall()
    cursor.close()
    # Brings the customer to this page where it will show results
    return render_template(
        'searchFlightResults.html',
        outbound_flights=outbound_flights,
        return_flights=return_flights,
        source=source,
        destination=destination)


# Created a function to query the customer's name, need to get name when resubmitting the page after success/fail
def query_customer_name():
    email = session['email']
    cursor = conn.cursor()
    query = '''SELECT first_name FROM customer WHERE email = %s'''
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
            SELECT * FROM purchase
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
    data = cursor.fetchone()
    # Shows error if customer does not have the ticket
    if not data:
        cursor.close()
        name = query_customer_name()
        return render_template('homeCustomer.html', name=name, cancel_error="Invalid ticket ID or ticket not found. Can not cancel.")
    # query to delete the ticket
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
    query = '''
            DELETE FROM ticket
            WHERE ticket_id = %s
            AND departure_date > CURDATE()
            OR (departure_date = CURDATE() AND departure_time > CURTIME())
        '''
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
    try:
        # Insert into review table after info was retrieved
        review_post = '''INSERT INTO review VALUES(%s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(review_post, (email, flight_number, airline_name, departure_date, departure_time, rating, comment))
        conn.commit()
        cursor.close()
        name = query_customer_name()
        return render_template('homeCustomer.html', name=name, rating_message="Your review has been submitted!")
    except:
        name = query_customer_name()
        return render_template('homeCustomer.html', name=name, rating_message="Please shorten the length of your review")



# route for purchasing ticket - and verifying purchase
@app.route('/authPurchase', methods=['POST'])
def authPurchase():
    # collect user info from session and form
    email = session['email']
    flight_number = request.form['flight_number']
    airline_name = request.form['airline_name']
    base_price = request.form['base_price']
    departure_time = request.form['departure_time']
    departure_date = request.form['departure_date']
    card_type = request.form['card_type']
    name_on_card = request.form['card_name']
    card_number = request.form['card_num']
    card_exp = request.form['exp_date']
    # if there are seats on the plane, then continue with purchase
    if remainingSeats(flight_number, airline_name):
        # create ticket id using helper function
        ticket_id = generate_ticket_id()
        cursor = conn.cursor()
        # fetch purchase time and date - i just did using datetime, i can also use sql
        purchase_date = datetime.datetime.now().date()
        purchase_time = datetime.datetime.now().time()
        ticket_insert = '''INSERT INTO ticket VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        try:
            cursor.execute(ticket_insert, (ticket_id, flight_number, airline_name,
                                        departure_date, departure_time, base_price,
                                        card_type, card_number, name_on_card,
                                        card_exp, purchase_date, purchase_time))
            purchase_insert = '''INSERT INTO purchase VALUES(%s, %s)'''
            cursor.execute(purchase_insert, (email, ticket_id))
            conn.commit()
            cursor.close()
        except:
            name = query_customer_name()
            return render_template('homeCustomer.html', error="One or more fields of information have invalid information. Please reenter your information.", name=name)
    else: # give an error message that tells you plane is full
        name = query_customer_name()
        return render_template('homeCustomer.html', error="This flight is fully booked. Please select another flight.", name=name)
    # should prob add a message that says purchase was successful
    name = query_customer_name()
    return render_template('homeCustomer.html',success='You have successfully booked a ticket.', name=name)


# helper function to create a random unique ticket_id
def generate_ticket_id():
    return f"T{uuid.uuid4().hex[:8]}"


# helper function to deal with calculating number of seats on the plane
def remainingSeats(flight_number, airline_name):
    cursor = conn.cursor()
    # find total number of seats in the airplane

    seat_num = '''
    SELECT a.seats - COUNT(t.ticket_id) AS seat_num
    FROM airplane a
    JOIN flight f ON f.airline_name = a.airline_name AND f.airplane_id = a.id
    LEFT JOIN ticket t ON t.flight_number = f.flight_number AND t.airline_name = f.airline_name
    WHERE f.flight_number = %s AND f.airline_name = %s
    '''
    cursor.execute(seat_num, (flight_number, airline_name))
    remaining_seats = cursor.fetchone()
    cursor.close()
    if remaining_seats['seat_num'] > 0:
        return True
    return False


# Route for showing the amount of money the customer has spent. Customer will enter a date range and result will be shown
@app.route('/trackSpending', methods=['POST'])
def trackSpending():
    email = session['email']
    cursor = conn.cursor()
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    # Query for customer spending in the past 6 months
    past_6months_query = '''
        SELECT SUM(t.ticket_price) AS total_spent
        FROM ticket t
        JOIN purchase p ON t.ticket_id = p.ticket_id
        WHERE p.email = %s AND t.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
    '''
    cursor.execute(past_6months_query, (email,))
    past_6months_spent = cursor.fetchone()['total_spent'] or 0
    # query for total spent in the past year
    past_year_query = '''
        SELECT SUM(t.ticket_price) AS total_spent
        FROM ticket t
        JOIN purchase p ON t.ticket_id = p.ticket_id
        WHERE p.email = %s AND t.purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    '''
    cursor.execute(past_year_query, (email,))
    past_year_spent = cursor.fetchone()['total_spent'] or 0
    choose_range = None
    # If the customer enters a start and end date, then we do an extra query
    if start_date and end_date:
        # Query for the specific date customer asks for 
        query = '''
            SELECT SUM(t.ticket_price) AS total_spent
            FROM ticket t
            JOIN purchase p ON t.ticket_id = p.ticket_id
            WHERE p.email = %s AND t.purchase_date BETWEEN %s AND %s
        '''
        cursor.execute(query, (email, start_date, end_date))
        choose_range = cursor.fetchone()['total_spent'] or 0
    cursor.close()
    # Bring customer to a new page and show them a table of their spend
    return render_template('trackSpending.html', past_6months_spent=past_6months_spent, past_year_spent=past_year_spent,
        choose_range=choose_range, start_date=start_date, end_date=end_date)


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
        AND purchase_date < DATE_SUB(CURDATE(), INTERVAL DAYOFMONTH(CURDATE()) - 1 DAY)
    '''
    cursor.execute(last_month_query, (airline_name,))
    last_month_rev = cursor.fetchone()['total_revenue'] or 0
    # Query to get revenue from the last year.
    last_year_query = '''
        SELECT SUM(ticket_price) AS total_revenue
        FROM ticket
        WHERE airline_name = %s
        AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
        AND purchase_date < CURDATE()
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
    try:
        query = '''INSERT INTO airport VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (code, name, city, country, number_of_terminals, type))
        conn.commit()
        cursor.close()
        return redirect(url_for('staffHome'))
    except:
        return render_template('homeStaff.html', error="One or more fields in adding airport were incorrect. Please reenter your information.")


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
    try:
        cursor.execute(query, (airplane_id, airline_name, seats, company, model_number, manufacture_date))
        conn.commit()
        cursor.close()
        return redirect(url_for('staffHome'))
    except:
        return render_template('homeStaff.html', error="One or more fields in adding airplane were incorrect. Please reenter your information.")


# Route for staff to view future flights (or past flights)
@app.route('/staffViewFlight', methods=['POST'])
def staffViewFlight():
    # get airline from session
    airline_name = session['airline_name']
    # get the rest of the info from the form
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    source = request.form['source']
    destination = request.form['destination']
    cursor = conn.cursor()
    default_query = '''
    SELECT flight_number, arrival_code, departure_code, departure_date, departure_time, arrival_time, arrival_date, base_price, flight_status
    FROM flight
    WHERE airline_name = %s
    '''
    filters = [airline_name]
    # if start date not specified, make default present
    if not start_date:
        default_query += " AND departure_date >= NOW()"
    else:
        default_query += " AND departure_date >= %s"
        filters.append(start_date)
    # if end date not specified, make default 30 days
    if not end_date:
        default_query += " AND departure_date <= DATE_ADD(CURRENT_DATE(), INTERVAL 30 DAY)"
    else:
        default_query += " AND departure_date <= %s"
        filters.append(end_date)

    # if source is given, use it to filter query
    if source:
        default_query += " AND departure_code = %s"
        filters.append(source)

    # if destination airport is given, use to filter query
    if destination:
        default_query += " AND arrival_code = %s"
        filters.append(destination)

    cursor.execute(default_query, filters)
    flights = cursor.fetchall()
    cursor.close()
    return render_template('staffFlights.html', flights=flights)


# Route for the customer to be able to view their upcoming flights, to click the button, it should bring them to the next page
@app.route('/viewFlight', methods=['POST'])
def viewFlight():
    # get the customer's email to determine what they've bought
    email = session['email']
    cursor = conn.cursor()  # add arrival and departure code
    flights_query = '''
    SELECT f.flight_number, f.airline_name, f.departure_date, f.departure_time, f.arrival_time, f.arrival_date, f.base_price, f.flight_status, t.ticket_id
    FROM purchase p
    JOIN ticket t ON p.ticket_id = t.ticket_id
    JOIN flight f ON f.flight_number = t.flight_number
    WHERE p.email = %s AND (f.departure_date > CURDATE() OR (f.departure_date = CURDATE() AND f.departure_time > CURTIME()))

    '''
    cursor.execute(flights_query, (email))
    flights = cursor.fetchall()
    cursor.close()
    # result is sent to the page
    return render_template('viewFlights.html', flights=flights)


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


# Route for airline staff to view flights a customer has taken
@app.route('/viewCustomer', methods=['POST'])
def viewCustomer():
    # get the customer info and airline name
    airline_name = session['airline_name']
    email = request.form['email']
    cursor = conn.cursor()
    # query to get customer full name for display
    customer_name_query = '''
        SELECT first_name, last_name
        FROM customer
        WHERE email = %s
    '''
    cursor.execute(customer_name_query, (email,))
    customer = cursor.fetchone()
    if not customer:
        error = "Customer not found."
        cursor.close()
        return render_template('viewCustomer.html', error=error)
    # query to get flight info
    flight_info_query = '''
        SELECT f.flight_number, f.departure_date, f.arrival_date, f.departure_code, f.arrival_code
        FROM purchase p
        JOIN ticket t ON p.ticket_id = t.ticket_id
        JOIN flight f ON t.flight_number = f.flight_number AND t.airline_name = f.airline_name
        WHERE p.email = %s AND f.airline_name = %s
    '''
    cursor.execute(flight_info_query, (email, airline_name))
    flights = cursor.fetchall()
    cursor.close()
    # display info on new page
    return render_template('viewCustomer.html', customer=customer, flights=flights)


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


# Route for the airline staff to schedule a maintenance for the plane, staff needs to input the data
@app.route('/scheduleMaintenance', methods=['POST'])
def scheduleMaintenance():
    # Get the info that the staff inputs
    airline_name = request.form['airline_name']
    airplane_id = request.form['airplane_id']  # add a case where airplane doesn't exist?
    maintenance_start = request.form['start_date']
    maintenance_end = request.form['end_date']
    cursor = conn.cursor()
    # Do the SQL insert with the data provided
    query = '''INSERT INTO maintenance VALUES (%s, %s, %s, %s)'''
    try:
        cursor.execute(query, (airplane_id, airline_name, maintenance_start, maintenance_end))
        conn.commit()
        cursor.close()
        return redirect(url_for('staffHome'))
    except:
        return render_template('homeStaff.html', error="One or more fields in scheduling maintenance were incorrect. Please reenter your information.")


# route for airline staff to view customers on a given flight
@app.route('/viewRoster', methods=['POST'])
def viewRoster():
    airline_name = session['airline_name']
    flight_number = request.form['flight_number']
    cursor = conn.cursor()
    query = '''
    SELECT c.first_name, c.last_name, c.email, t.ticket_id
    FROM ticket t
    JOIN purchase p on t.ticket_id = p.ticket_id
    JOIN customer c on c.email = p.email
    WHERE t.airline_name = %s AND t.flight_number = %s
    '''
    cursor.execute(query, (airline_name, flight_number))
    customer_info = cursor.fetchall()
    cursor.close()
    return render_template('flightRoster.html', flight_number=flight_number, customer_info=customer_info)


# Route for the airline staff to add a flight
@app.route('/createFlight', methods=['POST'])
def createFlight():
    # Grab the info the staff enters
    flight_number = request.form['flight_number']
    airplane_id = request.form['airplane_id']
    departure_code = request.form['departure_code']
    arrival_code = request.form['arrival_code']
    departure_date = request.form['departure_date']
    departure_time = request.form['departure_time']
    arrival_date = request.form['arrival_date']
    arrival_time = request.form['arrival_time']
    base_price = request.form['base_price']
    airline_name = session['airline_name']
    # We are going to assume that the flight created starts out on time
    flight_status = 'on_time'
    cursor = conn.cursor()
    # check to make sure that the airports exist
    airport_check_query = '''SELECT code FROM airport WHERE code IN (%s, %s)'''
    cursor.execute(airport_check_query, (departure_code, arrival_code))
    airports = cursor.fetchall()
    if len(airports) < 2:  # Both departure and arrival codes must exist
        cursor.close()
        missing_airports = []
        if not any(a['code'] == departure_code for a in airports):
            missing_airports.append(departure_code)
        if not any(a['code'] == arrival_code for a in airports):
            missing_airports.append(arrival_code)
        error_message = f"The following airports are missing: {', '.join(missing_airports)}. Please add them before creating a flight."
        return render_template('staffError.html', error_message=error_message)
    # check to make sure airplane exists
    airplane_check_query = '''SELECT id FROM airplane WHERE id = %s AND airline_name = %s'''
    cursor.execute(airplane_check_query, (airplane_id, airline_name))
    airplane = cursor.fetchone()
    if not airplane:
        cursor.close()
        error_message = f"The airplane with ID {airplane_id} does not exist for your airline. Please add it before creating a flight."
        return render_template('staffError.html', error_message=error_message)
    query = '''INSERT INTO flight VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (
            flight_number, airline_name, arrival_code, departure_code, airplane_id,
            departure_date, departure_time, flight_status,
            arrival_date, arrival_time, base_price
        ))
    conn.commit()
    cursor.close()
    return redirect(url_for('staffHome'))


# General things:
# 1) measures to prevent cross-site scripting vulnerabilities (if we haven't already)
# should use the function thing dey mentioned that cleans text
# 2) other prevention included in Enforcing complex constraints (if we haven't already)


app.secret_key = 'some key that you will never guess'
# Run the app on localhost port 5000
debug = True  # -> you don't have to restart flask
# for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
