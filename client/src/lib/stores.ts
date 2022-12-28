import { writable, get } from "svelte/store";
import type { Writable } from "svelte/store";
import { geoMercator, geoPath, geoOrthographic, geoEqualEarth, geoNaturalEarth1 } from "d3-geo";


export const LOCAL_SERVER_URL: string = "http://127.0.0.1:8000"
export const SERVER_URL: string = LOCAL_SERVER_URL;

export let country: Writable<string> = writable("Poland");
export let features: Writable<Array<any>> = writable([]);
export let projection = geoMercator();
export let geo_generator = geoPath().projection(projection);
export let svg_width = writable(2000);
export let svg_height = writable(1000);

// Gets map data from server. Is in stores as its used from maps and panel component
export async function get_map_data() {
  const res = await fetch(`${SERVER_URL}/select`, 
                          {method:"POST", 
                          headers: {"Content-type": "application/json"}, 
                          body: JSON.stringify({"country": get(country)})});

  if (res.status === 200){
    let resdata = await res.json();
    if(resdata.data !== null){
      projection.fitSize([get(svg_width), get(svg_height)], resdata.data);
      features.set(resdata.data.features);
    }
    return resdata.data;  
  } else {
    return null;
  }
}

