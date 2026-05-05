from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.paid_engine import LeadScorer

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_audience_overlap(client_id: str, current_audiences: list) -> dict:
    """Menganalisis tumpang tindih audiens untuk kampanye Programmatic & Display (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "programmatic")
    return {"status": "success", "insights": ["High overlap between retargeting and lookalike"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_lead_scoring_update(client_id: str, recent_leads: list) -> dict:
    """Memperbarui skor prospek (Lead Scoring) berdasarkan perilaku web untuk penyesuaian audiens (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "programmatic")
    
    scored_leads = []
    for lead in recent_leads:
        scored = LeadScorer.score_lead(client_id, lead)
        scored_leads.append(scored)
        
    return {
        "a2ui_component": "DataTable",
        "title": "Lead Scoring Update",
        "description": "Hasil penskoran otomatis untuk optimasi audiens programmatic.",
        "data": scored_leads,
        "client_id": client_id,
        "status": "success"
    }
