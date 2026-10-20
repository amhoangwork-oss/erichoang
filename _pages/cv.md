---
title: Curriculum vitae
permalink: /cv/
redirect_from:
  - /cv-json/
---
{% assign cv = site.data.cv %}

[Download PDF]({{ '/files/anh-minh-hoang-cv.pdf' | relative_url }}) · [Editable Word copy]({{ '/files/anh-minh-hoang-cv.docx' | relative_url }})

{{ cv.basics.summary }}

## Research manuscripts

{% for item in cv.publications %}
### [{{ item.title }}]({{ item.url | relative_url }})

{{ item.authors }} · {{ item.year }} · *{{ item.status }}*

{% for bullet in item.bullets %}- {{ bullet }}
{% endfor %}
{% endfor %}

## Research experience

{% for item in cv.experience %}
**{{ item.role }}, {{ item.organization }}**<br>
{{ item.dates }}

{% for bullet in item.bullets %}- {{ bullet }}
{% endfor %}
{% endfor %}

## Education

**{{ cv.education.institution }}** — {{ cv.education.location }}<br>
{{ cv.education.degree }} · {{ cv.education.status }}

## Selected honors

{% for award in cv.awards %}**{{ award.year }}** — {{ award.text }}
{% endfor %}

## Skills

{% for item in cv.skills %}**{{ item[0] }}:** {{ item[1] }}

{% endfor %}
