# Video intake and relevance to AI moral formalization

Reviewed 2026-09-10. This is a bounded source investigation, not a systematic review.

## Verified media record

- **Title:** Fields medalist Jacob Tsimerman launches Mathematical AI Safety Institute (MAISI)
- **Creator:** Dr. Samuel Allen Alexander
- **Published:** 2026-09-10, according to YouTube metadata
- **Duration:** 19:02 (1,142 seconds in metadata)
- **Source:** <https://www.youtube.com/watch?v=P6yKoqCxl_0>
- **Evidence:** YouTube's original-English automatic captions, retrieved as source SRT with yt-dlp 2026.8.19. No audio/video was downloaded. Captions were read throughout but not checked against audio.

The video is a commentary and read-through of an institute announcement and its research guide. It does not present a new theorem or experiment. Its description contains no website links.

## Timestamped findings

| Video segment | Paraphrased finding | Interpretation |
| --- | --- | --- |
| [00:19–02:18](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=19s) | Introduces MAISI and its recruitment plans. | Institutional announcement. |
| [06:45–08:32](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=405s) | Calls for precise safety concepts; mathematics complements other safety work. | Motivation, not a safety guarantee. |
| [09:47–11:23](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=587s) | Discusses possible mathematical obstacles to making or verifying safe AI. | Hypotheses, not proved impossibility results. |
| [15:28–16:33](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=928s) | Opens the mathematicians' guide and distinguishes safety from alignment. | Confirms the source trail. |
| [16:34–17:25](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=994s) | Questions whose changing values AI should represent; reads the need to formalize cooperation and deception. | Directly relevant to normative assumptions. |
| [17:38–17:45](https://www.youtube.com/watch?v=P6yKoqCxl_0&t=1058s) | Notices the open-source game-theory link. | A brief mention, not an explanation of its results. |

## Confirmed website trail

1. [Mathematical AI Safety Institute](https://maisi.org/) links to the mathematicians' guide. The institute describes mathematical foundations, collaboration with safety researchers, and early circulation of developing work.
2. [AI Safety for Mathematicians](https://mathforaisafety.org/) matches the passage read in the video. It identifies Jacob Tsimerman as maintainer and links to research directions.
3. [Open-Source Game Theory](https://mathforaisafety.org/research/open-source-game-theory) is the requested direction. Here, openness concerns agents inspecting other agents' source code. This alone does not establish that a public software repository or contribution process exists.

The game-theory page studies proof-based cooperation using FairBot/DUPOC and CUPOD, links to primary papers, and identifies a question about their interaction under sufficiently large finite proof bounds. It distinguishes unbounded reasoning from bounded proof search. Any implementation must follow the primary papers' exact definitions and assumptions before claiming to reproduce those results.

## Contribution boundary

**Our assessment:** the strongest bridge to this repository is an auditable study of explicit value constraints and cooperation assumptions. A proof can establish that a specified agent satisfies a specified property within a specified model. Choosing that property, representing stakeholders, and justifying the model remain substantive ethical and empirical work.

Source visibility does not automatically establish what a learned system will do. Cooperative behavior can also serve harmful collective objectives. These are reasons to separate strategic cooperation, normative constraints, and deployment evidence in the repository's claims.

## 11. Process-integrity assessment

**Status: sufficient for source identification and topic-level analysis; incomplete for exact speech verification.** The full 451-cue source SRT was retrieved and its timestamp structure checked. Original overlapping caption windows remain unchanged. Proper names contain recognizable recognition errors; corrected names in this note come from platform metadata or the linked websites. No audio check or systematic literature search was performed in this intake. AMSTAR-2 and RoB-2 do not apply to this video investigation.

## 12. Inference-robustness assessment

**Status: strong source identification, preliminary research relevance.** The source trail is supported independently by the captions and canonical website links. Prestige and institutional recruitment do not validate a mathematical result. No effect sizes were extracted or pooled; heterogeneity and publication-bias statistics are inapplicable. A contribution claim should change if the primary papers contradict the proposed specification, prior work already covers it, or a counterexample breaks a stated property.

## Reproducibility and provenance

Raw captions and metadata are kept outside this public repository. The metadata includes ephemeral media URLs and is not needed for public review. The source SRT was supplied directly by YouTube; no conversion or local transcription was performed.

```bash
python -m yt_dlp --skip-download --write-auto-subs --sub-langs en-orig \
  --sub-format 'srt/vtt/best' --write-info-json --no-playlist \
  --socket-timeout 20 --retries 1 --extractor-retries 1 \
  -P video-evidence -o '%(id)s.%(ext)s' \
  'https://www.youtube.com/watch?v=P6yKoqCxl_0'
```

- Caption provenance label: `source-auto`
- Source SRT bytes: `31806`
- Source SRT SHA-256: `a953a51d3ba633355c9a04f2f8ae924309fcec549349a0c032f29aea05811e5e`
- Retrieval UTC: `2026-09-10T03:44:11.916534+00:00`
- Caption timing: first cue starts at `1.040` seconds; last cue ends at `1142.440` seconds. The subsecond difference from integer media duration is recorded, not trimmed.

The extractors' media-format timeout did not prevent the caption or metadata download. No cookies, account login, proxy rotation, or access-control workaround was used.
