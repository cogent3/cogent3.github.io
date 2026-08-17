#!/usr/bin/env bash
# Build cogent3.org into docs/: wrapper pages at the root, cogent3 library docs
# under /doc/. That /doc/ layout is what the site has served since 2020.
#
#   ./build.sh                            both halves, from the pinned submodule
#   C3_REPO=/path/to/cogent3 ./build.sh   both halves, from another checkout
#   ./build.sh --skip-c3                  wrapper only, reuse existing docs/doc/
#   ./build.sh --skip-quartodoc           skip the API reference regeneration
#   ./build.sh --skip-site                library docs only
#
# QUARTO may point at a quarto binary; CI sets it from the quarto-dev action so
# that no network install happens there.
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$here"

# the cogent3 checkout whose doc/ tree becomes docs/doc/. Overriding this is how
# you build against a cogent3 branch the submodule has not been bumped to yet.
C3_REPO="${C3_REPO:-$here/doc/cogent3}"
C3_DOC="${C3_DOC:-$C3_REPO/doc}"

skip_c3=0
skip_site=0
skip_quartodoc=0
for arg in "$@"; do
  case "$arg" in
    --skip-c3) skip_c3=1 ;;
    --skip-site) skip_site=1 ;;
    --skip-quartodoc) skip_quartodoc=1 ;;
    -h | --help)
      sed -n '2,11p' "$0"
      exit 0
      ;;
    *)
      printf 'unknown argument: %s\n' "$arg" >&2
      exit 2
      ;;
  esac
done
if ((skip_c3 && skip_site)); then
  echo "--skip-c3 and --skip-site leave nothing to build" >&2
  exit 2
fi

# quarto is not a python dependency of the cogent3 repo -- its CI installs it
# with the quarto-dev action. Here the `doc` dependency group is a fallback, but
# an externally supplied binary always wins.
if [[ -n "${QUARTO:-}" ]]; then
  QUARTO="$(command -v "$QUARTO")" || {
    echo "QUARTO is set but not executable" >&2
    exit 1
  }
else
  uv sync --group doc --quiet
  QUARTO="$here/.venv/bin/quarto"
  [[ -x "$QUARTO" ]] || {
    echo "no quarto at $QUARTO" >&2
    exit 1
  }
fi

# both halves need the cogent3 checkout: the library docs are rendered from it,
# and the wrapper's bibliography is copied out of it. Check once, up front, so
# an uninitialised submodule fails with a diagnostic rather than a bare `cp:`.
[[ -f "$C3_DOC/cogent3.bib" ]] || {
  echo "no cogent3 docs at $C3_DOC -- is the submodule initialised? Otherwise" >&2
  echo "set C3_REPO to a cogent3 checkout, e.g. C3_REPO=~/repos/Cogent3" >&2
  exit 1
}

if ((!skip_c3)); then
  [[ -f "$C3_DOC/_quarto.yml" ]] || {
    echo "$C3_DOC predates the quarto migration -- set C3_REPO to a checkout" >&2
    echo "that has one, or pass --skip-c3." >&2
    exit 1
  }
  if ((!skip_quartodoc)); then
    # quartodoc writes doc/reference/ and doc/objects.json, which `quarto
    # render` then needs to exist. Order matters.
    (cd "$C3_REPO" && uv run --group doc quartodoc build --config doc/_quarto.yml)
  fi
  # quarto finds the interpreter, and so the kernel, from QUARTO_PYTHON
  QUARTO_PYTHON="$C3_REPO/.venv/bin/python" "$QUARTO" render "$C3_DOC"
fi

if ((!skip_site)); then
  # quarto resolves `bibliography:` against the project, so take a build-time
  # copy instead of committing a second cogent3.bib. Gitignored.
  cp "$C3_DOC/cogent3.bib" doc/cogent3.bib
  "$QUARTO" render doc
fi

mkdir -p docs
# CNAME and .nojekyll live only in docs/ and are tracked; excluding them keeps
# --delete from removing them. Excluding /doc/ keeps the two halves independent,
# so either --skip flag leaves the other half of the site intact.
if ((!skip_site)); then
  rsync -a --delete \
    --exclude '/doc/' --exclude '/CNAME' --exclude '/.nojekyll' \
    doc/_site/ docs/
fi
if ((!skip_c3)); then
  rsync -a --delete "$C3_DOC/_site/" docs/doc/

  # Point the masthead logo at the site root. Quarto offsets navbar *item*
  # hrefs against the site root once they leave the project, which is why the
  # `../` entries in the cogent3 navbar land correctly at every depth -- but it
  # offsets `logo-href` against the *project* root instead, so inside docs/doc/
  # the logo would link to the library docs home rather than cogent3.org. There
  # is no config that expresses "site root" to a project that does not know it
  # is nested, so rewrite it here.
  python3 - <<'PY'
import pathlib
import re

root = pathlib.Path("docs")
brand = re.compile(r'(class="navbar-brand" href=")[^"]*(")')
for page in (root / "doc").rglob("*.html"):
    depth = len(page.relative_to(root).parts) - 1
    patched, n = brand.subn(rf'\g<1>{"../" * depth}index.html\g<2>', page.read_text())
    if n:
        page.write_text(patched)
PY
fi

printf 'built %s\n' "$here/docs"
