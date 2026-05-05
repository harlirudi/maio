from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.cro_engine import CROAuditEngine, GrowthExperimenter

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_conversion_heuristics(client_id: str, page_html_text: str) -> dict:
    """Mengaudit halaman arahan berdasarkan 5 dimensi heuristik konversi (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "uiux_ab_test")
    
    # Menggunakan logika nyata CRO audit
    audit_result = CROAuditEngine.audit_landing_page(client_id, page_html_text)
    
    return {"status": "success", "audit_result": audit_result}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_ab_test_scoring(client_id: str, variant_a_data: tuple, variant_b_data: tuple) -> dict:
    """Melakukan uji statistik (T-Test) untuk menentukan pemenang A/B testing kampanye berjalan (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "uiux_ab_test")
    
    # Menggunakan logika perhitungan P-Value
    result = GrowthExperimenter.run_statistical_analysis(client_id, variant_a_data, variant_b_data)
    
    return {
        "a2ui_component": "DataTable",
        "title": "A/B Test Statistical Report",
        "description": f"Status: {result['status']}",
        "data": [
            {"Metric": "Control CR", "Value": f"{result['control_cr']}%"},
            {"Metric": "Variant CR", "Value": f"{result['variant_cr']}%"},
            {"Metric": "Lift", "Value": f"{result['lift_pct']}%"},
            {"Metric": "P-Value", "Value": result['p_value']},
            {"Metric": "Significant", "Value": str(result['statistically_significant'])}
        ],
        "client_id": client_id,
        "status": "success"
    }
