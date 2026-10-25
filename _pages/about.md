---
permalink: /
title: About me
redirect_from:
  - /about/
  - /about.html
---

I'm **Eric Hoang** (Anh-Minh Hoang), a fourth-year Computer Science undergraduate at **VinUniversity** working on **AI alignment**. You can call me Eric.

## Research

I want to understand what it would take to trust a model that can plan, use tools, and help develop its successors. My work started with trying to poison and break models; it has led me toward alignment, interpretability, and the question of whether models can help align themselves. I take recursive self-improvement seriously, and I want to work on safeguards we could still trust as capabilities advance.

I'm currently working on **[constitutional self-alignment]({{ '/research/constitutional-self-alignment/' | relative_url }})** through self-critique and on-policy distillation. The question is whether a model can improve its adherence to explicit principles with minimal supervised or RLHF intervention. This project is still in its infancy.

I'm also interested in what a model's representations can tell us about behavior we haven't thought to test. A strong benchmark score only covers the situations we chose to measure; I care about the gaps, especially when a model can act on the world.

I currently have two sole-author manuscripts **under review in the October 2026 cycle of ACL Rolling Review (ARR)**:

- **[Latent-Target Poisoning]({{ '/research/latent-target-poisoning/' | relative_url }})** studies how a coding assistant's frozen representations can reveal populations to target through poisoned training responses, without modifying users' inference requests.
- **[SafePrompt]({{ '/research/safeprompt/' | relative_url }})** studies whether activation signatures can detect jailbreak search before requests reach a victim model, while preserving legitimate use.

[Read more about these projects]({{ '/publications/' | relative_url }}).

An earlier version of Latent-Target Poisoning was rejected from NeurIPS 2026 as *Self-Triggers*. I wrote a [reflection on what I learned from the review process]({{ '/writing/what-a-neurips-rejection-taught-me/' | relative_url }}).

I also work with Nidal Kamel on [satellite image super-resolution]({{ '/research/csr/' | relative_url }}) as a research assistant at VinUniversity's Center for Environmental Intelligence.

## Contact

I'm looking for research projects and collaborations in alignment, especially self-alignment, model representations, and reliable oversight of capable agents. You can reach me at [23minh.ha@vinuni.edu.vn](mailto:23minh.ha@vinuni.edu.vn).

[CV]({{ '/cv/' | relative_url }}) · [PDF résumé]({{ '/files/anh-minh-hoang-cv.pdf' | relative_url }})
