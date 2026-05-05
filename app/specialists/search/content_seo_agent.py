from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.search_engine import ContentSEOEngine, TrendScoutEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_keyword_gaps(client_id: str, my_domain: str, competitor_domains: list[str]) -> dict:
    """Mencari celah kata kunci (Keyword Gap) vs kompetitor untuk ide konten proposal (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "search", "content_seo")
    
    # Menggunakan logika nyata Content Gap Analysis
    gap_analysis = ContentSEOEngine.identify_content_gaps(client_id, my_domain, competitor_domains)
    
    return {
        "a2ui_component": "DataTable",
        "title": "SEO Content Gap Analysis",
        "description": f"Peluang kata kunci vs {', '.join(competitor_domains)}",
        "data": gap_analysis["actionable_gaps"],
        "client_id": client_id,
        "status": "success"
    }

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def execute_trend_scouting(client_id: str, niche_subreddit: str) -> dict:
    """Mendeteksi tren pencarian dari Reddit untuk menemukan ide artikel blog instan (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "search", "content_seo")
    
    # Menggunakan logika nyata TrendScout
    trends = TrendScoutEngine.fetch_reddit_trends(client_id, niche_subreddit)
    
    return {
        "a2ui_component": "ApprovalCard",
        "title": f"Reddit Trends: r/{niche_subreddit}",
        "message": f"Ditemukan {len(trends)} topik panas. Apakah ingin membuat draf artikel dari tren ini?",
        "data": trends,
        "action_label": "Generate Blog Drafts",
        "client_id": client_id,
        "status": "pending_human_approval"
    }
