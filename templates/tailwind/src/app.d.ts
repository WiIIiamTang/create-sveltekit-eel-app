// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}

	interface Window {
		// eel is injected at runtime by the eel package
		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		eel: any | undefined;
	}
}

export {};
