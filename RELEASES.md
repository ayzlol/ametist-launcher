# Releases

Bu dosya Ametist Launcher’ın yayımlanan sürümlerini özetler. Hazır Windows ve Linux paketleri için [GitHub Releases sayfasını](https://github.com/ayzlol/ametist-launcher/releases) kullanabilirsin.

## v1.2.1 — Tam sürüm — 2026-08-26

Ametist Launcher v1.2.1, Windows ve Linux için hazır paketleri bulunan tam sürümdür. Launcher; Vanilla, Fabric, Forge ve Quilt sürümlerini yönetebilir.

### Dahil olanlar

- Offline kullanıcı adı ile giriş
- Vanilla, Fabric, Forge ve Quilt sürümlerini seçme ve başlatma
- İlk kullanımda gerekli Minecraft ve loader dosyalarını indirme
- İnternet bağlantısı olmadığında yerel kurulumları algılama
- Dinamik veya manuel RAM sınırı
- JVM performans seçenekleri
- Kurulu ve indirilebilir sürümlerin arayüzde ayırt edilmesi
- İngilizce, Türkçe, Rusça ve İspanyolca arayüz
- Koyu tasarım
- Menü panelini sol veya sağ tarafa alma
- Özel arka plan ve profil resmi
- Yerel mod klasörünü açma
- Sistem, işletim sistemi ve RAM bilgilerini görüntüleme

### İndirme

- **Windows:** `AmetistLauncher.exe` dosyasını indirip çalıştır.
- **Linux:** `AmetistLauncher-x86_64.AppImage` dosyasına çalıştırma izni verip çalıştır.

```bash
chmod +x AmetistLauncher-x86_64.AppImage
./AmetistLauncher-x86_64.AppImage
```

Hazır paketlerde Python ve proje bağımlılıkları bulunur. Minecraft için uyumlu Java Runtime Environment kurulumu gerekir. Dosyaların SHA-256 değerleri GitHub release sayfasında gösterilir.

### İlk kullanım notu

Yeni bir Minecraft sürümünü veya loader’ı ilk kez kurarken internet bağlantısı gerekir. Dosyalar indirildikten sonra Ametist bunları `.ametist_mc` klasöründeki yerel kurulumlardan algılar. İnternet bağlantısı olmadığında yalnızca bilgisayarda hazır bulunan sürümler gösterilir.

### Geri bildirim

Bir sorunla karşılaşırsan [Issues](https://github.com/ayzlol/ametist-launcher/issues) üzerinden işletim sistemini, Java sürümünü, Minecraft sürümünü, seçtiğin loader’ı ve hata mesajını paylaşabilirsin. Fikir ve öneriler için [GitHub Discussions](https://github.com/ayzlol/ametist-launcher/discussions) kullanılabilir.

## v0.1.0-beta — 2026-07-31

İlk geliştirme sürümüydü. Temel launcher akışı ve offline Vanilla/Fabric başlatma desteği içeriyordu.
