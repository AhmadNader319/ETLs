import requests
import config

api_key = config.get_api_key()
base_url = config.get_base_url()
api_endpoints = config.get_api_endpoints()

def get_weather_data(query, method="current"):
    if method not in api_endpoints:
        raise ValueError(f"Invalid API method: {method}. Available methods are: {', '.join(api_endpoints.keys())}")

    url = f"{base_url}{api_endpoints[method]}?key={api_key}&q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    try:
        current_weather = get_weather_data("Egypt")
        if current_weather:
            print("Current Weather in Egypt:")
            print(current_weather['location'])
            print(current_weather['current'])

        forecast_weather = get_weather_data("Egypt", method="forecast")
        if forecast_weather and 'forecast' in forecast_weather:
            print("\nForecast for Cairo:")
            print(forecast_weather['location'])
            print(forecast_weather['forecast']['forecastday'][0]['day'])

        search_results = get_weather_data("Cair", method="search")
        if search_results:
            print("\nSearch Results for Egypt:")
            for result in search_results:
                print(result['name'], result['region'], result['country'])

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred in the main section: {e}")


"""
Current Weather in Egypt:
{'name': 'Cairo', 'region': 'Al Qahirah', 'country': 'Egypt', 'lat': 30.05, 'lon': 31.25, 'tz_id': 'Africa/Cairo', 'localtime_epoch': 1746753862, 'localtime': '2025-05-09 04:24'}
"""
