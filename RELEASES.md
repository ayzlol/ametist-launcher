# Releases

## v0.1.0-beta — Beta Initial Release

Date: 2026-07-31

Summary:
- Ametist Launcher beta initial release (offline-only). Includes basic launcher functionality for Vanilla & Fabric.

How to run:
1. If Python 3.11+ is installed:
   - pip install -r requirements.txt
   - python Ametist.py
2. Use `run.bat` on Windows or `run.sh` on Linux/macOS.

Known notes / warnings:
- This is a beta release; some features may be missing or unstable.
- To make it easier for users to run, consider creating standalone binaries (e.g., with PyInstaller) and uploading them as release assets.

Recommendations:
- Build binaries for Windows, Linux, and macOS and attach them to the GitHub Release.
- Add a SHA256 checksum file for any binary assets.
- Create a `CHANGELOG.md` to track version history.
- Expand the release section in `README.md` with installation and usage examples.

If you want, I can prepare release artifacts (exe/zip) and provide the gh CLI commands to upload them, or add a GitHub Actions workflow to automate building and publishing releases.
