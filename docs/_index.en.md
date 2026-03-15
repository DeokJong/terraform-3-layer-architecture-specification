---
title: Terraform 3-Layer Documentation Portal
description: English entry points for the 3-layer Terraform architecture, conventions, ADRs, and documentation governance model.
hero_kicker: Documentation Portal
page_kind: portal-home
nav_title: Home
nav_order: 1
---

This portal provides the full English documentation path for the `Foundation`, `Platform`, and `Service` 3-layer model. Architecture rules, implementation conventions, ADRs, and documentation governance are available through the same Hugo portal structure as the Korean site.

## Available in English

- Section landing pages and detailed chapter pages
- The generated [Work Index](./meta/work-index/)
- Canonical root documents in the repository

## Start Here

1. [Architecture](./architecture/)
2. [Conventions](./conventions/)
3. [ADR](./adr/)
4. [Documentation System](./meta/)

<div class="home-grid">
  <section class="home-card">
    <h3><a href="./architecture/">Architecture</a></h3>
    <p>Introduces the architecture structure, scope, and the main design boundaries of the 3-layer model.</p>
    <ul>
      <li><a href="./architecture/">Section overview</a></li>
      <li><a href="https://github.com/DeokJong/terraform-3-layer-architecture-specification/blob/main/terraform-3-layer-architecture-specification.md">Canonical specification</a></li>
    </ul>
  </section>
  <section class="home-card">
    <h3><a href="./conventions/">Conventions</a></h3>
    <p>Summarizes the implementation conventions used to turn the architecture model into repeatable Terraform practice.</p>
    <ul>
      <li><a href="./conventions/">Section overview</a></li>
      <li><a href="https://github.com/DeokJong/terraform-3-layer-architecture-specification/blob/main/terraform-3-layer-architecture-conventions.md">Canonical conventions</a></li>
    </ul>
  </section>
  <section class="home-card">
    <h3><a href="./adr/">ADR</a></h3>
    <p>Explains the architectural decision record structure and where the primary rationale is documented.</p>
    <ul>
      <li><a href="./adr/">Section overview</a></li>
      <li><a href="https://github.com/DeokJong/terraform-3-layer-architecture-specification/blob/main/adr-3layer-architecture-contract-workspace.md">Canonical ADR-0001</a></li>
    </ul>
  </section>
  <section class="home-card">
    <h3><a href="./meta/">Documentation System</a></h3>
    <p>Tracks the registry, work index, and agent guidance used to maintain the documentation system itself.</p>
    <ul>
      <li><a href="./meta/work-index/">Work Index</a></li>
      <li><a href="./meta/agent-instructions/">Agent Instructions Source</a></li>
      <li><a href="./meta/document-registry.json">Document Registry</a></li>
    </ul>
  </section>
</div>

## Reading Guide

- Use the Architecture section for the conceptual model and decision rules.
- Use the Conventions section for repeatable implementation guidance.
- Use ADR for decision context and the Documentation System section for maintenance workflow.
