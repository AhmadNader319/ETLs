import requests
import config
import db_utils
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("weather_app.log"),
        logging.StreamHandler()
    ]
)

api_key = config.get_api_key()
base_url = config.get_base_url()
api_endpoints = config.get_api_endpoints()

def get_forecast_weather_data(query):
    url = f"{base_url}/forecast.json?key={api_key}&q={query}&days=4"
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Forecast weather data fetched successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching forecast weather data: {e}")
        return None
    except Exception as e:
        logging.exception("Unexpected error in forecast data fetching.")
        return None

def get_current_weather_data(query):
    url = f"{base_url}/current.json?key={api_key}&q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Current weather data fetched successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching current weather data: {e}")
        return None
    except Exception as e:
        logging.exception("Unexpected error in current data fetching.")
        return None

if __name__ == "__main__":
    try:
        logging.info("Starting weather data fetch and save sequence...")

        current_weather_data = get_current_weather_data('Egypt')
        weather_snapshot_hour = 13
        if current_weather_data:
            logging.info("Saving current weather data to the database...")
            db_utils.save_current_weather(current_weather_data)
        else:
            logging.warning("No current weather data to save.")

        forecast_weather_data = get_forecast_weather_data('Egypt')
        if forecast_weather_data:
            logging.info("Saving forecast weather data to the database...")
            for day in range(1, 4):
                db_utils.save_forecast_weather(forecast_weather_data, day, weather_snapshot_hour)
        else:
            logging.warning("No forecast weather data to save.")

    except ValueError as ve:
        logging.error(f"Value error occurred: {ve}")
    except Exception as e:
        logging.exception("Unexpected error occurred in the main section.")
