<script>
   import { country, get_map_data, highlighted_element_data, show_cities, show_rivers } from './stores'
</script>

<div id='main-panel'>
  <input type="text" 
        id="input-country" 
        placeholder="Country" 
        bind:value={$country} 
        on:change={() => get_map_data()}>

  <label for="input-show-cities">Show cities?</label>
  <input type="checkbox" id="input-show-cities" bind:checked={$show_cities} on:change={() => get_map_data()}>

  <label for="input-show-rivers">Show rivers?</label>
  <input type="checkbox" id="input-show-rivers" bind:checked={$show_rivers} on:change={() => get_map_data()}>


  {#if $highlighted_element_data['name'] !== undefined}
    <p id="info-box">{$highlighted_element_data['name']}</p>
  {/if}

</div>


<style>
  #info-box {
    display: inline;
  }

  #input-country {
    width:500px;
    margin-bottom: 10px;
    display: inline;
  }
</style>
