
<script lang="ts">
  import { SERVER_URL, show_spinner } from './stores'
  export let country: string = "Australia";

  async function post_data(): Promise<string> {
    // show_spinner = true;
    const res = await fetch(`${SERVER_URL}/select`, 
                            {method:"POST", 
                            headers: {"Content-type": "application/json"}, 
                            body: JSON.stringify({"country": country})});
    // show_spinner = false;
    if (res.status === 200){
      let resdata = await res.json();
      console.log(resdata.data);
      return resdata.data;
    }  else {
      let resdata = await res.json();
      console.log(resdata.data);
      return resdata.data;
    }
  }

</script>

<p>Map</p>
<input type="text" id="input-country" placeholder="Country" bind:value={country} on:change={() => post_data()}>
<button on:click={post_data}> Send Data</button>