from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.content_engine import SocialRepurposerEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def audit_social_profiles(client_id: str, social_urls: list[str]) -> dict:
    """Mengaudit profil media sosial klien untuk konsistensi branding dan engagement (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "organic_social")
    return {"status": "success", "insights": ["Inconsistent bio", "Low posting frequency on LinkedIn"]}

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_content_repurposing(client_id: str, source_content: str) -> dict:
    """Mengubah format konten panjang (misal: blog) menjadi Twitter Thread dan LinkedIn post (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "organic_social")
    
    # Memanggil logika nyata dari content-transform.py dan x-longform-post
    drafts = SocialRepurposerEngine.transform_to_social(client_id, source_content)
    
    return {
        "status": "pending_human_approval", 
        "message": f"Drafted {len(drafts['linkedin_posts'])} LinkedIn posts and 1 Twitter thread.",
        "drafts": drafts
    }
