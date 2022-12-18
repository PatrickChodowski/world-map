<script lang="ts">
  import Maps from '../lib/maps.svelte';
  let country: string; 
</script>

<Maps bind:country={country}/>
