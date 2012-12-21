def run(num_orders):
    urls = open('urls', 'w')
    for i in xrange(num_orders):
        urls.write('http://localhost:5000/push?order_id=' + str(i) + '\n')

