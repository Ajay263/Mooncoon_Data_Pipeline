select

    
    stg_upcoming_launches.id as Pad_id,
    stg_upcoming_launches.pad__name  as Pad_Name,
    stg_upcoming_launches.pad__wiki_url as Wiki_Url,
    stg_upcoming_launches.pad__map_url as Map_url,
    stg_upcoming_launches.pad__location__url as Location_Url,
    stg_upcoming_launches.pad__location__name as Location_name,
    stg_upcoming_launches.pad__location__country_code as Country,
    stg_upcoming_launches.pad__location__map_image as Map_image,
    stg_upcoming_launches.pad__location__total_launch_count as Total_Launch_Count,
    stg_upcoming_launches.pad__country_code as Total_Landings_Count
     

from {{ ref('stg_upcoming_launches') }}