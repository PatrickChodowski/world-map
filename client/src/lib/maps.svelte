
<script>
  import { SERVER_URL, show_spinner } from './stores'
  import { geoMercator, geoPath, geoOrthographic, geoEqualEarth, geoNaturalEarth1 } from "d3-geo";
  import { feature } from "topojson";
  import { onMount } from "svelte";


  export let country = "Europe";
  const START_VALUE_X = 0;
  const START_VALUE_Y = 0;
  // const START_VALUE_SCALE = 140;
  let map_data = "";
  let features = [];
  let selected;

  let translate_x = START_VALUE_X;
  let translate_y = START_VALUE_Y;
  // let map_scale = START_VALUE_SCALE;
  let drag_click_x = 0;
  let drag_click_y = 0;
  let on_drag = false;

  // let projection = geoOrthographic().translate([translate_x, translate_y]);
  let projection = geoMercator();
  let geo_generator = geoPath().projection(projection);
  let svg;



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
        projection.fitSize([svg.width.baseVal.value, svg.height.baseVal.value], map_data);
        console.log(map_data.bbox);
        features = map_data.features;
        on_drag = false;
        drag_click_x = 0;
        drag_click_y = 0;
      } else {
        features = [];
      }
    } else {
      features = [];
    }
  }


  onMount(async function() {post_data()});


  function zoom_map(e){
    // e.preventDefault = true;  
    // const svg = document.getElementById("main-map");

    // console.log(svg);

    // console.log(svg.children[0]);

    // console.log(svg.children[0].transform);

    // let svg_matrix = svg.createSVGMatrix();
    // let svg_transform = svg.createSVGTransform();

    // svg_transform.setScale(1.0, 1.0);
    // svg_transform.setMatrix(svg_matrix);
    // circle.transform.baseVal.initialize(transform);

    // console.log(svg_transform);
    // var   path_transform = svg.createSVGMatrix();
    // console.log(e.clientX);
    // console.log(e.clientY);

    // console.log("Click: ", e.clientX, e.clientY);
    // // console.log("Mapped coords: ", coords.x, coords.y);
    // console.log("Current Translate: ", translate_x, translate_y);
    // console.log(coords);

    // let diff_x = coords.x - 0.0;
    // let diff_y = e.clientY - 0.0;
    // console.log(diff_x, diff_y);
    // translate_x = coords.x;
    // translate_y = coords.y;

    // // path_transform = path_transform.translate(coords.x, coords.y);
    // map_scale -= e.deltaY*0.3;
    // // projection.translate([coords.x, coords.y]);
    // projection.scale(map_scale);
    // // // projection.translate([-translate_x, -translate_y]);
    // geo_generator = geoPath().projection(projection);
  }

  function pan_map_down(e){
    if(e.button  === 1){
      // console.log(svg.children[0]);

      // let svg_matrix = svg.getScreenCTM();
      // console.log(svg_matrix);
      // translate_x = svg_matrix.e;
      // translate_y = svg_matrix.f;

      drag_click_x = e.clientX;
      drag_click_y = e.clientY;
      on_drag = true;
      console.log("Clicked on: ", drag_click_x, drag_click_y);
    }
  }

  function pan_map_move(e){
    if(on_drag){
      let diff_x = (e.clientX - drag_click_x);
      let diff_y = (e.clientY - drag_click_y);

      console.log("Diff is: ", diff_x, diff_y);
      drag_click_x = e.clientX;
      drag_click_y = e.clientY;
      console.log()
      translate_x += diff_x;
      translate_y += diff_y;
      projection.translate([translate_x, translate_y]);
      geo_generator = geoPath().projection(projection);
    }
  }

  function pan_map_up(e){
    if((e.button  === 1) && (on_drag)){
      let diff_x = e.clientX - drag_click_x;
      let diff_y = e.clientY - drag_click_y;
      
      translate_x += diff_x;
      translate_y += diff_y;
      on_drag = false;
      projection.translate([translate_x, translate_y]);
      geo_generator = geoPath().projection(projection);

      console.log("Moved to ", translate_x, translate_y);
    }
  }




</script>
<svelte:window on:wheel|preventDefault={zoom_map} on:mousedown={pan_map_down} on:mouseup={pan_map_up} on:mousemove={pan_map_move}/>

<input type="text" id="input-country" placeholder="Country" bind:value={country} on:change={() => post_data()}>
  <svg id="main-map" width="100%" height="100%" preserveAspectRatio=True bind:this={svg}>
    <g fill="white" stroke="black">
      {#each features as feature, i}
          <path d={geo_generator(feature)}  on:click={() => selected = feature} class="state"></path>
      {/each}
    </g>
  </svg>


<div class="selectedName">{selected?.properties.name ?? ''}</div>

<style>

  #main-map {
    background-color: gray;
    height:92vh;
  }

  #input-country {
    width:500px;
    margin-bottom: 10px;
  }

  .state:hover {
		fill: aquamarine;
	}
	
	.selectedName {
		text-align: center;
		margin-top: 8px;
		font-size: 1.5rem;
	}

</style>
