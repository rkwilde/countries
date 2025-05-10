-- ran in snowflake to schedule first super-simple transform
create task countries_transform
    warehouse = compute_wh
    schedule = '24 hours'
    as
        create or replace table aptive.staging.countries as
            select
                raw:name:common::varchar as country_name,
                raw:independent::boolean as independent,
                raw:unMember::boolean as united_nations_member,
                raw:capital[0]::varchar as capital,
                raw:region::varchar as country_region,
                raw:subregion::varchar as country_subregion,
                raw:population::integer as population
            from aptive.raw.countries
