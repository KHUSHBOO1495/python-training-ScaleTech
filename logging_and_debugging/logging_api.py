import logging
import requests
import pandas as pd

logging.basicConfig(
    filename="api_app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

url = "https://jsonplaceholder.typicode.com/users"
logger.info("Starting API request")

try:

    response = requests.get(url, timeout=10)
    logger.info("API response received with status code %s",
                response.status_code)
    response.raise_for_status()

    data = response.json()
    logger.info("JSON response parsed successfully")

    df = pd.json_normalize(data)
    logger.info("Created DataFrame with %s rows", len(df))

    df.to_csv("users_api_data.csv", index=False)
    logger.info("Data saved successfully")

except requests.exceptions.RequestException:
    logger.exception("API request failed")