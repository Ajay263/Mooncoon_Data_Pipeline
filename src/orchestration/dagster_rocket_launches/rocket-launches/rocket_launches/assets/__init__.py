from dagster import asset, get_dagster_logger
from ..resources import DltResource
from ..dlt import Rocketapi_resource

@asset
def launches_pipeline(pipeline: DltResource):

    logger = get_dagster_logger()
    results = pipeline.create_pipeline(Rocketapi_resource)
    logger.info(results)