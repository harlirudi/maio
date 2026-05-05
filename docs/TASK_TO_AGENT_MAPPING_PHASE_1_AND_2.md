# MAIO Task to Agent Mapping: Phase 1 (Proposal) & Phase 2 (Execution)

Dokumen ini memetakan seluruh aset script Python dari repositori `ericosiu_skills` (Single Grain) ke dalam 19 Spesialis MAIO. Pemetaan ini dibagi menjadi dua fase operasional: **Pre-Sales (Proposal)** dan **Execution (Delivery)**.

---

## Prinsip Utama
1. **Multi-Tenancy:** Setiap script harus menerima `client_id` untuk mengisolasi data di `./workspaces/{client_id}/`.
2. **Fungsi Ganda:** Spesialis yang sama mengerjakan riset proposal (Fase 1) dan eksekusi kampanye (Fase 2) menggunakan toolset yang berbeda.
3. **Human-in-the-Loop (HitL):** Tool eksekusi di Fase 2 akan menghasilkan draf yang memerlukan persetujuan Operator sebelum dipublikasikan.

---

## Lapis C-Suite (Decision Makers)

| Role | Tanggung Jawab Utama | Tool Terkait (Finance Ops) |
| :--- | :--- | :--- |
| **CMO (Ardi)** | Discovery Klien, Strategi Makro, Approval Final JSON. | `call_analyzer.py` (Evaluasi kualitas draf). |
| **VP Finance** | Perhitungan COGS, Margin, Pricing Tiers, Profitabilitas. | `cfo-analyzer.py`, `scenario-modeler.py`. |

---

## Lapis 5 VP & 19 Spesialis (Execution Units)

### 1. VP Search (SEO & SEM Strategy)
Mengarahkan traffic organik dan berbayar berbasis niat pencarian.

| Spesialis | Fokus | Tool Fase 1 (Proposal) | Tool Fase 2 (Eksekusi) |
| :--- | :--- | :--- | :--- |
| **Technical SEO** | Kesehatan Web & Crawling | `gsc_client.py` (Audit) | API GSC Monitoring |
| **Content SEO** | Keyword Gap & Trends | `content_attack_brief.py` | `trend_scout.py` (Alert harian) |
| **Local & E-comm SEO** | Katalog & Google Maps | Custom GMB Scraper | Product Feed Optimizer |

### 2. VP Paid Media (Instant Traffic & Scale)
Manajemen budget iklan dan eksperimen performa.

| Spesialis | Fokus | Tool Fase 1 (Proposal) | Tool Fase 2 (Eksekusi) |
| :--- | :--- | :--- | :--- |
| **Meta Ads Specialist** | Facebook & Instagram | `growth-engine` (Scenario) | Ad Spend Monitor |
| **Google Ads Specialist** | Search, Display, YouTube | `gsc_client.py` (Keyword) | Bidding Optimizer |
| **TikTok & Short Ads** | Viral Paid Content | `yt-competitive-analysis` | Hook/Creative Builder |
| **Programmatic** | Native & Display | `cross-signal-detector.py` | Media Buying Pipeline |

### 3. VP Content & Media (Brand & Authority)
Pusat pabrik konten dan narasi merek.

| Spesialis | Fokus | Tool Fase 1 (Proposal) | Tool Fase 2 (Eksekusi) |
| :--- | :--- | :--- | :--- |
| **Content Strategy** | Pilar Konten & Ideasi | `autoresearch.py` | `quote-mining-engine.py` |
| **Organic Social** | Twitter, LinkedIn, IG | `content-eval` (Ideasi) | `content-transform.py`, `x-longform-post` |
| **Video/Multimedia** | Video Pendek & Podcast | `analyze.py` (YouTube) | `shortform_pipeline.py`, `podcast_pipeline.py`, `video_clipper.py` |
| **Copywriting** | Teks Persuasif & Naskah | `content-quality-scorer.py`| `autoresearch.py` (Iterasi draf) |

### 4. VP CRO & Web (Conversion & Experience)
Mengoptimalkan pengalaman pengguna untuk menjadi leads.

| Spesialis | Fokus | Tool Fase 1 (Proposal) | Tool Fase 2 (Eksekusi) |
| :--- | :--- | :--- | :--- |
| **Web Analytics** | Data Tracking & ROI | `revenue_attribution.py` | `autogrowth-weekly-scorecard.py` |
| **UI/UX & A/B Test** | Audit Konversi & Tes | `cro_audit.py` | `experiment-engine.py` |
| **Landing Page Spec** | Struktur & Wireframe | `clone-site` (Recon) | JSON Component Drafter |

### 5. VP RevOps (Revenue & Automation)
Infrastruktur sales, CRM, dan sistem outbound.

| Spesialis | Fokus | Tool Fase 1 (Proposal) | Tool Fase 2 (Eksekusi) |
| :--- | :--- | :--- | :--- |
| **CRM & Automation** | Alur Kerja & Webhook | `lead-enricher.py` | `rb2b_webhook_ingest.py`, `rb2b_instantly_router.py` |
| **Outbound Lead Gen** | Pencarian Prospek Baru | `trigger_prospector.py` | `lead-pipeline.py`, `cascade-enricher.py` |
| **Revenue Intel** | Analisis Sales Call | `gong_insight_pipeline.py`| `deal_resurrector.py` |
| **Sales Enablement** | Pitch Deck & Pricing | `value_pricing_packager.py`| `generate-deck.py` |
| **Data Integrator** | SQL & Machine Learning | `icp_learning_analyzer.py`| Cross-Client Dashboard |

---

## Logika Folder Kerja (Workspace)

Setiap aksi spesialis akan menghasilkan output di:
`./workspaces/{client_id}/{vp_name}/{specialist_name}/`

Contoh:
`./workspaces/toko_sepatu/content/video_specialist/clips/viral_hook_1.mp4`

---

## Alur Persetujuan (Operator Loop)
1. **Agent** menghasilkan file di folder `pending_approval`.
2. **Agent** memanggil `ask_user` untuk memberitahu Operator.
3. **Operator** meninjau file.
4. **Agent** memindahkan file ke folder `production` dan mengeksekusi script pengiriman (API/SMTP).
