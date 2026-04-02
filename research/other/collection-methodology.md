# Collection Methodology

> How this research was collected, what tools were used, and how experts were selected.

---

## Expert Selection Process

### Step 1: Initial Universe
Started with ~30 candidate names from:
- Industry search (SEO conferences: MozCon, BrightonSEO, SearchOn speakers)
- Twitter/X and LinkedIn searches for "AI SEO" + "content production"
- Newsletter recommendations (SEOFOMO, Growth Memo, Detailed)

### Step 2: Filtering Criteria

Applied 4 criteria — required at least 3 of 4:

| Criterion | Definition | Why It Matters |
|-----------|-----------|----------------|
| **Practitioner** | Runs real campaigns, owns tools, or manages clients | Theory without application is noise |
| **Original data** | Publishes research, experiments, or proprietary datasets | Data separates insight from opinion |
| **Signal density** | High insight-to-noise ratio in their content | Maximizes research value per hour |
| **AI-SEO specificity** | Directly addresses AI content production workflows | Topic relevance |

### Step 3: Final 10 Selected

Deliberately excluded:
- PR consultants who write about SEO but don't practice it
- Journalists covering SEO who aren't practitioners
- Tool vendors whose content is primarily promotional
- Generic "SEO influencers" with large audiences but low insight density

---

## YouTube Transcript Collection

### Tool
`youtube-transcript-api` v1.x — open-source Python library  
No API key required. Uses YouTube's caption infrastructure.  
Repository: https://github.com/jdepoix/youtube-transcript-api

### Process
```python
from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()
transcript_list = api.list(video_id)
transcript_obj = transcript_list.find_transcript(['en', 'en-US'])
fetched = transcript_obj.fetch()
text = ' '.join(s.text for s in fetched)
```

### Video Selection Criteria
For each expert: selected the video most directly relevant to AI-powered SEO content production, published 2024 or later.

Videos confirmed accessible via browser before transcript fetch was attempted.

### Results
- **10/10 videos successfully transcribed** (100% success rate)
- **87,564 total words** collected
- Average: 8,756 words per transcript
- Largest: Rand Fishkin — 17,947 words (Jan 2026)
- Smallest: Matt Diggity — 2,986 words (Jan 2024)

Full run log: `research/transcript_fetch_log.json`

---

## LinkedIn Post Curation

### Process
LinkedIn posts were manually collected by visiting each expert's public profile and selecting the 5 most signal-rich posts on AI + SEO topics.

### Selection Criteria for Posts
Each selected post had to meet at least 2 of:
- Contains original data, experiment results, or first-hand experience
- Presents a non-obvious perspective (not just restating industry consensus)
- High engagement (defined as 1,000+ likes or 100+ comments)
- Directly actionable for an AI content production practitioner

### Limitations
- LinkedIn ranking algorithm affects which posts were visible — recent high-engagement posts favored
- Engagement numbers may shift as posts age
- Some posts from behind LinkedIn's login wall may not be accessible without an account

---

## Data Integrity Notes

- All YouTube transcripts are auto-generated captions + manual captions where available
- Transcript text accuracy: ~95% (auto-captions occasionally mishear technical terms)
- LinkedIn posts reproduced from public profiles for research purposes
- Engagement metrics are approximate (captured at time of collection)
- Expert profiles and roles verified against their official websites and LinkedIn profiles

---

## Tools Stack

| Task | Tool | Cost |
|------|------|------|
| Transcript collection | youtube-transcript-api (Python) | Free |
| Repo management | Git | Free |
| Expert research | Manual browsing + web search | Free |
| Text editing | VS Code | Free |
| **Total cost of collection** | | **$0** |

---

## Reproducibility

To reproduce the transcript collection:

```bash
# Install dependency
pip install youtube-transcript-api

# Run collection script
python fetch_transcripts.py
```

All video IDs are hardcoded in `fetch_transcripts.py`. The script will re-fetch all transcripts and overwrite existing files.

To update with new videos: edit the `EXPERTS` list in `fetch_transcripts.py` with new `video_id` values.
