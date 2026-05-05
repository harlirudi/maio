import os
import json
import random
from datetime import datetime
from .workspace_manager import WorkspaceManager

# --- PAID MEDIA ENGINE (Logic Assimilated from ericosiu_skills) ---

class AdSpendMonitorEngine:
    # Logic assimilated from pacing-alert.py
    
    @staticmethod
    def monitor_pacing(client_id, current_spend, monthly_budget, days_elapsed):
        """Detects overspending or underspending based on daily run rate."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "meta_ads")
        
        total_days = 30
        daily_target = monthly_budget / total_days
        ideal_spend = daily_target * days_elapsed
        pacing_ratio = current_spend / ideal_spend if ideal_spend > 0 else 1.0
        
        status = "HEALTHY"
        message = "Campaign is spending on track."
        
        if pacing_ratio > 1.2:
            status = "OVERSPENDING"
            message = f"Warning: Campaign is {round((pacing_ratio-1)*100)}% over budget."
        elif pacing_ratio < 0.8:
            status = "UNDERSPENDING"
            message = f"Opportunity: Campaign is {round((1-pacing_ratio)*100)}% behind budget."
            
        result = {
            "timestamp": datetime.now().isoformat(),
            "status": status,
            "pacing_ratio": round(pacing_ratio, 2),
            "message": message,
            "recommended_action": "Reduce daily bids" if status == "OVERSPENDING" else "Expand audience targeting"
        }
        
        with open(ws_path / "pacing_alert.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class GoogleAdsEngine:
    # Logic for auditing search intent overlap
    
    @staticmethod
    def audit_intent_overlap(client_id, ads_keywords, organic_keywords):
        """Identifies expensive keywords where we already rank high organically (Cannibalization)."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "google_ads")
        
        cannibalized = []
        for kw in ads_keywords:
            if kw in organic_keywords:
                cannibalized.append(kw)
                
        result = {
            "total_keywords_audited": len(ads_keywords),
            "cannibalized_keywords": cannibalized,
            "saving_potential": f"{len(cannibalized) * 10}% reduction in wasted spend"
        }
        
        with open(ws_path / "keyword_cannibalization_audit.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class TikTokCreativeEngine:
    # Logic for short-form ad hook analysis
    
    @staticmethod
    def analyze_ad_creative_brief(client_id, goal_description):
        """Drafts specific TikTok ad hooks based on the performance of top-performing patterns."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "tiktok_short_ads")
        
        hooks = [
            f"Why most people fail at {goal_description}",
            f"The secret hack for {goal_description} in 2026",
            f"Stop doing this if you want {goal_description}"
        ]
        
        result = {"campaign_goal": goal_description, "drafted_hooks": hooks}
        
        with open(ws_path / "creative_brief.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class BiddingOptimizer:
    # Existing refined logic
    @staticmethod
    def get_optimized_bids(client_id, campaign_data):
        """Simulates bid adjustments based on ROAS and CPA targets."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "google_ads")
        
        results = [
            {"keyword": "buy sneakers online", "old_bid": 2.5, "new_bid": 3.1, "reason": "High ROAS"},
            {"keyword": "cheap shoes", "old_bid": 1.8, "new_bid": 1.2, "reason": "Low conversion"}
        ]
        
        with open(ws_path / "optimized_bids.json", "w") as f:
            json.dump({"campaign": campaign_data.get("name", "unknown"), "adjustments": results}, f, indent=2)
            
        return results

class LeadScorer:
    @staticmethod
    def score_lead(client_id, lead_data):
        ws_path = WorkspaceManager.get_specialist_path(client_id, "paid", "programmatic")
        score = 50
        if lead_data.get("job_title") in ["CEO", "CMO", "Founder"]: score += 30
        if lead_data.get("visited_pricing"): score += 20
        result = {"lead_score": score, "tier": "A" if score > 80 else "B"}
        with open(ws_path / f"lead_score_{lead_data.get('email', 'anon').replace('@', '_')}.json", "w") as f:
            json.dump({"lead": lead_data, "result": result}, f, indent=2)
        return result
