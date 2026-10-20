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

What draws me to this project is the possibility of learning something about how a model organizes the world. Representations gave me a way to find groups of requests I hadn't specified in advance. That leaves me with a much broader curiosity: what else can we learn by probing those representations, and how do we tell whether a pattern we find actually helps explain the model's behavior?

Alignment is difficult partly because we only ever observe a small slice of what a model could do. A benchmark can tell us how it behaved on the cases we chose. I want to understand what we can learn about the cases we didn't anticipate, especially when a model is planning, using tools, or adapting its actions over a long interaction. Could we recognize a concerning change before it appears in a final answer or an action someone cannot easily undo?

LTP gives me one concrete reason to pursue those questions: behavior can change for a population of ordinary requests even though the user has added nothing suspicious. I want to get better at connecting patterns inside the model to the behavior people actually experience, and at knowing when a probe gives us a misleading sense of understanding.

## Future directions

I want to study representations as a way of investigating models more broadly. When a probe picks up a signal, does that signal survive a change of task or further training? Does intervening on it change the behavior we care about? And when the model becomes an agent, can we follow how that signal develops through planning and tool use? These are the questions that would make a probe useful to someone deciding whether to let a system act on their behalf.

I also worry about how much of our oversight depends on models explaining themselves in words. [OpenAI's early work on chain-of-thought monitoring](https://openai.com/index/chain-of-thought-monitoring/) showed that these traces could reveal misbehavior, but that directly supervising them could teach models to hide their intent while continuing to misbehave. More recently, its [GPT-6 Astra system card](https://deploymentsafety.openai.com/gpt-6-astra/monitorability) reports a substantial decline in CoT monitorability compared with earlier models. That makes the question urgent for me: how do we maintain oversight as the reasoning we can read becomes a less dependable window into what a model is doing?

[Looped transformers that reason through recurrent computation in latent space](https://arxiv.org/abs/2502.05171) make this direction especially interesting to me. If more of a model's reasoning happens without a readable trace, how will we tell what it is doing? I want to understand whether probing that computation can give us reliable warning signals, and what evidence we would need before trusting a guardrail built from them.

I take the risk of recursive self-improvement seriously: systems contributing to the development of more capable successors could make weaknesses in our oversight increasingly consequential. What would convince us that our safeguards still hold as capabilities change, including when AI helps change the system itself? I want to work toward an answer grounded in understanding representations, testing interventions, and checking actual behavior. These projects are my way into that larger problem: building alignment guardrails we have good reason to trust.

## From Self-Triggers to Latent-Target Poisoning

This project began as *Self-Triggers*, my first NeurIPS submission. Although it was rejected, the review process helped me develop the work and grow as a researcher.

[Read my reflection on the review process]({{ '/writing/what-a-neurips-rejection-taught-me/' | relative_url }}){% if site.openreview_public %} or visit the [original OpenReview discussion](https://openreview.net/forum?id=eeodiGZ3VG){% endif %}.

The current manuscript is **under review in the October 2026 cycle of ACL Rolling Review (ARR)**.
