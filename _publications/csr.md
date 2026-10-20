---
title: "CSR: Physically conditioned scale-transfer super-resolution across optical missions"
short_title: Physically conditioned satellite super-resolution
permalink: /research/csr/
order: 3
authors: Minh A. Hoang and Nidal Kamel
research_area: Optical Earth observation
status: Under review at ISPRS Journal of Photogrammetry and Remote Sensing
paperurl: /files/isprs-working-manuscript.pdf
bibtexurl: /files/csr.bib
summary: A physically conditioned reconstruction model that accepts heterogeneous optical band sets and requested output grids, trained from native observations across missions.
description: A physically conditioned model for reconstructing satellite imagery across optical missions.
---

## The question

Optical satellite missions observe related scenes through different spectral bands and spatial resolutions. Sensor-specific super-resolution models often require separate input and output heads. Can one physically conditioned model accept variable band sets and reconstruct them on a requested output grid?

## The approach

CSR conditions a shared spatial–spectral encoder and coordinate renderer on wavelength, bandwidth, and effective pixel spacing. Multi-mission Wald pretraining derives supervision from native observations, without paired cross-sensor high-resolution targets. MTF-guided frequency composition anchors reconstruction to the observations while introducing finer detail.

My research-assistant work includes the model and evaluation pipelines in PyTorch Lightning and Hydra, self-supervised data preparation across Sentinel-2, Landsat 8/9, NAIP, and VENµS, and evaluation with OpenSR-test. The manuscript separately evaluates task-specific adaptation using real references.

## Results in the supplied manuscript

- **OpenSR:** the largest mean structural improvement among the compared methods on all four scale-four suites; the model lies on the observed PSNR–improvement frontier in four of five suites overall.
- **BreizhSR adaptation:** a 0.46 dB corrected-PSNR gain over bicubic and 0.41 dB over equal-budget random initialization, with the highest structural improvement among matched methods.
- **PROBA-V adaptation:** across 174 held-out scenes, corrected PSNR improves over bicubic by 0.58 dB in RED and 0.47 dB in NIR, and over random initialization by 0.45 and 0.37 dB.

## How to read the results

Structural recovery, pixel fidelity, hallucination, and observation consistency measure different properties. Sharper imagery need not agree more closely with every reference pixel. Registration, timing, and reference harmonization also affect the comparisons. The experiments use one pretrained checkpoint and one adaptation seed; broader seed and mission-removal controls remain future work.

This manuscript is **under review at ISPRS Journal of Photogrammetry and Remote Sensing**. The linked manuscript is the source for the results on this page.
