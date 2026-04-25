# Konsep ADK: Dynamic Task Router (VP Omnichannel)

Dokumen ini mendemonstrasikan bagaimana membangun VP Agent (Tier 2) yang cerdas menggunakan ADK. Alih-alih menjalankan semua spesialis, VP ini hanya akan memicu agen yang relevan berdasarkan instruksi CMO.

---

### Implementasi Strategis (ADK 1.x / 2.0 Hybrid)

Dalam arsitektur ini, kita tidak menggunakan `ParallelAgent` statis. Kita menggunakan **VP Agent (LlmAgent)** sebagai orkestrator yang memiliki akses ke 10 spesialis sebagai **AgentTools**.

#### Struktur Kode Mockup (Python)

```python
from google.adk.agents import Agent
from google.adk.tools import AgentTool
from google.adk.models import Gemini

# 1. Inisialisasi 10 Spesialis (Contoh 2 saja)
content_semantic_agent = Agent(name="content_semantic_agent", ...)
ecommerce_cro_agent = Agent(name="ecommerce_cro_agent", ...)
# ... (inisialisasi 8 agen lainnya)

# 2. Bungkus Spesialis menjadi Tools
# Ini memungkinkan VP memanggil mereka hanya jika dibutuhkan.
tools_katalog = [
    AgentTool(agent=content_semantic_agent),
    AgentTool(agent=ecommerce_cro_agent),
    # ... (tambah 8 AgentTool lainnya)
]

# 3. Definisikan VP sebagai Dynamic Router
vp_omnichannel_pro = Agent(
    name="vp_omnichannel_search",
    model=Gemini(
        model="gemini-2.5-pro", # UPGRADE: Butuh penalaran tinggi untuk memilah task
    ),
    description="VP Operasional Agensi. Menganalisis kebutuhan task dan memanggil spesialis yang tepat.",
    instruction="""Anda adalah VP Omnichannel Search.
Tugas Anda:
1. Baca daftar 'sprint_tasks' yang diberikan oleh CMO.
2. Identifikasi agen spesialis mana yang dibutuhkan dari katalog alat Anda.
3. Panggil agen tersebut satu per satu atau secara paralel (menggunakan alat yang tersedia).
4. JANGAN memanggil agen yang tidak relevan dengan brief untuk menghemat resource dan waktu klien.

Katalog Spesialis Anda:
- content_semantic_agent: Untuk riset keyword dan penulisan.
- ecommerce_cro_agent: Untuk Amazon SEO dan optimasi konversi.
- ... (jelaskan 8 lainnya di sini)
""",
    tools=tools_katalog # Semua spesialis kini menjadi 'Alat' bagi VP
)
```

---

### Mengapa Arsitektur Ini Unggul?

1.  **Efisiensi Token & Biaya:** Jika klien hanya meminta "Optimasi Google Maps", VP hanya akan memanggil `local_seo_agent`. Sembilan agen lainnya tetap "tidur", sehingga tidak ada penggunaan token model Pro yang sia-sia.
2.  **Penanganan Brief Campuran:** Jika klien meminta "SEO Lokal + Iklan Facebook", VP cukup cerdas untuk memanggil `local_seo_agent` DAN `paid_media_agent` secara berurutan.
3.  **Skalabilitas:** Jika di masa depan Anda ingin menambah agen ke-11 (misalnya: *Voice Search Specialist*), Anda cukup menambahkannya ke daftar `tools` VP tanpa perlu merombak alur kerja CMO.
4.  **Kepatuhan ADK 2.0:** Pendekatan ini selaras dengan prinsip *Function Calling* di ADK 2.0, di mana LLM memutuskan jalur eksekusi terbaik secara dinamis.

---
**Status Dokumen:** Rancangan Disetujui (Draft).
