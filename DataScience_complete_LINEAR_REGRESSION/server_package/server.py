from flask import Flask, request, jsonify
import util

app = Flask(__name__)


# write the routine
@app.route("/show_locations_names", methods=['GET'])
def show_locations_names():
    response = jsonify({
        'locations': util.show_location_names()
    })
    response.headers.add("Access-control-Allow-Origin", "*")
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    room_size = int(request.form['room-size'])

    response = jsonify({
        'estimated_price': util.show_estimated_price(location, total_sqft, bath, room_size)
    })
    return response


if __name__ == "__main__":
    print("Start up my Python Flask Server For Home Price Prediction...")
    util.load_server_effects()
    app.run()
