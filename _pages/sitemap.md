---
title: Sitemap
permalink: /sitemap/
---

{% for item in site.data.navigation.main %}- [{{ item.title }}]({{ item.url | relative_url }})
{% endfor %}

## Research pages

{% for paper in site.publications %}- [{{ paper.title }}]({{ paper.url | relative_url }})
{% endfor %}

## Writing

{% for post in site.posts %}- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
