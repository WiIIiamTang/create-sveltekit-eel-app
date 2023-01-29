#!/usr/bin/env node

const { execSync } = require('child_process');

const runCommand = (command) => {
	try {
		execSync(`${command}`, { stdio: 'inherit' });
	} catch (error) {
		console.error(error);
		return false;
	}
	return true;
};

const repoName = process.argv[2];
const gitCheckoutCommand = `git clone --depth 1 https://github.com/WiIIiamTang/create-sveltekit-eel-app ${repoName}`;
const installDepsCommand = `cd ${repoName} && npm install`;

console.log(`Creating a new SvelteKitEel app in ${repoName}...`);
const checkedOut = runCommand(gitCheckoutCommand);

if (!checkedOut) {
	console.error('Failed to clone the repo');
	process.exit(1);
}

console.log('Installing dependencies...');
const installed = runCommand(installDepsCommand);

if (!installed) {
	console.error('Failed to install dependencies');
	process.exit(1);
}

console.log('Done!');
console.log(`
    To get started:
        cd ${repoName}
        npm run start:eel
`);
