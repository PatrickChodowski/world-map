<script>
   import { country, get_map_data  } from './stores'
</script>

<input type="text" 
       id="input-country" 
       placeholder="Country" 
       bind:value={$country} 
       on:change={() => get_map_data()}>


<style>
  #input-country {
    width:500px;
    margin-bottom: 10px;
  }
</style>
