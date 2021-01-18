import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def show_estimated_price(locations, sqft, bath, room_size):
    try:
        loc_index = __data_columns.index(locations.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = room_size
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def show_locations_names():
    return __locations


def load_server_effects():
    print("loading the server effects... starting now")
    global __data_columns
    global __locations


    with open("./server_effects/bengluru_columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open("./server_effects/bengluru_home_price_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading server effects ... done")


if __name__ == "__main__":
    load_server_effects()
    print(show_locations_names())
    print(show_estimated_price("1st block jayanagar", 1000, 3, 3)) # other locations
    print(show_estimated_price("1st phase jp nagar", 1000, 2, 2)) # other locations
    print(show_estimated_price("2nd phase judicial layout", 1000, 2, 2))  # other locations
    print(show_estimated_price("2nd stage nagarbhavi", 1000, 3, 3))  # other locations
