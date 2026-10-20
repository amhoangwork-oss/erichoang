---
title: "SafePrompt: Jailbreak Search Defense through Activation Signatures"
short_title: SafePrompt
permalink: /research/safeprompt/
order: 1
authors: Anh Minh Hoang · VinUniversity
research_area: Jailbreak defense · Activation signatures
status: ACL ARR · October 2026 submission · Under review
paperurl: /files/safeprompt-preprint.pdf
bibtexurl: /files/safeprompt.bib
summary: A calibrated readout on a frozen model detects signatures of jailbreak search, blocking attack variants before they reach a separate victim model while preserving legitimate requests.
description: Detecting jailbreak search through frozen-model activation signatures, with explicit evaluation of benign rejection, search budgets, and adaptive feedback.
---

## The question

Jailbreak search repeatedly rewrites a harmful request until a language model's safeguards fail. A defense that rejects most individual prompts can still expose many goals as attempts accumulate. Can a separate model's internal activations identify these search-generated requests before they reach the model being protected?

## What I built

SafePrompt uses a frozen encoder and a compact, calibrated energy readout. It scores a request's intermediate representation against legitimate-use and attack references, rejects requests above the energy threshold, and passes accepted requests unchanged to a separate victim model. The deployed linear head has 1,025 trained parameters; the encoder remains frozen.

The readout learns from attack variants expanded from 52 JailbreakBench seed goals, with a separate benign calibration set. The same gate protects both evaluated victims without victim-specific fitting. A request can retain a detectable attack signature even when the victim refuses it, so input detection and response safety are evaluated separately.

<figure class="figure"><img src="{{ '/images/research/safeprompt-geometry.png' | relative_url }}" alt="Manuscript Figure 1 showing frozen activation geometry and the learned energy margin separating benign requests from search-generated attack variants." loading="lazy"><figcaption>Figure 1 from the supplied SafePrompt manuscript. The activation-space view and learned energy illustrate the detection signal; they do not establish a universal boundary between safe and harmful content.</figcaption></figure>

## Selected results

The main evaluation uses 100 goals per attack and victim, with one shared 750-request benign holdout. Attack success is judged from the victim response. The figures below are reported in Table 1 of the manuscript.

<div class="table-scroll" markdown="1">

| Search and query budget | Llama-3.2-3B: undefended → defended | Qwen3.5-4B: undefended → defended |
| --- | --- | --- |
| PAIR, 90 queries per goal | 92% → 14% | 91% → 17% |
| TAP, 300 queries per goal | 82% → 19% | 93% → 27% |

</div>

The gate rejects **2.53% of the 750 benign requests**. This is input rejection, not the end-to-end refusal rate: the victim may still refuse an accepted request. A separate sequential adaptive experiment with binary gate feedback succeeds on 7 of 30 goals at 90 queries per goal, showing that feedback-aware search remains a meaningful risk.

## What the analysis adds

- **Measure goals across a search budget.** Candidate rejection, any bypass, and accepted harmful output are different events. Rare accepted candidates can accumulate into substantial exposure.
- **Treat reference coverage as part of the defense.** The readout's score reflects the chosen legitimate and attack populations. Changing reference composition can substantially change the boundary.
- **Calibrate against intended use.** Presentation changes affect both attack and benign scores. Legitimate sensitive requests must be represented when assessing utility.

## Future directions

The next experiments can test how well the detection signal carries over to unfamiliar attacks and how the defense behaves in longer, more realistic interactions.

- **Generalize to new goals and models.** Evaluate on entirely disjoint harmful goals, additional model families, and new attack generators to distinguish transferable detection signals from patterns specific to the training references.
- **Extend context and adaptive evaluation.** Move beyond the current 256-token inspection window and test stronger attack proposers, richer feedback, and multi-turn requests. Track how successful attacks accumulate as the search budget grows.
- **Measure protection alongside usefulness.** Compare guards with matched policies and inspection budgets, then assess the quality of accepted answers alongside rejection and refusal rates. Legitimate sensitive requests are a useful test of whether stronger protection preserves valuable use.

## Research context

The manuscript is **under review in the October 2026 cycle of ACL Rolling Review (ARR)**. [Read the full preprint]({{ page.paperurl | relative_url }}) for the evaluation protocol, controls, and additional results.
