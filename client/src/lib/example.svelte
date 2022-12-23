<script>
	// https://github.com/topojson/us-atlas
	// https://github.com/d3/d3-geo
	// https://observablehq.com/@mbostock/u-s-state-map
	// TODO: https://observablehq.com/@d3/u-s-map
	// TODO: https://observablehq.com/@jeantimex/us-state-county-map
	
	import { onMount } from 'svelte';
	import * as topojson from 'topojson-client';
	import { geoPath, geoAlbersUsa, geoAlbers } from 'd3-geo';
	import { draw } from 'svelte/transition';
	
	// https://github.com/topojson/us-atlas#us-atlas-topojson
	const projection = geoAlbersUsa().scale(1300).translate([487.5, 305])
	
	const path = geoPath().projection(null);
	
	let features = [];
	let counties = []
	let mesh;
	let selected;
	//$: console.log({ selected })
	
	const points = [
		{ lat: 38.421115245736, long: -82.44432596047203 },
	].map(p => projection([p.long, p.lat]))
	
	onMount(async () => {
		const us = await fetch('https://cdn.jsdelivr.net/npm/us-atlas@3/counties-albers-10m.json')
			.then(d => d.json())
		console.log({ us })
		
		features = topojson.feature(us, us.objects.states).features;
		// console.log({ features })
		
		counties = topojson.feature(us, us.objects.counties).features;
		
		mesh = topojson.mesh(us, us.objects.states, (a, b) => a !== b);
	})
</script>

<svg viewBox="0 0 975 610">
	<!-- State shapes -->
	<g fill="white" stroke="black">
		{#each features as feature, i}
			<path d={path(feature)} on:click={() => selected = feature} class="state" in:draw={{ delay: i * 50, duration: 1000 }} />
		{/each}
				

	</g>
		
	<!-- Interior lines -->
<!-- 	<path d={path(mesh)} fill="none" stroke="black" /> -->
		
	{#if selected}
		<path d={path(selected)} fill="hsl(0 0% 50% / 20%)" stroke="black" stroke-width={2} />
	{/if}
		
	{#each counties as feature, i}
	  <path d={path(feature)} on:click={() => selected = feature} class="state" stroke="rgb(0 0 0 / 10%)" fill="none" />
	{/each}
	
	{#each points as [cx, cy]}
		<circle {cx} {cy} r={10} fill="black" />
		<circle {cx} {cy} r={8} fill="white" />
		<circle {cx} {cy} r={5} fill="black" />
	{/each}
</svg>

<div class="selectedName">{selected?.properties.name ?? ''}</div>
	
<style>
	.state:hover {
		fill: hsl(0 0% 50% / 20%);
	}
	
	.selectedName {
		text-align: center;
		margin-top: 8px;
		font-size: 1.5rem;
	}
</style>