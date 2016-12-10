import logging
import boto3

from dotenv import load_dotenv, find_dotenv
from base64 import b64decode

from chalice import Chalice, BadRequestError
from chalicelib import delivery, payment, promo, auth, tracking

app = Chalice(app_name='chefit-api')
app.log.setLevel(logging.DEBUG)
app.debug = True


# Process environment variables
de = find_dotenv()
if de is not None:
    load_dotenv(de)


###################################
#          Tracking APIs          #
###################################

@app.route('/api/track/{event_type}', methods=['PUT'], cors=True)
def track(event_type):
    state = tracking.process_request(app.current_request.json_body)
    tracking.push_event(event_type, state)
    return {'Ok'}


###################################
#            Cart APIs            #
###################################

@app.route('/api/cart/validate-promo', methods=['PUT'], cors=True)
def validate_promo():
    return {'Ok'}


@app.route('/api/cart/shipping-cost', methods=['POST'], cors=True)
def get_shipping_cost():
    return {'Ok'}


###################################
#          Payment APIs           #
###################################

@app.route('/api/pay', methods=['POST'], cors=True)
def update_cart():
    claims = app.current_request.claims
    state = payment.process_request(app.current_request.json_body)
    if state is None:
        raise BadRequestError

    result = payment.process_payment(state)
    return {'Ok'}
