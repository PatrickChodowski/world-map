<script lang="ts">
  import Maps from '../lib/maps.svelte';
  import Example from '../lib/example.svelte'; 
  let country: string; 
</script>

<Maps bind:country={country}/>

<!-- <Example></Example> -->
