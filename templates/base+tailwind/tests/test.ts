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
