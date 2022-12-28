

<script>
// @ts-nocheck

  import { onMount } from "svelte";
  import { get_map_data, features, geo_generator, svg_height, svg_width } from './stores'

  let selected = [];
  let svg;

  onMount(async function() {
    get_map_data();
    svg_width.set(svg.width.baseVal.value);
    svg_height.set(svg.height.baseVal.value);

  });

  function click_map(e) {
    // let coords = get_mouse_position(e);
    // console.log("Screen click:", e.clientX, e.clientY);
    console.log("Map click");
    
  }

</script>


<svg id="main-map" width="100%" height="100%" preserveAspectRatio=True bind:this={svg} on:click={click_map}>
  <g fill="white" stroke="black">
    {#each $features as feature, i}
        <path d={geo_generator(feature)} 
              data-name = {feature.properties.NAME} 
              on:click={() => selected = feature}
              class="state">
        </path>
    {/each}
  </g>
</svg>


<style>

  #main-map {
    background-color: gray;
    height:92vh;
  }

  .state:hover {
		fill: aquamarine;
	}
	
</style>
