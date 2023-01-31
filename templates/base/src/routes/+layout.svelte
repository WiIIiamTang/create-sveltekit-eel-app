<svelte:head>
	<title>SvelteKitEel</title>
</svelte:head>

<div class="mainlayout">
	<slot />
</div>

<style>
	.mainlayout {
		height: 100vh;
		width: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
	}
</style>
