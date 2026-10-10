# Job Tracker & Automation

[English](README.md) | [Türkçe](README_TR.md) | [Deutsch](README_DE.md)

## English
**Purpose**  
A job tracking API that lets users save listings, see matched skills, and move listings through workflow states (saved, applied, interview, rejected).

**Verified features**  
- `POST /api/v1/jobs` saves a listing and returns matched skills.  
- `PATCH /api/v1/jobs/{id}/status?status=...` updates the workflow state.  
- `GET /api/v1/jobs` lists the dashboard feed.  
- Salary text is parsed into currency and a numeric range; listings marked volunteer, unpaid, equity‑only, token‑only or project‑token are returned with `is_paid=false` so they can be excluded before applying.  
- Interactive API documentation is available at `/docs`.  
- The project can be run with Docker Compose.

**Stack**  
Python, FastAPI, Pydantic, Playwright‑ready ingestion boundary, SQLite/PostgreSQL‑ready persistence boundary, Docker, pytest, GitHub Actions.

**Setup / Usage**  
```bash
# Install dependencies (including dev extras)
pip install -e ".[dev]"

# Run the API locally with hot reload
uvicorn app.main:app --reload

# Or start with Docker Compose
docker compose up --build
```
Access the interactive docs at `http://localhost:8000/docs`.

**Testing**  
Run the test suite with:
```bash
pytest -q
```

**Limitations**  
The current MVP keeps records in memory to ensure deterministic tests. A planned adapter will add persistent storage (SQLite/PostgreSQL) and schedule Playwright collectors with retries.

**License**  
See the `LICENSE` file for details.

## Türkçe
**Purpose**  
Kullanıcıların ilan kaydedebileceği, eşleşen yetenekleri görebileceği ve ilanları kayıtlı, başvuru, mülakat, reddedilmiş durumlar arasında taşıyabileceği bir iş takibi API'si.

**Doğrulanmış özellikler**  
- `POST /api/v1/jobs` bir ilanı kaydeder ve eşleşen yetenekleri döndürür.  
- `PATCH /api/v1/jobs/{id}/status?status=...` iş akışı durumunu günceller.  
- `GET /api/v1/jobs` kontrol paneli akışını listeler.  
- Maaş metni para birimi ve sayısal aralığa ayrıştırılır; gönüllü, ücretsiz, sadece hisse, sadece token veya proje‑token olarak işaretlenen ilanlar `is_paid=false` döndürülür ve başvuru öncesi filtrelenebilir.  
- Etkileşimli API dokümantasyonu `/docs` adresinde sunulur.  
- Proje Docker Compose ile çalıştırılabilir.

**Yığın**  
Python, FastAPI, Pydantic, Playwright‑tahmin hazır giriş sınırı, SQLite/PostgreSQL‑tahmin hazır kalıcılık sınırı, Docker, pytest, GitHub Actions.

**Kurulum / Kullanım**  
```bash
# Bağımlılıkları yükle (dev ekstraları dahil)
pip install -e ".[dev]"

# Yerel olarak API'yi hot reload ile çalıştır
uvicorn app.main:app --reload

# Ya da Docker Compose ile başlat
docker compose up --build
```
Etkileşimli dokümantasyona `http://localhost:8000/docs` adresinden erişin.

**Test**  
Test paketini şu şekilde çalıştırın:
```bash
pytest -q
```

**Sınırlamalar**  
Şu anki MVP, deterministik testler için bellek içinde kayıt tutar. Planlanan adaptör, kalıcı depolama (SQLite/PostgreSQL) ekleyecek ve Playwright toplucularını yeniden deneme mekanizmasıyla zamanlayacaktır.

**Lisans**  
Detaylar için `LICENSE` dosyasına bakın.

## Deutsch
**Purpose**  
Eine Job‑Tracking‑API, die es Benutzern ermöglicht, Einträge zu speichern, passende Fähigkeiten anzuzeigen und Einträge durch die Zustände gespeichert, beworben, Vorstellungsgespräch oder abgelehnt zu bewegen.

**Verifizierte Funktionen**  
- `POST /api/v1/jobs` speichert ein Listing und gibt die übereinstimmenden Fähigkeiten zurück.  
- `PATCH /api/v1/jobs/{id}/status?status=...` aktualisiert den Workflow‑Status.  
- `GET /api/v1/jobs` listet das Dashboard‑Feed.  
- Der Gehalts‑Text wird in Währung und numerischen Bereich geparsed; Einträge, die als freiwillig, unbezahlte, nur Aktien, nur Token oder Projekt‑Token gekennzeichnet sind, erhalten `is_paid=false` und können vor der Bewerbung ausgefiltert werden.  
- Interaktive API‑Dokumentation steht unter `/docs` zur Verfügung.  
- Das Projekt kann mit Docker Compose gestartet werden.

**Stack**  
Python, FastAPI, Pydantic, Playwright‑bereite Eingabegrenze, SQLite/PostgreSQL‑bereite Persistenzgrenze, Docker, pytest, GitHub Actions.

**Einrichtung / Nutzung**  
```bash
# Abhängigkeiten installieren (inkl. dev‑Extras)
pip install -e ".[dev]"

# API lokal mit Hot‑Reload starten
uvicorn app.main:app --reload

# Oder über Docker Compose starten
docker compose up --build
```
Die interaktive Dokumentation ist unter `http://localhost:8000/docs` erreichbar.

**Tests**  
Führe die Testsuite aus mit:
```bash
pytest -q
```

**Einschränkungen**  
Der aktuelle MVP speichert Datensätze im Speicher für deterministische Tests. Ein geplanter Adapter wird persistente Speicherung (SQLite/PostgreSQL) hinzufügen und Playwright‑Sammler mit Wiederholungslogik zeitplanen.

**Lizenz**  
Siehe die `LICENSE` Datei.
