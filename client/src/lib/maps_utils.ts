
const START_VALUE_X = 0;
const START_VALUE_Y = 0;
// const START_VALUE_SCALE = 140;
let drag_click_x = 0;
let drag_click_y = 0;
let on_drag = false;

let translate_x = START_VALUE_X;
let translate_y = START_VALUE_Y;

// function get_mouse_position(e) {
  //     var CTM = svg.getScreenCTM();
  //     return {
  //       x: (e.clientX - CTM.e) / CTM.a,
  //       y: (e.clientY - CTM.f) / CTM.d
  //     };
  //   }



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

  // function pan_map_down(e){
  //   if(e.button  === 1){
  //     // console.log(svg.children[0]);

  //     // let svg_matrix = svg.getScreenCTM();
  //     // console.log(svg_matrix);
  //     // translate_x = svg_matrix.e;
  //     // translate_y = svg_matrix.f;

  //     drag_click_x = e.clientX;
  //     drag_click_y = e.clientY;
  //     on_drag = true;
  //     console.log("Clicked on: ", drag_click_x, drag_click_y);
  //   }
  // }

  // function pan_map_move(e){
  //   if(on_drag){
  //     let diff_x = (e.clientX - drag_click_x);
  //     let diff_y = (e.clientY - drag_click_y);

  //     console.log("Diff is: ", diff_x, diff_y);
  //     drag_click_x = e.clientX;
  //     drag_click_y = e.clientY;
  //     console.log()
  //     translate_x += diff_x;
  //     translate_y += diff_y;
  //     projection.translate([translate_x, translate_y]);
  //     geo_generator = geoPath().projection(projection);
  //   }
  // }

  // function pan_map_up(e){
  //   if((e.button  === 1) && (on_drag)){
  //     let diff_x = e.clientX - drag_click_x;
  //     let diff_y = e.clientY - drag_click_y;
      
  //     translate_x += diff_x;
  //     translate_y += diff_y;
  //     on_drag = false;
  //     projection.translate([translate_x, translate_y]);
  //     geo_generator = geoPath().projection(projection);

  //     console.log("Moved to ", translate_x, translate_y);
  //   }
  // }

