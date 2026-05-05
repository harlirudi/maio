from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.revops_engine import LeadPipeline, TriggerProspector

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_tam_and_signals(client_id: str, industry: str) -> dict:
    """Menganalisis Total Addressable Market (TAM) dan sinyal pembelian untuk proposal (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "outbound_lead_gen")
    signals = TriggerProspector.scout_signals(client_id, days=30)
    return {"status": "success", "market_signals": signals, "tam_estimate": 5000}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_lead_sourcing_pipeline(client_id: str, criteria: dict) -> dict:
    """Melakukan scraping profil LinkedIn/Apollo dan memverifikasi email untuk kampanye outbound (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "outbound_lead_gen")
    leads = LeadPipeline.source_leads(client_id, criteria.get("titles", ""), criteria.get("industries", ""))
    valid_leads, stats = LeadPipeline.verify_emails(client_id, leads)
    
    return {
        "a2ui_component": "ApprovalCard",
        "title": "Outbound Lead Pipeline Ready",
        "message": f"Sourced {stats['total']} leads, {stats['valid']} verified and ready for sequences.",
        "data": valid_leads[:5], # Preview top 5
        "action_label": "Push to Instantly.ai",
        "client_id": client_id,
        "status": "pending_human_approval"
    }
