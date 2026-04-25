# DESIGN_SPEC.md: GEAP Agency Core (MAIO SEVO)

## 1. Overview
Sistem ini adalah orkestrator multi-agen untuk agensi pemasaran digital bertenaga AI. Menggunakan Google ADK dengan protokol A2A (Agent-to-Agent) untuk koordinasi antar departemen.

## 2. Agent Hierarchy & Roles

### Tier 1: CMO Agent (Orchestrator)
- **Role:** Strategist & Resource Allocator.
- **Model:** Gemini 2.5 Pro.
- **Goal:** Menganalisis brief klien, menetapkan KPI, dan mendelegasikan kampanye ke VP departemen.
- **Output:** JSON berisi `client_goal`, `assigned_vp`, dan `budget_allocation`.

### Tier 2: VP Omnichannel Search (Router)
- **Role:** Tactical Planner & Team Leader.
- **Model:** Gemini 2.5 Flash.
- **Goal:** Memecah kampanye besar menjadi tugas-tugas spesifik untuk tim Spesialis.
- **Output:** JSON berisi daftar `sprint_tasks`.

### Tier 3: Specialist Agents (Execution)
1. **Technical & Infra Agent:** Audit SEO Teknis.
2. **Programmatic SEO Agent:** Landing page generation.
3. **Content Strategy Agent:** Copywriting & Brand Voice.
4. **GEO Agent:** AI Overview Optimization.
5. **Social & Video Agent:** Multimodal Video Analysis.
6. **Community Trust Agent:** PR & Backlink building.
7. **SEO Exp & CRO Agent:** Conversion optimization.

## 3. Communication Pattern
- CMO Agent berkomunikasi dengan VP melalui `adk.flows.llm_flows.agent_transfer`.
- VP memicu spesialis secara paralel menggunakan `adk.agents.parallel_agent`.
- State global seperti `client_id` dan `total_budget` dikelola melalui `adk.sessions.state`.

## 4. Technical Constraints
- **Platform:** Gemini Enterprise Agent Platform (GEAP).
- **Authentication:** Level 2 Option A (API Key).
- **Language:** Python (ADK).
