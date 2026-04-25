from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

# Import 10 Specialists from app.specialists
from app.specialists import (
    content_semantic_agent,
    technical_seo_agent,
    pr_community_agent,
    local_seo_agent,
    ecommerce_cro_agent,
    geo_sge_agent,
    video_search_agent,
    paid_media_agent,
    analytics_architect_agent,
    creative_director_agent,
)

# --- TIER 2: VP AGENT (DYNAMIC TASK ROUTER) ---

vp_omnichannel_agent = Agent(
    name="vp_omnichannel_search",
    model=Gemini(
        model="gemini-2.5-pro", # Upgrade ke Pro untuk routing analitis
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="VP of Omnichannel Search. Dynamic Task Router for 10 specialist agents.",
    instruction="""Anda adalah VP Omnichannel Search di agensi MAIO SEVO.
Anda bertindak sebagai orkestrator eksekusi setelah proposal disetujui.

Tugas Anda:
1. Menganalisis daftar 'sprint_tasks' yang didelegasikan oleh CMO.
2. Memilih secara dinamis dari 10 spesialis di katalog alat Anda untuk mengeksekusi tugas tersebut.
3. JANGAN memanggil agen yang tidak relevan dengan kebutuhan klien untuk efisiensi biaya.
4. Pastikan koordinasi antar spesialis berjalan lancar (misal: data riset keyword diberikan ke pembuat konten).

Katalog Spesialis Anda:
- content_semantic_agent: Riset keyword & Strategi Konten.
- technical_seo_agent: Audit teknis & Kanibalisasi.
- pr_community_agent: Backlink & Reddit.
- local_seo_agent: Google Maps & SEO Lokal.
- ecommerce_cro_agent: UX & Amazon SEO.
- geo_sge_agent: Schema & AI Overview optimization.
- video_search_agent: YouTube & TikTok.
- paid_media_agent: Iklan berbayar (Meta/Google).
- analytics_architect_agent: GA4 & GTM setup.
- creative_director_agent: Storyboarding & Visual strategy.""",
    tools=[
        AgentTool(agent=content_semantic_agent),
        AgentTool(agent=technical_seo_agent),
        AgentTool(agent=pr_community_agent),
        AgentTool(agent=local_seo_agent),
        AgentTool(agent=ecommerce_cro_agent),
        AgentTool(agent=geo_sge_agent),
        AgentTool(agent=video_search_agent),
        AgentTool(agent=paid_media_agent),
        AgentTool(agent=analytics_architect_agent),
        AgentTool(agent=creative_director_agent),
    ]
)
