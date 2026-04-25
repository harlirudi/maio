# DESIGN_SPEC.md: MAIO SEVO Neural Operating System (V2 Enterprise)

## 1. Overview
Sistem orkestrasi multi-agen tingkat lanjut untuk agensi pemasaran digital, dibangun di atas **Google ADK 2.0** dan berjalan di platform **GEAP**. Sistem ini mengutamakan efisiensi biaya kognitif dan profitabilitas agensi melalui Dynamic Routing.

## 2. Agent Hierarchy & Roles

### Tier 1: Strategic Client Interface
- **CMO Agent (Gemini 2.5 Pro):** Bertindak sebagai konsultan Socratic. Mengelola alur 'State Machine' dari Discovery, Negosiasi, hingga Delegasi Eksekusi.

### Tier 2: Management & Financials
- **AI CFO Agent (Gemini 2.5 Pro):** Penasihat finansial real-time. Menghitung COGS API berdasarkan beban compute (teks/vision) dan menetapkan batas bawah harga (Walk Away Price).
- **VP Omnichannel Search (Gemini 2.5 Pro):** Project Manager dinamis. Menggunakan *AgentTool* untuk hanya mengaktifkan spesialis yang relevan dengan brief, menghindari pemborosan token.

### Tier 3: Specialist Matrix (10 Units)
1. **content_semantic_agent:** Arsitektur klaster konten.
2. **technical_seo_agent:** Audit kesehatan situs & crawler.
3. **pr_community_agent:** Otoritas brand & Reddit engagement.
4. **local_seo_agent:** Optimasi Google Maps (GBP).
5. **ecommerce_cro_agent:** Psikologi konversi & Amazon SEO.
6. **geo_sge_agent:** Insinyur Knowledge Graph & AI Overviews.
7. **video_search_agent:** Algoritma visual YouTube & TikTok.
8. **paid_media_agent:** Arbitrase media & ROAS optimization.
9. **analytics_architect_agent:** Arsitek data (GA4/GTM).
10. **creative_director_agent:** Strategi visual & multichannel calendar.

## 3. Core Framework Implementation
- **Dynamic Task Routing:** Menggunakan pola *Conditional Delegation* (bukan paralel statis).
- **Session State Management:** Berbagi data riset (misal: keywords) antar agen melalui memori sesi ADK.
- **Financial Guardrail:** Integrasi COGS Calculator sebelum fase proposal.

## 4. Technical Stack
- **Platform:** GEAP (Gemini Enterprise Agent Platform)
- **Framework:** Google ADK 2.0
- **Auth:** Level 2 Option A (API Key)
- **Deployment Target:** Managed Agent Runtime
