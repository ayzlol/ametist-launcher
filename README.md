# Ametist Launcher

Ametist Launcher is a small, open-source Minecraft launcher for people who want a simple way to start Vanilla or Fabric Minecraft without a complicated interface.

> Ametist is currently in early beta. It supports offline usernames and Vanilla/Fabric installations. Microsoft account login, Forge, Quilt, and macOS support are not available yet.

## Download

The easiest way to try Ametist is to download the latest release:

- [Windows portable executable](https://github.com/ayzlol/ametist-launcher/releases/latest)
- [Linux AppImage](https://github.com/ayzlol/ametist-launcher/releases/latest)

The current release is available from the [Releases page](https://github.com/ayzlol/ametist-launcher/releases). Checksums are shown next to the downloadable files on the release page.

## What works today

- Offline username login
- Vanilla Minecraft versions
- Fabric installation and launching
- RAM allocation from the launcher interface
- Local version caching for later offline use
- Dark and light themes
- Custom background and avatar support
- English, Turkish, Russian, Chinese, and Spanish interface translations
- A local mods-folder viewer

## Current limitations

Ametist is still being developed. Microsoft account authentication is not implemented, so this project is currently intended for offline use. Forge and Quilt are not supported in the current application. The mods screen currently helps you open and inspect the local mods folder; it does not yet provide a Modrinth or CurseForge browser.

Please check the release notes before updating. The `main` branch may contain newer development changes than the latest stable release.

## Screenshots

### Main window

![Ametist Launcher main window](screenshot-main-window.png)

### Settings

![Ametist Launcher settings window](screenshot-settings.png)

## Requirements

For the pre-built Windows and Linux downloads, Python and the project dependencies are already bundled. Minecraft still requires a compatible Java Runtime Environment.

To run the project from source, you need:

- Python 3.8 or newer
- pip
- Git, if you are cloning the repository
- A compatible Java Runtime Environment

## Run from source

```bash
git clone https://github.com/ayzlol/ametist-launcher.git
cd ametist-launcher
python -m venv venv
```

On Windows:

```bat
venv\Scripts\activate
pip install -r requirements.txt
python Ametist.py
```

On Linux or macOS:

```bash
source venv/bin/activate
pip install -r requirements.txt
python3 Ametist.py
```

You can also use `run.bat` on Windows or `run.sh` on Linux.

## First launch

1. Start Ametist and enter an offline username.
2. Select Vanilla or Fabric.
3. Select a Minecraft version.
4. Choose the amount of RAM to allocate.
5. Click Launch.

The first launch needs an internet connection to download the selected Minecraft files. Once a version has been installed, it can be used from the local cache when the required files are available.

## Configuration

Ametist stores its local configuration in the `.ametist_mc` directory:

```text
Windows: %APPDATA%\\.ametist_mc\\ametist_config.json
Linux:   ~/.ametist_mc/ametist_config.json
macOS:   ~/.ametist_mc/ametist_config.json
```

## Troubleshooting

### Java is not detected

Install a compatible Java Runtime Environment and make sure the `java` command is available in your system PATH. On Ubuntu, for example:

```bash
sudo apt install openjdk-17-jre-headless
```

### The AppImage does not start

Make the file executable before running it:

```bash
chmod +x AmetistLauncher-x86_64.AppImage
./AmetistLauncher-x86_64.AppImage
```

### The launcher reports a network error

Check your connection and try again. The first installation of a Minecraft version requires access to the relevant Minecraft and Fabric services.

### Minecraft runs out of memory

Lower or increase the allocated RAM according to your system memory. Leaving enough memory for the operating system is important.

## Reporting a problem

If something does not work, please open an [issue](https://github.com/ayzlol/ametist-launcher/issues) and include your operating system, Java version, Minecraft version, selected loader, the exact error message, and relevant logs or screenshots.

Feature ideas and longer discussions are welcome in [GitHub Discussions](https://github.com/ayzlol/ametist-launcher/discussions).

## Roadmap

The next planned improvements include Microsoft account authentication, better Java detection, clearer logs and crash reports, Modrinth integration, instance management, and broader loader support. The roadmap may change as the project receives feedback.

## Contributing

Ametist is a small project and practical feedback is valuable. If you would like to help, open an issue first for a large change, then create a focused pull request with a clear description and testing notes.

## License

Ametist Launcher is released under the [MIT License](LICENSE).

Ametist Launcher is an independent open-source project and is not affiliated with or endorsed by Mojang or Microsoft.

## Credits

Created by [Unfayd](https://github.com/Unfayd) and [Thepan](https://github.com/ayzlol).

Built with Python, CustomTkinter, `minecraft-launcher-lib`, and Pillow.
