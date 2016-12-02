# Creating menu with different options for customer

customer = 0
while customer >= 0:
    print '========================='
    print '1. Returning Customer'
    print '2. New Customer'
    print '3. Guest'
    print '========================= \n'

    customer = int(raw_input('Please Select Your Customer Type:  \n'))
    try:
        if customer < 1 or customer > 3:
            customer = int(raw_input('Please Select Your Customer Type Number 1, 2, or 3:  '))
        elif customer == 1:
            print 'Welcome Back, Returning Customer'
            customer = -1
        elif customer == 2:
            print 'Welcome to the Coffee Kiosk New Customer'
            customer = -1
        elif customer == 3:
            print 'Welcome to the Coffee Kiosk Guest'
            customer = -1
        else:
            print 'Enter Your Customer Type Number, 1, 2, or 3'
    except ValueError:
        print 'Enter Your Customer Type Number, 1, 2, or 3'
