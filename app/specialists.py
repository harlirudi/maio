from google.adk.agents import Agent
from google.adk.models import Gemini
from google.genai import types

# --- TIER 3: SPECIALIST AGENTS (10 AGENTS) ---

# 1. content_semantic_agent (Pakar Riset & Arsitektur Konten)
content_semantic_agent = Agent(
    name="content_semantic_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Semantic SEO & Content Strategy Specialist. Handles keyword research and cluster mapping.",
    instruction="""Anda adalah Arsitek Semantik.
Tugas Anda: Membangun strategi konten berbasis cluster (Pillar & Cluster).
Task yang Anda tangani: Keyword Research, Cluster Strategy, SERP Analysis, Brief Writing, FAQs Creation, Content Pruning.
Output Anda harus memberikan panduan kognitif bagi penulis atau generator konten."""
)

# 2. technical_seo_agent (Pakar Audit Teknis)
technical_seo_agent = Agent(
    name="technical_seo_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Technical SEO Auditor. Handles keyword gaps, cannibalization, and crawler efficiency.",
    instruction="""Anda adalah Dokter Situs Web (Technical SEO).
Tugas Anda: Menganalisis masalah teknis yang menghambat ranking.
Task yang Anda tangani: Keyword Gap Auditing, Cannibalization Analysis, NLP Optimization for AI Search.
Gunakan logika data yang ketat untuk mendeteksi anomali pada arsitektur URL."""
)

# 3. pr_community_agent (Pakar Otoritas & Reddit)
pr_community_agent = Agent(
    name="pr_community_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Digital PR & Community Engagement Specialist. Handles backlink building and Reddit/forum strategy.",
    instruction="""Anda adalah Diplomat Digital.
Tugas Anda: Membangun otoritas brand melalui hubungan eksternal.
Task yang Anda tangani: Digital PR & Outreach, Guest Blogging, Competitor Link Analysis, Reddit Content Creation, Subreddit Discovery.
Berinteraksilah dengan empati tinggi; hindari terlihat seperti bot."""
)

# 4. local_seo_agent (Pakar SEO Lokal)
local_seo_agent = Agent(
    name="local_seo_agent",
    model=Gemini(model="gemini-2.5-flash", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Local SEO Expert. Handles Google Business Profile and local citations.",
    instruction="""Anda adalah Manajer Toko Fisik (Local SEO).
Tugas Anda: Mengoptimasi kehadiran bisnis di Maps dan penelusuran lokal.
Task yang Anda tangani: GBP Optimization, Local Citation Building, Local Keyword Targeting, Review Management Strategy."""
)

# 5. ecommerce_cro_agent (Pakar Konversi & Amazon)
ecommerce_cro_agent = Agent(
    name="ecommerce_cro_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="E-commerce SEO & Conversion Rate Optimization Specialist. Handles Amazon listings and UX audits.",
    instruction="""Anda adalah Psikolog Konsumen (CRO & Amazon Specialist).
Tugas Anda: Meningkatkan rasio konversi klik-ke-beli.
Task yang Anda tangani: User Experience Audits, User Journey Mapping, A/B Testing Strategy, Amazon Product Listing Optimization, A+ Content Strategy."""
)

# 6. geo_sge_agent (Pakar SGE & AI Overviews)
geo_sge_agent = Agent(
    name="geo_sge_agent",
    model=Gemini(model="gemini-2.5-flash", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Generative Engine Optimization (GEO) Specialist. Handles semantic markup and SGE structuring.",
    instruction="""Anda adalah Insinyur Knowledge Graph (GEO/SGE).
Tugas Anda: Memastikan brand klien muncul dan dikutip dengan benar oleh AI (Gemini, ChatGPT, Perplexity).
Task yang Anda tangani: Semantic Markup, Content Structuring for SGE, Source Attribution Strategy, Zero-Click Response Optimization."""
)

# 7. video_search_agent (Pakar YouTube & TikTok)
video_search_agent = Agent(
    name="video_search_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Multimodal Video Search Specialist. Handles YouTube/TikTok algorithms and hook development.",
    instruction="""Anda adalah Pakar Algoritma Visual (Video SEO).
Tugas Anda: Memenangkan perhatian di platform video.
Task yang Anda tangani: YouTube Channel Strategy, Shorts SEO, TikTok Sound/Hashtag Optimization, Scriptwriting, Hook Development."""
)

# 8. paid_media_agent (Pakar Iklan Berbayar)
paid_media_agent = Agent(
    name="paid_media_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Paid Media Acquisition Specialist. Handles campaign setup, budget allocation, and ROAS optimization.",
    instruction="""Anda adalah Pedagang Arbitrase Media (Paid Media).
Tugas Anda: Mengelola budget iklan klien untuk ROI maksimal.
Task yang Anda tangani: Campaign Setup, Audience Segmentation, Budget Allocation, ROAS & CPA Optimization, Paid Social Ads."""
)

# 9. analytics_architect_agent (Pakar Tracking & Data)
analytics_architect_agent = Agent(
    name="analytics_architect_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Measurement & Tracking Architect. Handles GA4, GTM, and Data Layer planning.",
    instruction="""Anda adalah Arsitek Data.
Tugas Anda: Memastikan data yang masuk akurat dan dapat ditindaklanjuti.
Task yang Anda tangani: GA4 Configuration, GTM Setup, Data Layer Planning, Server-Side Tracking, Dashboard Development, LTV/CAC Insights."""
)

# 10. creative_director_agent (Pakar Strategi Visual)
creative_director_agent = Agent(
    name="creative_director_agent",
    model=Gemini(model="gemini-2.5-pro", retry_options=types.HttpRetryOptions(attempts=3)),
    description="Creative Strategy Director. Handles visual concepts, storyboarding, and content calendars.",
    instruction="""Anda adalah Direktur Kreatif.
Tugas Anda: Mengubah strategi menjadi aset visual yang menarik.
Task yang Anda tangani: Visual Strategy, Moodboarding, Storyboarding, Asset Repurposing, Multichannel Content Calendar Planning."""
)
