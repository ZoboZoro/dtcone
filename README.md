# dtcone

##

```sql
SELECT COUNT(*) FROM green_taxi 
    WHERE trip_distance <= 1 
    AND lpep_pickup_datetime < '2025-12-01';


SELECT trip_distance, lpep_pickup_datetime FROM green_taxi
    WHERE trip_distance < 100
    ORDER BY trip_distance DESC;
```