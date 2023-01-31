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

<div>
	<div>
		<h1>SvelteKitEel</h1>
		<h2>Build GUI applications with SvelteKit and Python-Eel</h2>
	</div>
	<div>
		{#if message}
			<p>{message}</p>
		{/if}

		<button
			on:click={handleClickButtonMessage}
			type="button"
			class="px-2 py-4 bg-slate-800 rounded-lg text-white hover:bg-slate-700 w-full"
		>
			Call Eel function
		</button>

		<button on:click={handleClickButtonFile} type="button"> Select a file </button>
	</div>
	<br />
	<a href="/app">Link to another route</a>
</div>
