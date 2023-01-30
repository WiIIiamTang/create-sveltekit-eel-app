<h1 align="center">
  SvelteKitEel App
</h1>

<p align="center">
  CLI to start an Eel app with SvelteKit.
</p>

<div align="center">

[![npm version](https://badge.fury.io/js/create-sveltekit-eel-app.svg)](https://badge.fury.io/js/create-sveltekit-eel-app)
[![tagged-release](https://github.com/WiIIiamTang/create-sveltekit-eel-app/actions/workflows/tagged-release.yml/badge.svg)](https://github.com/WiIIiamTang/create-sveltekit-eel-app/actions/workflows/tagged-release.yml)
![npm](https://img.shields.io/npm/dy/create-sveltekit-eel-app)

</div>

```
npx create-sveltekit-eel-app@latest my-gui-app
```

<div align="center">

![exampleskeelapp](https://user-images.githubusercontent.com/48343678/215373055-6cb73a55-9d1f-4b56-89c3-0f4e8211e781.png)

</div>

## About

create-sveltekit-eel-app is a CLI to create all the boilerplate needed for a lightweight Eel app with SvelteKit integration. It was created to make simple desktop GUI applications. As the name implies, this combines two main technologies:

- Eel: A Python library for ["making simple Electron-like offline HTML/JS GUI apps."](https://github.com/python-eel/Eel)
- SvelteKit: ["A framework for rapidly developing robust, performant web applications using Svelte"](https://kit.svelte.dev/docs/introduction)
  - SvelteKit will be running in SPA mode.

This template also comes with Tailwind CSS preconfigured.

## Requirements

- Chrome or Microsoft Edge
- git
- npm
- node ≥ 16
- Python ≥ 3.10 (lower versions have not been tested)

## Usage

Get started with:

```
npx create-sveltekit-eel-app@latest my-gui-app
```

After it's done setting up, you can optionally create a virtual environment for your Python dependencies. Then,

```
cd my-gui-app
pip3 install -r requirements.txt
```

Start the app with

```
npm run start:eel
```

## Development

You can always preview the full app and test Eel-SvelteKit connections with

```
npm run start:eel
```

Develop the SvelteKit GUI with

```
npm run dev
```

And restart `npm run start:eel` as needed.

Currently, `npm run start:eel-dev` will try to serve the eel app using the `src` folder but exposed functions will not work - so it's better to go with the above workflow.

### List of commands

`npm run`

- `dev`: Starts the SvelteKit site in dev mode.
- `build`: Builds the SvelteKit app into a folder `build`.
- `preview`: Previews the SvelteKit app in `build`.
- `test`: Run playwright tests.
- `check`: Run `svelte-check` against your project.
- `check:watch`: Same as the above command but with `--watch`.
- `test:unit`: Run vitest tests.
- `lint`: Run linting.
- `format`: Format files with Prettier.
- `start:eel`: Starts the Eel app. The SvelteKit app is served through the `build` folder.
- `start:eel-dev`: Starts the Eel app in dev mode. The SvelteKit app is served through your `src` folder. SvelteKit also needs to run for this to work. **SEE THE NOTE ABOUT DEV MODE BELOW**
- `build:eel-generate-spec`: This should be used the first time you create a production build of your Eel app. Generates a `.spec` file along with the build.
- `build:eel`: Create a production build of your Eel app according to the generated `.spec` file.

#### Note on developing with create-sveltekit-eel

There are currently some issues that prevent a better developer experience - specifically, hot-reloading the eel app with SvelteKit does not seem to work right now **for Eel exposed functions.**

This means that calling any functions exposed by Eel may not work as intended.

If you'd still like to continue, you can run

```
npm run start:eel-dev
```

To start up an Eel app in development mode. The window will pop up, and you may see an error similar to this:

```
This site can’t be reached
localhost refused to connect.
```

Which is expected. Then, start up your SvelteKit app with

```
npm run dev
```

Go back to your Eel app and you should see everything now. You can develop like this if you want to test anything that _doesn't_ involve exposed Eel functions. The Python app always needs to be restarted for changes to take effect.

## Distributing

The first time you create a production build of your Eel app, you need to run

```
npm run build:eel-generate-spec
```

This will create a `.spec` file along with the build. You can test out the application by running the executable in the `dist` folder.

In subsequent builds, you can run

```
npm run build:eel
```

Which will generate a production build according to the provided `.spec` file. For example, you may want to turn on the console window, or change the icon, or make the entire project a single file. Log output is not currently available in the console for production builds to ensure compatibility with the `--noconsole` setting, see [here](https://github.com/python-eel/Eel/issues/654).

You can always manually run pyinstaller with

```
pyinstaller eelApp.spec --clean --onefile
```

The example above generates a single file executable.

Note that pyinstaller does not support cross-platform builds. If you want to deploy your app on Linux and Windows, you need pipelines to install pyinstaller and build the app for each platform.

## Chrome and Edge warning

Eel will open a Chrome window by default, and will try to open a Microsoft Edge window on Windows operating systems if Chrome is not found. This means if your end user has none of these browsers installed, the app will not work.

## Examples

You can view the [examples on Eel](https://github.com/python-eel/Eel/tree/master/examples) for an idea on how to use it.

This template comes with basic examples of communicating between Python and SvelteKit. Here are some things you can look at:

```svelte
<script>
...

function hello_from_sk(name: string) {
    message = `Hello ${name}, this function is being called from Python [${count}]`;
    count++;
}
if (eel) {
    window.eel.expose(hello_from_sk, 'hello_from_sk');
}

...
</script>
```

This exposes a function to your Python backend that can be called with `eel.hello_from_sk(name)`. You can modify elements such as the `message` or `count` variables in your SvelteKit app whenever it's called.

You can also deal with functions asynchronously with callbacks. Say you exposed a function that lets you pick a file from your computer:

```python3
def choose_file() -> str:
    tkinter.Tk().withdraw()
    root = tkinter.Tk()
    root.attributes("-alpha", 0.0)
    root.attributes("-topmost", True)
    filename = fd.askopenfilename(
        parent=root, title="Choose a file", filetypes=[("All files", "*.*")]
    )
    root.destroy()
    return filename
```

This returns the filename at some point. In your SvelteKit application, call the exposed function like so:

```svelte
eel?.choose_file()((file: string) => {
  // handle the selected file
  message = `File selected: ${file}`;
});
```

The callback function will be called when the Python function returns.
