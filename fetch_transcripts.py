"""
Fetch YouTube transcripts for AI-powered SEO content research project.
Uses youtube-transcript-api v1.x  (api.list + transcript.fetch)
"""

import os
import json
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

EXPERTS = [
    {"name": "Ross Simmonds",  "slug": "ross-simmonds",  "video_id": "nRSr9KW4U2s", "title": "Marketing In The AI Age: Research, Trends & Data for 2024",                  "date": "2024-06-14", "channel": "RossSimmondsTV",              "url": "https://www.youtube.com/watch?v=nRSr9KW4U2s"},
    {"name": "Lily Ray",       "slug": "lily-ray",       "video_id": "zjlAVsjwe4E", "title": "Why Sites Lose Rankings: The 'Too Much SEO' Problem",                       "date": "2025-12-01", "channel": "Lily Ray",                    "url": "https://www.youtube.com/watch?v=zjlAVsjwe4E"},
    {"name": "Aleyda Solis",   "slug": "aleyda-solis",   "video_id": "lEtXlk0XTsI", "title": "AI Mode & The Query Fan-Out Technique: How Google AI Search Works",         "date": "2025-05-01", "channel": "Aleyda Solis / Crawling Mondays", "url": "https://www.youtube.com/watch?v=lEtXlk0XTsI"},
    {"name": "Kevin Indig",    "slug": "kevin-indig",    "video_id": "qujABKOAThA", "title": "SEO in the Age of AI",                                                       "date": "2025-09-01", "channel": "Kevin Indig",                 "url": "https://www.youtube.com/watch?v=qujABKOAThA"},
    {"name": "Matt Diggity",   "slug": "matt-diggity",   "video_id": "x2FTDqR-aH4", "title": "My SEO 2024 Predictions (And How to Prepare for Them)",                     "date": "2024-01-01", "channel": "Matt Diggity",                "url": "https://www.youtube.com/watch?v=x2FTDqR-aH4"},
    {"name": "Nathan Gotch",   "slug": "nathan-gotch",   "video_id": "qG5yrDFDgJA", "title": "On-Page SEO Checklist 2024 — AI-Augmented Workflows",                       "date": "2024-01-01", "channel": "Nathan Gotch",                "url": "https://www.youtube.com/watch?v=qG5yrDFDgJA"},
    {"name": "Mike King",      "slug": "mike-king",      "video_id": "2NYAgb5Jzh4", "title": "The Future of Search: Google I/O Recap & AI SEO Implications",              "date": "2025-05-23", "channel": "iPullRank",                   "url": "https://www.youtube.com/watch?v=2NYAgb5Jzh4"},
    {"name": "Ryan Law",       "slug": "ryan-law",       "video_id": "D7LBx8RFOcQ", "title": "AI Writing at Scale: Ahrefs' Step-by-Step Workflow",                        "date": "2025-08-05", "channel": "Ahrefs",                      "url": "https://www.youtube.com/watch?v=D7LBx8RFOcQ"},
    {"name": "Rand Fishkin",   "slug": "rand-fishkin",   "video_id": "WLzhfmaXxBg", "title": "Good vs Bad Marketing Use Cases for LLMs",                                  "date": "2026-01-01", "channel": "Rand Fishkin / SparkToro",    "url": "https://www.youtube.com/watch?v=WLzhfmaXxBg"},
    {"name": "Britney Muller", "slug": "britney-muller", "video_id": "l4fIHPtjIMY", "title": "Breaking Down AI & Search Changes in 2025",                                 "date": "2025-11-23", "channel": "Britney Muller",              "url": "https://www.youtube.com/watch?v=l4fIHPtjIMY"},
]

PREFER_LANGS = ['en', 'en-US', 'en-GB', 'en-CA', 'en-AU']

api = YouTubeTranscriptApi()

def fetch(video_id):
    tl = api.list(video_id)
    # prefer a manually created transcript in English; fallback to generated
    transcript_obj = None
    for lang in PREFER_LANGS:
        try:
            transcript_obj = tl.find_transcript([lang])
            break
        except Exception:
            pass
    if transcript_obj is None:
        # grab any available
        transcript_obj = next(iter(tl))
    fetched = transcript_obj.fetch()
    snippets = list(fetched)
    text = ' '.join(s.text if hasattr(s, 'text') else s['text'] for s in snippets)
    return text

def save_md(expert, text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{expert['slug']}.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# Transcript: {expert['title']}\n\n")
        f.write(f"**Expert:** {expert['name']}  \n")
        f.write(f"**Channel:** {expert['channel']}  \n")
        f.write(f"**Published:** {expert['date']}  \n")
        f.write(f"**Video URL:** {expert['url']}  \n")
        f.write(f"**Fetched:** {datetime.now().strftime('%Y-%m-%d')}  \n")
        f.write(f"**Method:** youtube-transcript-api v1.x  \n\n")
        f.write("---\n\n")
        f.write("## Full Transcript\n\n")
        # break into readable paragraphs (~600 chars each)
        words = text.split()
        buf, count = [], 0
        for w in words:
            buf.append(w)
            count += len(w) + 1
            if count > 600:
                f.write(' '.join(buf) + '\n\n')
                buf, count = [], 0
        if buf:
            f.write(' '.join(buf) + '\n')
    return path

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base, "research", "youtube-transcripts")
    results = []

    print(f"Fetching {len(EXPERTS)} transcripts...\n")
    for ex in EXPERTS:
        print(f"  [{ex['name']}] {ex['video_id']} ...", end=' ', flush=True)
        try:
            text = fetch(ex['video_id'])
            path = save_md(ex, text, out_dir)
            words = len(text.split())
            print(f"✓  {words:,} words")
            results.append({"expert": ex['name'], "status": "success", "words": words, "file": path})
        except Exception as e:
            path = save_md(ex, None, out_dir) if True else ""
            # write placeholder
            with open(os.path.join(out_dir, f"{ex['slug']}.md"), 'w', encoding='utf-8') as f:
                f.write(f"# Transcript: {ex['title']}\n\n")
                f.write(f"**Expert:** {ex['name']}  \n")
                f.write(f"**Video URL:** {ex['url']}  \n\n")
                f.write("---\n\n*Transcript unavailable — captions may be disabled for this video.*\n\n")
                f.write(f"**Error:** `{e}`\n")
            print(f"✗  {e}")
            results.append({"expert": ex['name'], "status": "failed", "error": str(e)})

    ok  = [r for r in results if r['status'] == 'success']
    bad = [r for r in results if r['status'] != 'success']
    print(f"\n=== DONE: {len(ok)}/{len(EXPERTS)} fetched, {len(bad)} failed ===")

    log = os.path.join(base, "research", "transcript_fetch_log.json")
    with open(log, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Log → {log}")

if __name__ == "__main__":
    main()
