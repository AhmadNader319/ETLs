def get_api_key():
    return "2b2ccf51b4784a65aa100305250905"

def get_base_url():
    return "http://api.weatherapi.com/v1"

def get_api_endpoints():
    return {
        "current": "/current.json",
        "forecast": "/forecast.json",
        "search": "/search.json"
    }
def get_current_day():
    return {
        "day1": 5,
        "day2": 6,
        "day3": 7
    }
def get_connection():
    connection_string = "mongodb+srv://ahmadnader2:4kpOAgC8yqXJU6Hq@form-cluster.a4uuarh.mongodb.net/?retryWrites=true&w=majority&appName=Form-Cluster"
    return connection_string
