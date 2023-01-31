<div class="spin h-24 w-24 border-2 rounded-full my-2 border-indigo-600" />

<style>
	.spin {
		animation: 1s linear 0s infinite normal none running rotate;
		border-top-color: transparent;
	}
	@keyframes rotate {
		0% {
			transform: rotate(0);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>
