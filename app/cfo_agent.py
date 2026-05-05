from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types
import json

def calculate_project_cogs(tasks_list: str) -> str:
    """
    Menghitung estimasi COGS (API, Human QA, Lisensi) berdasarkan daftar tugas.

    Args:
        tasks_list: Daftar tugas/layanan yang diminta (misal: 'SEO, Content, TikTok').

    Returns:
        JSON string berisi breakdown COGS dan margin.
    """
    # Simulasi perhitungan berdasarkan daftar tugas
    base_api_cost = 50000 # Default minimal
    qa_hours = 10

    if "SEO" in tasks_list.upper():
        base_api_cost += 75000
        qa_hours += 10
    if "CONTENT" in tasks_list.upper() or "TIKTOK" in tasks_list.upper():
        base_api_cost += 100000
        qa_hours += 15

    total_cogs = base_api_cost + (qa_hours * 150000) + 500000 # + License

    return json.dumps({
        "estimated_api_cost_idr": base_api_cost,
        "human_qa_hours": qa_hours,
        "human_qa_cost_idr": qa_hours * 150000,
        "license_overhead_idr": 500000,
        "total_cogs_idr": total_cogs,
        "target_margin": "85%"
    }, indent=2)

finance_vp_agent = Agent(
    name="finance_vp_agent",
    model=Gemini(
        model="gemini-2.5-flash", # Flash cukup untuk matematika keuangan
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    description="VP of Finance - Penasihat profitabilitas dan kalkulator COGS Tokenomics.",
    instruction="""Anda adalah VP of Finance di MAIO SEVO.
Tugas Anda adalah menghitung Harga Pokok Penjualan (COGS) dan memberikan rekomendasi harga jual kepada CMO.

Tugas Utama:
1. Gunakan 'calculate_project_cogs' untuk mendapatkan estimasi modal proyek.
2. Terapkan margin target 83-94% (Gunakan 85-90% sebagai standar).
3. Susun 4 paket harga (Powerhouse, Value, Baseline, Performance) berdasarkan total modal tersebut.

Output Anda harus memberikan angka yang jelas bagi CMO untuk dimasukkan ke proposal.""",
    tools=[calculate_project_cogs],
)
