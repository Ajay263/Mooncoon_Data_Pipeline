select
    stg_upcoming_launches.id  as Mission_id,
    stg_upcoming_launches.mission__name  as Mission_Name,
    stg_upcoming_launches.mission__description as Mission_Description,
    stg_upcoming_launches.mission__type as Mission_type,
    stg_upcoming_launches.mission__orbit__name as Orbit
from {{ ref('stg_upcoming_launches') }}