import os
from dotenv import load_dotenv
from google import genai
from google.adk.tools import ToolContext

# Muat variabel environment dari file .env
load_dotenv()

def generate_visual_proposal(proposal_data: str, tool_context: ToolContext) -> dict:
    """Menghasilkan file MD dan Golden Prompt untuk pembuatan proposal visual di AI Studio.
    
    Args:
        proposal_data: Data strategi dan harga hasil orkestrasi agen.
    """
    # 1. Simpan Brief MD
    md_path = os.path.join(os.getcwd(), "docs", "LATEST_PROPOSAL_BRIEF.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(proposal_data)
        
    # 2. Rancang Golden Prompt (Gaya Research Visualization)
    golden_prompt = """
    ROLE: Senior Full-Stack Creative Developer.
    TASK: Build a Single Page Application (SPA) React Proposal.
    VISUAL STYLE: 'Research Visualization' (Refer to the AlphaQubit project).
    - Palette: Cream background (#F9F8F4), Gold accents (#C5A059), Charcoal text (#1a1a1a).
    - Typography: 'Playfair Display' for Headings, 'Inter' for Body.
    - WOW Factor: Use Framer Motion for scroll-reveal animations. Include an interactive SVG chart for 'ROI Prediction'.
    - Required Interactive: A Budget Slider that unbundles 'Agency Fee' vs 'Ad Spend'.
    
    DATA SOURCE: Use the provided Markdown brief.
    OUTPUT: Return ONLY raw TypeScript/React code for App.tsx.
    """
    
    return {
        "status": "success",
        "message": "Brief proposal dan Golden Prompt telah disiapkan.",
        "brief_file": md_path,
        "golden_prompt": golden_prompt,
        "next_step": "Copy file MD dan Golden Prompt ini ke Gemini 3.1 Pro di AI Studio untuk hasil artistik maksimal."
    }
