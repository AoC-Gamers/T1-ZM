.DEFAULT_GOAL := help
PYTHON ?= python3
ROOT_DIR := $(shell $(PYTHON) -c "import sys; from pathlib import Path; print(Path(sys.argv[1]).resolve().parent.as_posix())" "$(MAKEFILE_LIST)")
RUN = cd "$(ROOT_DIR)" && $(PYTHON) scripts/package/artifact_contract.py
RELEASE_BASENAME ?= t1-zm-local

.PHONY: help validate-modes package-modes release validate-artifact
help:
	@$(PYTHON) -c "print('validate-modes, package-modes, release, validate-artifact')"

validate-modes:
	$(RUN) validate-modes

package-modes:
	$(RUN) package-modes

release: package-modes
	$(RUN) release --basename "$(RELEASE_BASENAME)"

validate-artifact:
	$(RUN) validate-artifact --basename "$(RELEASE_BASENAME)"
