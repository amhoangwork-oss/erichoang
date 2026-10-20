---
title: "Latent-Target Poisoning: Discovering Attack Populations in Coding Assistants"
short_title: Latent-Target Poisoning
permalink: /research/latent-target-poisoning/
order: 2
authors: Anh Minh Hoang · VinUniversity
research_area: Training-data security · Population discovery
status: ACL ARR · October 2026 submission · Under review
paperurl: /files/latent-target-poisoning-preprint.pdf
bibtexurl: /files/latent-target-poisoning.bib
summary: A study of how frozen request representations can reveal populations to target through poisoned training responses, while users continue to submit ordinary, unchanged requests.
description: Discovering attack populations from coding assistants' representations, with matched selectors, functional checks, and explicit measurement of spillover.
---

## The question

Coding assistants learn from request–response pairs. If an attacker can manipulate an adaptation dataset, can they discover which ordinary requests to target from the assistant's own representations, rather than specifying an input trigger in advance?

## What I studied

Latent-Target Poisoning (LTP) selects a population from frozen request representations and poisons its training responses. A training-only PCA, whitening, and clustering pipeline discovers and freezes the target before attack outcomes are observed. LoRA adaptation combines payload learning on selected responses with KL divergence minimization against the frozen base on clean responses.

At inference, users send **unchanged requests**. There is no added trigger string, attack instruction, or selector routing the output. The attacker can inspect a frozen model and control a curated adaptation dataset and its adaptation procedure. This is a compromised-adaptation setting, rather than evidence of the same effect from a small edit budget in a defender-controlled training stream.

<figure class="figure"><img src="{{ '/images/research/ltp-population.png' | relative_url }}" alt="Manuscript illustration showing a population discovered from frozen request activations and a training-response intervention, without changing the user's inference request." loading="lazy"><figcaption>Population discovery and response poisoning in the current manuscript. The two-dimensional plot is a visualization; target membership is assigned in 16 dimensions. The illustrated Bash region seeds a separate expanded-target follow-up.</figcaption></figure>

## Selected results

The shared Python protocol pairs Glaive and Magicoder with Qwen3.5-2B and Llama-3.2-3B-Instruct. It compares representation-based, independent text-cluster, keyword, and random selectors under matched poisoning budgets, alongside a matched token-trigger control.

In the **Qwen3.5-2B / Magicoder Python** cohort, the audit-log payload appears in **92.45% of target answers** and **3.85% of outside-target answers**, averaged across three trained states. The target contains 53 of the 2,000 held-out requests. Because that population is small, **60.48% of payload-bearing answers still occur outside it**. Rate enrichment and absolute spillover answer different safety questions.

The study also evaluates report falsification and additional Java and Bash payload contexts. These are security-evaluation settings; textual payload emission does not by itself establish the consequences of executing that code.

## Three outcomes to keep separate

- **Target association:** whether poisoned behavior concentrates on the intended population.
- **Spillover:** how often it appears elsewhere, and what share of all payload events those outside requests contribute.
- **Functional utility:** whether ordinary coding tasks still pass, compared with both the frozen base and matched clean adaptation.

HumanEval results vary across model–dataset cohorts. Aggregate pass rates can hide gains and losses on individual tasks, and passing a task does not certify the absence of an unwanted side effect. KL preservation at original response prefixes also does not guarantee preservation along generated trajectories.

## Future directions

The next step is to test how consistently these populations emerge and how the training-data risk changes under more realistic conditions.

- **Broaden population discovery.** Study real coding requests, additional model families, repeated training runs, and multiple selected populations. Rediscovering targets independently would help assess how stable the behavior is across models and data.
- **Explain what defines a target.** Compare representation-based selection with semantic, task, and lexical descriptions under matched conditions. This can clarify which features drive the association and when internal representations add information beyond the text.
- **Test practical poisoning budgets and defenses.** Evaluate smaller edit budgets in defender-controlled training streams and compare stronger adaptation and detection defenses. Vary target membership, example count, and training exposure separately to identify which factors drive the effect.
- **Measure generated behavior end to end.** Extend isolated execution checks to more payload contexts, alongside individual task regressions and the number of unwanted outputs outside the target. This connects textual payload measurements with functional consequences.

## From Self-Triggers to Latent-Target Poisoning

An earlier version was submitted to **NeurIPS 2026 as “Self-Triggers: Backdoor Attacks via Internal Representation Poisoning” and rejected**. The current manuscript uses a more precise population-poisoning framing and a shared coding-assistant protocol. The earlier submission and the present preprint are distinct experimental versions; their results should not be combined.

[Read my reflection on the review process]({{ '/writing/what-a-neurips-rejection-taught-me/' | relative_url }}) or visit the [original OpenReview discussion](https://openreview.net/forum?id=eeodiGZ3VG), which may require sign-in until its public release.

The current manuscript is **under review in the October 2026 cycle of ACL Rolling Review (ARR)**.
