#!/usr/bin/env python3
"""Stage and validate the T1-ZM configuration package."""

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile

MAP_PATH = Path("scripts/package/package-map.json")
STAGE = Path(".build/package-modes")
RELEASE_DIR = Path("dist/release")
PROJECT_FILES = (Path("README.md"), Path("LICENSE"), Path("NOTICES.md"))
EXEC = re.compile(r'^\s*exec\s+(?:"([^"]+)"|([^\s;"]+))', re.IGNORECASE)


def load_product(root: Path) -> set[Path]:
    manifest = json.loads((root / MAP_PATH).read_text(encoding="utf-8"))
    mode = manifest["mode"]
    if not re.fullmatch(r"[a-z][a-z0-9_]*", mode):
        raise ValueError(f"Invalid Confogl mode identifier: {mode}")

    names = manifest["configs"]
    if len({name.casefold() for name in names}) != len(names):
        raise ValueError("Configuration names must be unique across platforms")
    for name in names:
        if not re.fullmatch(r"[a-zA-Z0-9_][a-zA-Z0-9_.-]*\.(?:cfg|txt)", name):
            raise ValueError(f"Invalid mode configuration path: {name}")
    required = {"confogl.cfg", "confogl_off.cfg", "confogl_plugins.cfg", f"{mode}.cfg"}
    if missing := required - set(names):
        raise ValueError(f"Missing Confogl entrypoints: {sorted(missing)}")

    cfg_root = Path("cfg")
    mode_dir = cfg_root / "cfgogl" / mode
    configs = {mode_dir / name for name in names}
    external_exec = set(manifest["external_exec"])
    product = configs.union(PROJECT_FILES)

    for relative in sorted(product):
        source = root / relative
        if not source.is_file() or not source.stat().st_size:
            raise ValueError(f"Missing or empty product file: {relative}")
    for relative in sorted(configs):
        if relative.suffix == ".cfg":
            for number, line in enumerate((root / relative).read_text(encoding="utf-8-sig").splitlines(), 1):
                match = EXEC.match(line)
                if match:
                    target = match[1] or match[2]
                    if cfg_root / target not in configs and target not in external_exec:
                        raise ValueError(f"{relative}:{number}: undeclared exec target {target}")
    return product


def stage_product(root: Path, product: set[Path]) -> None:
    stage = root / STAGE
    if stage.resolve() != stage:
        raise ValueError(f"Staging path must not traverse symlinks: {stage}")
    stage.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=stage.parent) as temporary:
        candidate = Path(temporary) / "artifact"
        for relative in sorted(product):
            destination = candidate / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / relative, destination)
        if stage.exists():
            shutil.rmtree(stage)
        candidate.rename(stage)


def validate_stage(root: Path, product: set[Path]) -> None:
    stage = root / STAGE
    actual = {path.relative_to(stage) for path in stage.rglob("*") if path.is_file()}
    if actual != product:
        raise ValueError(f"Staging differs from package map: missing {product - actual}, extra {actual - product}")
    for path in sorted(product):
        if (root / path).read_bytes() != (stage / path).read_bytes():
            raise ValueError(f"Stale staged file: {path}")


def validate_archive(root: Path, product: set[Path], archive: Path) -> None:
    members = {path.as_posix(): path for path in product}
    with ZipFile(archive) as package:
        files = package.namelist()
        if len(files) != len(members) or set(files) != set(members):
            raise ValueError("ZIP entries do not match the package map")
        for name, path in members.items():
            if package.read(name) != (root / path).read_bytes():
                raise ValueError(f"ZIP content differs from source: {name}")


def release(root: Path, product: set[Path], archive: Path) -> None:
    validate_stage(root, product)
    archive.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=archive.parent) as temporary:
        candidate = Path(temporary) / archive.name
        with ZipFile(candidate, "w", compression=ZIP_DEFLATED) as package:
            for path in sorted(product):
                package.write(root / STAGE / path, arcname=path.as_posix())
        validate_archive(root, product, candidate)
        os.replace(candidate, archive)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("validate-modes", "package-modes", "release", "validate-artifact"))
    parser.add_argument("--basename", default="t1-zm-local")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.basename):
        parser.error("expected a ZIP basename without path separators")

    root = Path(__file__).resolve().parents[2]
    archive = root / RELEASE_DIR / f"{args.basename}.zip"
    try:
        product = load_product(root)
        if args.operation == "package-modes":
            stage_product(root, product)
            validate_stage(root, product)
        if args.operation == "release":
            release(root, product, archive)
            print(archive)
        if args.operation == "validate-artifact":
            validate_archive(root, product, archive)
    except (OSError, ValueError, BadZipFile) as error:
        parser.exit(1, f"{error}\n")
    print(f"{args.operation}: OK")


if __name__ == "__main__":
    main()
