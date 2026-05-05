import os
import json
import re
import random
from datetime import datetime, timedelta
from .workspace_manager import WorkspaceManager

# --- REV OPS ENGINE (Logic Assimilated from ericosiu_skills) ---

class RevenueIntelEngine:
    # Patterns from gong_insight_pipeline.py
    OBJECTION_PATTERNS = {
        "pricing": [r"(?i)(too expensive|budget.*tight|pricing is|cost too high)"],
        "timing": [r"(?i)(not the right time|next quarter|not ready)"],
        "competition": [r"(?i)(already using|working with|competitor)"],
    }
    
    BUYING_SIGNAL_PATTERNS = {
        "budget_confirmed": [r"(?i)(budget.*approved|have.*budget|willing to spend)"],
        "timeline_mentioned": [r"(?i)(need.*live by|start date|asap)"],
        "champion_identified": [r"(?i)(exactly what we need|perfect fit|game changer)"],
    }

    @classmethod
    def analyze_transcript(cls, client_id, transcript_text):
        """Extracts structured insights using regex patterns from Single Grain scripts."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "revenue_intel")
        
        objections = []
        for cat, patterns in cls.OBJECTION_PATTERNS.items():
            for p in patterns:
                if re.search(p, transcript_text):
                    objections.append(cat)
                    break
        
        signals = []
        for sig, patterns in cls.BUYING_SIGNAL_PATTERNS.items():
            for p in patterns:
                if re.search(p, transcript_text):
                    signals.append(sig)
                    break
                    
        result = {
            "timestamp": datetime.now().isoformat(),
            "objections_detected": list(set(objections)),
            "buying_signals": list(set(signals)),
            "deal_temperature": "HOT" if len(signals) > len(objections) else "WARM"
        }
        
        with open(ws_path / "call_analysis.json", "w") as f:
            json.dump(result, f, indent=2)
        return result

class DealResurrectorEngine:
    # Logic from deal_resurrector.py
    @staticmethod
    def calculate_resurrection_score(days_since_close, deal_value, loss_reason):
        """Calculates a score (0-100) for deal revival priority."""
        score = 0
        # Time decay logic: 60-90 days is sweet spot
        if 60 <= days_since_close <= 180: score += 40
        elif days_since_close > 180: score += 20
        
        # Value component
        if deal_value > 50000: score += 30
        elif deal_value > 10000: score += 20
        
        # Reason bonus
        if "timing" in loss_reason.lower(): score += 30
        elif "budget" in loss_reason.lower(): score += 15
        
        return min(100, score)

class SalesEnablementEngine:
    # Logic from value_pricing_packager.py
    @staticmethod
    def generate_tiered_pricing(deal_target):
        """Generates S/M/L tiers based on psychological anchoring."""
        return {
            "powerhouse": {
                "price": round(deal_target * 1.5, -2),
                "strategy": "Maximum growth + Senior Strategist"
            },
            "value": {
                "price": round(deal_target, -2),
                "strategy": "Recommended: Core growth levers"
            },
            "baseline": {
                "price": round(deal_target * 0.5, -2),
                "strategy": "Foundational: Critical items only"
            }
        }

class LeadPipeline:
    @staticmethod
    def source_leads(client_id, titles, industries, volume=10):
        """Simulation of lead sourcing from Apollo/Source API."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "outbound_lead_gen")
        mock_leads = []
        for i in range(volume):
            company = random.choice(["TechFlow", "CloudScale", "MarketGen", "DataSync"])
            mock_leads.append({
                "email": f"contact{i}@{company.lower()}.com",
                "first_name": f"Lead_{i}",
                "last_name": "Doe",
                "title": random.choice(titles.split(",")),
                "company_name": company,
                "domain": f"{company.lower()}.com"
            })
        with open(ws_path / "last_sourced_leads.json", "w") as f:
            json.dump(mock_leads, f, indent=2)
        return mock_leads

    @staticmethod
    def verify_emails(client_id, leads):
        """Simulation of email verification."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "outbound_lead_gen")
        valid = [l for l in leads if random.random() > 0.1]
        stats = {"total": len(leads), "valid": len(valid)}
        with open(ws_path / "verified_leads.json", "w") as f:
            json.dump({"stats": stats, "leads": valid}, f, indent=2)
        return valid, stats

def process_rb2b_visitor(client_id, visitor_data):
    """Assimilated logic from rb2b_instantly_router.py."""
    ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "crm_automation")
    pages = visitor_data.get("pages_visited", [])
    score = 30
    if any("pricing" in p for p in pages): score = 90
    elif any("case-study" in p for p in pages): score = 70
    result = {
        "email": visitor_data.get("email"),
        "intent_score": score,
        "is_agency": "agency" in visitor_data.get("company_name", "").lower(),
        "recommended_campaign": "High-Intent-SDR" if score > 80 else "Nurture-Sequence"
    }
    log_file = ws_path / "visitor_routing_log.jsonl"
    with open(log_file, "a") as f:
        f.write(json.dumps({"timestamp": datetime.now().isoformat(), "result": result}) + "\n")
    return result

class DataIntegrationEngine:
    # Logic assimilated from icp_learning_analyzer.py and client_report_generator.py
    
    @staticmethod
    def analyze_icp_win_rates(closed_won, closed_lost):
        """Analyzes historical deal data to find high-probability ICP (Ideal Customer Profile) traits."""
        industry_wins = {}
        for deal in closed_won:
            ind = deal.get("industry", "unknown")
            industry_wins[ind] = industry_wins.get(ind, 0) + 1
            
        industry_losses = {}
        for deal in closed_lost:
            ind = deal.get("industry", "unknown")
            industry_losses[ind] = industry_losses.get(ind, 0) + 1
            
        # Calculate win rates per industry
        insights = []
        for ind in industry_wins.keys():
            wins = industry_wins[ind]
            losses = industry_losses.get(ind, 0)
            total = wins + losses
            win_rate = (wins / total) * 100 if total > 0 else 0
            
            if win_rate > 30 and total >= 5:
                insights.append({"industry": ind, "win_rate": round(win_rate, 1), "action": "Double Down"})
            elif win_rate < 10 and total >= 5:
                insights.append({"industry": ind, "win_rate": round(win_rate, 1), "action": "Add to Suppression List"})
                
        return insights

    @staticmethod
    def generate_unified_roi_report(client_id, ga4_data, hubspot_data, ad_spend_data):
        """Merges traffic, deals, and spend data to generate a unified BI ROI report."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "revops", "data_integrator")
        
        total_spend = sum(ad_spend_data.values()) if ad_spend_data else 0
        total_revenue = sum([d.get("amount", 0) for d in hubspot_data if d.get("status") == "closed_won"])
        total_traffic = ga4_data.get("total_users", 0)
        
        roi = ((total_revenue - total_spend) / total_spend * 100) if total_spend > 0 else 0
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "total_traffic": total_traffic,
                "ad_spend": total_spend,
                "revenue_closed": total_revenue,
                "roi_percentage": round(roi, 2)
            },
            "status": "HEALTHY" if roi > 300 else "NEEDS_OPTIMIZATION"
        }
        
        report_path = ws_path / f"unified_bi_report_{datetime.now().strftime('%Y%m%d')}.json"
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)
            
        return report, report_path
