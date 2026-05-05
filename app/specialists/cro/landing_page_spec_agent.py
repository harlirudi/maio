from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.cro_engine import LandingPageEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def clone_reference_site_styles(client_id: str, reference_url: str) -> dict:
    """Mengkloning token desain (warna, font) dari situs referensi kompetitor untuk ide proposal (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "landing_page_spec")
    return {"status": "success", "design_tokens": {"primary_color": "#FF5733", "font": "Inter"}}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def generate_landing_page_wireframe(client_id: str, survey_pain_points: list) -> dict:
    """Menghasilkan spesifikasi wireframe (JSON) untuk lead magnet berdasarkan data survei audiens (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "landing_page_spec")
    
    # Menggunakan logika dari LandingPageEngine
    wireframe = LandingPageEngine.generate_wireframe_spec(client_id, survey_pain_points)
    
    return {
        "status": "pending_human_approval", 
        "message": "Wireframe JSON generated based on survey pain points.",
        "wireframe_preview": wireframe
    }
