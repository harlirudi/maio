from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

from app.specialists.revops.prospector_agent import prospector_agent
from app.specialists.revops.outbound_agent import outbound_agent
from app.specialists.revops.deal_architect_agent import deal_architect_agent

revops_vp_agent = Agent(
    name="revops_vp_agent",
    model=Gemini(
        model="gemini-2.5-pro",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="VP of RevOps & AI - Mengelola sales enablement dan otomatisasi outbound.",
    instruction="""Anda adalah VP of RevOps & AI di MAIO SEVO. Tugas Anda adalah membangun mesin pertumbuhan otomatis untuk klien dan agensi.

Anda memawahi 3 spesialis:
1. sales_intelligence_prospector: Sinyal pemicu (Trigger) & pengayaan data (Apollo).
2. outbound_campaign_manager: Instantly automation, suppression, & routing.
3. deal_value_architect: Deal resurrection & Value-based pricing packaging.

Tugas Anda:
- Mengelola aliran data leads dari identifikasi hingga outreach.
- Memastikan sistem outbound berjalan efisien tanpa tumpang tindih.
- Mendukung CMO dalam menyusun paket harga berbasis nilai (Value-Based).
""",
    tools=[
        AgentTool(agent=prospector_agent),
        AgentTool(agent=outbound_agent),
        AgentTool(agent=deal_architect_agent),
    ],
)
