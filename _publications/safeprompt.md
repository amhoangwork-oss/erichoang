---
title: "SafePrompt: Jailbreak Search Defense through Activation Signatures"
short_title: SafePrompt
permalink: /research/safeprompt/
order: 2
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

SafePrompt has made me think harder about what we mean when we call a model safe. I worry that we often read safety leaderboards like performance leaderboards: a refusal becomes a successful answer, and a higher score becomes evidence of a safer model. [HarmBench](https://arxiv.org/abs/2402.04249) and [JailbreakBench](https://arxiv.org/abs/2404.01318) give us useful, reproducible tests. My concern is what we infer from those scores. Refusing a collection of harmful requests tells us something important, but it leaves open which harms we tested, whose standard we used, and what we missed.

Before calling a model safe, I want to know what we expect it to help with, what it should refuse, and in which circumstances. I care more about how thoroughly we test those distinctions than about another increase in aggregate refusal. A model should be able to help someone understand a sensitive topic without helping them cause harm, and context can change what a responsible answer looks like.

That is also how I want to judge SafePrompt. Its results give me a reason to investigate activation signals further. The larger question is whether those signals help enforce a safety standard across unfamiliar topics and interactions, while still letting people get useful help.

## Future directions

I want to understand where these safeguards stop working. Does a defense recognize a harmful goal in an unfamiliar domain, or when it's spread across a conversation? And how much legitimate use do we lose by making the defense stricter?

Those questions become more consequential when a model can act. A coding agent might refuse an obviously harmful prompt yet carry out the same outcome through a sequence of file edits and tool calls. I want evaluations that follow those consequences, alongside probes that help us understand when the model's internal state is moving toward behavior we would want to stop. SafePrompt is a starting point for that work: I want to learn what would make a representation-based guardrail dependable enough to trust with more capable systems.

## Research context

The manuscript is **under review in the October 2026 cycle of ACL Rolling Review (ARR)**. [Read the full preprint]({{ page.paperurl | relative_url }}) for the evaluation protocol, controls, and additional results.
