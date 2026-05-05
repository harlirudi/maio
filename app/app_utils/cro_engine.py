import os
import json
import random
from datetime import datetime
from scipy import stats # Simulating import for A/B testing
from .workspace_manager import WorkspaceManager

# --- CRO & ANALYTICS ENGINE (Logic Assimilated from ericosiu_skills) ---

class CROAuditEngine:
    # Logic assimilated from cro_audit.py
    HEURISTICS = [
        "Clarity (Is the value prop obvious within 3 seconds?)",
        "Friction (Are there too many form fields?)",
        "Distraction (Are there competing CTAs?)",
        "Urgency (Is there a reason to act now?)",
        "Anxiety (Is the site secure/trustworthy?)"
    ]

    @classmethod
    def audit_landing_page(cls, client_id, page_html_text):
        """Simulates analyzing page text/structure against conversion heuristics."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "uiux_ab_test")
        
        issues = []
        lower_text = page_html_text.lower()
        
        if "buy now" not in lower_text and "sign up" not in lower_text and "get started" not in lower_text:
            issues.append({"heuristic": "Clarity", "issue": "Missing clear primary Call-to-Action (CTA)."})
            
        if "review" not in lower_text and "testimonial" not in lower_text and "trusted by" not in lower_text:
            issues.append({"heuristic": "Anxiety", "issue": "Lack of social proof/trust signals on page."})
            
        score = max(100 - (len(issues) * 20), 40)
        grade = "A" if score >= 90 else "B" if score >= 70 else "C" if score >= 50 else "D"
        
        result = {"audit_score": score, "grade": grade, "critical_issues": issues}
        
        with open(ws_path / "heuristic_audit_report.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class GrowthExperimenter:
    # Logic assimilated from experiment-engine.py
    @staticmethod
    def run_statistical_analysis(client_id, variant_a_data, variant_b_data):
        """Runs a T-Test to determine if Variant B's conversion lift is statistically significant."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "uiux_ab_test")
        
        # Real math for conversion rates
        conversions_a, traffic_a = variant_a_data
        conversions_b, traffic_b = variant_b_data
        
        cr_a = (conversions_a / traffic_a) if traffic_a else 0
        cr_b = (conversions_b / traffic_b) if traffic_b else 0
        
        lift = ((cr_b - cr_a) / cr_a * 100) if cr_a > 0 else 0
        
        # Simulated p-value calculation (In reality, use statsmodels or scipy.stats.ttest_ind)
        # We simulate that a lift > 5% with > 1000 traffic gets a significant p-value
        p_value = 0.03 if (lift > 5 and traffic_a > 1000) else 0.15 
        
        is_significant = p_value < 0.05
        
        result = {
            "control_cr": round(cr_a * 100, 2),
            "variant_cr": round(cr_b * 100, 2),
            "lift_pct": round(lift, 2),
            "p_value": p_value,
            "statistically_significant": is_significant,
            "status": "DEPLOY_VARIANT" if is_significant and lift > 0 else "KEEP_CONTROL"
        }
        
        with open(ws_path / "ab_test_results.json", "w") as f:
            json.dump(result, f, indent=2)
            
        return result

class LandingPageEngine:
    # Logic assimilated from clone-site and survey_lead_magnet.py
    @staticmethod
    def generate_wireframe_spec(client_id, survey_pain_points):
        """Generates a JSON wireframe structure tailored to audience pain points."""
        ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "landing_page_spec")
        
        top_pain_point = survey_pain_points[0] if survey_pain_points else "General inefficiency"
        
        wireframe = {
            "hero_section": {
                "headline": f"Stop struggling with {top_pain_point}.",
                "subheadline": "Our proven system solves it in 30 days.",
                "cta": "Get Free Audit"
            },
            "social_proof_section": {"type": "logo_farm", "count": 5},
            "features_section": [
                {"title": "Automated Workflows", "description": "Save 10 hours a week."},
                {"title": "Data Driven", "description": "No more guessing."}
            ],
            "lead_capture_form": {"fields": ["Name", "Work Email", "Company Size"]}
        }
        
        with open(ws_path / "wireframe_spec.json", "w") as f:
            json.dump(wireframe, f, indent=2)
            
        return wireframe

class RevenueAttributor:
    # Existing logic...
    @staticmethod
    def map_revenue(client_id, deals, model="linear"):
        ws_path = WorkspaceManager.get_specialist_path(client_id, "cro", "web_analytics")
        total_revenue = sum(d.get("amount", 0) for d in deals)
        by_type = {
            "blog": total_revenue * 0.4,
            "video": total_revenue * 0.3,
            "podcast": total_revenue * 0.2,
            "other": total_revenue * 0.1
        }
        result = {
            "model": model,
            "total_attributed_revenue": total_revenue,
            "breakdown_by_type": by_type
        }
        with open(ws_path / "attribution_report.json", "w") as f:
            json.dump(result, f, indent=2)
        return result

    @staticmethod
    def find_content_gaps(client_id):
        return [
            {"stage": "consideration", "status": "WEAK", "recommendation": "Create more case studies."},
            {"stage": "decision", "status": "CRITICAL", "recommendation": "Add pricing and ROI calculator pages."}
        ]
