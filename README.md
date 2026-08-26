# ✨ Ametist Launcher v1.2.1

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-GUI-FF6B6B?style=for-the-badge&logo=tkinter)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen?style=for-the-badge)
![Offline Capable](https://img.shields.io/badge/Mode-Offline%20Capable-blue?style=for-the-badge)

---

**A fast, lightweight, and modern open-source Minecraft launcher for everyone.**

*Crafted by Unfayd & Thepan* 🚀

</div>

---

## 📸 Screenshots

![Ametist Launcher Main Interface](https://github.com/ayzlol/ametist-launcher/raw/main/Ekran%20Görüntüsü%202026-07-31%2022-10-07.png)

---

## 📖 Overview

**Ametist Launcher** is a powerful, community-driven Minecraft launcher designed with **speed, simplicity, and elegance** at its core. Whether you're a vanilla purist, a heavy modder with Forge, or exploring the latest with Quilt, Ametist delivers a seamless gaming experience with deep customization and intelligent resource management.

### 🎯 Core Philosophy

- **🚀 Fast & Responsive**: Lightning-quick startup and smooth gameplay
- **🪶 Lightweight**: Minimal resource footprint, maximum efficiency
- **🎨 Modern Design**: Beautiful, intuitive interface built with CustomTkinter
- **🔓 100% Open Source**: Community-driven development with MIT License
- **🌍 Global Support**: Multi-language UI for players worldwide
- **📦 Offline-Ready**: Full offline support with local version caching
- **⚡ Zero Dependencies**: Pre-built AppImage (Linux) & EXE (Windows) — no Python needed!

---

## ✨ Key Features

### 🌐 Multi-Language Support
Ametist Launcher speaks your language:
- **English** 🇬🇧
- **Turkish** 🇹🇷 (Türkçe)
- **Russian** 🇷🇺 (Русский)
- **Chinese** 🇨🇳 (中文)
- **Spanish** 🇪🇸 (Español)

Fully localized interface with instant "Please wait..." loading prompts in your preferred language.

### 📦 Complete Loader Support
Launch **any** Minecraft variant with full support:

| Loader | Status | Details |
|--------|--------|---------|
| **Vanilla** | ✅ Full Support | Pure Minecraft releases |
| **Fabric** | ✅ Full Support | Lightweight modding framework |
| **Forge** | ✅ Full Support | Heavy modding powerhouse |
| **Quilt** | ✅ Full Support | Modern, community-focused loader |

### 🧠 Dynamic & Smart RAM Management
- **Auto-Detection**: `get_system_ram_gb()` automatically detects your system memory
- **Intelligent Allocation**: Smart suggestions based on available resources
- **Manual Control**: Fine-tune RAM from 2 GB to 16 GB
- **Performance Tuning**: Advanced JVM flags (`-XX:+UseG1GC`, parallel processing) for optimal gameplay
- **Safe Defaults**: Never crash your system with unsafe allocations

### 🎨 Deep UI Customization
Personalize every aspect:
- **Layout Flexibility**: Arrange panels left or right
- **Custom Backgrounds**: Load your own stunning background images
- **Visual Effects**: Blur and brightness overlays
- **Circular Profile Avatars**: Auto-generated initials with custom skin support
- **Theme Support**: Dark mode (default) and Light mode
- **Responsive Design**: Perfectly adapts to any screen size

### 🔒 Advanced Offline Mode & Local Version Caching
- **[✔] Status Indicators**: Clear visual feedback on installation status
- **Local Cache**: Downloaded versions available indefinitely offline
- **Fallback Versions**: Built-in list for offline scenarios
- **Persistent Storage**: All settings saved locally in `.ametist_mc` directory

### 🛠️ Built-in System Hardware Inspector
Monitor and optimize:
- **Java Version Detection**: Automatic JRE validation
- **System RAM Monitoring**: Real-time memory information
- **OS & Architecture Info**: Linux, Windows, macOS, x86_64, ARM64
- **Diagnostic Reports**: Detailed error messages with solutions

### 🎮 Additional Features
- **Mod Management**: Browse, install, and manage mods effortlessly
- **CustomSkinLoader Integration**: Auto-sync skins with mod loader
- **Session Persistence**: Remember your last version, loader, and settings
- **Thread-Safe Operations**: Non-blocking UI during downloads
- **Comprehensive Error Handling**: Helpful messages with next steps

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.8+ | Core runtime |
| **GUI** | CustomTkinter | Modern UI framework |
| **Launcher** | minecraft-launcher-lib | Version & mod management |
| **Images** | Pillow (PIL) | Avatar & skin processing |
| **Config** | JSON | Settings storage |

**Runtime Dependencies** (included in pre-built releases):
- `customtkinter` — Beautiful, native-feeling UI
- `minecraft-launcher-lib` — Minecraft ecosystem integration
- `Pillow` — Image processing

---

## 🚀 Quick Start

### ⚡ Fastest Way: Pre-Built Releases (Recommended)

**No installation required** — just download and run!

#### Windows
1. Download [`AmetistLauncher.exe`](https://github.com/ayzlol/ametist-launcher/releases/latest) from Releases
2. Double-click the `.exe` file
3. Done! 🎮

#### Linux
1. Download [`AmetistLauncher-x86_64.AppImage`](https://github.com/ayzlol/ametist-launcher/releases/latest) from Releases
2. Make it executable:
   ```bash
   chmod +x AmetistLauncher-x86_64.AppImage
   ```
3. Run it:
   ```bash
   ./AmetistLauncher-x86_64.AppImage
   ```

---

### 🔧 Developer Setup: Running from Source

For developers who want to modify the launcher:

#### Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Java Runtime Environment (JRE)** — required for Minecraft
- **Git** (optional)

#### Installation Steps

##### 1️⃣ Clone Repository

```bash
git clone https://github.com/ayzlol/ametist-launcher.git
cd ametist-launcher
```

##### 2️⃣ Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

##### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

##### 4️⃣ Run Launcher

**Windows:**
```bash
python Ametist.py
```
Or use the batch script:
```bash
run.bat
```

**Linux / macOS:**
```bash
python3 Ametist.py
```
Or use the shell script:
```bash
chmod +x run.sh
./run.sh
```

---

## 📁 Project Structure

```
ametist-launcher/
├── Ametist.py              # Main application (38KB)
├── requirements.txt        # Python dependencies
├── run.bat                 # Windows launcher script
├── run.sh                  # Unix launcher script
├── LICENSE                 # MIT License
├── README.md               # This file
└── .gitignore              # Git rules
```

---

## ⚙️ Configuration

Settings are stored in a local JSON file:

**Location:**
```
Windows:   %APPDATA%\.ametist_mc\ametist_config.json
Linux:     ~/.ametist_mc/ametist_config.json
macOS:     ~/.ametist_mc/ametist_config.json
```

**Configuration Schema:**
```json
{
  "language": "en",                    // Language: en, tr, ru, zh, es
  "avatar_path": "/path/to/avatar",   // Custom avatar image
  "last_version_type": "Vanilla",     // Last selected loader
  "last_version": "1.20.4",           // Last selected version
  "last_ram": "4 GB",                 // Last RAM allocation
  "theme": "Dark",                    // Theme: Dark or Light
  "username": "Player",               // Offline username
  "first_run": false,                 // First-run setup flag
  "layout": "default",                // Panel layout
  "background": ""                    // Custom background path
}
```

---

## 🎮 Usage Guide

### Launching Minecraft

1. **Select Loader**: Choose from Vanilla, Fabric, Forge, or Quilt
2. **Pick Version**: Select any available Minecraft version
3. **Allocate RAM**: Choose 2-16 GB (or let auto-detect decide)
4. **Press LAUNCH**: Minecraft starts instantly

### Managing Mods

1. Open **Settings** → **Mods** tab
2. Click **"Open Mods Folder"**
3. Drop `.jar` or `.zip` files into the folder
4. Mods load automatically on next launch

### Customizing Your Experience

| Setting | Where | Options |
|---------|-------|---------|
| **Language** | Settings → Language | 5 languages |
| **Theme** | Settings → Theme | Dark / Light |
| **Layout** | Settings → Layout | Left / Right panels |
| **Background** | Settings → Background | Custom image |
| **Avatar** | Click profile picture | Custom image / Auto-generated |

---

## 🐛 Troubleshooting

### ❌ "Java not found"
**Solution:** Install Java from [java.com](https://www.java.com) or your package manager:
```bash
# Linux
sudo apt install openjdk-17-jre-headless

# macOS
brew install openjdk@17
```

### ❌ Network Error (offline mode)
**Solution:** Ametist works offline after downloading versions once. Check internet, then try again.

### ❌ Permission Error
**Solution:** Ensure write access to `.ametist_mc`:
```bash
chmod -R 755 ~/.ametist_mc
```

### ❌ Fabric/Forge Installation Failed
**Solution:** 
- Ensure version is supported (1.16.5+)
- Try a different Minecraft version
- Check Java version compatibility

### ❌ AppImage won't run on Linux
**Solution:** Grant execute permissions:
```bash
chmod +x AmetistLauncher-x86_64.AppImage
```

### ❌ EXE won't start on Windows
**Solution:**
- Run as Administrator
- Check if Windows Defender quarantined it
- Ensure .NET Framework is installed

### ❌ Out of Memory Error
**Solution:** Increase allocated RAM in launcher settings (try 6-8 GB)

---

## 🐞 Reporting Issues

Found a bug? Help us improve!
- **Open an Issue**: [GitHub Issues](https://github.com/ayzlol/ametist-launcher/issues)
- **Join Discussion**: [GitHub Discussions](https://github.com/ayzlol/ametist-launcher/discussions)
- **Include**: Your OS, Java version, Minecraft version, error message

---

## 📝 License

**MIT License** — Free for everyone, forever.

**Copyright © 2026 Thepan & Unfayd**

This project is open-source and you're free to:
- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Sublicense

**Requirement:** Include original license in distributions.

See [LICENSE](LICENSE) for full terms.

---

## 👥 Contributing

We ❤️ contributions! Here's how:

1. **Fork** the repository
2. **Create branch**: `git checkout -b feature/your-feature`
3. **Make changes** and test thoroughly
4. **Commit**: `git commit -m 'Add awesome feature'`
5. **Push**: `git push origin feature/your-feature`
6. **Pull Request**: Open a PR with description

---

## 🎉 Credits & Credits

**Developers:**
- **Unfayd** 👨‍💻 — Full-stack development
- **Thepan** 👨‍💻 — Core architecture & UI design

**Built with:**
- **CustomTkinter** — Modern GUI framework
- **minecraft-launcher-lib** — Minecraft integration
- **Pillow** — Image processing

---

## 📊 Version History

| Version | Release Date | Highlights |
|---------|--------------|-----------|
| **v1.2.1** | Aug 26, 2026 | Stable release: AppImage & EXE distributions |
| **v1.2.0** | Aug 23, 2026 | Multi-language, Forge & Quilt support |
| **v1.1.0** | Aug 15, 2026 | Mod management, customization |
| **v0.1.0** | Aug 04, 2026 | Beta: Vanilla & Fabric |

---

<div align="center">

### ✨ Made with Love for the Minecraft Community ✨

**Download Latest Release:** [Releases](https://github.com/ayzlol/ametist-launcher/releases)

**⭐ Star us on GitHub** to show your support!

</div>
