from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.content_engine import CopywritingEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_website_copy(client_id: str, website_text: str) -> dict:
    """Mengevaluasi kualitas copy website klien saat ini (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "copywriting")
    
    score_result, _ = CopywritingEngine.score_and_de_slop_text(client_id, website_text, "website")
    
    return {"status": "success", "audit_result": score_result}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_copy_optimization(client_id: str, drafts: list[str]) -> dict:
    """Mengoptimalkan draf konten/email klien untuk menghindari pola tulisan AI (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "copywriting")
    
    optimized_drafts = []
    for i, draft in enumerate(drafts):
         # Menggunakan logika nyata de-slopping
         _, clean_text = CopywritingEngine.score_and_de_slop_text(client_id, draft, f"draft_{i}")
         optimized_drafts.append(clean_text)
         
    return {
        "a2ui_component": "ApprovalCard",
        "title": "Copywriting Optimization (De-Slop)",
        "message": f"Ditemukan indikasi bahasa AI pada {len(drafts)} draf. Teks telah dibersihkan.",
        "data": optimized_drafts,
        "action_label": "Gunakan Teks Optimasi",
        "client_id": client_id,
        "status": "pending_human_approval"
    }
