import feedparser
import os
from datetime import datetime

# CONFIGURATION
CHANNEL_ID = "UCLcPfeVlJWGlqN1QV9IIwLA"
# Ersetze das 'YOUR_HANDLE' durch deinen YouTube-Namen für den Abo-Button
SUBSCRIBE_LINK = "https://www.youtube.com/channel/UCLcPfeVlJWGlqN1QV9IIwLA?sub_confirmation=1"
RSS_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"

def generate_website():
    print(f"📡 Refining the WOCT Chess experience...")
    feed = feedparser.parse(RSS_URL)
    
    video_cards_html = ""
    count = 0
    
    for entry in feed.entries:
        count += 1
        video_url = entry.link
        title = entry.title
        video_id = entry.yt_videoid
        
        is_short = "/shorts/" in video_url
        badge_html = '<span class="badge position-absolute top-0 end-0 m-3 py-2 px-3">SHORT</span>' if is_short else ""
        
        img_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        
        try:
            published = datetime.strptime(entry.published, '%Y-%m-%dT%H:%M:%S+00:00').strftime('%b %d, %Y')
        except:
            published = "Recently"

        video_cards_html += f"""
        <div class="col-12 col-md-6 col-lg-4 mb-5">
            <div class="card h-100 shadow border-0 bg-dark text-white video-card position-relative">
                {badge_html}
                <div class="img-container">
                    <img src="{img_url}" class="card-img-top" alt="{title}">
                </div>
                <div class="card-body d-flex flex-column p-4">
                    <h5 class="card-title h6 mb-3 fw-bold lh-base">{title}</h5>
                    <div class="mt-auto d-flex justify-content-between align-items-center">
                        <span class="small text-secondary fw-semibold">📅 {published}</span>
                        <a href="{video_url}" target="_blank" class="btn btn-gold btn-sm px-4 fw-bold">WATCH</a>
                    </div>
                </div>
            </div>
        </div>
        """
        if count >= 30:
            break

    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="google-site-verification" content="RJEU9h3DT5L4xRKg5ANDmj_SPTnDKshY9n8KCSlrZfQ" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>World of Chess Tournaments | Official Masterclass</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
        <style>
            :root {{
                --gold: #D4AF37;
                --dark-bg: #0a0c10;
                --card-bg: #161b22;
            }}
            body {{ 
                background-color: var(--dark-bg); 
                color: #f0f6fc; 
                font-family: 'Inter', sans-serif; 
            }}
            /* ... Rest deiner Styles wie gehabt ... */
            .navbar {{ 
                background-color: rgba(10, 12, 16, 0.95) !important; 
                backdrop-filter: blur(10px);
                border-bottom: 1px solid #30363d;
            }}
            .hero {{ 
                background: radial-gradient(circle at center, #1e3a8a33 0%, var(--dark-bg) 100%);
                padding: 100px 0 60px 0; 
                border-bottom: 1px solid #30363d;
            }}
            .hero h1 {{ font-weight: 800; letter-spacing: -1px; }}
            .video-card {{ 
                transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); 
                border-radius: 16px; 
                background: var(--card-bg) !important;
                overflow: hidden;
            }}
            .video-card:hover {{ 
                transform: translateY(-10px); 
                box-shadow: 0 20px 40px rgba(0,0,0,0.6) !important;
                border: 1px solid var(--gold) !important;
            }}
            .img-container {{ overflow: hidden; }}
            .video-card img {{ transition: transform 0.5s ease; }}
            .video-card:hover img {{ transform: scale(1.05); }}
            
            .btn-gold {{ 
                background-color: var(--gold); 
                color: #000; 
                border-radius: 8px;
                border: none;
            }}
            .btn-gold:hover {{ background-color: #f1c40f; color: #000; }}
            
            .btn-outline-gold {{ 
                border: 2px solid var(--gold); 
                color: var(--gold); 
                border-radius: 8px;
            }}
            .btn-outline-gold:hover {{ background-color: var(--gold); color: #000; }}

            .badge {{ 
                background-color: rgba(212, 175, 55, 0.9); 
                color: #000; 
                font-weight: 800;
                z-index: 10;
            }}
            .gold-text {{ color: var(--gold); }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-dark fixed-top">
            <div class="container d-flex justify-content-between">
                <span class="navbar-brand fw-bold">♟️ <span class="gold-text">WOCT</span> CHESS</span>
                <a href="{SUBSCRIBE_LINK}" target="_blank" class="btn btn-outline-gold btn-sm fw-bold">SUBSCRIBE</a>
            </div>
        </nav>
        
        <header class="hero text-center">
            <div class="container">
                <h1 class="display-3 fw-bold mb-3">WORLD OF <span class="gold-text">CHESS</span> TOURNAMENTS</h1>
                <p class="lead text-secondary mx-auto shadow-text" style="max-width: 600px;">
                    Experience professional tournament analysis and grandmaster insights daily.
                </p>
            </div>
        </header>

        <div class="container mt-5">
            <div class="row">
                {video_cards_html}
            </div>
        </div>

        <footer class="text-center mt-5 py-5 border-top border-secondary text-secondary small">
            <p>&copy; {datetime.now().year} World of Chess Tournaments<br>
            <span class="text-uppercase tracking-widest" style="font-size: 0.65rem; opacity: 0.5;">Masterclass Digital Feed</span></p>
        </footer>
    </body>
    </html>
    """
    # SITEMAP GENERATION
    sitemap_html = f"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://emanuelwieland.github.io/woct-chess/</loc>
            <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
            <changefreq>hourly</changefreq>
            <priority>1.0</priority>
        </url>
    </urlset>
    """
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_html)
    print("✅ Sitemap.xml generated!")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ Premium Website generated! Check your index.html.")

if __name__ == "__main__":
    generate_website()
