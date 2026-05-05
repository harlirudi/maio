from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

# Placeholder specialists - will be implemented in app/specialists/search/
# For now, we define the VP and its routing logic.

from app.specialists.search.content_strategy_agent import content_strategy_agent
from app.specialists.search.technical_seo_agent import technical_seo_agent
from app.specialists.search.digital_pr_agent import digital_pr_agent
from app.specialists.search.aeo_agent import aeo_agent
from app.specialists.search.programmatic_seo_agent import pseo_agent

search_vp_agent = Agent(
    name="search_vp_agent",
    model=Gemini(
        model="gemini-2.5-pro",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="VP of Search (Organic, Programmatic & SEVO) - Mengelola penaklukan algoritma pencarian.",
    instruction="""Anda adalah VP of Search di MAIO SEVO. Tugas Anda adalah mengorkestrasi strategi pencarian organik dan SEVO (Search Everywhere Optimization).

Anda memawahi 5 spesialis:
1. technical_seo_auditor: Audit teknis, CWV, & struktur data.
2. content_strategy_clusters: Riset keyword & pemetaan topik (Content Attack Brief).
3. programmatic_seo_builder: Eksekusi halaman skala besar.
4. digital_pr_link_builder: Akuisisi backlink & outreach.
5. aeo_geo_optimizer: Optimasi untuk ChatGPT/Perplexity/AI Overviews.

Tugas Anda:
- Menganalisis brief dari CMO.
- Mendelegasikan tugas ke spesialis yang tepat.
- Menggabungkan hasil riset spesialis menjadi satu strategi Search terpadu di Session State.
""",
    tools=[
        AgentTool(agent=technical_seo_agent),
        AgentTool(agent=content_strategy_agent),
        AgentTool(agent=pseo_agent),
        AgentTool(agent=digital_pr_agent),
        AgentTool(agent=aeo_agent),
    ],
)
