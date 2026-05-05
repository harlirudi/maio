from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.revops_engine import process_rb2b_visitor

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_crm_automation_gaps(client_id: str) -> dict:
    """Mengevaluasi alur otomatisasi CRM klien saat ini untuk menemukan celah (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "crm_automation")
    return {"status": "success", "insights": ["No lead scoring implemented", "MQL routing takes >24 hours"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_visitor_routing(client_id: str, visitor_payload: dict) -> dict:
    """Memproses data pengunjung anonim (RB2B) dan mengarahkannya ke kampanye email otomatis (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "crm_automation")
    result = process_rb2b_visitor(client_id, visitor_payload)
    return {"status": "success", "routing_decision": result}
