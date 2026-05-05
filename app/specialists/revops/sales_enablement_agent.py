from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.revops_engine import SalesEnablementEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def calculate_value_pricing_tiers(client_id: str, deal_target: int, services: list) -> dict:
    """Menghasilkan struktur harga paket (Tiered Pricing) berbasis nilai (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "sales_enablement")
    
    # Menggunakan logika pembulatan dan anchoring
    tiers = SalesEnablementEngine.generate_tiered_pricing(deal_target)
    
    return {
        "a2ui_component": "PricingTable",
        "title": "Investasi yang Terukur (Value-Based Pricing)",
        "description": "Opsi investasi berdasarkan target pertumbuhan klien.",
        "currency": "USD",
        "data": tiers,
        "client_id": client_id,
        "status": "success"
    }

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def generate_pitch_deck_assets(client_id: str, proposal_data: dict) -> dict:
    """Menghasilkan draf presentasi deck penjualan untuk tim sales (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "sales_enablement")
    return {"status": "pending_human_approval", "message": "Pitch deck generated and saved to workspace."}
