import os
import json
import re
import random
from datetime import datetime
from .workspace_manager import WorkspaceManager

# --- CONTENT ENGINE (Logic Assimilated from ericosiu_skills) ---

class ContentStrategyEngine:
    # Logic from quote-mining-engine.py and autoresearch.py
    
    @staticmethod
    def mine_quotes(client_id, transcript_text):
        """Extracts highly quotable, controversial, or insightful sentences from raw transcripts."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "content_strategy")
        
        # Simulated NLP extraction for strong assertions
        sentences = re.split(r'(?<=[.!?]) +', transcript_text)
        strong_quotes = []
        for s in sentences:
            if len(s.split()) > 6 and any(word in s.lower() for word in ["believe", "never", "always", "secret", "truth", "fail"]):
                strong_quotes.append(s)
                
        # Limit to top 5
        result = {"source_length": len(transcript_text), "extracted_quotes": strong_quotes[:5]}
        
        with open(ws_path / "mined_quotes.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class SocialRepurposerEngine:
    # Logic from content-transform.py and x-longform-post
    
    @staticmethod
    def transform_to_social(client_id, blog_content):
        """Transforms a long-form blog post into LinkedIn posts and a Twitter thread."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "organic_social")
        
        # In reality, this passes the content to an LLM chain. Here we simulate the structural generation.
        paragraphs = [p for p in blog_content.split("\n\n") if len(p) > 20]
        
        thread = []
        for i, p in enumerate(paragraphs[:5]):
            thread.append(f"{i+1}/ {p[:200]}...")
            
        linkedin = [
            f"Here is a controversial take: {paragraphs[0][:150]}... \n\nWhat are your thoughts? 👇",
            f"3 things I learned this week:\n1. {paragraphs[1][:50]}\n2. {paragraphs[2][:50]}\n3. Focus on what matters."
        ]
        
        result = {"twitter_thread": thread, "linkedin_posts": linkedin}
        
        with open(ws_path / "repurposed_social_drafts.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class VideoMultimediaEngine:
    # Logic from shortform_pipeline.py and yt-competitive-analysis
    
    @staticmethod
    def analyze_youtube_hooks(client_id, competitor_data):
        """Analyzes competitor YouTube titles to find viral outliers (Views > 3x Subs)."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "video_multimedia")
        
        outliers = []
        for video in competitor_data:
            views = video.get("views", 0)
            subs = video.get("channel_subs", 1) # Prevent div by zero
            if views > (subs * 3):
                outliers.append(video["title"])
                
        # Extract common starting words (Hooks)
        hooks = [title.split()[0] + " " + title.split()[1] for title in outliers if len(title.split()) > 1]
        top_hooks = list(set(hooks))[:5]
        
        result = {"outlier_videos_found": len(outliers), "top_hook_patterns": top_hooks}
        with open(ws_path / "youtube_hook_analysis.json", "w") as f:
            json.dump(result, f, indent=2)
        return result

    @staticmethod
    def simulate_ffmpeg_clipping(client_id, youtube_url, transcript_timestamps):
        """Simulates the FFMpeg clipping process based on viral timestamps."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "video_multimedia")
        pending_dir = ws_path / "pending_approval"
        pending_dir.mkdir(exist_ok=True)
        
        clips = []
        for i, ts in enumerate(transcript_timestamps[:3]): # Take top 3 moments
            clip_name = f"viral_clip_{i+1}.mp4"
            # Simulate FFMpeg action
            with open(pending_dir / f"{clip_name}_metadata.txt", "w") as f:
                f.write(f"Source: {youtube_url}\nStart: {ts['start']}\nEnd: {ts['end']}\nHook: {ts['text']}")
            clips.append(clip_name)
            
        return clips

class CopywritingEngine:
    # Logic from content-quality-scorer.py
    
    @staticmethod
    def score_and_de_slop_text(client_id, text, content_type="blog"):
        """Detects AI slop words and calculates a human-readability score."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "content", "copywriting")
        
        slop_words = ["delve", "testament", "tapestry", "multifaceted", "moreover", "furthermore", "in conclusion"]
        found_slop = []
        lower_text = text.lower()
        
        for word in slop_words:
            count = lower_text.count(word)
            if count > 0:
                found_slop.extend([word] * count)
                
        base_score = 100 - (len(found_slop) * 5)
        
        # Simulate replacing slop with simpler words
        optimized_text = text
        optimized_text = re.sub(r'(?i)delve into', 'explore', optimized_text)
        optimized_text = re.sub(r'(?i)is a testament to', 'shows', optimized_text)
        
        result = {
            "original_score": max(base_score, 0),
            "slop_words_detected": found_slop,
            "optimized_preview": optimized_text[:200] + "..."
        }
        
        with open(ws_path / f"quality_score_{content_type}.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result, optimized_text
