import asyncio
import json
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.agent import root_agent

async def run_simulation_full():
    session_service = InMemorySessionService()
    app_name = "app"
    user_id = "client_001"
    session_id = "session_v2_full"
    
    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service)
    
    # --- PHASE 1: DISCOVERY ---
    print("\n[CLIENT]: Saya ingin meningkatkan penjualan sepatu lari lewat TikTok dan Google Maps. Budget saya terbatas di 15 Juta. Bisakah Anda memberikan proposal?\n")
    
    msg1 = "Saya ingin meningkatkan penjualan sepatu lari lewat TikTok dan Google Maps. Budget saya terbatas di 15 Juta. Bisakah Anda memberikan proposal?"
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=types.Content(role="user", parts=[types.Part.from_text(text=msg1)])):
        if event.author == "cmo_agent" and event.content:
             print(f"[CMO]: {event.content.parts[0].text[:200]}...\n")

    # --- PHASE 2: CLIENT ANSWERS QUIZ ---
    answers = "Jawaban saya: 1. B (Kenyamanan/Gaya), 2. C (Direct Sales), 3. B (Teknologi Unik)."
    print(f"[CLIENT]: {answers}\n")
    
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=types.Content(role="user", parts=[types.Part.from_text(text=answers)])):
        if event.author == "cmo_agent" and event.content:
             print(f"--- CMO RESPONSE TO CLIENT ---\n{event.content.parts[0].text}\n")
        
        # CFO Call detection
        if event.author == "finance_ops_agent" and event.content:
             print(f"--- INTERNAL FINANCE ADVISORY (CFO) ---\n{event.content.parts[0].text}\n")

if __name__ == "__main__":
    asyncio.run(run_simulation_full())
