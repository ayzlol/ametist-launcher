# Releases

This file summarizes the published Ametist Launcher versions. For ready-to-use Windows and Linux packages, visit the [GitHub Releases page](https://github.com/ayzlol/ametist-launcher/releases).

## v1.2.1 — Full release — 2026-08-26

Ametist Launcher v1.2.1 is the full release with ready-to-use packages for Windows and Linux. The launcher supports Vanilla, Fabric, Forge, and Quilt versions.

### Included

- Offline username login
- Version selection and launching for Vanilla, Fabric, Forge, and Quilt
- Downloading the required Minecraft and loader files on first installation
- Local installation detection when there is no internet connection
- Dynamic or manual RAM limits
- JVM performance options
- Clear distinction between installed and downloadable versions
- English, Turkish, Russian, and Spanish interface translations
- Dark interface
- Left or right version-panel position
- Custom background and profile avatar
- Local mods-folder access
- System, operating system, and RAM information

### Downloads

- **Windows:** Download and run `AmetistLauncher.exe`.
- **Linux:** Make `AmetistLauncher-x86_64.AppImage` executable and run it.

```bash
chmod +x AmetistLauncher-x86_64.AppImage
./AmetistLauncher-x86_64.AppImage
```

The packaged files include Python and the project dependencies. Minecraft still requires a compatible Java Runtime Environment. SHA-256 values for the files are shown on the GitHub release page.

### First-use note

An internet connection is required when installing a Minecraft version or loader for the first time. After the files are downloaded, Ametist detects them from the local installations in the `.ametist_mc` directory. When there is no internet connection, only versions already available on the computer are shown.

### Feedback

If you encounter a problem, share your operating system, Java version, Minecraft version, selected loader, and error message through [Issues](https://github.com/ayzlol/ametist-launcher/issues). Ideas and suggestions can be shared in [GitHub Discussions](https://github.com/ayzlol/ametist-launcher/discussions).

## v0.1.0-beta — 2026-07-31

This was the first development release. It included the basic launcher flow and offline Vanilla/Fabric launching support.
