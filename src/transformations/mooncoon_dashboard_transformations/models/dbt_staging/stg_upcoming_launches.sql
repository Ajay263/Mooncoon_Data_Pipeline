with source as (

    select * from {{ source('mooncon_rocket_data', 'raw_upcoming_launches') }}

),

renamed as (

    select
            
    id,
    name,
    status__name,
    status__description,
    last_updated,
    net,
    window_end, 
    window_start,
    launch_service_provider__name,
    launch_service_provider__total_launch_count,
    launch_service_provider__failed_launches,
    launch_service_provider__pending_launches,
    launch_service_provider__successful_landings,
    launch_service_provider__country_code,
    launch_service_provider__founding_year,
    launch_service_provider__failed_landings,
    launch_service_provider__info_url,
    launch_service_provider__wiki_url,	
    launch_service_provider__launchers,
    launch_service_provider__spacecraft,
    launch_service_provider__image_url,
    rocket__configuration__leo_capacity,																							
    rocket__configuration__image_url,
    rocket__configuration__name,
    rocket__configuration__description,
    rocket__configuration__family,
    rocket__configuration__manufacturer__country_code,
    rocket__configuration__manufacturer__description,
    rocket__configuration__manufacturer__administrator,
    rocket__configuration__manufacturer__founding_year,
    rocket__configuration__manufacturer__launchers,  
    rocket__configuration__manufacturer__spacecraft,
    rocket__configuration__manufacturer__total_launch_count,
    rocket__configuration__manufacturer__successful_launches,
    rocket__configuration__manufacturer__failed_launches,                                           
    mission__name,
    mission__description, 
    mission__type, 
    mission__orbit__id, 
    mission__orbit__name, 
    mission__orbit__abbrev,
    pad__name,
    pad__map_url,
    pad__wiki_url,
    pad__location__url,
    pad__location__name,
    pad__location__country_code, 
    pad__location__map_image, 
    pad__location__total_launch_count,
    pad__location__total_landing_count, 
    pad__country_code,
    pad__map_image, 
    pad__total_launch_count, 
    pad__orbital_launch_attempt_count,
    image, 
    orbital_launch_attempt_count, 
    location_launch_attempt_count, 
    pad_launch_attempt_count, 
    agency_launch_attempt_count, 
    orbital_launch_attempt_count_year,
    location_launch_attempt_count_year, 
    pad_launch_attempt_count_year, 
    agency_launch_attempt_count_year,
    pad_turnaround, 
    type
    from source

)

select * from renamed 
 
 
 
 
















