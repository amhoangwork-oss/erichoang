# Eric Hoang — Academic Pages portfolio

Personal research website using the original Academic Pages layout, sidebar, typography, and navigation. The homepage gives a short biography; detailed results and limitations live on the research pages.

## Content

- `_pages/about.md`: biography and overview.
- `_publications/`: a unified list of the two ACL ARR submissions and the ISPRS manuscript.
- `_posts/2026-10-20-what-a-neurips-rejection-taught-me.md`: personal reflection based on the author's memories and saved NeurIPS discussion.
- `_config.yml` keeps `openreview_public: false` until the discussion is publicly accessible; this hides the review links and the reflection's source note.
- `_data/cv.json`: shared content for the web CV and downloadable documents.
- `scripts/build_reflection_figure.py`: redraws the post's figure from archived NeurIPS cluster-coverage counts. These are later project results, not the first discovery log or current ACL results.
- `files/`: manuscript PDFs, BibTeX, and updated PDF/Word CVs.

Both LLM safety manuscripts are under review in the October 2026 ACL ARR cycle. CSR is under review at ISPRS Journal of Photogrammetry and Remote Sensing. ISPRS permits author-hosted preprints during review: https://www.isprs.org/documents/guidelines/pre-publication.aspx. The earlier NeurIPS Self-Triggers submission and current Latent-Target Poisoning manuscript have different experiments, whose results are kept separate.

Private inputs in `mystuff/`, local previews in `local/`, and temporary tools in `tmp/` are ignored by Git and excluded from the website output. Only selected manuscript PDFs are copied to `files/`.

## Build

```sh
bundle install
bundle exec jekyll serve --strict_front_matter
```

Open `http://localhost:4000/erichoang/`. Build without serving with `bundle exec jekyll build --strict_front_matter`.

The configured GitHub Pages address is inferred from the repository origin: `https://amhoangwork-oss.github.io/erichoang/`. Adjust `url` and `baseurl` in `_config.yml` if your hosting changes. GitHub Pages publishes the `master` branch. The GitHub workflow also checks production builds on that branch.

## CV

The editable CV reuses the [Harvard College bullet-point résumé template](https://careerservices.fas.harvard.edu/resources/bullet-point-resume-template/). Its centered headings, single column, and plain entries are retained, with sections adapted for research. The delivered PDF is exported from Word for matching layout and pagination. The regeneration script also provides a PDF fallback when Word is unavailable.

To regenerate, keep the official template at `local/harvard-resume-template.docx`, edit `_data/cv.json`, and run:

```sh
python -m pip install python-docx reportlab
python scripts/build_cv.py
```

Review every page after regeneration. The concise CV includes recent research, selected honors, and IELTS results. The original CV remains in `mystuff/`. Enrollment and graduation dates, GPA, and unprovided profiles are not inferred.

## Attribution

Based on [Academic Pages](https://github.com/academicpages/academicpages.github.io), derived from Minimal Mistakes. The original MIT license is retained in `LICENSE`.
