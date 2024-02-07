from dagster import Definitions
from .assets import launches_pipeline
from .resources import DltResource

defs = Definitions(
    assets=[launches_pipeline],
    resources={
        "pipeline": DltResource(
            pipeline_name = "upcoming_launches_datapipeline",
            dataset_name = "mooncoon_rocket_dataset",
            destination = "postgres",
        ),
    }
)

