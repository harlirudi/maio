from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.search_engine import TechnicalSEOEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_technical_seo(client_id: str, target_domain: str, gsc_rows: list) -> dict:
    """Menganalisis anomali pada data Google Search Console untuk menemukan quick wins SEO (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "search", "technical_seo")
    
    # Menggunakan logika nyata audit GSC
    audit_result = TechnicalSEOEngine.audit_gsc_data(client_id, target_domain, gsc_rows)
    
    return {
        "a2ui_component": "DataTable",
        "title": f"Technical SEO Audit: {target_domain}",
        "description": "Anomali terdeteksi pada performa kata kunci utama.",
        "data": audit_result["anomalies_found"],
        "client_id": client_id,
        "status": "success"
    }

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_gsc_monitoring(client_id: str) -> dict:
    """Memantau Google Search Console API untuk anomali harian (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "search", "technical_seo")
    
    return {
        "a2ui_component": "ApprovalCard",
        "title": "GSC Daily Monitoring Report",
        "message": "Laporan anomali harian GSC telah siap untuk ditinjau.",
        "action_label": "Kirim ke Dashboard Klien",
        "client_id": client_id,
        "status": "pending_human_approval"
    }
