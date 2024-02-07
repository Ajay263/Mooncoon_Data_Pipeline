with source as (

select   
 dim_launch_service_provider.Launch_Service_Provider_id,
 dim_mission.Mission_id,
 dim_pad.Pad_id,
 dim_rocket_config.Rocket_config_id,
 stg_upcoming_launches.id ,
 stg_upcoming_launches.name,
 stg_upcoming_launches.status__description,
 stg_upcoming_launches.last_updated,
 stg_upcoming_launches.net,
 stg_upcoming_launches.launch_service_provider__name,
 stg_upcoming_launches.launch_service_provider__total_launch_count,
 stg_upcoming_launches.rocket__configuration__image_url,
 stg_upcoming_launches.rocket__configuration__description,
 stg_upcoming_launches.mission__name,
 stg_upcoming_launches.mission__description,
 stg_upcoming_launches.pad__map_url,
 stg_upcoming_launches.launch_service_provider__country_code,
 stg_upcoming_launches.launch_service_provider__wiki_url,
 stg_upcoming_launches.pad__location__url,
 stg_upcoming_launches.pad__location__name,
 stg_upcoming_launches.status__abbrev  as  Status_value

    
from {{ ref('stg_upcoming_launches') }}  
left join  {{ ref('dim_launch_service_provider') }} 
on stg_upcoming_launches.id = dim_launch_service_provider.Launch_Service_Provider_id

left join  {{ ref('dim_mission') }} 
on stg_upcoming_launches.id = dim_mission.Mission_id


left join  {{ ref('dim_pad') }} 
on stg_upcoming_launches.id = dim_pad.Pad_id


left join  {{ ref('dim_rocket_config') }} 
on stg_upcoming_launches.id = dim_rocket_config.Rocket_config_id


),
unique_source as (

    select*,
           row_number() over(partition by id) as row_number
    from source
)
select*
from unique_source
where row_number=1