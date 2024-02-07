import dlt
from dlt.sources.helpers import requests
from datetime import datetime, timedelta
import json

@dlt.resource(table_name="raw_upcoming_launches", write_disposition="merge", primary_key="id")
def Rocketapi_resource():
    """
    This function fetches upcoming rocket launches data from the API and yields the results.
    The data is filtered to include launches within the next 31 days.
    The results are ordered by ascending T-0 (NET).
    """
    try:
        launch_base_url = 'https://lldev.thespacedevs.com/2.2.0/launch/'

        now = datetime.now()
        month_from_now = now + timedelta(days=31)

        net_filters = f'net__gte={now.isoformat()}&net__lte={month_from_now.isoformat()}'

        filters = net_filters

        #Including all related objects
        mode = 'mode=detailed'

        # Limit returned results to just 2 per query 
        limit = 'limit=14'

        # Ordering the results by ascending T-0 (NET)
        ordering = 'ordering=net'

        query_url = launch_base_url + '?' + '&'.join((filters, mode, limit, ordering))
        print(f'query URL for upcoming launches: {query_url}')

        results = get_results(query_url)

        # Checking if the query was  successful
        if results is None:
            print("No results returned from the API.")
            return

        # Yielding the extracted data
        for result in results:
            if result['id'] is not None:  # Check if 'id' is not None
                yield result
            else:
                print("Skipped an entry with null 'id'.")

    except Exception as e:
        print(f"An error occurred while fetching data from the API: {e}")
        return


def get_results(query_url: str) -> dict or None:
    """
    This function sends a GET request to the provided URL and yields the results.
    It handles pagination if the API returns multiple pages of results.
    """
    while query_url:
        try:
            response = requests.get(query_url, stream=True)
            response.raise_for_status()
        except Exception as e:
            print(f'Exception: {e}')
            return None
        else:
            # Checking status of the query
            status = response.status_code
            print(f'Status code: {status}')

            # Return when the query status isn't 200 OK
            if status != 200:
                print(f"Unexpected status code: {status}")
                return None

            # Extract relevant data from the response
            data = response.json()
            for item in data['results']:
                yield item

            # Get the next page URL
            query_url = data['next']