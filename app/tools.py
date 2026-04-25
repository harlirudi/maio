from google.adk.tools import ToolContext

# --- SEO Ops Tools ---

def fetch_search_trends(topic: str, tool_context: ToolContext) -> dict:
    """Mensimulasikan alat Trend Scout untuk mengambil kata kunci bervolume tinggi.
    
    Menyimpan kata kunci utama yang ditemukan ke dalam session state agar
    bisa digunakan oleh agen lain (seperti Content Agent).

    Args:
        topic: Topik atau niche yang ingin diriset (misal: "sepatu lari").
    """
    # Mock data berdasarkan topik
    simulated_keywords = [
        f"{topic} terbaik 2026",
        f"review {topic} murah",
        f"cara memilih {topic}"
    ]
    
    # MENYIMPAN KE STATE: Inilah cara agen berbagi informasi lintas departemen
    tool_context.state["target_keywords"] = simulated_keywords
    
    return {
        "status": "success",
        "topic_analyzed": topic,
        "high_volume_keywords": simulated_keywords,
        "search_intent": "transactional & informational"
    }

def audit_core_web_vitals(url: str) -> dict:
    """Mensimulasikan audit SEO teknis menggunakan data Core Web Vitals.

    Args:
        url: URL website klien yang akan diaudit.
    """
    # Mock pengujian teknis
    return {
        "url": url,
        "status": "needs_improvement",
        "metrics": {
            "LCP": "3.2s (Poor)",
            "FID": "40ms (Good)",
            "CLS": "0.15 (Needs Improvement)"
        },
        "recommendations": [
            "Kompresi gambar berukuran besar di homepage",
            "Tunda pemuatan JavaScript yang tidak kritis (render-blocking)"
        ]
    }


# --- Content Ops Tools ---

def evaluate_content_quality(draft: str, brand_voice_rules: str) -> dict:
    """Mensimulasikan 'Editorial Brain' / Expert Panel untuk menilai kualitas draf.
    Sistem akan memberikan skor berdasarkan kepatuhan pada brand voice.

    Args:
        draft: Teks draf konten yang ditulis oleh agen.
        brand_voice_rules: Aturan gaya bahasa (misal: "kasual, profesional, urgensi").
    """
    # Evaluasi mock (biasanya memanggil LLM lagi untuk menilai, tapi kita pakai mock sederhana)
    word_count = len(draft.split())
    
    # Logika fiktif sederhana: makin panjang, makin dianggap "detail" (untuk demonstrasi)
    base_score = 70
    if word_count > 50:
        base_score += 15
        
    is_compliant = brand_voice_rules.lower() in draft.lower()
    if is_compliant:
         base_score += 10
         
    return {
        "overall_score": min(base_score, 100), # Cap at 100
        "word_count": word_count,
        "feedback": "Draf cukup baik. Pastikan Call-to-Action (CTA) lebih menonjol di akhir paragraf." if base_score < 90 else "Konten sangat kuat dan siap publikasi.",
        "brand_voice_adherence": "Tinggi" if is_compliant else "Sedang"
    }
