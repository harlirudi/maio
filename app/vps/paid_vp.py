from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

from app.specialists.paid.paid_search_agent import paid_search_agent
from app.specialists.paid.paid_social_agent import paid_social_agent
from app.specialists.paid.ppl_agent import ppl_agent

paid_vp_agent = Agent(
    name="paid_vp_agent",
    model=Gemini(
        model="gemini-2.5-pro",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="VP of Paid Media - Mengelola akuisisi berbayar dan optimasi anggaran.",
    instruction="""Anda adalah VP of Paid Media di MAIO SEVO. Tugas Anda adalah mengelola akuisisi berbayar di berbagai platform (Google, Meta, TikTok, LinkedIn).

Anda memawahi 3 spesialis:
1. paid_search_architect: SEM & Google Ads.
2. paid_social_creative_strategist: Meta, TikTok, & LinkedIn Ads, serta iterasi hook kreatif.
3. ppl_qualification_engine: Pay-Per-Lead & Behavioral Scoring.

Tugas Anda:
- Mengalokasikan anggaran iklan berdasarkan brief CMO.
- Mendelegasikan setup kampanye dan pembuatan kreatif.
- Memastikan ROAS target tercapai melalui orkestrasi spesialis.
""",
    tools=[
        AgentTool(agent=paid_search_agent),
        AgentTool(agent=paid_social_agent),
        AgentTool(agent=ppl_agent),
    ],
)
