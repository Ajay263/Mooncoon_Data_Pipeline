import os
from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import mooncoon_dashboard_transformations_dbt_assets, raw_upcoming_launches_data
from .constants import dbt_project_dir
from .schedules import schedules

defs = Definitions(
    assets=[raw_upcoming_launches_data,mooncoon_dashboard_transformations_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)












