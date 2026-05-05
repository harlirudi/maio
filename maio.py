import asyncio
import os
import sys
import json
from datetime import datetime
from google.adk.runners import InMemoryRunner
from app.agent import app

async def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ ERROR: GEMINI_API_KEY belum di-set di Environment Variable.")
        return

    runner = InMemoryRunner(app=app)
    
    print("="*70)
    print("🚀 MAIO - AI MARKETING AGENCY OS (Enhanced Transparency)")
    print("="*70)
    print("Sistem Arsitektur 2 Fase: [1] Pre-Sales (Proposal) & [2] Execution (Delivery)")
    print("="*70)
    
    client_id = input("Masukkan Nama/ID Klien untuk sesi ini: ").strip()
    if not client_id:
        client_id = "default_client"
        print("⚠️ ID Klien kosong. Menggunakan 'default_client'.")
        
    print(f"✅ Workspace: ./workspaces/{client_id.lower().replace(' ', '_')}/")
    print("="*70 + "\n")
    
    session_id = f"{client_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    user_id = "agency_operator"

    print("Ardi (CMO): Halo! Saya siap membantu mengelola agensi Anda.")
    print("-" * 70)

    while True:
        try:
            user_input = input("\nOPERATOR > ")
            
            if user_input.lower() in ["exit", "keluar", "quit"]:
                print("\nArdi: Sampai jumpa kembali!")
                break

            if not user_input.strip():
                continue

            print("\n[ANALYZING DELEGATION PATH...]")
            
            contextualized_input = f"[SYSTEM: Klien saat ini adalah '{client_id}'. Gunakan workspace ini untuk semua tool.]\n\n{user_input}"
            
            # Gunakan runner.run secara langsung untuk kontrol event yang lebih baik di log
            # Sambil tetap menampilkan debug info di terminal
            await runner.run_debug(
                contextualized_input,
                user_id=user_id,
                session_id=session_id,
                verbose=True, 
                quiet=False
            )
            print("\n" + "-"*70)

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n[SYSTEM ERROR]: {e}")
            break

    # === LOGIC UNTUK EXPORT SESSION HISTORY (FULL TRANSPARENCY) ===
    print("\n[SYSTEM] Menyusun Laporan Transparansi Sesi...")
    try:
        events = runner.session_service.get_events(user_id=user_id, session_id=session_id)
        
        logs_dir = os.path.join(os.path.dirname(__file__), "docs", "learning_logs")
        os.makedirs(logs_dir, exist_ok=True)
        
        filepath = os.path.join(logs_dir, f"session_{session_id}.md")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# MAIO Full Transparency Log: {session_id}\n\n")
            f.write(f"Client ID: **{client_id}**\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Architecture: 19 Specialists / 5 VPs / 2-Phase Mode\n\n")
            f.write("---\n\n")
            
            for event in events:
                if event.type == "human_input":
                    clean_text = event.text.split("]\n\n", 1)[-1] if "]\n\n" in event.text else event.text
                    f.write(f"### 👤 OPERATOR INPUT\n> {clean_text}\n\n")
                
                elif event.type == "agent_response":
                    content = "".join([p.text for p in event.content.parts if p.text])
                    f.write(f"### 🧠 ARDI (CMO) RESPONSE\n{content}\n\n")
                
                elif event.type == "function_call":
                    f.write(f"#### ⚙️ DELEGATION STEP\n")
                    f.write(f"- **Target:** `{event.function_name}`\n")
                    # Mencoba mem-format argumen jika ada
                    try:
                        args = json.dumps(event.arguments, indent=2)
                        f.write(f"- **Parameters:**\n```json\n{args}\n```\n")
                    except:
                        pass
                    f.write("\n")
                    
                elif event.type == "function_response":
                    f.write(f"#### ✅ TOOL OUTPUT\n")
                    f.write(f"- **Source:** `{event.function_name}`\n")
                    try:
                        resp = json.dumps(event.response, indent=2)
                        f.write(f"- **Data returned:**\n```json\n{resp}\n```\n")
                    except:
                        pass
                    f.write("\n")
                
        print(f"✅ Laporan transparansi berhasil disimpan ke: {filepath}")
        print(f"💡 Anda sekarang bisa melihat seluruh alur 'Black Box' di file tersebut.")
    except Exception as e:
        print(f"⚠️ Gagal menyusun laporan: {e}")

    await runner.close()

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
