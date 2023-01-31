<script lang="ts">
	let message = 'Hello';
	let count = 0;
	let eel = window.eel;
	eel?.set_host('ws://localhost:8888');

	////////////////////////////////////////
	// functions to expose to eel
	function hello_from_sk(name: string) {
		message = `Hello ${name}, this function is being called from Python [${count}]`;
		count++;
	}
	if (eel) {
		// window.eel?.expose will not work due to regex
		window.eel.expose(hello_from_sk, 'hello_from_sk');
	}
	////////////////////////////////////////

	const handleClickButtonMessage = () => {
		eel?.hello_from_eel('World');
	};

	const handleClickButtonFile = () => {
		eel?.choose_file()((file: string) => {
			message = `File selected: ${file}`;
		});
	};
</script>

<div class="w-full h-full flex flex-col flex-wrap justify-center items-center py-2 px-2">
	<div class="mb-4 text-center">
		<h1 class="text-7xl font-light leading-relaxed">SvelteKitEel</h1>
		<h2 class="text-xl text-zinc-800">Build GUI applications with SvelteKit and Python-Eel</h2>
	</div>
	<div class="flex flex-col gap-2 justify-center items-center py-4 w-1/2">
		{#if message}
			<p class="text-2xl text-black text-center">{message}</p>
		{/if}

		<button
			on:click={handleClickButtonMessage}
			type="button"
			class="px-2 py-4 bg-slate-800 rounded-lg text-white hover:bg-slate-700 w-full"
		>
			Call Eel function
		</button>

		<button
			on:click={handleClickButtonFile}
			type="button"
			class="px-2 py-4 bg-slate-800 rounded-lg text-white hover:bg-slate-700 w-full"
		>
			Select a file
		</button>
	</div>
	<a href="/app" class="underline">Link to another route</a>
</div>
