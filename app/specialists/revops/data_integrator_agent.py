from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.revops_engine import DataIntegrationEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_icp_learning_patterns(client_id: str, closed_won_deals: list, closed_lost_deals: list) -> dict:
    """Menganalisis pola penerimaan/penolakan prospek dari database untuk memperbaiki kriteria ICP (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "data_integrator")
    
    # Menggunakan logika asli untuk menemukan tingkat kemenangan (win rate) per industri
    insights = DataIntegrationEngine.analyze_icp_win_rates(closed_won_deals, closed_lost_deals)
    
    return {"status": "success", "icp_insights": insights}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_client_bi_report(client_id: str, ga4_data: dict, hubspot_data: list, ad_spend_data: dict) -> dict:
    """Menggabungkan data dari GA4, HubSpot, Ahrefs, dan Gong menjadi satu laporan klien (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "data_integrator")
    
    # Menjalankan perhitungan ROI aktual
    report_data, report_path = DataIntegrationEngine.generate_unified_roi_report(
        client_id, ga4_data, hubspot_data, ad_spend_data
    )
    
    return {
        "status": "pending_human_approval", 
        "message": f"Unified BI report generated with ROI {report_data['metrics']['roi_percentage']}%.",
        "report_path": str(report_path)
    }
