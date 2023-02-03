import type { PlaywrightTestConfig } from '@playwright/test';

const config: PlaywrightTestConfig = {
	webServer: {
		command: 'npm run build && python eelApp.py --console --mode None',
		port: 8888
	},
	testDir: 'tests'
};

export default config;
