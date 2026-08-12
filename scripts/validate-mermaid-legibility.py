#!/usr/bin/env python3

"""Reject rendered Mermaid diagrams that become unreadable at document width."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as element_tree
from pathlib import Path


HEADING_PATTERN = re.compile(r"^## Diagram \d+: (.+)$")
IMAGE_PATTERN = re.compile(
    r"^!\[diagram\]\((?:\./)?(?:[^/)]+/)*([^/]+\.svg)\)$"
)
MAX_VIEWBOX_WIDTH = 1400.0
MAX_LANDSCAPE_RATIO = 4.0
MINIMUM_DIAGRAMS_BY_DOCUMENT = {
    "framework/README.md": 1,
    "framework/charter.md": 1,
    "framework/glossary.md": 1,
    "framework/operating-framework.md": 1,
    "framework/shared-operating-memory-standard.md": 2,
    "framework/sop-content-standard.md": 2,
    "framework/standards-maintenance-method.md": 1,
    "examples/README.md": 1,
    "examples/01-accounts-payable-invoice-processing.md": 2,
    "examples/02-software-change-delivery.md": 2,
    "examples/03-construction-field-incident-response.md": 2,
    "examples/04-employee-onboarding-offboarding.md": 2,
    "examples/05-ma-day-1-transition.md": 2,
    "examples/06-customer-complaint-service-recovery.md": 2,
    "examples/07-regulatory-change-implementation.md": 2,
    "examples/08-supply-chain-disruption-response.md": 2,
    "examples/09-sales-proposal-contract-approval.md": 2,
    "examples/10-patient-referral-care-transition.md": 2,
    "examples/11-shared-operating-memory-capture-and-handoff.md": 2,
}


def rendered_sources(rendered_document: Path) -> dict[str, str]:
    sources: dict[str, str] = {}
    current_source: str | None = None

    for line in rendered_document.read_text(encoding="utf-8").splitlines():
        heading = HEADING_PATTERN.fullmatch(line)
        if heading:
            current_source = heading.group(1)
            continue

        image = IMAGE_PATTERN.fullmatch(line)
        if image and current_source:
            sources[image.group(1)] = current_source

    return sources


def viewbox_size(svg_path: Path) -> tuple[float, float]:
    root = element_tree.parse(svg_path).getroot()
    viewbox = root.attrib.get("viewBox", "").split()
    if len(viewbox) != 4:
        raise ValueError("missing a four-value SVG viewBox")

    width = float(viewbox[2])
    height = float(viewbox[3])
    if width <= 0 or height <= 0:
        raise ValueError("SVG viewBox dimensions must be positive")
    return width, height


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("rendered_document", type=Path)
    parser.add_argument("assets_directory", type=Path)
    arguments = parser.parse_args()

    sources = rendered_sources(arguments.rendered_document)
    failures: list[str] = []
    svg_paths = sorted(arguments.assets_directory.glob("*.svg"))
    document_counts: dict[str, int] = {}

    for svg_path in svg_paths:
        source = sources.get(svg_path.name, svg_path.name)
        document = source.rsplit(" block ", maxsplit=1)[0]
        document_counts[document] = document_counts.get(document, 0) + 1
        try:
            width, height = viewbox_size(svg_path)
        except (OSError, ValueError, element_tree.ParseError) as error:
            failures.append(f"{source}: cannot inspect rendered SVG: {error}")
            continue

        ratio = width / height
        if width > MAX_VIEWBOX_WIDTH:
            failures.append(
                f"{source}: rendered width {width:.0f}px exceeds "
                f"{MAX_VIEWBOX_WIDTH:.0f}px"
            )
        if ratio > MAX_LANDSCAPE_RATIO:
            failures.append(
                f"{source}: landscape ratio {ratio:.1f}:1 exceeds "
                f"{MAX_LANDSCAPE_RATIO:.1f}:1"
            )

    for document, minimum in MINIMUM_DIAGRAMS_BY_DOCUMENT.items():
        actual = document_counts.get(document, 0)
        if actual < minimum:
            failures.append(
                f"{document}: expected at least {minimum} diagram(s), found {actual}"
            )

    if failures:
        for failure in failures:
            print(f"FAIL: Mermaid legibility: {failure}", file=sys.stderr)
        return 1

    print(
        "PASS: Mermaid legibility: "
        f"{len(svg_paths)} rendered diagrams fit document-width limits"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
