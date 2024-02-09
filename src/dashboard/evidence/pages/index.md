---
title: Upcoming launches 
---



_A dashboard that shows us all the Upcoming Rocket Launches_

<br>

<br> 

```sql card_data1
select 
  time_remaining,
  status_value,
  last_updated,
  rocket__configuration__image_url,
  description,
  pad__location__name,
  mission__name
from mooncoon_server.obt
```


{#each card_data1 as card_data}

<div class="card-container" style="max-width: 550px; border: 2px solid #007bff; border-radius: 20px; overflow: hidden; background-color: #f8f9fa; box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);">
  <!-- Image Section on the Left -->
  <div class="card-image" style="position: relative;">
  <a href="#" class="btn" style="position: absolute; top: 20px; right: 20px; background-color: #007bff; color: #fff; text-decoration: none; padding: 10px 20px; border-radius: 30px; font-weight: bold;">{card_data.status_value}</a>

</div>



  <!-- Text Details on the Right -->
<div class="card-details" style="padding: 10px;">   
    <h5 class="card-title" style="margin-bottom: 10px; color: #007bff; font-size: 24px;"> <Value data={card_data} column=mission__name  /></h5>


  <img src="{card_data.rocket__configuration__image_url}" class="card-img-top" alt="Launch Image" style="width: 90%; border-top-left-radius: 20px; border-bottom-left-radius: 20px;"><i>Last updated <Value data={card_data} column=last_updated  fmt='fulldate'/></i>

<br>
<br>

    <!-- Time Details -->
    <div class="card-section" style="margin-bottom: 20px;">
      <h6 style="color: #007bff; font-size: 16px;">Time Remaining:</h6>
      <p style="font-size: 14px; margin-top: 4px;"><Value data={card_data} column=time_remaining  fmt='hms'/></p>      
    </div>

    <!-- Date Details -->
    <div class="card-section" style="margin-bottom: 20px;">
      <h6 style="color: #007bff; font-size: 16px;">Date:</h6>
      <p style="font-size: 14px; margin-top: 4px;"><Value data={card_data} column=time_remaining  fmt='fulldate'/></p>
    </div>

    <!-- Location Details -->
    <div class="card-section" style="margin-bottom: 10px;">
      <h6 style="color: #007bff; font-size: 16px;">Location:</h6>
      <p style="font-size: 14px; margin-top: 4px;"><Value data={card_data} column=pad__location__name  /></p>
    </div>
  </div>
  <!-- Map Section at the Bottom -->
  <div class="card-footer" style="clear: both; padding: 10px; background-color: #fff;">
    <h6 style="color: #007bff; font-size: 16px; margin-bottom: 10px;">Description:</h6>
    <p><Value data={card_data} column=description  /></p>
   
  </div>
</div>

<br>

<br>

{/each}








# Created by

- Alexio Junior Aaron on [Github](https://github.com/Ajay263)