from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from dagster import AssetExecutionContext, asset
from dagster_dbt import DbtCliResource, dbt_assets
from dagster import define_asset_job, ScheduleDefinition
from dagster_dbt import build_dbt_asset_selection, dbt_assets
from .constants import dbt_manifest_path, dbt_project_dir
from .constants import dbt_manifest_path
from dagster import AssetSelection
from dlt.sources.helpers import requests
from datetime import datetime, timedelta
import json
from datetime import datetime, timedelta
from datetime import datetime, timedelta
import pandas as pd
import dlt
import os
from dagster_dbt import dbt_assets, build_dbt_asset_selection

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
        net_filters = f'net_gte={now.isoformat()}&net_lte={month_from_now.isoformat()}'
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

        if results is None:
            print("No results returned from the API.")
            return
        for result in results:
            if result['id'] is not None: 
                yield result
            else:
                print("Skipped an entry with null 'id'.")

    except Exception as e:
        print(f"An error occurred while fetching data from the API: {e}")
        return

def get_results(query_url: str):
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
            status = response.status_code
            print(f'Status code: {status}')
            if status != 200:
                print(f"Unexpected status code: {status}")
                return None

            data = response.json()
            for item in data['results']:
                yield item
            query_url = data['next']

@asset(compute_kind="python")
def raw_upcoming_launches_data(context: AssetExecutionContext) -> None:
    """
    Fetches upcoming launches data and loads it into a PostgreSQL database.

    """
    try:
        pipeline = dlt.pipeline(
            pipeline_name='upcoming_launches_datapipeline',
            destination='postgres',
            dataset_name='mooncoon_rocket_dataset'
        )
        load_info = pipeline.run(Rocketapi_resource())
        print(load_info)

    except Exception as e:
        print(f"An error occurred while fetching data: {e}")




@dbt_assets(manifest=dbt_manifest_path)
def mooncoon_dashboard_transformations_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()