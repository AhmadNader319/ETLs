def get_api_key():
    return "YOUR_ACTUAL_API_KEY"

def get_base_url():
    return "http://api.weatherapi.com/v1"

def get_api_endpoints():
    return {
        "current": "/current.json",
        "forecast": "/forecast.json",
        "search": "/search.json",
        "history": "/history.json"
    }
