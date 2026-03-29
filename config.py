"""Runway AI動画クリエイターズガイド - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "Runway AI動画クリエイターズガイド"
BLOG_DESCRIPTION = "プロ向けAI動画生成RunwayのGen-4使い方・最新機能・Veo比較を毎日更新。映像クリエイターのためのAI動画生成完全ガイド。"
BLOG_URL = "https://musclelove-777.github.io/runway-creators-guide"
BLOG_TAGLINE = "映像クリエイターのためのRunway AI動画生成完全ガイド"
BLOG_LANGUAGE = "ja"

GITHUB_REPO = "MuscleLove-777/runway-creators-guide"
GITHUB_BRANCH = "gh-pages"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

TARGET_CATEGORIES = [
    "Runway 使い方",
    "Runway 料金・プラン",
    "Runway Gen-4",
    "Runway vs Veo",
    "AI動画生成テクニック",
    "Runway 最新ニュース",
    "Sora代替比較",
    "Runway 活用事例",
]

THEME = {
    "primary": "#6c5ce7",
    "accent": "#a29bfe",
    "gradient_start": "#6c5ce7",
    "gradient_end": "#a29bfe",
    "dark_bg": "#0a0a1a",
    "dark_surface": "#1a1530",
    "light_bg": "#f5f3ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 4000
ARTICLES_PER_DAY = 3
SCHEDULE_HOURS = [7, 12, 19]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 75
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "Runway": [
        {"service": "Runway", "url": "https://runwayml.com", "description": "Runwayに登録する"},
    ],
    "Runway Pro": [
        {"service": "Runway Pro", "url": "https://runwayml.com/pricing", "description": "Runway Proプランに申し込む"},
    ],
    "動画編集ソフト": [
        {"service": "Adobe Premiere Pro", "url": "https://www.adobe.com/products/premiere.html", "description": "Adobe Premiere Proを試す"},
        {"service": "DaVinci Resolve", "url": "https://www.blackmagicdesign.com/products/davinciresolve", "description": "DaVinci Resolveを試す"},
    ],
    "オンライン講座": [
        {"service": "Udemy", "url": "https://www.udemy.com", "description": "UdemyでAI動画講座を探す"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "AmazonでAI動画制作の書籍を探す"},
        {"service": "楽天ブックス", "url": "https://www.rakuten.co.jp", "description": "楽天でAI動画制作の書籍を探す"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
ADSENSE_ENABLED = bool(ADSENSE_CLIENT_ID)
DASHBOARD_PORT = 8102
