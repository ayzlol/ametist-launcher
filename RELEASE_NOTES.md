# Release Notes — v1.2.1

Ametist Launcher v1.2.1 is the current full release for Windows and Linux.

## Highlights

- Vanilla, Fabric, Forge, and Quilt version selection and launching
- Offline username login
- Automatic installation of required Minecraft and loader files
- Local installation detection when there is no internet connection
- Dynamic or manual RAM allocation
- JVM performance options for launching Minecraft
- English, Turkish, Russian, and Spanish interface translations
- Dark interface with configurable panel position
- Custom background and avatar support
- Local mods-folder access
- System, operating system, and RAM information
- Portable Windows executable and Linux AppImage packages

## Installation

Download `AmetistLauncher.exe` for Windows or `AmetistLauncher-x86_64.AppImage` for Linux from the [latest release](https://github.com/ayzlol/ametist-launcher/releases/latest).

Minecraft still requires a compatible Java Runtime Environment. The first installation of a Minecraft version requires an internet connection. After the required files are present locally, Ametist can detect the installed versions when offline.

To run from source:

```bash
git clone https://github.com/ayzlol/ametist-launcher.git
cd ametist-launcher
pip install -r requirements.txt
python Ametist.py
```

## Notes

Ametist is distributed as a full release. As with any actively maintained desktop application, issues can still occur on particular operating systems or Java installations. Please report the operating system, Java version, Minecraft version, loader, and exact error message when opening an issue.

The project is independent and is not affiliated with or endorsed by Mojang or Microsoft.
