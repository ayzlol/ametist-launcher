# Ametist Launcher

Ametist Launcher is a complete, open-source Minecraft launcher for Windows and Linux. It provides a focused interface for selecting a Minecraft version, choosing Vanilla, Fabric, Forge, or Quilt, configuring RAM, and starting the game.

## Download

Download the latest ready-to-use package from the [Latest Release](https://github.com/ayzlol/ametist-launcher/releases/latest).

- **Windows:** `AmetistLauncher.exe`
- **Linux:** `AmetistLauncher-x86_64.AppImage`

On Linux, make the AppImage executable before starting it:

```bash
chmod +x AmetistLauncher-x86_64.AppImage
./AmetistLauncher-x86_64.AppImage
```

The packaged files include Python and the project dependencies. Minecraft still requires a compatible Java Runtime Environment. SHA-256 checksums are displayed next to the release assets on GitHub.

## What Ametist provides

Ametist supports Vanilla, Fabric, Forge, and Quilt version selection, installation, and launching. On the first installation, the required Minecraft and loader files are downloaded automatically. When the internet is unavailable, Ametist checks the local `.ametist_mc` installation directory and shows versions that are already available.

The launcher includes dynamic or manual RAM allocation and applies JVM performance options when starting Minecraft. It also displays system, operating system, architecture, Python, and RAM information so that launch settings are easier to understand.

The interface is available in English, Turkish, Russian, and Spanish. Users can switch between a dark interface, left or right version-panel layouts, custom backgrounds, and custom profile avatars. Settings are saved locally and remain available between launches.

The Mods tab opens the local mods folder inside the Ametist data directory. It is intended for managing local mod files and does not currently provide an online Modrinth or CurseForge browser.

## Supported loaders

| Loader | Support |
|---|---|
| Vanilla | Supported |
| Fabric | Supported |
| Forge | Supported |
| Quilt | Supported |

## Screenshots

### Main window

![Ametist Launcher main window](screenshot-main-window.png)

### Settings

![Ametist Launcher settings window](screenshot-settings.png)

## Requirements

The ready-to-use Windows and Linux packages include the Python runtime and project libraries. You still need a compatible Java Runtime Environment for Minecraft.

To run from source, install:

- Python 3.8 or newer
- pip
- Git
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

You can also use `run.bat` on Windows or `run.sh` on Linux and macOS.

## First launch

1. Start Ametist and enter an offline username.
2. Select Vanilla, Fabric, Forge, or Quilt.
3. Choose a Minecraft version.
4. Select the amount of RAM to allocate.
5. Press Launch.

The first installation of a Minecraft version or loader requires an internet connection. After the files are downloaded, Ametist detects the local installation. If there is no internet connection, only versions already installed on the computer are shown.

## Offline usernames and account support

Ametist currently uses offline username login. Microsoft account authentication is not included. This behavior is described clearly so users know what to expect before downloading the launcher.

## Data and configuration

Ametist stores settings and Minecraft files in the `.ametist_mc` directory:

```text
Windows: %APPDATA%\\.ametist_mc
Linux:   ~/.ametist_mc
macOS:   ~/.ametist_mc
```

The directory contains the configuration file, installed Minecraft versions, loader installations, and the local mods folder. Back up this directory before resetting or moving the launcher data.

## Troubleshooting

### Java is not detected

Install a compatible Java Runtime Environment and make sure the `java` command is available in your system PATH. On Ubuntu, for example:

```bash
sudo apt install openjdk-17-jre-headless
```

### The AppImage does not start

Grant execute permission and try again:

```bash
chmod +x AmetistLauncher-x86_64.AppImage
```

### The version list is empty

Check your internet connection. When offline, Ametist only lists versions that are already installed locally. A new Minecraft version must be installed while an internet connection is available.

### Minecraft reports a memory error

Change the RAM allocation in the launcher settings. Leave enough memory available for the operating system and other applications.

## Reporting issues

If something does not work, open an [issue](https://github.com/ayzlol/ametist-launcher/issues) and include your operating system, Java version, Minecraft version, selected loader, exact error message, and relevant logs or screenshots.

Feature ideas and general feedback are welcome in [GitHub Discussions](https://github.com/ayzlol/ametist-launcher/discussions).

## Version

This repository contains the full Ametist Launcher v1.2.1 release. The `main` branch may contain newer changes than the packaged release assets. Use the [Latest Release](https://github.com/ayzlol/ametist-launcher/releases/latest) page when you want the downloadable Windows or Linux package.

## Contributing

Ametist is an independent open-source project, and practical feedback is welcome. For a large change, open an issue first. Pull requests should explain what changed and how the change was tested.

## License and trademark notice

Ametist Launcher is released under the [MIT License](LICENSE).

Ametist Launcher is an independent project and is not affiliated with, endorsed by, or sponsored by Mojang or Microsoft.

## Developers

Ametist Launcher is developed by [Unfayd](https://github.com/Unfayd) and [Thepan](https://github.com/ayzlol).

Built with Python, CustomTkinter, `minecraft-launcher-lib`, and Pillow.
