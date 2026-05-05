from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.revops_engine import RevenueIntelEngine, DealResurrectorEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_sales_calls_insights(client_id: str, transcript_text: str) -> dict:
    """Mengekstrak keberatan (objections) dan sinyal pembelian dari transkrip panggilan sales (Proposal)."""
    # Menggunakan logika regex nyata dari ericosiu_skills
    analysis = RevenueIntelEngine.analyze_transcript(client_id, transcript_text)
    return {"status": "success", "analysis": analysis}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def generate_deal_resurrection_campaign(client_id: str, lost_deals: list) -> dict:
    """Menganalisis kesepakatan yang hilang dan menentukan prioritas pemulihan berdasarkan skor (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "revenue_intel")
    
    prioritized_deals = []
    for deal in lost_deals:
        # Menghitung skor nyata berdasarkan logika deal_resurrector.py
        score = DealResurrectorEngine.calculate_resurrection_score(
            days_since_close=deal.get("days_ago", 0),
            deal_value=deal.get("value", 0),
            loss_reason=deal.get("reason", "unknown")
        )
        if score > 50:
            prioritized_deals.append({**deal, "resurrection_score": score})
        
    return {
        "status": "pending_human_approval", 
        "message": f"Identified {len(prioritized_deals)} high-priority deals for resurrection.",
        "deals": prioritized_deals
    }
