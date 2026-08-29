# Releases

This file summarizes the published Ametist Launcher releases. For downloads, use the [GitHub Releases page](https://github.com/ayzlol/ametist-launcher/releases).

## v1.2.1 — 2026-08-26

This release adds the first pre-built Windows and Linux downloads.

### Downloads

- **Windows:** `AmetistLauncher.exe`
- **Linux:** `AmetistLauncher-x86_64.AppImage`

The release page includes SHA-256 checksums for both files. On Linux, make the AppImage executable before starting it:

```bash
chmod +x AmetistLauncher-x86_64.AppImage
./AmetistLauncher-x86_64.AppImage
```

### Important notes

Ametist is an early beta and currently uses offline username login. The launcher’s tested application flow supports Vanilla and Fabric. Microsoft account authentication, Forge, Quilt, macOS, automatic updates, and online mod catalog integration are not available yet.

The `main` branch may include changes that are newer than this release. Use the release assets when you want the stable packaged build.

## v0.1.0-beta — 2026-07-31

The initial beta release included the basic offline launcher flow for Vanilla and Fabric.

To run it from source:

```bash
pip install -r requirements.txt
python Ametist.py
```

## Versioning policy

Release notes should describe user-visible changes, known limitations, supported platforms, and any migration or installation steps. Packaged files should be attached to a GitHub Release and accompanied by checksums whenever possible.
