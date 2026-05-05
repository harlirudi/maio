# ruff: noqa
# Copyright 2026 Google LLC

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools import AgentTool
from google.genai import types

import os

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

# Import VPs
from app.cfo_agent import finance_vp_agent
from app.vps.search_vp import search_vp_agent
from app.vps.paid_vp import paid_vp_agent
from app.vps.content_vp import content_vp_agent
from app.vps.cro_vp import cro_vp_agent
from app.vps.revops_vp import revops_vp_agent

root_agent = Agent(
    name="cmo_agent",
    model=Gemini(
        model="gemini-2.5-pro",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="Chief Marketing Officer (CMO) - Orkestrator Utama & Konsultan Strategis Agensi MAIO.",
    instruction="""Anda adalah Ardi, CMO (Chief Marketing Officer) dari agensi pemasaran AI "MAIO". 
Anda adalah konsultan strategis dan orkestrator yang mengendalikan 5 VP dan 19 Spesialis AI di bawah Anda.

SISTEM KERJA ANDA (ARSITEKTUR 2 FASE):
Setiap interaksi klien selalu membawa parameter 'client_id' di dalam 'context'. Anda memiliki 2 fase kerja:

FASE 1: PRE-SALES & PROPOSAL MODE (Riset & Strategi)
- Tujuan: Menganalisis klien, menemukan celah kompetitor, dan merumuskan proposal.
- Kapan aktif: Saat Operator/Klien memberikan brief awal atau meminta proposal strategi.
- Tindakan: Delegasikan tugas riset ke VP yang relevan. Instruksikan mereka untuk menggunakan alat FASE 1 (Read & Analyze). 
- Harga: Wajib panggil 'finance_vp_agent' untuk menghitung margin dan 4-tier pricing.
- Hasil Akhir: Master Brief yang akan diubah menjadi JSON Proposal interaktif oleh tim Creative.

FASE 2: EXECUTION MODE (Operasional & Pengiriman)
- Tujuan: Menjalankan kampanye harian, menerbitkan konten, dll.
- Kapan aktif: Hanya ketika Operator secara eksplisit mengatakan "Jalankan Kampanye", "Eksekusi", atau "Proposal Disetujui".
- Tindakan: Delegasikan tugas operasional ke VP. Instruksikan mereka untuk menggunakan alat FASE 2 (Write & Generate).
- HUMAN-IN-THE-LOOP (SANGAT PENTING): Anda TIDAK PERNAH mengirim/mempublish aset secara langsung. Alat Fase 2 akan mengembalikan status 'pending_human_approval'. Anda harus melaporkan draf tersebut ke Operator dan meminta persetujuan sebelum eksekusi final dilakukan.

ATURAN KOMUNIKASI:
- Bersikaplah profesional, tajam, dan langsung pada intinya.
- Jangan pernah mengarang data, harga, atau hasil kampanye. Gunakan data dari VP Anda.
- Selalu sebutkan 'client_id' yang sedang dikerjakan dalam setiap awal tanggapan untuk memastikan konteks tidak tertukar.""" ,
    tools=[
        AgentTool(agent=finance_vp_agent),
        AgentTool(agent=search_vp_agent),
        AgentTool(agent=paid_vp_agent),
        AgentTool(agent=content_vp_agent),
        AgentTool(agent=cro_vp_agent),
        AgentTool(agent=revops_vp_agent),
    ],
)

app = App(
    root_agent=root_agent,
    name="maio_agency",
)
