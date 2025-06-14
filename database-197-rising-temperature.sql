# Write your MySQL query statement below
with temp_weather as (
    select 
Weather.id, Weather.recordDate, Weather.temperature, LAG(Weather.temperature) over (order by recordDate) as prev_day_value 
from Weather
)
select id 
from temp_weather 
where prev_day_value is not null and temperature > prev_day_value;
