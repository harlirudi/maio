from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

from app.specialists.cro.cro_optimizer_agent import cro_optimizer_agent
from app.specialists.cro.growth_experiment_agent import growth_experiment_agent
from app.specialists.cro.revenue_analyst_agent import revenue_analyst_agent

cro_vp_agent = Agent(
    name="cro_vp_agent",
    model=Gemini(
        model="gemini-2.5-pro",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="VP of Conversion & Analytics (CRO) - Mengelola optimasi konversi dan intelijen data.",
    instruction="""Anda adalah VP of Conversion & Analytics di MAIO SEVO. Tugas Anda adalah memastikan setiap kunjungan berbuah menjadi konversi dan pendapatan.

Anda memawahi 3 spesialis:
1. landing_page_funnel_optimizer: Audit landing page & A/B testing copy.
2. growth_experimentation_lead: Manajemen hipotesis & Auto-Playbook.
3. data_revenue_analyst: Multi-source client reporting (GA4, HubSpot, Ahrefs).

Tugas Anda:
- Menganalisis corong konversi klien.
- Merancang strategi eksperimentasi untuk meningkatkan ROI.
- Menyediakan dashboard laporan yang memberikan wawasan 'so what' kepada klien.
""",
    tools=[
        AgentTool(agent=cro_optimizer_agent),
        AgentTool(agent=growth_experiment_agent),
        AgentTool(agent=revenue_analyst_agent),
    ],
)
