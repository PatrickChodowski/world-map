
<script>
  import { SERVER_URL, show_spinner } from './stores'
  import { geoMercator, geoPath } from "d3-geo";
  import { feature } from "topojson";
  import { onMount } from "svelte";


  export let country = "Poland";
  
  let show_map = true;
  let map_data = "";
  let features = [];

  const projection = geoMercator();
  const geo_generator = geoPath().projection(projection);


  async function post_data() {

    if(country === ""){
      show_map = false;
    } else {
      show_map = true;
    }

    // show_spinner = true;
    const res = await fetch(`${SERVER_URL}/select`, 
                            {method:"POST", 
                            headers: {"Content-type": "application/json"}, 
                            body: JSON.stringify({"country": country})});
    // show_spinner = false;
    if (res.status === 200){
      let resdata = await res.json();
      map_data = resdata.data;
      features = map_data.features;
      return map_data;
    } else {
      return "";
    }
  }


  onMount(async function() {post_data()});

  // something not working here
  // https://bost.ocks.org/mike/map/


</script>
<input type="text" id="input-country" placeholder="Country" bind:value={country} on:change={() => post_data()}>

{#if show_map}
  <svg viewBox="0 0 975 610">
    <g fill="white" stroke="black">
      {#each features as feature, i}
        <!-- <path d={path(feature)} on:click={() => selected = feature} class="state" in:draw={{ delay: i * 50, duration: 1000 }} /> -->
          <path d={geo_generator(feature)}></path>
      {/each}
    </g>
  </svg>
{/if}


<style>

  #input-country {
    width:500px;
  }

</style>
