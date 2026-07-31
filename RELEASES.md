# Releases

## v0.1.0-beta — Beta İlk Sürüm

Tarih: 2026-07-31

Kısa özet:
- Ametist Launcher beta ilk sürümü (offline-only). Vanilla & Fabric için temel launcher işlevleri içerir.

Nasıl çalıştırılır:
1. Python 3.11+ yüklü ise:
   - pip install -r requirements.txt
   - python Ametist.py
2. Windows için `run.bat`, Linux/macOS için `run.sh` kullanılabilir.

Bilinen notlar / uyarılar:
- Bu bir beta sürümüdür; bazı özellikler eksik veya kararlı olmayabilir.
- Eğer kullanıcıların kolay çalıştırmasını istiyorsan, PyInstaller ile ikili (exe) paketleri oluşturup release'e eklemeyi öneririm.

Yapılabilecekler (öneri):
- Binaries (Windows/Linux/macOS) oluşturup GitHub Release'e asset olarak ekle.
- SHA256 checksum dosyası ekle.
- CHANGELOG.md oluşturup versiyon geçmişini takip et.
- README.md içinde sürüm bilgisi ve kurulum talimatlarını genişlet.

Eğer isterseniz, ben artefakt (exe/zip) hazırlayıp release oluşturma komutlarını da verebilirim veya bir GitHub Action workflow ile otomatik release kurulumunu ekleyebilirim.
