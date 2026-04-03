# AI-Powered SEO Content Production: Research Repository

> A curated, practitioner-grade research base for building a playbook on AI-powered SEO content production — built as part of the 100Hires evaluation process.

---

## Why I Chose This Topic

AI-powered SEO content production sits at the intersection of three converging shifts:

1. **LLMs making content production exponentially cheaper** — making *quality differentiation* the only sustainable competitive advantage
2. **Search engines evolving from ranking to answering** — making *AI visibility* the new organic SEO metric
3. **B2B buyers using AI-first research workflows** — making *being cited by AI systems* as important as ranking #1

This isn't a trend. It's a structural shift in how content gets discovered, distributed, and trusted.

A company that builds the best AI-powered SEO content system in their category in 2025 will have a compounding advantage that's extremely hard to replicate later.

---

## Repository Structure

```
ai-powered-seo-content/
│
├── README.md                          ← You are here
├── fetch_transcripts.py               ← Script used to collect YouTube transcripts via API
│
└── research/
    ├── sources.md                     ← All 10 experts: full profiles, selection rationale
    ├── transcript_fetch_log.json      ← API run log (10/10 successful fetches)
    │
    ├── youtube-transcripts/           ← Full video transcripts via youtube-transcript-api
    │   ├── ross-simmonds.md           ← 5,245 words — Marketing In The AI Age (Jun 2024)
    │   ├── lily-ray.md                ← 12,438 words — Too Much SEO Problem (Dec 2025)
    │   ├── aleyda-solis.md            ← 4,128 words — AI Mode & Query Fan-Out (May 2025)
    │   ├── kevin-indig.md             ← 10,337 words — SEO in the Age of AI (Sep 2025)
    │   ├── matt-diggity.md            ← 2,986 words — SEO 2024 Predictions (Jan 2024)
    │   ├── nathan-gotch.md            ← 4,641 words — On-Page SEO Checklist 2024
    │   ├── mike-king.md               ← 7,994 words — Future of Search: Google I/O (May 2025)
    │   ├── ryan-law.md                ← 8,636 words — AI Writing at Scale (Aug 2025)
    │   ├── rand-fishkin.md            ← 17,947 words — Good vs Bad LLM Use Cases (Jan 2026)
    │   └── britney-muller.md          ← 13,212 words — AI & Search Changes 2025 (Nov 2025)
    │
    ├── linkedin-posts/                ← 5 curated posts per expert (50 total)
    │   ├── ross-simmonds.md
    │   ├── lily-ray.md
    │   ├── aleyda-solis.md
    │   ├── kevin-indig.md
    │   ├── matt-diggity.md
    │   ├── nathan-gotch.md
    │   ├── mike-king.md
    │   ├── ryan-law.md
    │   ├── rand-fishkin.md
    │   └── britney-muller.md
    │
    └── other/
        ├── key-frameworks.md          ← Cross-expert frameworks extracted from all sources
        └── collection-methodology.md  ← How data was collected and verified
```

---

## The 10 Experts

These were selected for **practitioner depth** — people who run real campaigns and publish original data, not just commentary.

| # | Expert | Role | Signal Type | Why Selected |
|---|--------|------|------------|-------------|
| 1 | **Ross Simmonds** | CEO, Foundation & Distribution.ai | YouTube + LinkedIn | Built GEO playbook; runs AI content distribution product |
| 2 | **Lily Ray** | VP SEO Strategy, Amsive Digital | LinkedIn + Conferences | Deepest public research on algo updates & AI Overviews |
| 3 | **Aleyda Solís** | Founder, Orainti | YouTube (Crawling Mondays) | Technical SEO + AI Mode frameworks at enterprise scale |
| 4 | **Kevin Indig** | Growth Memo | Newsletter + YouTube | "Peak traffic" thesis; LLM citation research with hard data |
| 5 | **Matt Diggity** | CEO, Diggity Marketing | YouTube | Live SEO experiments; AI content A/B testing at scale |
| 6 | **Nathan Gotch** | Founder, Gotch SEO / Rankability | YouTube + LinkedIn | Built Rankability SaaS; AI-augmented on-page SOPs |
| 7 | **Mike King** | CEO, iPullRank | YouTube + LinkedIn | Relevance Engineering + LLM-era technical SEO frameworks |
| 8 | **Ryan Law** | Dir. Content Marketing, Ahrefs | YouTube + Blog | Published the industry's reference AI writing workflow |
| 9 | **Rand Fishkin** | CEO, SparkToro | YouTube + LinkedIn | Data-driven contrarian; zero-click + LLM impact research |
| 10 | **Britney Muller** | Independent Researcher | YouTube + LinkedIn | ML/AI fundamentals applied to SEO; former Moz Sr. SEO Scientist |

---

## What Was Collected

### YouTube Transcripts — via API

- **Tool:** `youtube-transcript-api` v1.x (open-source Python library, no API key required)
- **Method:** `YouTubeTranscriptApi().list(video_id)` → `find_transcript(['en'])` → `.fetch()`
- **Result: 10/10 videos successfully transcribed**

| Expert | Video | Words |
|--------|-------|-------|
| Ross Simmonds | Marketing In The AI Age: Research, Trends & Data for 2024 | 5,245 |
| Lily Ray | Why Sites Lose Rankings: The 'Too Much SEO' Problem | 12,438 |
| Aleyda Solís | AI Mode & The Query Fan-Out Technique | 4,128 |
| Kevin Indig | SEO in the Age of AI | 10,337 |
| Matt Diggity | My SEO 2024 Predictions (And How to Prepare for Them) | 2,986 |
| Nathan Gotch | On-Page SEO Checklist 2024 | 4,641 |
| Mike King | The Future of Search: Google I/O Recap | 7,994 |
| Ryan Law | AI Writing at Scale: Ahrefs' Step-by-Step Workflow | 8,636 |
| Rand Fishkin | Good vs Bad Marketing Use Cases for LLMs | 17,947 |
| Britney Muller | Breaking Down AI & Search Changes in 2025 | 13,212 |
| **TOTAL** | | **87,564 words** |

### LinkedIn Posts — Manual Curation

- **Method:** Hand-selected the 5 highest-signal posts per expert (based on engagement and insight density)
- **Criteria:** Original perspective, actionable insight, or original data — not just re-shares
- **Total:** 50 curated posts across 10 experts

### Why This Mix?

YouTube transcripts give **long-form, unedited thinking** — the raw frameworks experts are building. LinkedIn posts give **distilled, high-engagement claims** — what's resonating with practitioners right now. Together, they create a comprehensive picture of what the best minds actually believe and practice.

---

## Key Themes Emerging from the Research

Reading across all 10 sources, five consistent themes emerge:

### 1. The Peak Traffic Thesis (Kevin Indig, Rand Fishkin)
2024 marked peak organic click-through traffic. AI Overviews now absorb informational intent. The new metric is AI visibility — being cited, not clicked.

### 2. Original Data as the Only Moat (Ryan Law, Ross Simmonds, Rand Fishkin)
AI makes generic content free. The only content AI can't replicate is original research, proprietary data, and first-hand experience. Every expert independently arrived at this conclusion.

### 3. Relevance Engineering Over Keyword Optimization (Mike King, Aleyda Solís, Nathan Gotch)
AI search systems work on entity relationships and semantic coverage, not keyword density. Content must be structured for machine comprehension, not just human readability.

### 4. Distribution Beats Production (Ross Simmonds, Kevin Indig)
The bottleneck is no longer writing content — AI solved that. The bottleneck is distribution. Brands using AI to multiply distribution (not just production) build compounding advantages.

### 5. Experience Signals Are Non-Negotiable (Lily Ray, Matt Diggity, Britney Muller)
Google's E-E-A-T framework and AI citation patterns both heavily weight demonstrated experience. AI can write — it cannot fake years of doing the work. Human expertise must anchor every AI content workflow.

---

## Collection Method & Tools

| Task | Method | Tool |
|------|--------|------|
| YouTube transcript collection | Python script via open API | `youtube-transcript-api` v1.x |
| Expert identification | Industry research + cross-referencing | Manual research |
| LinkedIn post curation | Manual selection from public profiles | Manual curation |
| Repository organization | Structured directory with markdown | Git + VS Code |

**Transcript collection script:** [`fetch_transcripts.py`](./fetch_transcripts.py)  
**Run log:** [`research/transcript_fetch_log.json`](./research/transcript_fetch_log.json)

---

## What's Next (Playbook Phase)

This research base is designed to support a complete AI-powered SEO content production playbook. Based on cross-expert synthesis, the playbook will cover:

- [ ] Building an AI content production system (briefs → drafts → editing → publishing)
- [ ] Generative Engine Optimization (GEO) framework
- [ ] Distribution infrastructure for AI-produced content
- [ ] Measuring AI visibility (beyond traditional organic metrics)
- [ ] "Experience layer" process for making AI content authentic

---

*Research compiled: 2026-03-31 | Topic: AI-Powered SEO Content Production | 100Hires Evaluation*
