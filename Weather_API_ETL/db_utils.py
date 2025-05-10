from pymongo import MongoClient
import config

def get_database():
    """Connects to the MongoDB database and returns the database object."""
    connection_string = config.get_connection()
    client = MongoClient(connection_string)
    return client.weather_db

def save_current_weather(weather_data):
    db = get_database()
    current_weather_collection = db.current_weather
    try:
        result = current_weather_collection.insert_one(weather_data['current'])
        return result.inserted_id
    except Exception as e:
        print(f"Error saving current weather data: {e}")
        return None
    finally:
        db.client.close()

def save_forecast_weather(forecast_data, day, hour):
    """Saves forecast weather data for a specific day to the 'forecast_weather' collection."""
    db = get_database()
    forecast_weather_collection = db.forecast_weather
    try:
        forecast_hour_data = forecast_data['forecast']['forecastday'][day]['hour'][hour]
        forecast_weather_collection.insert_one(forecast_hour_data)
        
    except IndexError:
        return None
    except Exception as e:
        return None
    finally:
        db.client.close()
