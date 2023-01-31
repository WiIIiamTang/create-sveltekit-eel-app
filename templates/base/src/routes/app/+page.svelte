<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';

	let eel = window.eel;
	eel?.set_host('ws://localhost:8888');

	type Product = {
		id: number;
		title: string;
		description: string;
		price: number;
		thumbnail: string;
	};

	let data: Array<Product> = [];
	let isLoading = false;

	const handleDataClick = () => {
		isLoading = true;
		data = [];
		eel?.get_data()((products: Array<Product>) => {
			data = products;
			isLoading = false;
		});
	};
</script>

<div
	class="w-full h-full flex flex-col flex-wrap justify-center items-center py-2 px-2 overflow-x-hidden"
>
	<h1 class="text-6xl font-light leading-relaxed mb-4 text-center">SvelteKitEel</h1>
	<button
		type="button"
		on:click={handleDataClick}
		class="py-2 px-2 bg-slate-800 rounded-md text-white my-2">Load data</button
	>
	{#if isLoading}
		<Spinner />
	{/if}
	<div class="my-4 w-1/2 flex flex-col gap-2">
		{#each data as product}
			<div class="flex flex-row justify-between w-full">
				<div>
					{product.title}
				</div>
				<img src={product.thumbnail} alt={product.title} class="h-10 w-10" />
			</div>
		{/each}
	</div>
	<a href="/" class="underline mt-4">Back to home</a>
</div>
