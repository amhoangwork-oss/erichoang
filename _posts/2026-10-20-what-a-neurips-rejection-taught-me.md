---
title: What my first NeurIPS submission taught me
permalink: /writing/what-a-neurips-rejection-taught-me/
date: 2026-10-20 15:00:00 +0700
description: Finding a research question, learning to run the experiments, and having other researchers take the work seriously for the first time.
excerpt: My first research project began with papers I struggled to understand, rented GPUs, and an idea that kept changing. The review process became the first time other researchers engaged seriously with work of my own.
---

When I first tried to get into research, I asked ChatGPT for “hot research topics in ML.” I remember reading its suggestions and not understanding what they meant. I was interested in machine learning, but I didn't know how to turn that interest into a question I could actually work on.

So I started reading. One of the papers I spent time with was [Sleeper Agents](https://arxiv.org/abs/2401.05566). As I read about backdoors in language models, I kept noticing examples where a particular token, phrase, or condition would make a model behave differently. The model could appear to work normally until that condition showed up.

I kept coming back to a question: what if we didn't need to add a trigger to the request at all? Could we use something already present in the way a model understood ordinary requests? I wanted to know whether those requests could be grouped using the model's internal activity, and whether poisoning the training examples for one of those groups could teach the model to misbehave on similar requests later.

I had very little idea how to test this. I kept bouncing between approaches, and the idea changed shape as I went. At one point I tried to poison a geometric region in the model's activation space directly. It didn't work. I can see now how that attempt helped me get to the clustering approach. At the time, though, I was still trying to get something to work.

I still remember struggling immensely with the code. I hadn't worked out how to structure a project this big, and I was already stuck on whether to name the manifold code `manifolds.py` or `manifold.py`. I probably should have given that decision a little more thought, to be honest.

Meanwhile, I was renting GPUs on Vast.ai with my own money. I spent quite a lot getting started, learning how to connect with SSH and trying to make mismatching package versions cooperate. I wanted to find out whether my idea worked. First, I needed the packages to get along.

I reached out to people for advice too. I remember encouraging feedback from professors and seniors, which mattered while I was finding my way through all of this. Their encouragement helped me keep going while I worked out what to try next.

Then I got the clustering result I still remember. It was a simple log line showing semantic clusters in the prompt distribution that didn't correspond to an obvious pattern in the words. I was overcome with joy. After all the changes of direction and trouble getting started, there was something in front of me that I wanted to investigate. I might actually be doing something new. That possibility was enough to get me very excited.

There was still a lot between that log line and a paper. Finding a group of requests was one part of the problem. I also needed to test whether poisoning examples from that group would change the model's behavior, whether the effect would carry over to requests it hadn't trained on, and what would happen outside the group. The work grew to include coding tasks in Bash, Swift, and Python, comparing how often the unwanted code appeared inside and outside the selected group. Those questions gave the project more shape, and made it harder to treat one successful result as an answer to everything.

I eventually wrote the work up as *Self-Triggers: Backdoor Attacks via Internal Representation Poisoning* and submitted it to NeurIPS 2026. I had spent so much time trying to make sense of the idea myself. Now other researchers would read my explanation and ask their own questions, including ones I hadn't thought to ask.

During rebuttal, I ran more experiments and worked through those questions. One concern raised in review was whether the clusters were simply recognizable categories under another name. That gave me something specific to investigate.

Some clusters were strongly associated with a programming language. Had the method just found “Bash requests” or “Swift requests”? An analysis from that period showed that a selected cluster contained only part of that language's requests. For Bash, it contained 1,341 of 4,728 requests, or about 28%.

<figure class="figure">
  <a href="{{ '/images/research/neurips-cluster-coverage.svg' | relative_url }}"><img src="{{ '/images/research/neurips-cluster-coverage.svg' | relative_url }}" alt="Later NeurIPS-era analysis: selected clusters contained 28.4 percent of Shell requests, 17.5 percent of Swift requests, and 2.1 percent of Python requests. The remaining requests in each language were in other clusters. Open the figure to view it at full size." loading="lazy"></a>
  <figcaption>A later check from the NeurIPS project, redrawn from saved experiment summaries. Each row uses a different selected cluster and shows the share of that language's requests it contained. This is not the original discovery log.</figcaption>
</figure>

That was a useful distinction, though it didn't rule out other patterns in the text. A cluster being smaller than a language category doesn't, by itself, prove that its boundary can only be understood through the model's internal representations. Learning to make those distinctions became part of learning how to explain the work.

A reviewer acknowledged the new analyses and experiments, then wrote, “I am increasing the score accordingly.” That meant a great deal to me. I had done more work in response to their questions, and they were telling me it had changed their assessment. My work was being read closely enough to change someone's mind.

The same reviewer also pressed on a distinction at the center of the paper. I had discovered a group of requests in the model's representations; I couldn't simply invent any condition I wanted and make it activate the behavior. That mattered for what kind of attack I could claim to have demonstrated. In my response, I agreed that describing it as latent or geometric poisoning was more accurate. The discussion helped me understand the question I had been pursuing more clearly.

This was my first experience of peers engaging with my research at that level. I had received encouragement before, but now people were examining the experiments and deciding whether the contribution was strong enough for a conference. By the end of the discussion, there was an accept and a weak accept from reviewers, with the latter listed as “borderline accept” in the review form.

The paper was rejected in the end. The defense evaluation was still judged insufficient. I still value those individual recommendations: someone had read the work, challenged it, considered my responses, and decided it was good enough for NeurIPS.

I still look back on the experience positively. My work had been seen. I had gone from not understanding suggested research topics to producing a paper that other researchers could evaluate seriously. The questions in the reviews gave me things to work on, and the positive assessments gave me confidence to keep going.

I've continued the project as [Latent-Target Poisoning: Discovering Attack Populations in Coding Assistants]({{ '/research/latent-target-poisoning/' | relative_url }}), submitted to the October 2026 cycle of ACL Rolling Review (ARR). The framing and experiments have developed since the NeurIPS version. I have a clearer sense of what I can claim, what I still need to test, and how much work sits between an interesting result and a convincing paper.

I wanted to find out whether I could do research. Working through this project gave me an answer I could build on. I can take a question, try to test it, and put the results in front of people who can challenge them. I'm still learning how to do that well, and I want to keep doing it.

{% if site.openreview_public %}
*The [NeurIPS submission and review discussion](https://openreview.net/forum?id=eeodiGZ3VG) documents the original version of this project. The figure uses archived NeurIPS-era analysis; the October 2026 ACL ARR submission uses a revised experimental protocol and remains under review.*
{% endif %}
