# Job Tracker & Automation

[English](README.md) | [Türkçe](README_TR.md)

İlan kaydeden, beceri eşleşmesini açıklayan ve ilanı saved, applied, interview veya rejected durumları arasında ilerleten üretime yakın takip API'si.

![Demo](docs/demo.svg)

## Teknolojiler
Python, FastAPI, Pydantic, Playwright entegrasyon sınırı, SQLite/PostgreSQL'e hazır kalıcılık sınırı, Docker, pytest ve GitHub Actions. MVP deterministik testler için bellekte çalışır; sonraki adaptör ilanları veritabanına kaydeder ve retry'lı Playwright collector/scheduler ekler.

## API ve çalıştırma
- POST /api/v1/jobs ilanı kaydeder ve eşleşen becerileri döndürür.
- PATCH /api/v1/jobs/{id}/status?status=applied durum günceller.
- GET /api/v1/jobs dashboard akışını listeler.

    pip install -e ".[dev]"
    uvicorn app.main:app --reload
    pytest -q

Docker: docker compose up --build. API dokümanı: /docs.

Gelecek collector yalnızca gerçek maaş bilgisini kabul etmeli; token, gönüllü ve ücretsiz ilanları elemelidir.

