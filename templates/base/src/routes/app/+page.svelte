<script lang="ts">
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

<div>
	<h1>SvelteKitEel</h1>
	<button type="button" on:click={handleDataClick}>Load data</button>
	{#if isLoading}
		<p>Loading...</p>
	{/if}
	<div>
		{#each data as product}
			<div>
				<div>
					{product.title}
				</div>
				<img src={product.thumbnail} alt={product.title} class="h-10 w-10" />
			</div>
		{/each}
	</div>
	<br />
	<a href="/">Back to home</a>
</div>
