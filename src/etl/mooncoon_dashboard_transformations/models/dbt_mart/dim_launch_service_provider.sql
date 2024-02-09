with source as (

select   

    stg_upcoming_launches.id as Launch_Service_Provider_id,
    stg_upcoming_launches.launch_service_provider__name   as Launch_SP_Name,
    stg_upcoming_launches.launch_service_provider__country_code as Country,
    stg_upcoming_launches.launch_service_provider__founding_year as Founding_Year,
    stg_upcoming_launches.launch_service_provider__launchers as Launchers,
    stg_upcoming_launches.launch_service_provider__spacecraft as Spacecraft,
    stg_upcoming_launches.launch_service_provider__total_launch_count as Launch_Count,
    stg_upcoming_launches.launch_service_provider__failed_launches as Failed_Launches,
    stg_upcoming_launches.launch_service_provider__pending_launches as Pending_Launches,
    stg_upcoming_launches.launch_service_provider__successful_landings as Successful_Landings,
    stg_upcoming_launches.launch_service_provider__failed_landings as Failed_Landings,
    stg_upcoming_launches.launch_service_provider__info_url  as Info_Url,
    stg_upcoming_launches.launch_service_provider__image_url as Image_Url,
    stg_upcoming_launches.status__abbrev  as Status
    
from {{ ref('stg_upcoming_launches') }}

),
unique_source as (

    select*,
           row_number() over(partition by Launch_Service_Provider_id) as row_number
    from source
)
select*
from unique_source
where row_number=1