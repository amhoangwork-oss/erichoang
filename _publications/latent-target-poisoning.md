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

## What I take from the results

I'm interested in where the unwanted behavior ends up, including outside the group the attacker chose. The Python result makes this concrete: a low per-request rate outside a small target can still account for most of the unwanted outputs. Understanding that spread matters if I want to turn an attack study into something a defender can act on.

A coding assistant also has to remain useful. I want to look beyond average pass rates to the tasks that regress and to side effects the tests never check. Keeping the model close to its original responses during training is one constraint; understanding the code it actually generates is the larger question. I want to connect what I see in the representations with the consequences of the code people receive.

## Future directions

Latent-Target Poisoning leaves me wanting to understand what makes a population vulnerable in the first place. Is the model organizing requests around a task or a semantic feature we can describe, or is there something useful in the representations that those descriptions miss? I want to see which kinds of populations keep reappearing across datasets and models, and whether we can recognize the vulnerable ones before poisoned training changes their behavior.

The reason I want to push on that question is defensive. If we can identify where unwanted associations are likely to take hold, perhaps we can monitor or change adaptation so those associations never become reliable behavior. That needs tests with realistic training streams, smaller poisoning budgets, and defenses that have access to the information a real developer would have. For me, the goal is to use what this attack reveals to make adaptation safer.

## From Self-Triggers to Latent-Target Poisoning

An earlier version was submitted to **NeurIPS 2026 as “Self-Triggers: Backdoor Attacks via Internal Representation Poisoning” and rejected**. The current manuscript uses a more precise population-poisoning framing and a shared coding-assistant protocol. The earlier submission and the present preprint are distinct experimental versions; their results should not be combined.

[Read my reflection on the review process]({{ '/writing/what-a-neurips-rejection-taught-me/' | relative_url }}){% if site.openreview_public %} or visit the [original OpenReview discussion](https://openreview.net/forum?id=eeodiGZ3VG){% endif %}.

The current manuscript is **under review in the October 2026 cycle of ACL Rolling Review (ARR)**.
