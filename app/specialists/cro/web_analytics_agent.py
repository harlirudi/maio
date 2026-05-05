from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.cro_engine import RevenueAttributor

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_content_roi_gaps(client_id: str) -> dict:
    """Menganalisis celah atribusi pendapatan dari konten yang ada (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "web_analytics")
    gaps = RevenueAttributor.find_content_gaps(client_id)
    return {"status": "success", "gaps": gaps}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def generate_weekly_growth_scorecard(client_id: str, deals_data: list) -> dict:
    """Menghasilkan laporan mingguan diatribusikan ke revenue (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "web_analytics")
    report = RevenueAttributor.map_revenue(client_id, deals_data)
    
    return {
        "a2ui_component": "DataTable",
        "title": "Weekly Growth Scorecard",
        "description": "Atribusi pendapatan berdasarkan saluran konten.",
        "data": [
            {"Channel": k, "Revenue": f"${v:,.2f}"} for k, v in report["breakdown_by_type"].items()
        ],
        "total_revenue": f"${report['total_attributed_revenue']:,.2f}",
        "client_id": client_id,
        "status": "success"
    }
