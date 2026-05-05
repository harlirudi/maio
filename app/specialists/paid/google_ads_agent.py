from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.paid_engine import BiddingOptimizer, GoogleAdsEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_google_ads_search_intent(client_id: str, ads_keywords: list, organic_keywords: list) -> dict:
    """Mengaudit kanibalisasi kata kunci antara Google Ads dan SEO untuk menghemat budget (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "google_ads")
    
    # Menggunakan logika nyata audit kanibalisasi
    audit_result = GoogleAdsEngine.audit_intent_overlap(client_id, ads_keywords, organic_keywords)
    
    return {"status": "success", "audit_result": audit_result}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_bidding_optimization(client_id: str, campaign_data: dict) -> dict:
    """Mengoptimalkan penawaran (bidding) Google Ads berdasarkan ROAS (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "google_ads")
    # Panggil logic dari paid_engine.py
    adjustments = BiddingOptimizer.get_optimized_bids(client_id, campaign_data)
    
    return {
        "status": "pending_human_approval", 
        "message": f"Generated {len(adjustments)} bid adjustments.",
        "review_path": str(ws_path)
    }
