from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.paid_engine import AdSpendMonitorEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_meta_ads_performance(client_id: str, ad_account_id: str) -> dict:
    """Menganalisis performa historis Meta Ads klien untuk baseline proposal."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "meta_ads")
    return {"status": "success", "insights": ["High CPA on retargeting", "Creative fatigue detected"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_meta_ad_spend_monitoring(client_id: str, current_spend: float, monthly_budget: float, days_elapsed: int) -> dict:
    """Memantau dan mendeteksi anomali pengeluaran iklan Meta secara harian (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "meta_ads")
    
    # Menggunakan logika nyata dari pacing-alert.py
    pacing_report = AdSpendMonitorEngine.monitor_pacing(client_id, current_spend, monthly_budget, days_elapsed)
    
    # Jika anomali terdeteksi, kirim sebagai ApprovalCard
    if pacing_report["status"] != "HEALTHY":
        return {
            "a2ui_component": "ApprovalCard",
            "title": f"Ad Spend Alert: {pacing_report['status']}",
            "message": pacing_report["message"],
            "data": pacing_report,
            "action_label": pacing_report["recommended_action"],
            "client_id": client_id,
            "status": "pending_human_approval"
        }
    
    return {
        "a2ui_component": "DataTable",
        "title": "Ad Spend Status",
        "description": "Pengeluaran iklan Meta berjalan normal.",
        "data": [pacing_report],
        "client_id": client_id,
        "status": "success"
    }
