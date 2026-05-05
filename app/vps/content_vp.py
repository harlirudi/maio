from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

from app.specialists.content.podcast_editor_agent import podcast_editor_agent
from app.specialists.content.short_form_agent import short_form_agent
from app.specialists.content.content_ops_agent import content_ops_agent
from app.specialists.content.social_manager_agent import social_manager_agent
from app.specialists.content.creative_builder_agent import creative_builder_agent

content_vp_agent = Agent(
    name="content_vp_agent",
    model=Gemini(
        model="gemini-2.5-pro",
    ),
    description="VP of Content & Media - Mengorkestrasi produksi multimedia dan manajemen komunitas.",
    instruction="""Anda adalah VP of Content & Media di MAIO SEVO. Tugas Anda adalah mengubah ide strategis menjadi aset konten yang viral dan bernilai tinggi.

Anda memawahi 5 spesialis:
1. podcast_video_editor: Podcast-to-Everything pipeline & ekstraksi narasi.
2. short_form_virality_specialist: Produksi klip TikTok/Reels & captioning.
3. written_content_humanizer: Penulisan artikel panjang & QC anti-AI slop.
4. community_social_manager: Engagement, reputasi, & employee advocacy.
5. creative_presentation_builder: Visual design, Slide Decks, & Proposal Landing Page.

Tugas Anda:
- Memimpin 'pabrik konten' agensi.
- Memastikan setiap aset konten selaras dengan brand voice klien.
- Mengarahkan agen Creative untuk membuat presentasi/proposal interaktif jika diminta CMO.
""",
    tools=[
        AgentTool(agent=podcast_editor_agent),
        AgentTool(agent=short_form_agent),
        AgentTool(agent=content_ops_agent),
        AgentTool(agent=social_manager_agent),
        AgentTool(agent=creative_builder_agent),
    ],
)
