# Arsitektur Sistem GEAP Agency Core (MAIO SEVO) - Final Enterprise Version

Sistem ini telah dimutakhirkan menjadi struktur agensi pemasaran digital bertenaga AI yang lengkap, berbasis laba, dan memiliki pembagian tugas kognitif yang sangat spesifik.

## 1. Hierarki & Peran (Command Center)

```text
[App: geap-agency-core]
│
├── [Tier 1: Strategic Client Interface]
│   └── cmo_agent (Gemini 2.5 Pro)
│       ├── Peran: Konsultan, Negosiator, & Client Handler.
│       ├── Alur: Discovery -> Pricing (via CFO) -> Proposal -> Delegation (via VP).
│       └── Alat bantu: finance_ops_agent, vp_omnichannel_agent.
│
├── [Tier 2: Managerial & Operational]
│   ├── finance_ops_agent (Gemini 2.5 Pro) - THE AI CFO
│   │   ├── Peran: Kalkulator COGS API & Dynamic Pricing Advisor.
│   │   └── Output: JSON (Target Price, Walk Away Price).
│   │
│   └── vp_omnichannel_agent (Gemini 2.5 Pro) - THE DYNAMIC ROUTER
│       ├── Peran: Orkestrator Eksekusi & Project Manager.
│       ├── Sifat: Dynamic Routing (Hanya mengaktifkan agen yang relevan).
│       └── Membawahi: 10 Spesialis (sebagai Tools).
│
└── [Tier 3: 10 Specialist Units]
    ├── content_semantic_agent: Riset Keyword & Klaster Strategi.
    ├── technical_seo_agent: Audit Teknis & Efisiensi Crawler.
    ├── pr_community_agent: Digital PR, Backlink, & Reddit Engagement.
    ├── local_seo_agent: SEO Lokal & Google Business Profile.
    ├── ecommerce_cro_agent: UX Audit, Amazon SEO, & Conversion Rate.
    ├── geo_sge_agent: Optimasi SGE, AI Overviews, & Schema.
    ├── video_search_agent: YouTube & TikTok Algorithmic Optimization.
    ├── paid_media_agent: Iklan Berbayar (Meta/Google) & Bidding.
    ├── analytics_architect_agent: GA4, GTM, & Data Pipeline.
    └── creative_director_agent: Visual Strategy & Multichannel Content Calendar.
```

## 2. Dynamic Pricing & Financial Guardrail

Sistem ini memproteksi agensi dari kerugian biaya API melalui **CFO Agent**.
- **Estimasi COGS:** CFO menghitung biaya penggunaan model Pro, Flash, dan Image Gen API sebelum tawaran dikirim.
- **Dynamic Margin:** Margin disesuaikan dengan tingkat kesulitan tugas (85% untuk teknis/multimodal, 50% untuk komoditas).

## 3. Dynamic Task Routing (Cost & Token Efficiency)

Berbeda dengan sistem paralel statis, **VP Omnichannel** hanya akan membangunkan agen spesialis yang secara eksplisit diminta oleh CMO. Jika klien hanya ingin SEO Lokal, maka unit *Video Search* atau *Paid Media* tidak akan menyala, menghemat ribuan token kognitif.

## 4. Lokasi Kode & Referensi
- `app/agent.py`: Root CMO.
- `app/cfo_agent.py`: Finansial.
- `app/vp_omnichannel.py`: Orkestrasi Eksekusi.
- `app/specialists.py`: Definisi 10 Agen Spesialis.
- `docs/TASK_TO_AGENT_MAPPING.md`: Daftar 100 task Single Grain yang dipetakan ke agen.
