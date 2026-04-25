# TECHNICAL_SPEC.md: MAIO SEVO Internal Architecture

This document provides the exhaustive technical blueprint of the MAIO SEVO Neural Operating System, detailing the 4-Tier Agent Hierarchy and the Dynamic Task Routing logic.

## 1. Multi-Agent Hierarchy

### Tier 1: Strategic Layer
- **cmo_agent (Gemini 2.5 Pro):** Orchestrates the client-facing 'State Machine'. 
  - *Functions:* Discovery, Diagnostic Questionnaires, Proposal Generation, Negotiation.
  - *Decision Logic:* Must consult AI CFO for pricing before proposal issuance.

### Tier 2: Management & Financial Layer
- **finance_ops_agent (AI CFO):** Real-time Profitability Engine.
  - *Logic:* Estimates raw API COGS based on task complexity (Text/Vision/Multimodal).
  - *Guardrails:* Establishes Walk-Away Price thresholds to protect agency margins.
- **vp_omnichannel_search (Dynamic Router):** Execution Manager.
  - *Architecture:* Uses AgentTools to trigger specific specialists only as needed.
  - *Efficiency:* Prevents redundant compute costs by keeping unnecessary specialists idle.

### Tier 3: Specialist Matrix (10 Units)
1. **content_semantic_agent:** Semantic research & Pillar/Cluster strategy.
2. **technical_seo_agent:** Website health, crawler efficiency, and NLP audit.
3. **pr_community_agent:** Digital PR, authority building, and Reddit infiltration.
4. **local_seo_agent:** Google Maps (GBP) hyper-local optimization.
5. **ecommerce_cro_agent:** Conversion psychology, Amazon SEO, and UX audits.
6. **geo_sge_agent:** Insinyur Knowledge Graph & SGE/AI Overview optimization.
7. **video_search_agent:** YouTube & TikTok Multimodal algorithmic optimization.
8. **paid_media_agent:** Paid media arbitrage (Meta/Google) & ROAS management.
9. **analytics_architect_agent:** Data Layer (GTM/GA4) and server-side tracking architecture.
10. **creative_director_agent:** Visual concepts, storyboarding, and multichannel calendar.

## 2. Framework Implementation Details
- **Platform:** Gemini Enterprise Agent Platform (GEAP).
- **Core SDK:** Google Agent Development Kit (ADK) 2.0.
- **State Management:** Session-scoped shared memory for cross-agent data sharing (e.g., keyword research results passed to content agents).
- **Routing Pattern:** Conditional Delegation via LlmAgent + AgentTools.

---
*Documentation for internal system developers and strategists.*
