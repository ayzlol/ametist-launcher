import os
import sys
import json
import uuid
import threading
import subprocess
import urllib.request
import urllib.error
import webbrowser
import shutil
from tkinter import filedialog, messagebox

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

import customtkinter as ctk
import minecraft_launcher_lib as mll

# ============================================================
# CONSTANTS & THEMES
# ============================================================
BG_DARK = "#0c0c0e"
CARD_DARK = "#151518"
INPUT_BG_DARK = "#1c1c21"
BORDER_DARK = "#27272a"
TEXT_DARK = "#e4e4e7"
TEXT_SEC_DARK = "#a1a1aa"

BG_LIGHT = "#f0f0f0"
CARD_LIGHT = "#ffffff"
INPUT_BG_LIGHT = "#e8e8e8"
BORDER_LIGHT = "#d0d0d0"
TEXT_LIGHT = "#1a1a1a"
TEXT_SEC_LIGHT = "#555555"

ACCENT = "#7c3aed"
ACCENT_HOVER = "#6d28d9"
GREEN = "#22c55e"
RED = "#ef4444"

# ============================================================
# TRANSLATIONS
# ============================================================
TRANSLATIONS = {
    "tr": {
        "welcome_first": "Ametist Launcher'a Hoş Geldin!",
        "choose_language_first": "Devam etmek için dil seçin:",
        "login_title": "GİRİŞ",
        "offline_login": "Offline Giriş",
        "offline_title": "Offline Giriş",
        "username_placeholder": "Kullanıcı adı",
        "continue": "Devam Et",
        "welcome": "Hoş geldin, {name}!",
        "version_type": "Sürüm Türü:",
        "version_label": "Minecraft Sürümü:",
        "ram_label": "RAM Tahsisi:",
        "status_ready": "Hazır",
        "launch_btn": "BAŞLAT",
        "checking_version": "{version} kontrol ediliyor...",
        "installing_fabric": "Fabric kuruluyor...",
        "applying_flags": "Başlatma hazırlanıyor...",
        "launching": "Minecraft başlatılıyor...",
        "error": "Hata: {error}",
        "fabric_not_found": "Seçilen sürüm için Fabric bulunamadı veya desteklenmiyor.",
        "settings_title": "Ayarlar",
        "about_tab": "Hakkında",
        "language_tab": "Dil",
        "theme_tab": "Tema",
        "mods_tab": "Modlar",
        "about_text": "Ametist Launcher v5 (Fabric)",
        "developers": "Geliştiriciler:",
        "dev_names": "Unfayd & Thepan",
        "select_language": "Dil:",
        "select_avatar": "Avatar / Cilt Seç",
        "close": "Kapat",
        "theme_label": "Tema:",
        "dark_theme": "Koyu",
        "light_theme": "Açık",
        "open_mods_folder": "Modlar Klasörünü Aç",
        "mods_folder_created": "Modlar klasörü oluşturuldu.",
        "no_java": "Java bulunamadı. Lütfen Java'yı yükleyin.",
        "java_version": "Java Sürümü: {version}",
        "permission_error": "Dosya izin hatası: {error}",
        "network_error": "Ağ hatası: {error}",
        "mods_list_title": "Yüklü Modlar",
        "no_mods": "Hiç mod yok.",
    },
    "en": {
        "welcome_first": "Welcome to Ametist Launcher!",
        "choose_language_first": "Select your language to continue:",
        "login_title": "LOGIN",
        "offline_login": "Offline Login",
        "offline_title": "Offline Login",
        "username_placeholder": "Username",
        "continue": "Continue",
        "welcome": "Welcome, {name}!",
        "version_type": "Version Type:",
        "version_label": "Minecraft Version:",
        "ram_label": "RAM Allocation:",
        "status_ready": "Ready",
        "launch_btn": "LAUNCH",
        "checking_version": "Checking {version}...",
        "installing_fabric": "Installing Fabric...",
        "applying_flags": "Preparing launch...",
        "launching": "Launching Minecraft...",
        "error": "Error: {error}",
        "fabric_not_found": "Fabric not found or not supported for selected version.",
        "settings_title": "Settings",
        "about_tab": "About",
        "language_tab": "Language",
        "theme_tab": "Theme",
        "mods_tab": "Mods",
        "about_text": "Ametist Launcher v5 (Fabric)",
        "developers": "Developers:",
        "dev_names": "Unfayd & Thepan",
        "select_language": "Language:",
        "select_avatar": "Select Avatar / Skin",
        "close": "Close",
        "theme_label": "Theme:",
        "dark_theme": "Dark",
        "light_theme": "Light",
        "open_mods_folder": "Open Mods Folder",
        "mods_folder_created": "Mods folder created.",
        "no_java": "Java not found. Please install Java.",
        "java_version": "Java Version: {version}",
        "permission_error": "Permission error: {error}",
        "network_error": "Network error: {error}",
        "mods_list_title": "Installed Mods",
        "no_mods": "No mods installed.",
    },
    "zh": {
        "welcome_first": "欢迎使用 Ametist 启动器！",
        "choose_language_first": "请选择语言以继续：",
        "login_title": "登录",
        "offline_login": "离线登录",
        "offline_title": "离线登录",
        "username_placeholder": "用户名",
        "continue": "继续",
        "welcome": "欢迎, {name}!",
        "version_type": "版本类型：",
        "version_label": "Minecraft 版本：",
        "ram_label": "内存分配：",
        "status_ready": "就绪",
        "launch_btn": "启动",
        "checking_version": "正在检查 {version}...",
        "installing_fabric": "正在安装 Fabric...",
        "applying_flags": "正在准备启动...",
        "launching": "正在启动 Minecraft...",
        "error": "错误: {error}",
        "fabric_not_found": "找不到所选版本的 Fabric 或不支持。",
        "settings_title": "设置",
        "about_tab": "关于",
        "language_tab": "语言",
        "theme_tab": "主题",
        "mods_tab": "模组",
        "about_text": "Ametist Launcher v5 (Fabric)",
        "developers": "开发者：",
        "dev_names": "Unfayd & Thepan",
        "select_language": "语言：",
        "select_avatar": "选择头像 / 皮肤",
        "close": "关闭",
        "theme_label": "主题：",
        "dark_theme": "深色",
        "light_theme": "浅色",
        "open_mods_folder": "打开模组文件夹",
        "mods_folder_created": "模组文件夹已创建。",
        "no_java": "未找到 Java，请安装 Java。",
        "java_version": "Java 版本：{version}",
        "permission_error": "权限错误：{error}",
        "network_error": "网络错误：{error}",
        "mods_list_title": "已安装模组",
        "no_mods": "没有模组。",
    },
    "ru": {
        "welcome_first": "Добро пожаловать в Ametist Launcher!",
        "choose_language_first": "Выберите язык для продолжения:",
        "login_title": "ВХОД",
        "offline_login": "Офлайн вход",
        "offline_title": "Офлайн вход",
        "username_placeholder": "Имя пользователя",
        "continue": "Продолжить",
        "welcome": "Добро пожаловать, {name}!",
        "version_type": "Тип версии:",
        "version_label": "Версия Minecraft:",
        "ram_label": "Выделение RAM:",
        "status_ready": "Готов",
        "launch_btn": "ЗАПУСК",
        "checking_version": "Проверка {version}...",
        "installing_fabric": "Установка Fabric...",
        "applying_flags": "Подготовка к запуску...",
        "launching": "Запуск Minecraft...",
        "error": "Ошибка: {error}",
        "fabric_not_found": "Fabric для выбранной версии не найден или не поддерживается.",
        "settings_title": "Настройки",
        "about_tab": "О программе",
        "language_tab": "Язык",
        "theme_tab": "Тема",
        "mods_tab": "Моды",
        "about_text": "Ametist Launcher v5 (Fabric)",
        "developers": "Разработчики:",
        "dev_names": "Unfayd & Thepan",
        "select_language": "Язык:",
        "select_avatar": "Выбрать аватар / скин",
        "close": "Закрыть",
        "theme_label": "Тема:",
        "dark_theme": "Тёмная",
        "light_theme": "Светлая",
        "open_mods_folder": "Открыть папку модов",
        "mods_folder_created": "Папка модов создана.",
        "no_java": "Java не найдена. Установите Java.",
        "java_version": "Версия Java: {version}",
        "permission_error": "Ошибка доступа: {error}",
        "network_error": "Ошибка сети: {error}",
        "mods_list_title": "Установленные моды",
        "no_mods": "Модов нет.",
    }
}

# ============================================================
# CONFIG MANAGER
# ============================================================
class ConfigManager:
    def __init__(self, mc_dir):
        self.mc_dir = mc_dir
        self.config_path = os.path.join(mc_dir, "ametist_config.json")
        self.config = self.load()
        defaults = {
            "language": "",
            "avatar_path": "",
            "last_version_type": "Vanilla",
            "last_version": "",
            "last_ram": "4 GB",
            "first_run": True,
            "theme": "Dark",
            "username": "",
        }
        for k, v in defaults.items():
            if k not in self.config:
                self.config[k] = v
        self.save()

    def load(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save(self):
        try:
            os.makedirs(self.mc_dir, exist_ok=True)
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Config save error: {e}")

# ============================================================
# FIRST-RUN LANGUAGE WINDOW
# ============================================================
class FirstRunLanguageWindow(ctk.CTk):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.selected_lang = None
        self.title("Ametist Launcher")
        self.geometry("400x360")
        self.resizable(False, False)
        self.configure(fg_color=BG_DARK)
        self.setup_ui()

    def setup_ui(self):
        frame = ctk.CTkFrame(self, fg_color=CARD_DARK, corner_radius=8, border_width=1, border_color=BORDER_DARK)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        ctk.CTkLabel(frame, text="Ametist Launcher", font=("Segoe UI", 18, "bold"), text_color=TEXT_DARK).pack(pady=(30, 5))
        ctk.CTkLabel(frame, text="Select your language to continue", font=("Segoe UI", 12), text_color=TEXT_SEC_DARK).pack(pady=(0, 20))
        langs = [("tr", "Türkçe"), ("en", "English"), ("zh", "中文"), ("ru", "Русский")]
        for code, name in langs:
            ctk.CTkButton(
                frame, text=name, font=("Segoe UI", 13, "bold"),
                fg_color=INPUT_BG_DARK, hover_color="#25252c", border_color=BORDER_DARK, border_width=1,
                text_color=TEXT_DARK, height=40, corner_radius=6,
                command=lambda c=code: self.select_language(c)
            ).pack(padx=30, pady=6, fill="x")

    def select_language(self, code):
        self.config_manager.config["language"] = code
        self.config_manager.config["first_run"] = False
        self.config_manager.save()
        self.selected_lang = code
        self.destroy()

# ============================================================
# LOGIN WINDOW (Offline only)
# ============================================================
class LoginWindow(ctk.CTk):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.current_lang = self.config_manager.config.get("language", "en")
        self.title("Ametist Launcher")
        self.geometry("380x320")
        self.resizable(False, False)
        self.configure(fg_color=BG_DARK)
        self.user_data = None
        self.setup_ui()

    def tr(self, key):
        return TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"]).get(key, key)

    def setup_ui(self):
        frame = ctk.CTkFrame(self, fg_color=CARD_DARK, corner_radius=8, border_width=1, border_color=BORDER_DARK)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        ctk.CTkLabel(frame, text=self.tr("login_title"), font=("Segoe UI", 17, "bold"), text_color=TEXT_DARK).pack(pady=(25, 20))
        ctk.CTkLabel(frame, text=self.tr("offline_title"), font=("Segoe UI", 14), text_color=TEXT_DARK).pack(pady=(0, 10))
        self.entry_username = ctk.CTkEntry(
            frame, placeholder_text=self.tr("username_placeholder"),
            fg_color=INPUT_BG_DARK, border_color=BORDER_DARK, text_color=TEXT_DARK,
            height=38, corner_radius=6)
        self.entry_username.pack(padx=25, pady=10, fill="x")
        self.entry_username.insert(0, self.config_manager.config.get("username", "Player"))
        ctk.CTkButton(
            frame, text=self.tr("continue"), font=("Segoe UI", 12, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_HOVER, height=40, corner_radius=6,
            command=self.save_offline
        ).pack(padx=25, pady=20, fill="x")

    def save_offline(self):
        username = self.entry_username.get().strip()
        if not username:
            username = "Player"
        self.config_manager.config["username"] = username
        self.config_manager.save()
        offline_uuid = str(uuid.uuid3(uuid.NAMESPACE_OID, f"OfflinePlayer:{username}"))
        self.user_data = {"username": username, "uuid": offline_uuid, "token": ""}
        self.destroy()

# ============================================================
# SETTINGS WINDOW
# ============================================================
class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent, config_manager, current_lang, on_language_change, on_theme_change):
        super().__init__(parent)
        self.parent = parent
        self.config_manager = config_manager
        self.current_lang = current_lang
        self.on_language_change = on_language_change
        self.on_theme_change = on_theme_change
        self.configure(fg_color=BG_DARK)
        self.title(self.tr("settings_title"))
        self.geometry("560x500")
        self.resizable(False, False)
        self.setup_ui()
        self.grab_set()

    def tr(self, key):
        return TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"]).get(key, key)

    def setup_ui(self):
        frame = ctk.CTkFrame(self, fg_color=CARD_DARK, corner_radius=8, border_width=1, border_color=BORDER_DARK)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.tabview = ctk.CTkTabview(
            frame, fg_color=CARD_DARK,
            segmented_button_fg_color=INPUT_BG_DARK,
            segmented_button_selected_color=ACCENT,
            segmented_button_selected_hover_color=ACCENT_HOVER,
            segmented_button_unselected_hover_color="#25252c",
            text_color=TEXT_DARK
        )
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)

        # About tab
        about_tab = self.tabview.add(self.tr("about_tab"))
        self.setup_about_tab(about_tab)
        # Language tab
        lang_tab = self.tabview.add(self.tr("language_tab"))
        self.setup_language_tab(lang_tab)
        # Theme tab
        theme_tab = self.tabview.add(self.tr("theme_tab"))
        self.setup_theme_tab(theme_tab)
        # Mods tab
        mods_tab = self.tabview.add(self.tr("mods_tab"))
        self.setup_mods_tab(mods_tab)

        ctk.CTkButton(
            frame, text=self.tr("close"), font=("Segoe UI", 12, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_HOVER, height=34, corner_radius=6,
            command=self.destroy
        ).pack(padx=20, pady=(0, 15), fill="x")

    def setup_about_tab(self, parent):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(expand=True)
        ctk.CTkLabel(container, text=self.tr("about_text"), font=("Segoe UI", 20, "bold"), text_color=TEXT_DARK).pack(pady=(30, 10))
        ctk.CTkLabel(container, text=self.tr("developers"), font=("Segoe UI", 13), text_color=TEXT_SEC_DARK).pack(pady=(10, 4))
        ctk.CTkLabel(container, text=self.tr("dev_names"), font=("Segoe UI", 15, "bold"), text_color=TEXT_DARK).pack(pady=(0, 10))
        ctk.CTkFrame(container, fg_color=BORDER_DARK, height=2, width=180).pack(pady=10)

    def setup_language_tab(self, parent):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(expand=True, fill="both", padx=20, pady=20)
        ctk.CTkLabel(container, text=self.tr("select_language"), font=("Segoe UI", 13, "bold"), text_color=TEXT_DARK).pack(anchor="w", pady=(10, 10))
        lang_options = {"tr": "Türkçe", "en": "English", "zh": "中文", "ru": "Русский"}
        self.lang_var = ctk.StringVar(value=self.current_lang)
        for code, display in lang_options.items():
            ctk.CTkRadioButton(
                container, text=display, variable=self.lang_var, value=code,
                font=("Segoe UI", 13), text_color=TEXT_DARK, fg_color=ACCENT, border_color=BORDER_DARK,
                hover_color=ACCENT_HOVER, command=self.change_language
            ).pack(anchor="w", pady=8, padx=10)

    def change_language(self):
        new_lang = self.lang_var.get()
        if new_lang != self.current_lang:
            self.current_lang = new_lang
            self.config_manager.config["language"] = new_lang
            self.config_manager.save()
            self.on_language_change(new_lang)
            self.title(self.tr("settings_title"))

    def setup_theme_tab(self, parent):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(expand=True, fill="both", padx=20, pady=20)
        ctk.CTkLabel(container, text=self.tr("theme_label"), font=("Segoe UI", 13, "bold"), text_color=TEXT_DARK).pack(anchor="w", pady=(10, 10))
        current_theme = self.config_manager.config.get("theme", "Dark")
        self.theme_var = ctk.StringVar(value=current_theme)
        themes = [("Dark", self.tr("dark_theme")), ("Light", self.tr("light_theme"))]
        for value, display in themes:
            ctk.CTkRadioButton(
                container, text=display, variable=self.theme_var, value=value,
                font=("Segoe UI", 13), text_color=TEXT_DARK, fg_color=ACCENT, border_color=BORDER_DARK,
                hover_color=ACCENT_HOVER, command=self.change_theme
            ).pack(anchor="w", pady=8, padx=10)

    def change_theme(self):
        new_theme = self.theme_var.get()
        if new_theme != self.config_manager.config.get("theme"):
            self.config_manager.config["theme"] = new_theme
            self.config_manager.save()
            self.on_theme_change(new_theme)

    def setup_mods_tab(self, parent):
        container = ctk.CTkFrame(parent, fg_color="transparent")
        container.pack(expand=True, fill="both", padx=20, pady=20)
        btn_open = ctk.CTkButton(
            container, text=self.tr("open_mods_folder"), font=("Segoe UI", 12, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_HOVER, height=36, corner_radius=6,
            command=self.open_mods_folder
        )
        btn_open.pack(pady=10)
        self.mods_listbox = ctk.CTkTextbox(
            container, fg_color=INPUT_BG_DARK, text_color=TEXT_DARK,
            border_color=BORDER_DARK, border_width=1, corner_radius=6, height=150
        )
        self.mods_listbox.pack(fill="both", expand=True, pady=10)
        self.refresh_mods_list()

    def open_mods_folder(self):
        mods_dir = os.path.join(self.parent.mc_dir, "mods")
        try:
            os.makedirs(mods_dir, exist_ok=True)
            if sys.platform == "win32":
                os.startfile(mods_dir)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", mods_dir])
            else:
                subprocess.Popen(["xdg-open", mods_dir])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open mods folder: {e}")

    def refresh_mods_list(self):
        mods_dir = os.path.join(self.parent.mc_dir, "mods")
        self.mods_listbox.delete("1.0", "end")
        if os.path.exists(mods_dir):
            mods = [f for f in os.listdir(mods_dir) if f.endswith((".jar", ".zip"))]
            if mods:
                self.mods_listbox.insert("1.0", "\n".join(mods))
            else:
                self.mods_listbox.insert("1.0", self.tr("no_mods"))
        else:
            self.mods_listbox.insert("1.0", self.tr("no_mods"))

# ============================================================
# MAIN LAUNCHER
# ============================================================
class AmetistLauncher(ctk.CTk):
    def __init__(self, user_data, config_manager):
        super().__init__()
        self.user_data = user_data
        self.config_manager = config_manager
        self.current_lang = self.config_manager.config.get("language", "en")
        self.title("Ametist Launcher")
        self.geometry("720x520")
        self.resizable(False, False)
        self.mc_dir = os.path.join(
            os.getenv("APPDATA") if os.name == "nt" else os.path.expanduser("~"),
            ".ametist_mc"
        )
        self.avatar_image_ref = None
        self.all_versions = []
        self.destroying = False

        self.apply_theme(self.config_manager.config.get("theme", "Dark"))
        self.setup_ui()
        self.load_saved_settings()
        self.check_java_installed()

    def tr(self, key):
        return TRANSLATIONS.get(self.current_lang, TRANSLATIONS["en"]).get(key, key)

    def apply_theme(self, theme):
        if theme == "Light":
            ctk.set_appearance_mode("Light")
            self.bg = BG_LIGHT
            self.card = CARD_LIGHT
            self.input_bg = INPUT_BG_LIGHT
            self.border = BORDER_LIGHT
            self.text = TEXT_LIGHT
            self.text_sec = TEXT_SEC_LIGHT
        else:
            ctk.set_appearance_mode("Dark")
            self.bg = BG_DARK
            self.card = CARD_DARK
            self.input_bg = INPUT_BG_DARK
            self.border = BORDER_DARK
            self.text = TEXT_DARK
            self.text_sec = TEXT_SEC_DARK
        self.configure(fg_color=self.bg)

    def refresh_ui_texts(self):
        if self.destroying: return
        self.title_label.configure(text=self.tr("welcome").format(name=self.user_data["username"]))
        self.type_label.configure(text=self.tr("version_type"))
        self.version_label.configure(text=self.tr("version_label"))
        self.ram_label.configure(text=self.tr("ram_label"))
        self.launch_btn.configure(text=self.tr("launch_btn"))
        current = self.status_label.cget("text")
        if current in ["Hazır", "Ready", "就绪", "Готов"]:
            self.status_label.configure(text=self.tr("status_ready"))

    def on_language_change(self, new_lang):
        self.current_lang = new_lang
        self.refresh_ui_texts()

    def on_theme_change(self, new_theme):
        self.apply_theme(new_theme)
        for widget in self.winfo_children(): widget.destroy()
        self.setup_ui()
        self.load_saved_settings()
        self.refresh_ui_texts()

    def setup_ui(self):
        header = ctk.CTkFrame(self, fg_color=self.card, corner_radius=8, border_width=1, border_color=self.border)
        header.pack(fill="x", padx=20, pady=(20, 10))
        avatar_path = self.config_manager.config.get("avatar_path", "")
        self.avatar_image_ref = self.create_avatar_image(avatar_path)
        self.avatar_label = ctk.CTkLabel(header, image=self.avatar_image_ref, text="", cursor="hand2")
        self.avatar_label.pack(side="left", padx=(15, 10), pady=10)
        self.avatar_label.bind("<Button-1>", lambda e: self.select_avatar())
        self.title_label = ctk.CTkLabel(
            header, text=self.tr("welcome").format(name=self.user_data["username"]),
            font=("Segoe UI", 16, "bold"), text_color=self.text)
        self.title_label.pack(side="left", padx=5, pady=12)
        ctk.CTkButton(
            header, text=self.tr("settings_title"), font=("Segoe UI", 12, "bold"),
            fg_color=self.input_bg, hover_color="#25252c", border_color=self.border, border_width=1,
            text_color=self.text, height=32, corner_radius=6, command=self.open_settings
        ).pack(side="right", padx=15, pady=10)

        main = ctk.CTkFrame(self, fg_color=self.card, corner_radius=8, border_width=1, border_color=self.border)
        main.pack(padx=20, pady=10, fill="both", expand=True)

        self.type_label = ctk.CTkLabel(main, text=self.tr("version_type"), font=("Segoe UI", 12, "bold"), text_color=self.text)
        self.type_label.pack(anchor="w", padx=25, pady=(20, 4))
        self.type_option = ctk.CTkOptionMenu(
            main, values=["Vanilla", "Fabric"],
            fg_color=self.input_bg, button_color=ACCENT, button_hover_color=ACCENT_HOVER,
            dropdown_fg_color=self.card, dropdown_text_color=self.text, text_color=self.text,
            height=36, corner_radius=6, command=self.on_type_changed)
        self.type_option.pack(fill="x", padx=25, pady=(0, 14))
        self.type_option.set("Vanilla")

        self.version_label = ctk.CTkLabel(main, text=self.tr("version_label"), font=("Segoe UI", 12, "bold"), text_color=self.text)
        self.version_label.pack(anchor="w", padx=25, pady=(6, 4))
        self.all_versions = self.get_available_versions()
        self.version_option = ctk.CTkOptionMenu(
            main, values=self.all_versions,
            fg_color=self.input_bg, button_color=ACCENT, button_hover_color=ACCENT_HOVER,
            dropdown_fg_color=self.card, dropdown_text_color=self.text, text_color=self.text,
            height=36, corner_radius=6)
        self.version_option.pack(fill="x", padx=25, pady=(0, 14))
        if self.all_versions: self.version_option.set(self.all_versions[0])

        self.ram_label = ctk.CTkLabel(main, text=self.tr("ram_label"), font=("Segoe UI", 12, "bold"), text_color=self.text)
        self.ram_label.pack(anchor="w", padx=25, pady=(6, 4))
        self.ram_option = ctk.CTkOptionMenu(
            main, values=["2 GB", "4 GB", "6 GB", "8 GB", "12 GB", "16 GB"],
            fg_color=self.input_bg, button_color=ACCENT, button_hover_color=ACCENT_HOVER,
            dropdown_fg_color=self.card, dropdown_text_color=self.text, text_color=self.text,
            height=36, corner_radius=6)
        self.ram_option.pack(fill="x", padx=25, pady=(0, 14))
        self.ram_option.set("4 GB")

        self.status_label = ctk.CTkLabel(main, text=self.tr("status_ready"), font=("Segoe UI", 11), text_color=self.text_sec)
        self.status_label.pack(anchor="w", padx=25, pady=(18, 4))
        self.progress_bar = ctk.CTkProgressBar(main, progress_color=ACCENT, fg_color=self.input_bg, height=5, corner_radius=3)
        self.progress_bar.pack(fill="x", padx=25, pady=(0, 20))
        self.progress_bar.set(0)

        self.launch_btn = ctk.CTkButton(
            self, text=self.tr("launch_btn"), font=("Segoe UI", 14, "bold"),
            fg_color=ACCENT, hover_color=ACCENT_HOVER, text_color="#ffffff",
            height=44, corner_radius=8, command=self.start_launch_thread)
        self.launch_btn.pack(padx=20, pady=(8, 20), fill="x")

    def on_type_changed(self, choice):
        self.config_manager.config["last_version_type"] = choice
        self.config_manager.save()

    def load_saved_settings(self):
        cfg = self.config_manager.config
        if cfg.get("last_version_type") in ["Vanilla", "Fabric"]:
            self.type_option.set(cfg["last_version_type"])
        if cfg.get("last_version") and cfg["last_version"] in self.all_versions:
            self.version_option.set(cfg["last_version"])
        if cfg.get("last_ram"):
            self.ram_option.set(cfg["last_ram"])

    def create_avatar_image(self, image_path, size=(48, 48)):
        if PIL_AVAILABLE and image_path and os.path.exists(image_path):
            try:
                img = Image.open(image_path).convert("RGBA")
                img = img.resize(size, Image.Resampling.LANCZOS)
                mask = Image.new("L", size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, size[0], size[1]), fill=255)
                output = Image.new("RGBA", size, (0, 0, 0, 0))
                output.paste(img, (0, 0), mask)
                return ctk.CTkImage(output, size=size)
            except Exception as e:
                print(f"Avatar error: {e}")
        if PIL_AVAILABLE:
            img = Image.new("RGBA", size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            draw.ellipse((0, 0, size[0], size[1]), fill=ACCENT)
            try:
                initial = self.user_data.get("username", "P")[0].upper()
                font = None
                for font_name in ["SegoeUI.ttf", "Arial.ttf", "arial.ttf", "DejaVuSans.ttf", "FreeSans.ttf"]:
                    try:
                        font = ImageFont.truetype(font_name, 24)
                        break
                    except: continue
                if font is None: font = ImageFont.load_default()
            except Exception:
                font = ImageFont.load_default()
                initial = "P"
            bbox = draw.textbbox((0, 0), initial, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            draw.text(((size[0] - tw) // 2, (size[1] - th) // 2 - 2), initial, fill="white", font=font)
            return ctk.CTkImage(img, size=size)
        return None

    def select_avatar(self):
        path = filedialog.askopenfilename(
            title=self.tr("select_avatar"),
            filetypes=[("Images", "*.png *.jpg *.jpeg *.gif"), ("All files", "*.*")])
        if path:
            self.config_manager.config["avatar_path"] = path
            self.config_manager.save()
            new_avatar = self.create_avatar_image(path)
            self.avatar_image_ref = new_avatar
            self.avatar_label.configure(image=new_avatar)
            
            # Custom Skin Loader integration
            try:
                username = self.user_data.get("username", "Player")
                skin_dir = os.path.join(self.mc_dir, "CustomSkinLoader", "LocalSkin", "skins")
                os.makedirs(skin_dir, exist_ok=True)
                skin_dest = os.path.join(skin_dir, f"{username}.png")
                
                if PIL_AVAILABLE:
                    img = Image.open(path).convert("RGBA")
                    img.save(skin_dest, "PNG")
                else:
                    shutil.copy(path, skin_dest)
            except Exception as e:
                print(f"Skin copy error: {e}")

    def open_settings(self):
        SettingsWindow(self, self.config_manager, self.current_lang, self.on_language_change, self.on_theme_change)

    def get_available_versions(self):
        try:
            versions = mll.utils.get_version_list()
            release_versions = [v["id"] for v in versions if v["type"] == "release"]
            return release_versions[:30]
        except Exception as e:
            messagebox.showerror("Network Error", self.tr("network_error").format(error=str(e)))
            return ["1.21", "1.20.4", "1.20.2", "1.20.1", "1.19.4", "1.18.2", "1.16.5"]

    def check_java_installed(self):
        try:
            result = subprocess.run(["java", "-version"], capture_output=True, text=True, timeout=5)
            if result.returncode != 0: raise Exception("Java not found")
            version_line = result.stderr.splitlines()[0] if result.stderr else result.stdout.splitlines()[0]
            self.java_available = True
            self.java_version = version_line.replace("java version ", "").replace("openjdk version ", "").strip('"')
        except Exception:
            self.java_available = False
            self.java_version = "Unknown"
            messagebox.showwarning("Java Missing", self.tr("no_java"))

    def log_status(self, text, progress=None):
        if self.destroying: return
        try:
            self.status_label.configure(text=text)
            if progress is not None: self.progress_bar.set(progress)
        except Exception: pass

    def safe_log_status(self, text, progress=None):
        if self.destroying: return
        try: self.after(0, lambda: self.log_status(text, progress))
        except Exception: pass

    def start_launch_thread(self):
        if not self.java_available:
            messagebox.showerror("Error", self.tr("no_java"))
            return
        self.launch_btn.configure(state="disabled", fg_color="#3B0764")
        threading.Thread(target=self.launch_game, daemon=True).start()

    def get_jvm_args(self, ram_gb):
        xms = max(1, ram_gb // 2)
        return [
            f"-Xmx{ram_gb}G", f"-Xms{xms}G",
            "-XX:+UseG1GC", "-XX:+ParallelRefProcEnabled",
            "-XX:MaxGCPauseMillis=200", "-XX:+DisableExplicitGC"
        ]

    def launch_game(self):
        version = self.version_option.get()
        version_type = self.type_option.get()
        ram_gb = int(self.ram_option.get().split()[0])
        self.config_manager.config["last_version_type"] = version_type
        self.config_manager.config["last_version"] = version
        self.config_manager.config["last_ram"] = self.ram_option.get()
        self.config_manager.save()
        try:
            player_uuid = self.user_data.get("uuid", "")
            if not player_uuid: player_uuid = str(uuid.uuid3(uuid.NAMESPACE_OID, f"OfflinePlayer:{self.user_data['username']}"))
            options = {
                "username": self.user_data["username"],
                "uuid": player_uuid,
                "token": self.user_data.get("token", ""),
            }
            callback = {
                "setStatus": lambda s: self.safe_log_status(s),
                "setProgress": lambda p: self.safe_log_status(None, p / 100),
                "setMax": lambda v: None
            }
            if version_type == "Vanilla":
                self.safe_log_status(self.tr("checking_version").format(version=version), 0.0)
                mll.install.install_minecraft_version(version, self.mc_dir, callback=callback)
                options["jvmArguments"] = self.get_jvm_args(ram_gb)
                command = mll.command.get_minecraft_command(version, self.mc_dir, options)
            elif version_type == "Fabric":
                self.safe_log_status(self.tr("checking_version").format(version=version), 0.0)
                mll.install.install_minecraft_version(version, self.mc_dir, callback=callback)
                self.safe_log_status(self.tr("installing_fabric"), 0.0)
                try:
                    mll.fabric.install_fabric(version, self.mc_dir, callback=callback)
                    loader_version = mll.fabric.get_latest_loader_version()
                    fabric_version = f"fabric-loader-{loader_version}-{version}"
                except Exception as e:
                    raise Exception(f"{self.tr('fabric_not_found')} ({e})")
                options["jvmArguments"] = self.get_jvm_args(ram_gb)
                command = mll.command.get_minecraft_command(fabric_version, self.mc_dir, options)
            else:
                raise Exception("Unknown version type")
            
            self.safe_log_status(self.tr("applying_flags"), 0.9)
            self.safe_log_status(self.tr("launching"), 1.0)
            pop_kwargs = {}
            if os.name == "nt": pop_kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
            process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **pop_kwargs)
            self.destroying = True
            self.after(1500, self.quit_and_destroy)
        except PermissionError as e:
            self.safe_log_status(self.tr("permission_error").format(error=str(e)), 0)
            messagebox.showerror("Error", self.tr("permission_error").format(error=str(e)))
            self.launch_btn.configure(state="normal", fg_color=ACCENT)
        except urllib.error.URLError as e:
            self.safe_log_status(self.tr("network_error").format(error=str(e)), 0)
            messagebox.showerror("Error", self.tr("network_error").format(error=str(e)))
            self.launch_btn.configure(state="normal", fg_color=ACCENT)
        except Exception as e:
            self.safe_log_status(self.tr("error").format(error=str(e)), 0)
            messagebox.showerror("Error", self.tr("error").format(error=str(e)))
            self.launch_btn.configure(state="normal", fg_color=ACCENT)
            import traceback
            traceback.print_exc()

    def quit_and_destroy(self):
        try:
            self.destroying = True
            self.quit()
            self.destroy()
        except Exception: pass
        os._exit(0)

# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    mc_dir = os.path.join(
        os.getenv("APPDATA") if os.name == "nt" else os.path.expanduser("~"),
        ".ametist_mc"
    )
    config_manager = ConfigManager(mc_dir)

    if config_manager.config.get("first_run", True) or not config_manager.config.get("language"):
        lang_app = FirstRunLanguageWindow(config_manager)
        lang_app.mainloop()

    login_app = LoginWindow(config_manager)
    login_app.mainloop()

    if login_app.user_data:
        app = AmetistLauncher(login_app.user_data, config_manager)
        app.mainloop()