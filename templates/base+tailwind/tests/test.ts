import { expect, test } from '@playwright/test';

test('index page has expected h1', async ({ page }) => {
	await page.goto('/');
	expect(await page.textContent('h1')).toBe('SvelteKitEel');
});

test('index page has expected buttons', async ({ page }) => {
	await page.goto('/');
	expect(await page.textContent('button')).toBe('Call Eel function');
	expect(await page.textContent('button:nth-of-type(2)')).toBe('Select a file');
});

test('click on call eel function button', async ({ page }) => {
	await page.goto('/');
	await page.waitForURL('http://localhost:8888/');
	await page.waitForLoadState('networkidle');
	await page.getByRole('button', { name: 'Call Eel function' }).waitFor();
	await page.getByRole('button', { name: 'Call Eel function' }).click({ clickCount: 2 });
	expect(await page.textContent('p')).toBe(
		'Hello World, this function is being called from Python [1]'
	);
});

test('click on link to /app', async ({ page }) => {
	await page.goto('/');
	await page.getByRole('link', { name: 'Link to another route' }).click();
	await expect(page).toHaveURL('http://localhost:8888/app');
});
