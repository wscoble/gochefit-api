import logging

from chalice import Chalice
from chalicelib import delivery

app = Chalice(app_name='chefit-api')
app.log.setLevel(logging.DEBUG)
app.debug = True

@app.route('/api/track', methods=['PUT'], cors=True)
def track():
    return 'Ok'

@app.route('/api/delivery-days/{date}', methods=['GET'], cors=True)
def get_delivery_days(date):
    return delivery.get_days(date)

@app.route('/api/ping')
def ping():
    return 'Pong!'

# The view function above will return {"hello": "world"}
# whenver you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.json_body
#     # Suppose we had some 'db' object that we used to
#     # read/write from our database.
#     # user_id = db.create_user(user_as_json)
#     return {'user_id': user_id}
#
# See the README documentation for more examples.
#
