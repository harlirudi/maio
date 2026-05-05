from google.adk.tools import tool
from app.app_utils.workspace_manager import WorkspaceManager
from app.app_utils.content_engine import VideoMultimediaEngine

# ==============================================================================
# FASE 1: PRE-SALES / PROPOSAL MODE (Read & Analyze)
# ==============================================================================

@tool
def analyze_competitor_youtube(client_id: str, competitor_data: list) -> dict:
    """Menganalisis channel YouTube kompetitor mencari video viral (outlier) dan pola judul (Proposal)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "video_multimedia")
    
    # Menggunakan logika analitik dari yt-competitive-analysis
    analysis = VideoMultimediaEngine.analyze_youtube_hooks(client_id, competitor_data)
    
    return {
        "a2ui_component": "DataTable",
        "title": "YouTube Viral Hooks Analysis",
        "description": "Pola judul video kompetitor dengan performa outlier.",
        "data": analysis["top_hook_patterns"],
        "client_id": client_id,
        "status": "success"
    }

# ==============================================================================
# FASE 2: EXECUTION MODE (Write & Generate)
# ==============================================================================

@tool
def generate_short_form_clips(client_id: str, youtube_url: str, transcript_timestamps: list) -> dict:
    """Memotong video panjang klien menjadi klip pendek viral menggunakan FFMpeg (Eksekusi)."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "video_multimedia")
    
    # Simulate FFMpeg clipping logic based on timestamps
    clips = VideoMultimediaEngine.simulate_ffmpeg_clipping(client_id, youtube_url, transcript_timestamps)
    
    return {
        "a2ui_component": "VideoPreview",
        "title": "Klip Video Siap Tinjau",
        "message": f"Berhasil memotong {len(clips)} klip dari {youtube_url}.",
        "data": clips,
        "action_label": "Publish to TikTok/Reels",
        "client_id": client_id,
        "status": "pending_human_approval"
    }
