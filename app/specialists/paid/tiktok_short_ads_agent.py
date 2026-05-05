from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.paid_engine import TikTokCreativeEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_viral_ad_hooks(client_id: str, competitor_handles: list[str]) -> dict:
    """Menganalisis pola hook video pendek kompetitor untuk ide iklan TikTok/Reels (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "tiktok_short_ads")
    return {"status": "success", "patterns": ["3-second problem reveal", "UGC testimonial style"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_ad_creative_briefs(client_id: str, campaign_goal: str) -> dict:
    """Membuat brief kreatif iklan video pendek untuk tim produksi berdasarkan pola outlier (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "tiktok_short_ads")
    
    # Menggunakan logika draf hook otomatis
    brief = TikTokCreativeEngine.analyze_ad_creative_brief(client_id, campaign_goal)
    
    return {
        "a2ui_component": "DataTable",
        "title": "TikTok Ad Creative Briefs",
        "description": f"Draf hook iklan untuk target: {campaign_goal}",
        "data": [{"Hook": h} for h in brief["drafted_hooks"]],
        "client_id": client_id,
        "status": "success"
    }
