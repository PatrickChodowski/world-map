
<script>
  import { SERVER_URL, show_spinner } from './stores'
  import { geoMercator, geoPath } from "d3-geo";
  import { feature } from "topojson";
  import { onMount } from "svelte";


  export let country = "Poland";
  
  let map_data = "";
  let features = [];
  let selected;

  const projection = geoMercator();
  const geo_generator = geoPath().projection(projection);


  async function post_data() {

    if((country === "") || country === null){
      features = [];
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
      if (map_data !== null){
        features = map_data.features;
      } else {
        features = [];
      }
    } else {
      features = [];
    }
  }


  onMount(async function() {post_data()});

  // something not working here
  // https://bost.ocks.org/mike/map/


</script>
<input type="text" id="input-country" placeholder="Country" bind:value={country} on:change={() => post_data()}>

  <svg viewBox="0 0 975 610">
    <g fill="white" stroke="black">
      {#each features as feature, i}
          <path d={geo_generator(feature)}  on:click={() => selected = feature} class="state"></path>
      {/each}
    </g>
  </svg>


<div class="selectedName">{selected?.properties.name ?? ''}</div>

<style>

  #input-country {
    width:500px;
  }

  .state:hover {
		fill: hsl(0 0% 50% / 20%);
	}
	
	.selectedName {
		text-align: center;
		margin-top: 8px;
		font-size: 1.5rem;
	}

</style>
