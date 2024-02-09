from dagster import define_asset_job, ScheduleDefinition
from dagster import AssetSelection

schedules=[
ScheduleDefinition(
    job=define_asset_job(
        name="Hourly",
        selection=AssetSelection.all()   
    ),
     cron_schedule="@hourly",
)

]