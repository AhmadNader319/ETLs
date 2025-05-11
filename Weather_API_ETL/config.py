def get_api_key():
    return "YOUR_API_KEY"

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
    connection_string = "mongodb+srv://<username>:<password>@form-cluster.a4uuarh.mongodb.net/?retryWrites=true&w=majority&appName=YOUR-CLUSTER-NAME"
    return connection_string
