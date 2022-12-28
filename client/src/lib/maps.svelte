

<script>

  import { onMount } from "svelte";
  import { get_map_data, features, geo_generator, svg_height, svg_width, highlighted_element_data } from './stores'

  let selected = [];
  let svg;

  onMount(async function() {
    get_map_data();
    svg_width.set(svg.width.baseVal.value);
    svg_height.set(svg.height.baseVal.value);

  });

  function get_mouse_position(e) {
      var CTM = svg.getScreenCTM();
      return {
        x: (e.clientX - CTM.e) / CTM.a,
        y: (e.clientY - CTM.f) / CTM.d
      };
    }

  function click_map(e) {
    let coords = get_mouse_position(e);
    // console.log("Screen click:", [e.clientX, e.clientY]);
    // console.log("Map click:", [coords.x, coords.y]); 
  }

  function display_info(e){
    // console.log("Name: ", e.target.getAttribute("data-name"));
    highlighted_element_data.set({"name": e.target.getAttribute("data-name")});
  }

</script>


<svg id="main-map" width="100%" height="100%" preserveAspectRatio=True bind:this={svg} on:click={click_map}>
  <g fill="white" stroke="black">
    {#each $features as feature, i}
        <path d={geo_generator(feature)} 
              data-name = {feature.properties.NAME} 
              class="state"
              on:click={display_info}>
        </path>
    {/each}
  </g>
</svg>


<style>

  #main-map {
    background-color: gray;
    height:90vh;
  }

  .state:hover {
		fill: aquamarine;
	}
	
</style>
