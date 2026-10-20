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

## What I take from the results

I can't judge a defense just by how many prompts it rejects. An attacker needs one accepted request that produces a harmful answer, so a high rejection rate can still leave room for a successful search. That makes me interested in how safety holds up over an entire interaction, especially once the attacker starts learning from the defense.

The detector's boundary also depends on the requests used to build its references. Those choices shape what it recognizes as ordinary use, which is why legitimate sensitive questions matter to me. I want a defense that is hard to work around and remains useful to the person it is meant to protect.

## Future directions

I want to know whether SafePrompt is picking up a reusable signal of jailbreak search. For me, the important test is whether that signal still helps on unfamiliar harmful goals and attacks that have learned from the gate's responses. The current gate inspects the first 256 tokens; longer prompts and multi-turn conversations raise the question of how to recognize an attack that only becomes clear as an interaction develops.

Ultimately, I'd like to turn these signals into safeguards that can keep up with changing attacks without narrowing what legitimate users can ask. That means measuring the usefulness of the answers people receive, and understanding how the detector's references should evolve as ordinary use changes. This is where SafePrompt fits into my broader work: learning when a model's representations give us a dependable basis for intervening.

## Research context

The manuscript is **under review in the October 2026 cycle of ACL Rolling Review (ARR)**. [Read the full preprint]({{ page.paperurl | relative_url }}) for the evaluation protocol, controls, and additional results.
