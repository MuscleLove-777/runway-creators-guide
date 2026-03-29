"""Runway AI動画クリエイターズガイド - プロンプト定義

Runway AI動画生成特化ブログ用のプロンプトを一元管理する。
JSON-LD構造化データ（BlogPosting / FAQPage / BreadcrumbList）対応。
"""

# ペルソナ設定
PERSONA = (
    "あなたはAI動画生成ツールRunwayの日本語エキスパートです。"
    "Gen-4のモーション制御・カメラワーク設定・テキストtoビデオに精通し、"
    "映像クリエイターから初心者まで幅広い読者に実践的な情報を届けるプロのテックライターです。"
    "Runwayの最新アップデートを常にキャッチアップし、"
    "他のAI動画生成ツール（Veo、Kling、Pika、旧Sora等）との比較も客観的に行えます。"
    "商用利用・著作権・料金プランにも詳しく、プロの映像制作ワークフローへの"
    "組み込み方を具体的に解説できます。"
)

# 記事フォーマット指示
ARTICLE_FORMAT = """
【記事構成（必ずこの順序で書くこと）】

## この記事でわかること
- ポイント1（具体的なベネフィット）
- ポイント2
- ポイント3

## 結論（先に結論を述べる）
（読者が最も知りたい答えを最初に提示）

## 本題（H2で3〜5セクション）
（具体的な操作手順・設定パラメータ・プロンプト例を詳しく解説）

## プロの映像制作ワークフロー
（Premiere Pro / DaVinci Resolve / After Effects との連携方法）

## 他のAI動画ツールとの比較
（Veo / Kling / Pika / 旧Sora との違いを表形式で整理）

## よくある質問（FAQ）
### Q1: （よくある質問1）
A1: （回答1）

### Q2: （よくある質問2）
A2: （回答2）

### Q3: （よくある質問3）
A3: （回答3）

## まとめ
（要点整理と次のアクション提案）
"""

# カテゴリ別SEOキーワードヒント
CATEGORY_PROMPTS = {
    "Runway 使い方": "Runway 使い方、Runway 始め方、Runway 初心者、Runway 無料、Runway テキストtoビデオ、Runway プロンプト",
    "Runway 料金・プラン": "Runway 料金、Runway 無料 有料 違い、Runway Pro プラン、Runway 月額、Runway クレジット",
    "Runway Gen-4": "Runway Gen-4、Gen-4 新機能、Gen-4 モーション制御、Gen-4 カメラワーク、Gen-4 画質、Gen-4 10秒動画",
    "Runway vs Veo": "Runway Veo 比較、Runway Veo 違い、AI動画 比較 2026、Runway Google Veo どっち",
    "AI動画生成テクニック": "AI動画 プロンプト、モーション制御 コツ、カメラアングル AI、AI動画 高画質、AI動画 商用利用",
    "Runway 最新ニュース": "Runway アップデート、Runway 新機能、Runway リリース、AI動画 最新ニュース",
    "Sora代替比較": "Sora 代替、Sora 終了、OpenAI Sora 代わり、AI動画生成 おすすめ、Sora 代替 比較",
    "Runway 活用事例": "Runway 映像制作、Runway CM制作、Runway ミュージックビデオ、AI動画 ビジネス活用、Runway ポートフォリオ",
}

# ニュースソース
NEWS_SOURCES = [
    "Runway Blog (https://runwayml.com/blog)",
    "Runway Research (https://research.runwayml.com/)",
    "TechCrunch AI Video (https://techcrunch.com/tag/ai-video/)",
    "The Verge AI (https://www.theverge.com/ai-artificial-intelligence)",
    "PetaPixel (https://petapixel.com/category/ai/)",
]

# FAQ構造化データの有効化
FAQ_SCHEMA_ENABLED = True

# キーワード選定用の追加プロンプト
KEYWORD_PROMPT_EXTRA = (
    "Runway（AI動画生成ツール）に関するキーワードを選んでください。\n"
    "日本のクリエイター・映像制作者が検索しそうな実用的なキーワードを意識してください。\n"
    "「Runway 使い方」「Runway Gen-4」「Runway vs Veo」「Sora 代替」のような、\n"
    "検索ボリュームが見込めるキーワードを優先してください。\n"
    "AI動画生成の商用利用・プロンプトテクニック・料金比較も人気のトピックです。"
)


def build_keyword_prompt(config):
    """キーワード選定プロンプトを構築する"""
    categories_text = "\n".join(f"- {cat}" for cat in config.TARGET_CATEGORIES)
    category_hints = "\n".join(
        f"- {cat}: {hints}" for cat, hints in CATEGORY_PROMPTS.items()
    )
    return (
        f"{PERSONA}\n\n"
        "Runway AI動画クリエイターズガイド用のキーワードを選定してください。\n\n"
        f"{KEYWORD_PROMPT_EXTRA}\n\n"
        f"カテゴリ一覧:\n{categories_text}\n\n"
        f"カテゴリ別キーワードヒント:\n{category_hints}\n\n"
        "以下の形式でJSON形式のみで回答してください（説明不要）:\n"
        '{"category": "カテゴリ名", "keyword": "キーワード"}'
    )


def build_article_prompt(keyword, category, config):
    """Runway特化記事生成プロンプトを構築する"""
    category_hints = CATEGORY_PROMPTS.get(category, "")
    news_sources_text = "\n".join(f"- {src}" for src in NEWS_SOURCES)

    return f"""{PERSONA}

以下のキーワードに関する記事を、Runway AI動画生成の専門サイト向けに執筆してください。

【基本条件】
- ブログ名: {config.BLOG_NAME}
- キーワード: {keyword}
- カテゴリ: {category}
- カテゴリ関連キーワード: {category_hints}
- 言語: 日本語
- 文字数: {config.MAX_ARTICLE_LENGTH}文字程度

{ARTICLE_FORMAT}

【SEO要件】
1. タイトルにキーワード「{keyword}」を必ず含めること
2. タイトルは32文字以内で魅力的に（数字や年号を含めると効果的）
3. H2、H3の見出し構造を適切に使用すること
4. キーワード密度は{config.MIN_KEYWORD_DENSITY}%〜{config.MAX_KEYWORD_DENSITY}%を目安に
5. メタディスクリプションは{config.META_DESCRIPTION_LENGTH}文字以内
6. FAQ（よくある質問）を3つ以上含めること（FAQPage構造化データ対応）

【内部リンク】
- 内部リンクのプレースホルダーを2〜3箇所に配置（{{{{internal_link:関連トピック}}}}の形式）

【参考情報源】
{news_sources_text}

【条件】
- {config.MAX_ARTICLE_LENGTH}文字程度
- 2026年最新の情報を反映すること
- 具体的なプロンプト例・パラメータ設定・操作手順を含める
- プロの映像制作ワークフロー（Premiere Pro / DaVinci Resolve等）との連携を含める
- 他のAI動画ツール（Veo, Kling, Pika, 旧Sora等）との客観的な比較を含める
- 商用利用・著作権・ライセンスに関する情報を含める
- 初心者にもわかりやすく、専門用語には補足説明を付ける

【出力形式】
以下のJSON形式で出力してください。JSONブロック以外のテキストは出力しないでください。

```json
{{
  "title": "SEO最適化されたタイトル",
  "content": "# タイトル\\n\\n本文（Markdown形式）...",
  "meta_description": "120文字以内のメタディスクリプション",
  "tags": ["タグ1", "タグ2", "タグ3", "タグ4", "タグ5"],
  "slug": "url-friendly-slug",
  "faq": [
    {{"question": "質問1", "answer": "回答1"}},
    {{"question": "質問2", "answer": "回答2"}},
    {{"question": "質問3", "answer": "回答3"}}
  ]
}}
```

【注意事項】
- content内のMarkdownは適切にエスケープしてJSON文字列として有効にすること
- tagsは5個ちょうど生成すること
- slugは半角英数字とハイフンのみ使用すること
- faqは3個以上生成すること（FAQPage構造化データに使用）
- 読者にとって実用的で具体的な内容を心がけること"""
