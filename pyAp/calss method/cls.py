def nameFeeder():
    while True:
        fname = yield
        print('First Name:', fname)
        lname = yield
        print('Last Name:', lname)

n = nameFeeder()
next(n)
n.send('George')
n.send('Williams')
n.send('John')
