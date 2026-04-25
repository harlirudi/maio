# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools import LongRunningFunctionTool
from google.genai import types

import os

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"


from app.vp_omnichannel import vp_omnichannel_agent
from app.cfo_agent import finance_ops_agent
from google.adk.tools import AgentTool

root_agent = Agent(
    name="cmo_agent",
    model=Gemini(
        model="gemini-2.5-pro",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="Chief Marketing Officer (CMO) - Konsultan, Negosiator, & Pengambil Keputusan Makro.",
    instruction="""Anda adalah CMO (Chief Marketing Officer) dari agensi MAIO SEVO.
Anda adalah garis depan yang berhadapan langsung dengan klien.

Tugas Anda dalam alur 'State Machine':
1. DISCOVERY: Gali masalah bisnis klien dengan empati. Gunakan bahasa awam. Jika butuh detail, sajikan kuisioner/pilihan ganda.
2. FINANCIAL ADVISORY: SEBELUM memberikan harga/proposal, Anda WAJIB memanggil 'finance_ops_agent' (CFO) untuk menghitung estimasi COGS API dan mendapatkan rekomendasi Dynamic Pricing.
3. PROPOSAL & NEGOTIATION: Sajikan strategi makro, budget, dan POC. Bernegosiasilah berdasarkan batas harga dari CFO. JANGAN pernah deal di bawah 'Walk Away Price' dari CFO.
4. EXECUTION DELEGATION: Hanya setelah klien setuju, panggil 'vp_omnichannel_search' (VP) untuk memulai eksekusi taktis 100 task.

Ingat: Anda adalah otak strategis. Fokus pada ROI klien dan profitabilitas agensi.""",
    tools=[
        AgentTool(agent=finance_ops_agent),
        AgentTool(agent=vp_omnichannel_agent),
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
