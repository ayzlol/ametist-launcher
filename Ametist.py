import os
import sys
import json
import uuid
import threading
import subprocess
import urllib.request
import urllib.error
import shutil
import platform
import time
import tkinter as tk
from tkinter import filedialog, messagebox

try:
    from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageEnhance
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

import customtkinter as ctk
import minecraft_launcher_lib as mll

# ============================================================
# PURE AMETIST THEME CONSTANTS
# ============================================================
BG_DARK = "#0f0616"
CARD_DARK = "#180d24"
INPUT_BG_DARK = "#241436"
BORDER_DARK = "#3d225c"
TEXT_DARK = "#eadbf7"
TEXT_SEC_DARK = "#b996e6"
ACCENT = "#9d4edd"
ACCENT_HOVER = "#7b2cbf"
OFFLINE_COLOR = "#a78bfa" # Açık mor / mavi tonu

# ============================================================
# SYSTEM OPTIMIZATION (RAM DETECTION)
# ============================================================
def get_system_ram_gb():
    try:
        if sys.platform == "win32":
            import ctypes
            class MEMORYSTATUSEX(ctypes.Structure):
                _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong),
                            ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                            ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                            ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                            ("sullAvailExtendedVirtual", ctypes.c_ulonglong)]
            stat = MEMORYSTATUSEX()
            stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
            return int(stat.ullTotalPhys / (1024**3))
        else:
            return int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024**3))
    except:
        return 4

# ============================================================
# TRANSLATIONS (EN, TR, RU, ES)
# ============================================================
TRANSLATIONS = {
    "en": {
        "welcome": "Welcome, {name}!", "version_type": "Version Type:", "version_label": "Versions:",
        "ram_label": "RAM Allocation:", "dynamic_ram": "Dynamic RAM Limit (PC Based)",
        "status_ready": "Ready", "launch_btn": "LAUNCH",
        "settings_title": "Settings", "game_path_label": "Game Files:",
        "downloading_files": "Downloading files...", "installing_fabric": "Installing mod loader...",
        "launching": "Launching...", "error": "Error: {error}", "no_java": "Java not found.",
        "about_tab": "About", "language_tab": "Language", "theme_tab": "Layout", "mods_tab": "Mods", "bg_tab": "Background",
        "select_bg": "Select Background", "reset_bg": "Reset", "close": "Close",
        "username_placeholder": "Username", "login_title": "AMETIST LOGIN",
        "select_avatar": "Select Avatar", "open_mods": "Open Mods Folder",
        "installed": "Downloaded", "not_installed": "Not Downloaded",
        "version_pos": "Menu Position:", "pos_left": "Left Panel", "pos_right": "Right Panel",
        "logout": "Change Account", "extra_versions": "Show Extra Versions (Snapshot etc.)",
        "sys_info_title": "System & Hardware Info", "launcher_version": "Ametist Launcher v1.2.1",
        "offline": "No Internet"
    },
    "tr": {
        "welcome": "Hoş geldin, {name}!", "version_type": "Sürüm Türü:", "version_label": "Sürümler:",
        "ram_label": "RAM Tahsisi:", "dynamic_ram": "PC'ye Göre Dinamik RAM Sınırı",
        "status_ready": "Hazır", "launch_btn": "BAŞLAT",
        "settings_title": "Ayarlar", "game_path_label": "Oyun Dosyaları:",
        "downloading_files": "Dosyalar indiriliyor...", "installing_fabric": "Mod yükleyici kuruluyor...",
        "launching": "Başlatılıyor...", "error": "Hata: {error}", "no_java": "Java bulunamadı.",
        "about_tab": "Hakkında", "language_tab": "Dil", "theme_tab": "Düzen", "mods_tab": "Modlar", "bg_tab": "Arkaplan",
        "select_bg": "Arka Plan Seç", "reset_bg": "Sıfırla", "close": "Kapat",
        "username_placeholder": "Kullanıcı adı", "login_title": "AMETIST GİRİŞ",
        "select_avatar": "Profil Resmi Seç", "open_mods": "Modlar Klasörünü Aç",
        "installed": "İndirildi", "not_installed": "İndirilmedi",
        "version_pos": "Menü Konumu:", "pos_left": "Sol Panel", "pos_right": "Sağ Panel",
        "logout": "Hesap Değiştir", "extra_versions": "Gelişmiş Sürümleri Göster (Snapshot vb.)",
        "sys_info_title": "Sistem ve Donanım Bilgileri", "launcher_version": "Ametist Launcher v1.2.1",
        "offline": "İnternet Yok"
    },
    "ru": {
        "welcome": "Добро пожаловать, {name}!", "version_type": "Тип версии:", "version_label": "Версии:",
        "ram_label": "Выделение ОЗУ:", "dynamic_ram": "Динамический лимит ОЗУ (ПК)",
        "status_ready": "Готов", "launch_btn": "ИГРАТЬ",
        "settings_title": "Настройки", "game_path_label": "Файлы игры:",
        "downloading_files": "Загрузка файлов...", "installing_fabric": "Установка мод-лоадера...",
        "launching": "Запуск...", "error": "Ошибка: {error}", "no_java": "Java не найдена.",
        "about_tab": "О программе", "language_tab": "Язык", "theme_tab": "Макет", "mods_tab": "Моды", "bg_tab": "Фон",
        "select_bg": "Выбрать фон", "reset_bg": "Сбросить", "close": "Закрыть",
        "username_placeholder": "Имя пользователя", "login_title": "AMETIST ВХОД",
        "select_avatar": "Выбрать аватар", "open_mods": "Открыть папку модов",
        "installed": "Загружено", "not_installed": "Не загружено",
        "version_pos": "Положение меню:", "pos_left": "Левая панель", "pos_right": "Правая панель",
        "logout": "Сменить аккаунт", "extra_versions": "Показать дополнительные версии (Snapshot и др.)",
        "sys_info_title": "Информация о системе", "launcher_version": "Ametist Launcher v1.2.1",
        "offline": "Нет интернета"
    },
    "es": {
        "welcome": "¡Bienvenido, {name}!", "version_type": "Tipo de versión:", "version_label": "Versiones:",
        "ram_label": "Asignación de RAM:", "dynamic_ram": "Límite de RAM dinámico (según PC)",
        "status_ready": "Listo", "launch_btn": "INICIAR",
        "settings_title": "Ajustes", "game_path_label": "Archivos del juego:",
        "downloading_files": "Descargando archivos...", "installing_fabric": "Instalando mod loader...",
        "launching": "Iniciando...", "error": "Error: {error}", "no_java": "Java no encontrado.",
        "about_tab": "Acerca de", "language_tab": "Idioma", "theme_tab": "Diseño", "mods_tab": "Mods", "bg_tab": "Fondo",
        "select_bg": "Seleccionar fondo", "reset_bg": "Restablecer", "close": "Cerrar",
        "username_placeholder": "Nombre de usuario", "login_title": "AMETIST INICIO DE SESIÓN",
        "select_avatar": "Seleccionar avatar", "open_mods": "Abrir carpeta de mods",
        "installed": "Descargado", "not_installed": "No descargado",
        "version_pos": "Posición del menú:", "pos_left": "Panel izquierdo", "pos_right": "Panel derecho",
        "logout": "Cambiar cuenta", "extra_versions": "Mostrar versiones extra (Snapshot, etc.)",
        "sys_info_title": "Info del Sistema y Hardware", "launcher_version": "Ametist Launcher v1.2.1",
        "offline": "Sin conexión"
    }
}

class ConfigManager:
    def __init__(self, mc_dir):
        self.mc_dir = mc_dir
        self.config_path = os.path.join(mc_dir, "ametist_config.json")
        self.config = self.load()
        defaults = {
            "language": "en", "avatar_path": "", "bg_path": "", "last_version_type": "Vanilla", 
            "last_version": "", "last_ram": "2 GB", "first_run": True, "username": "", 
            "user_data": None, "version_panel_pos": "left", "show_extra_versions": False,
            "dynamic_ram_limit": True
        }
        for k, v in defaults.items():
            if k not in self.config: self.config[k] = v
        self.save()

    def load(self):
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f: return json.load(f)
            except: return {}
        return {}

    def save(self):
        try:
            os.makedirs(self.mc_dir, exist_ok=True)
            with open(self.config_path, "w", encoding="utf-8") as f: json.dump(self.config, f, ensure_ascii=False, indent=2)
        except: pass

class FirstRunLanguageWindow(ctk.CTk):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.title("Ametist Launcher")
        self.geometry("400x320")
        self.configure(fg_color=BG_DARK)
        ctk.set_appearance_mode("Dark")
        frame = ctk.CTkFrame(self, fg_color=CARD_DARK)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        ctk.CTkLabel(frame, text="Select Language / Dil Seçin\nВыберите язык / Selecciona idioma", font=("Segoe UI", 15, "bold"), text_color=TEXT_DARK).pack(pady=15)
        
        langs = [("en", "English"), ("tr", "Türkçe"), ("ru", "Русский"), ("es", "Español")]
        for code, name in langs:
            ctk.CTkButton(frame, text=name, fg_color=INPUT_BG_DARK, hover_color=ACCENT, text_color=TEXT_DARK, command=lambda c=code: self.select(c)).pack(pady=4, padx=20, fill="x")

    def select(self, code):
        self.config_manager.config.update({"language": code, "first_run": False})
        self.config_manager.save()
        self.destroy()

class LoginWindow(ctk.CTk):
    def __init__(self, config_manager):
        super().__init__()
        self.cm = config_manager
        self.lang = config_manager.config.get("language", "en")
        self.title("Ametist Login")
        self.geometry("380x250")
        self.configure(fg_color=BG_DARK)
        ctk.set_appearance_mode("Dark")
        self.user_data = None
        self.show_input()

    def tr(self, key): return TRANSLATIONS.get(self.lang, TRANSLATIONS["en"]).get(key, key)

    def show_input(self):
        frame = ctk.CTkFrame(self, fg_color=CARD_DARK)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        ctk.CTkLabel(frame, text=self.tr("login_title"), font=("Segoe UI", 18, "bold"), text_color=ACCENT).pack(pady=(20, 15))
        self.entry = ctk.CTkEntry(frame, placeholder_text=self.tr("username_placeholder"), fg_color=INPUT_BG_DARK, border_color=BORDER_DARK, text_color=TEXT_DARK)
        self.entry.pack(pady=10, padx=20, fill="x")
        self.entry.bind("<Return>", lambda e: self.login())
        ctk.CTkButton(frame, text=self.tr("launch_btn"), fg_color=ACCENT, hover_color=ACCENT_HOVER, command=self.login).pack(pady=10, padx=20, fill="x")

    def login(self):
        username = self.entry.get().strip()
        if not username: return
        self.user_data = {"username": username, "uuid": str(uuid.uuid3(uuid.NAMESPACE_OID, f"OfflinePlayer:{username}")), "type": "Offline"}
        self.cm.config.update({"username": username, "user_data": self.user_data})
        self.cm.save()
        self.destroy()

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent, cm, lang, on_update):
        super().__init__(parent)
        self.parent = parent
        self.cm = cm
        self.lang = lang
        self.on_update = on_update
        self.title(self.tr("settings_title"))
        self.geometry("520x520")
        self.configure(fg_color=BG_DARK)
        
        tabview = ctk.CTkTabview(self, fg_color=CARD_DARK, segmented_button_selected_color=ACCENT, segmented_button_unselected_color=INPUT_BG_DARK, text_color=TEXT_DARK)
        tabview.pack(padx=20, pady=20, fill="both", expand=True)
        
        t_about = tabview.add(self.tr("about_tab"))
        t_lang = tabview.add(self.tr("language_tab"))
        t_theme = tabview.add(self.tr("theme_tab"))
        t_bg = tabview.add(self.tr("bg_tab"))
        t_mods = tabview.add(self.tr("mods_tab"))
        
        ctk.CTkLabel(t_about, text="Ametist Launcher v1.2.1\nAmetist Edition (Optimized)", font=("Segoe UI", 16, "bold"), text_color=TEXT_DARK).pack(pady=15)
        ctk.CTkButton(t_about, text=self.tr("logout"), fg_color="#b91c1c", hover_color="#991b1b", command=self.logout).pack(pady=20)

        self.lang_var = tk.StringVar(value=self.lang)
        for c, n in [("en", "English"), ("tr", "Türkçe"), ("ru", "Русский"), ("es", "Español")]:
            ctk.CTkRadioButton(t_lang, text=n, variable=self.lang_var, value=c, fg_color=ACCENT, command=self.save_cfg).pack(anchor="w", pady=5, padx=10)

        self.pos_var = tk.StringVar(value=self.cm.config.get("version_panel_pos", "left"))
        ctk.CTkLabel(t_theme, text=self.tr("version_pos"), font=("Segoe UI", 12, "bold"), text_color=TEXT_DARK).pack(anchor="w", pady=(5, 5), padx=10)
        ctk.CTkRadioButton(t_theme, text=self.tr("pos_left"), variable=self.pos_var, value="left", fg_color=ACCENT, command=self.save_cfg).pack(anchor="w", pady=5, padx=10)
        ctk.CTkRadioButton(t_theme, text=self.tr("pos_right"), variable=self.pos_var, value="right", fg_color=ACCENT, command=self.save_cfg).pack(anchor="w", pady=5, padx=10)
        
        self.extra_var = tk.BooleanVar(value=self.cm.config.get("show_extra_versions", False))
        ctk.CTkSwitch(t_theme, text=self.tr("extra_versions"), variable=self.extra_var, progress_color=ACCENT, command=self.save_cfg).pack(anchor="w", pady=(20, 10), padx=10)

        self.dyn_ram_var = tk.BooleanVar(value=self.cm.config.get("dynamic_ram_limit", True))
        ctk.CTkSwitch(t_theme, text=self.tr("dynamic_ram"), variable=self.dyn_ram_var, progress_color=ACCENT, command=self.save_cfg).pack(anchor="w", pady=10, padx=10)

        ctk.CTkButton(t_bg, text=self.tr("select_bg"), fg_color=ACCENT, hover_color=ACCENT_HOVER, command=self.select_bg).pack(pady=10, fill="x", padx=20)
        ctk.CTkButton(t_bg, text=self.tr("reset_bg"), fg_color=INPUT_BG_DARK, hover_color=BORDER_DARK, command=self.reset_bg).pack(pady=10, fill="x", padx=20)
        ctk.CTkButton(t_mods, text=self.tr("open_mods"), fg_color=ACCENT, hover_color=ACCENT_HOVER, command=self.open_mods).pack(pady=10)

    def tr(self, key): return TRANSLATIONS.get(self.lang, TRANSLATIONS["en"]).get(key, key)
    
    def save_cfg(self):
        self.cm.config.update({
            "language": self.lang_var.get(), 
            "version_panel_pos": self.pos_var.get(), 
            "show_extra_versions": self.extra_var.get(),
            "dynamic_ram_limit": self.dyn_ram_var.get()
        })
        self.cm.save()
        self.on_update()

    def select_bg(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg")])
        if path:
            self.cm.config["bg_path"] = path
            self.cm.save()
            self.on_update()
            
    def reset_bg(self):
        self.cm.config["bg_path"] = ""
        self.cm.save()
        self.on_update()
        
    def open_mods(self):
        p = os.path.join(self.parent.mc_dir, "mods")
        os.makedirs(p, exist_ok=True)
        if sys.platform == "win32": os.startfile(p)
        else: subprocess.Popen(["xdg-open" if sys.platform.startswith("linux") else "open", p])

    def logout(self):
        self.cm.config["user_data"] = None
        self.cm.save()
        self.destroy()
        self.parent.logout_user()

class AmetistLauncher(ctk.CTk):
    def __init__(self, user_data, cm):
        super().__init__()
        self.user_data = user_data
        self.cm = cm
        self.lang = self.cm.config.get("language", "en")
        
        self.title("Ametist Launcher v1.2.1")
        self.geometry("960x600")
        self.minsize(800, 500)
        ctk.set_appearance_mode("Dark")
        self.configure(fg_color=BG_DARK)
        
        self.mc_dir = os.path.join(os.getenv("APPDATA") if os.name == "nt" else os.path.expanduser("~"), ".ametist_mc")
        self.sys_ram = get_system_ram_gb()
        
        self.bg_canvas = tk.Canvas(self, highlightthickness=0, bg=BG_DARK)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_canvas.bind("<Configure>", self.on_window_resize)
        
        self.setup_ui()
        self.update_ui_state()
        self.start_internet_monitor()

    def tr(self, key): return TRANSLATIONS.get(self.lang, TRANSLATIONS["en"]).get(key, key)

    def on_window_resize(self, event):
        if self.cm.config.get("bg_path"): self.set_background(self.cm.config["bg_path"], event.width, event.height)

    def set_background(self, path, width=None, height=None):
        if not PIL_AVAILABLE or not path or not os.path.exists(path):
            self.bg_canvas.delete("all")
            return
        try:
            w, h = width or self.winfo_width() or 960, height or self.winfo_height() or 600
            if w < 20 or h < 20: return
            img = Image.open(path).convert("RGBA").resize((w, h), Image.Resampling.LANCZOS)
            img = ImageEnhance.Brightness(img).enhance(0.5)
            img = Image.alpha_composite(img, Image.new('RGBA', img.size, (15, 6, 22, 170)))
            self.bg_image_ref = ImageTk.PhotoImage(img)
            self.bg_canvas.delete("all")
            self.bg_canvas.create_image(0, 0, image=self.bg_image_ref, anchor="nw")
            self.bg_canvas.lower()
        except: pass

    def setup_ui(self):
        self.header = ctk.CTkFrame(self, fg_color=CARD_DARK, border_width=1, border_color=BORDER_DARK)
        self.header.pack(fill="x", padx=15, pady=(15, 5))
        
        self.avatar_ref = self.create_avatar()
        self.avatar_label = ctk.CTkLabel(self.header, image=self.avatar_ref, text="", cursor="hand2")
        self.avatar_label.pack(side="left", padx=10, pady=8)
        self.avatar_label.bind("<Button-1>", lambda e: self.select_avatar())
        
        self.lbl_welcome = ctk.CTkLabel(self.header, text="", font=("Segoe UI", 15, "bold"), text_color=TEXT_DARK)
        self.lbl_welcome.pack(side="left", padx=10)
        
        self.lbl_launcher_ver = ctk.CTkLabel(self.header, text=self.tr("launcher_version"), font=("Segoe UI", 12, "bold"), text_color=TEXT_SEC_DARK)
        self.lbl_launcher_ver.pack(side="right", padx=15)
        
        self.lbl_offline = ctk.CTkLabel(self.header, text="", font=("Segoe UI", 14, "bold"), text_color=OFFLINE_COLOR)
        self.lbl_offline.pack(side="right", padx=10)
        
        ctk.CTkButton(self.header, text="Settings", width=40, fg_color=INPUT_BG_DARK, hover_color=BORDER_DARK, command=self.open_settings).pack(side="right", padx=5, pady=8)

        self.content_container = ctk.CTkFrame(self, fg_color="transparent")
        self.content_container.pack(fill="both", expand=True, padx=15, pady=5)

        self.version_panel = ctk.CTkFrame(self.content_container, fg_color=CARD_DARK, border_width=1, border_color=BORDER_DARK, width=320)
        self.main_panel = ctk.CTkFrame(self.content_container, fg_color=CARD_DARK, border_width=1, border_color=BORDER_DARK)

        self.create_option_row(self.version_panel, self.tr("version_type"), ["Vanilla", "Fabric", "Forge", "Quilt"], "type_opt", 15, command=lambda _: self.update_version_options())
        
        self.version_scroll = ctk.CTkScrollableFrame(self.version_panel, fg_color=INPUT_BG_DARK, border_color=BORDER_DARK, corner_radius=6)
        self.version_scroll.pack(fill="both", expand=True, padx=15, pady=5)
        self.selected_version_var = tk.StringVar(value="")

        self.create_option_row(self.version_panel, self.tr("ram_label"), ["2 GB"], "ram_opt", 10)
        
        self.btn_launch = ctk.CTkButton(self.version_panel, text="", font=("Segoe UI", 16, "bold"), height=50, fg_color=ACCENT, hover_color=ACCENT_HOVER, command=self.start_launch)
        self.btn_launch.pack(padx=15, pady=15, fill="x", side="bottom")

        path_frame = ctk.CTkFrame(self.main_panel, fg_color="transparent", border_width=1, border_color=BORDER_DARK)
        path_frame.pack(fill="x", padx=20, pady=20)
        ctk.CTkLabel(path_frame, text=self.tr("game_path_label"), font=("Segoe UI", 11, "bold"), text_color=ACCENT).pack(anchor="w", padx=10, pady=(8, 2))
        ctk.CTkLabel(path_frame, text="%APPDATA%\\.ametist_mc" if os.name == "nt" else "~/.ametist_mc", font=("Consolas", 10), text_color=TEXT_DARK).pack(anchor="w", padx=10, pady=(0, 8))

        sys_frame = ctk.CTkFrame(self.main_panel, fg_color="transparent", border_width=1, border_color=BORDER_DARK)
        sys_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.lbl_sys_title = ctk.CTkLabel(sys_frame, text=self.tr("sys_info_title"), font=("Segoe UI", 11, "bold"), text_color=ACCENT)
        self.lbl_sys_title.pack(anchor="w", padx=10, pady=(8, 2))
        
        os_info = f"OS: {platform.system()} ({platform.release()}) - Arch: {platform.machine()}"
        ram_info = f"RAM: {self.sys_ram} GB"
        python_info = f"Python: {platform.python_version()}"
        
        self.lbl_sys_details = ctk.CTkLabel(sys_frame, text=f"{os_info}\n{ram_info}\n{python_info}", font=("Consolas", 10), text_color=TEXT_SEC_DARK, justify="left")
        self.lbl_sys_details.pack(anchor="w", padx=10, pady=(0, 8))

        self.lbl_status = ctk.CTkLabel(self.main_panel, text="", font=("Segoe UI", 12), text_color=TEXT_DARK)
        self.lbl_status.pack(anchor="w", padx=20, pady=(5, 5))
        
        self.progress = ctk.CTkProgressBar(self.main_panel, progress_color=ACCENT, fg_color=INPUT_BG_DARK)
        self.progress.pack(fill="x", padx=20, pady=(0, 10))
        self.progress.set(0)

        cfg = self.cm.config
        if cfg.get("last_version_type") in ["Vanilla", "Fabric", "Forge", "Quilt"]: self.type_opt.set(cfg["last_version_type"])

    def create_option_row(self, parent, label_text, values, attr_name, pady_top, command=None):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=15, pady=(pady_top, 2))
        lbl = ctk.CTkLabel(frame, text=label_text, font=("Segoe UI", 12, "bold"), text_color=TEXT_DARK, justify="left")
        lbl.pack(anchor="w", pady=(0, 2))
        opt = ctk.CTkOptionMenu(frame, values=values, fg_color=INPUT_BG_DARK, button_color=ACCENT, button_hover_color=ACCENT_HOVER, dropdown_fg_color=CARD_DARK, text_color=TEXT_DARK, command=command)
        opt.pack(fill="x")
        setattr(self, attr_name, opt)
        setattr(self, f"{attr_name}_lbl", lbl)

    def update_ui_state(self):
        self.lang = self.cm.config.get("language", "en")
        self.lbl_welcome.configure(text=self.tr("welcome").format(name=self.user_data["username"]))
        self.btn_launch.configure(text=self.tr("launch_btn"))
        self.lbl_status.configure(text=self.tr("status_ready"))
        self.type_opt_lbl.configure(text=self.tr("version_type"))
        self.lbl_launcher_ver.configure(text=self.tr("launcher_version"))
        self.lbl_sys_title.configure(text=self.tr("sys_info_title"))
        
        if hasattr(self, 'lbl_offline'):
            self.lbl_offline.configure(text=self.tr("offline") if getattr(self, 'is_offline', False) else "")
            
        pos = self.cm.config.get("version_panel_pos", "left")
        self.version_panel.pack_forget()
        self.main_panel.pack_forget()
        if pos == "left":
            self.version_panel.pack(side="left", fill="y", padx=(0, 10), pady=5)
            self.main_panel.pack(side="right", fill="both", expand=True, pady=5)
        else:
            self.main_panel.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=5)
            self.version_panel.pack(side="right", fill="y", pady=5)
            
        self.update_version_options()
        self.update_ram_options()
        self.set_background(self.cm.config.get("bg_path", ""))

    def update_ram_options(self):
        dyn_limit = self.cm.config.get("dynamic_ram_limit", True)
        if dyn_limit:
            max_ram = max(2, self.sys_ram - 2) if self.sys_ram > 2 else 2
            ram_list = [f"{i} GB" for i in range(2, max_ram + 1, 2)]
            if not ram_list: ram_list = ["2 GB"]
            lbl_txt = f"{self.tr('ram_label')}"
            self.ram_opt_lbl.configure(text_color=TEXT_SEC_DARK, font=("Segoe UI", 11, "bold"))
        else:
            ram_list = ["2 GB", "4 GB", "6 GB", "8 GB", "12 GB", "16 GB", "24 GB", "32 GB"]
            lbl_txt = self.tr('ram_label')
            self.ram_opt_lbl.configure(text_color=TEXT_DARK, font=("Segoe UI", 12, "bold"))

        self.ram_opt_lbl.configure(text=lbl_txt)
        self.ram_opt.configure(values=ram_list)
        
        last_ram = self.cm.config.get("last_ram", "4 GB")
        if last_ram in ram_list: self.ram_opt.set(last_ram)
        else: self.ram_opt.set(ram_list[-1] if dyn_limit else "4 GB")

    def create_avatar(self):
        if not PIL_AVAILABLE: return None
        path = self.cm.config.get("avatar_path", "")
        img = None
        if path and os.path.exists(path):
            try: img = Image.open(path).convert("RGBA").resize((40, 40), Image.Resampling.LANCZOS)
            except: pass
        if not img:
            img = Image.new("RGBA", (40, 40), (0,0,0,0))
            d = ImageDraw.Draw(img)
            d.ellipse((0,0,40,40), fill=ACCENT)
            try: font = ImageFont.truetype("arial.ttf", 20)
            except: font = ImageFont.load_default()
            d.text((12, 8), self.user_data["username"][0].upper(), fill="white", font=font)
        
        mask = Image.new("L", (40, 40), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, 40, 40), fill=255)
        out = Image.new("RGBA", (40, 40), (0, 0, 0, 0))
        out.paste(img, (0, 0), mask)
        return ctk.CTkImage(out, size=(40, 40))

    def select_avatar(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg")])
        if path:
            self.cm.config["avatar_path"] = path
            self.cm.save()
            self.avatar_label.configure(image=self.create_avatar())

    def start_internet_monitor(self):
        threading.Thread(target=self._check_internet_bg, daemon=True).start()
        self.after(15000, self.start_internet_monitor) # Her 15 saniyede bir

    def _check_internet_bg(self):
        offline = False
        try:
            urllib.request.urlopen("http://clients3.google.com/generate_204", timeout=1.5)
        except:
            offline = True
        
        self.after(0, lambda: self._apply_internet_state(offline))

    def _apply_internet_state(self, offline):
        changed = not hasattr(self, 'is_offline') or getattr(self, 'is_offline') != offline
        self.is_offline = offline
        if hasattr(self, 'lbl_offline'):
            self.lbl_offline.configure(text=self.tr("offline") if offline else "")
        if changed:
            self.update_version_options()

    def get_versions(self):
        # İlk çalışma anında hızlı kontrol
        if not hasattr(self, 'is_offline'):
            try:
                urllib.request.urlopen("http://clients3.google.com/generate_204", timeout=1.0)
                self.is_offline = False
            except:
                self.is_offline = True
            if hasattr(self, 'lbl_offline'):
                self.lbl_offline.configure(text=self.tr("offline") if self.is_offline else "")

        if not self.is_offline:
            try: 
                raw_v = mll.utils.get_version_list()
                show_all = self.cm.config.get("show_extra_versions", False)
                v_list = [v["id"] for v in raw_v if show_all or v["type"] == "release"]
                if not show_all: v_list = v_list[:25]
                else: v_list = v_list[:100]
            except: 
                self.is_offline = True
                if hasattr(self, 'lbl_offline'):
                    self.lbl_offline.configure(text=self.tr("offline"))

        if self.is_offline:
            v_set = set()
            try:
                ver_dir = os.path.join(self.mc_dir, "versions")
                if os.path.exists(ver_dir):
                    for d in os.listdir(ver_dir):
                        if os.path.isdir(os.path.join(ver_dir, d)):
                            if "fabric-loader-" in d: v_set.add(d.split("-")[-1])
                            elif "quilt-loader-" in d: v_set.add(d.split("-")[-1])
                            elif "forge-" in d: v_set.add(d.replace("forge-", "").split("-")[0])
                            else: v_set.add(d)
            except: pass
            
            def sort_key(x):
                try: return [int(i) for i in x.split('.') if i.isdigit()]
                except: return [0]
            v_list = sorted(list(v_set), reverse=True, key=sort_key)

        v_type = self.type_opt.get()
        result = []
        for v in v_list:
            if self.is_offline:
                result.append(f"{v} (Installed)")
            else:
                result.append(f"{v} ({'Installed' if self.is_installed(v, v_type) else 'Download'})")
        return result

    def update_version_options(self):
        for widget in self.version_scroll.winfo_children(): widget.destroy()
        versions = self.get_versions()
        last_v = self.cm.config.get("last_version", "")
        matched = [v for v in versions if v.startswith(last_v)]
        if matched: self.selected_version_var.set(matched[0].split()[0])
        elif versions: self.selected_version_var.set(versions[0].split()[0])
            
        for v in versions:
            ver_id = v.split()[0]
            is_dl = '✔' in v
            rb = ctk.CTkRadioButton(self.version_scroll, text=v, variable=self.selected_version_var, value=ver_id,
                                    font=("Segoe UI", 12), text_color=TEXT_DARK if is_dl else TEXT_SEC_DARK, fg_color=ACCENT)
            rb.pack(anchor="w", pady=4, padx=5)

    def open_settings(self):
        SettingsWindow(self, self.cm, self.lang, self.update_ui_state)

    def logout_user(self):
        self.destroy()
        login = LoginWindow(self.cm)
        login.mainloop()
        if login.user_data: AmetistLauncher(login.user_data, self.cm).mainloop()

    def get_jvm_args(self, ram_gb):
        xms = max(1, ram_gb // 2)
        return [
            f"-Xmx{ram_gb}G", f"-Xms{xms}G",
            "-XX:+UseG1GC", "-XX:+ParallelRefProcEnabled", "-XX:MaxGCPauseMillis=200",
            "-XX:+UnlockExperimentalVMOptions", "-XX:+DisableExplicitGC", "-XX:+AlwaysPreTouch",
            "-XX:G1NewSizePercent=30", "-XX:G1MaxNewSizePercent=40", "-XX:G1HeapRegionSize=8M",
            "-XX:G1ReservePercent=20", "-XX:G1HeapWastePercent=5", "-XX:G1MixedGCCountTarget=4",
            "-XX:InitiatingHeapOccupancyPercent=15", "-XX:G1MixedGCLiveThresholdPercent=90",
            "-XX:SurvivorRatio=32", "-XX:+PerfDisableSharedMem", "-XX:MaxTenuringThreshold=1"
        ]

    def is_installed(self, ver_id, v_type):
        try:
            if v_type == "Fabric":
                return os.path.exists(os.path.join(self.mc_dir, "versions", f"fabric-loader-{mll.fabric.get_latest_loader_version()}-{ver_id}"))
            elif v_type == "Forge":
                return os.path.exists(os.path.join(self.mc_dir, "versions", mll.forge.find_forge_version(ver_id) or "NONE"))
            elif v_type == "Quilt":
                return os.path.exists(os.path.join(self.mc_dir, "versions", f"quilt-loader-{mll.quilt.get_latest_loader_version()}-{ver_id}"))
            return os.path.exists(os.path.join(self.mc_dir, "versions", ver_id))
        except: return False

    def start_launch(self):
        if not self.selected_version_var.get(): return
        self.btn_launch.configure(state="disabled", fg_color=BORDER_DARK)
        threading.Thread(target=self.launch_thread, daemon=True).start()

    def launch_thread(self):
        ver, v_type = self.selected_version_var.get(), self.type_opt.get()
        ram = int(self.ram_opt.get().split()[0])
        self.cm.config.update({"last_version": ver, "last_version_type": v_type, "last_ram": f"{ram} GB"})
        self.cm.save()

        try:
            opts = {"username": self.user_data["username"], "uuid": self.user_data["uuid"], "jvmArguments": self.get_jvm_args(ram)}
            cb = {"setStatus": lambda s: self.after(0, lambda: self.lbl_status.configure(text=s)), 
                  "setProgress": lambda p: self.after(0, lambda: self.progress.set(p/100))}

            if not self.is_installed(ver, v_type):
                self.after(0, lambda: self.lbl_status.configure(text=self.tr("downloading_files")))
                mll.install.install_minecraft_version(ver, self.mc_dir, callback=cb)
                if v_type == "Fabric": mll.fabric.install_fabric(ver, self.mc_dir, callback=cb)
                elif v_type == "Forge": mll.forge.install_forge_version(mll.forge.find_forge_version(ver), self.mc_dir, callback=cb)
                elif v_type == "Quilt": mll.quilt.install_quilt(ver, self.mc_dir, callback=cb)

            if v_type == "Fabric": cmd = mll.command.get_minecraft_command(f"fabric-loader-{mll.fabric.get_latest_loader_version()}-{ver}", self.mc_dir, opts)
            elif v_type == "Forge": cmd = mll.command.get_minecraft_command(mll.forge.find_forge_version(ver), self.mc_dir, opts)
            elif v_type == "Quilt": cmd = mll.command.get_minecraft_command(f"quilt-loader-{mll.quilt.get_latest_loader_version()}-{ver}", self.mc_dir, opts)
            else: cmd = mll.command.get_minecraft_command(ver, self.mc_dir, opts)

            self.after(0, lambda: self.lbl_status.configure(text=self.tr("launching")))
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, **({"creationflags": subprocess.CREATE_NO_WINDOW} if os.name == "nt" else {}))
            
            self.after(500, self.update_version_options)
            self.after(2000, lambda: os._exit(0))
        except Exception as e:
            self.after(0, lambda: self.lbl_status.configure(text=f"Error: {e}"))
            self.btn_launch.configure(state="normal", fg_color=ACCENT)

if __name__ == "__main__":
    mc_dir = os.path.join(os.getenv("APPDATA") if os.name == "nt" else os.path.expanduser("~"), ".ametist_mc")
    cm = ConfigManager(mc_dir)
    if cm.config.get("first_run", True): FirstRunLanguageWindow(cm).mainloop()
    user_data = cm.config.get("user_data")
    if not user_data or not user_data.get("username"):
        login = LoginWindow(cm)
        login.mainloop()
        user_data = login.user_data
    if user_data and user_data.get("username"): AmetistLauncher(user_data, cm).mainloop()