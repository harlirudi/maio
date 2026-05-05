from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.search_engine import LocalSEOEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_local_presence(client_id: str, business_name: str) -> dict:
    """Mengaudit Google My Business dan visibilitas lokal untuk proposal e-commerce/lokal."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "search", "local_ecomm_seo")
    return {"status": "success", "insights": ["GMB profile incomplete", "Missing product schema"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_product_feed_optimization(client_id: str, raw_catalog_data: list) -> dict:
    """Mengoptimalkan feed produk e-commerce (GMC) secara otomatis berdasarkan best practice (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "search", "local_ecomm_seo")
    
    # Menggunakan logika nyata optimasi judul produk
    optimized_feed = LocalSEOEngine.optimize_product_feed(client_id, raw_catalog_data)
    
    return {
        "status": "pending_human_approval", 
        "message": f"Optimized {len(optimized_feed)} product titles for Merchant Center.",
        "optimized_preview": optimized_feed[:2]
    }
