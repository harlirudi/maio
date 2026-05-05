from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.content_engine import ContentStrategyEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_content_pillars(client_id: str, company_info: dict) -> dict:
    """Merumuskan pilar konten strategis berdasarkan info perusahaan dan audiens target (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "content_strategy")
    return {"status": "success", "pillars": ["Industry disruption", "Productivity hacks", "Case studies"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_quote_mining(client_id: str, transcript_text: str) -> dict:
    """Mengekstrak kutipan menarik dari transkrip podcast/meeting untuk dijadikan konten sosial (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "content_strategy")
    
    # Memanggil logika nyata quote-mining-engine
    result = ContentStrategyEngine.mine_quotes(client_id, transcript_text)
    
    return {
        "status": "pending_human_approval", 
        "message": f"Extracted {len(result['extracted_quotes'])} quote candidates.",
        "quotes": result['extracted_quotes']
    }
