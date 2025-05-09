# Weather Data Fetcher

This Python script fetches weather information using the WeatherAPI.com.

## Features

* Fetches current weather data for a specified location (JSON format).
* Retrieves 7-day weather forecasts for a specified location (JSON format).
* Searches for locations based on a query (e.g., cities starting with a specific string) (JSON format).
* Configuration (API key, base URL, API endpoints) is managed in a separate `config.py` file for better organization.
* Includes basic error handling for API requests.

## Prerequisites

* Python 3.x
* `requests` library (Install using: `pip3 install requests`)
* A valid API key from WeatherAPI.com. You can sign up for a free API key [here](https://www.weatherapi.com/).

## Setup

1.  **Clone the repository** or create the following files: `main.py` and `config.py`.

2.  **Create or modify `config.py`:**

    ```python3
        
    def get_api_key():
        return "YOUR_ACTUAL_API_KEY"
    ```

    * **Important:** Replace `"YOUR_ACTUAL_API_KEY"` with your actual WeatherAPI.com API key.

3.  **Create or modify `main.py`:**

## Usage

1.  Ensure you have installed the required libraries.
2.  Make sure you have a valid API key in your `config.py` file.
3.  Run the `main.py` script: `python3 main.py`

The script will then fetch and display:

* Current weather information for Egypt.
* A day weather forecast for Cairo.
* Search results for cities starting with "Cair".

You can modify the `if __name__ == "__main__":` block in `main.py` to query different locations or use other API methods.

## Next Steps: Building a Comprehensive Weather Data Pipeline

This script provides a basic framework for interacting with the WeatherAPI. To build a more comprehensive and robust weather data pipeline, consider the following:

1.  **Understanding the Source (The Weather API):** Analyze the API's response structure and identify specific weather data points needed.
