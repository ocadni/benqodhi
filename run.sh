#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="${CONDA_ENV_NAME:-benqodhi}"
CMD="${1:-preview}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="${ROOT_DIR}/website"
CACHE_DIR="${QUARTO_CACHE_HOME:-${ROOT_DIR}/.quarto-cache}"

if ! command -v conda >/dev/null 2>&1; then
  echo "ERROR: conda was not found on PATH." >&2
  echo "Install conda or open a shell where conda is initialized, then retry." >&2
  exit 1
fi

CONDA_BASE="$(conda info --base)"
# shellcheck source=/dev/null
source "${CONDA_BASE}/etc/profile.d/conda.sh"
conda activate "${ENV_NAME}"
mkdir -p "${CACHE_DIR}"
export XDG_CACHE_HOME="${CACHE_DIR}"

case "${CMD}" in
  preview)
    cd "${SITE_DIR}"
    exec quarto preview
    ;;
  render)
    cd "${SITE_DIR}"
    exec quarto render
    ;;
  *)
    echo "Usage: ./run.sh [preview|render]" >&2
    echo "  preview  Start the local Quarto preview server (default)." >&2
    echo "  render   Build the static site into website/_site/." >&2
    exit 2
    ;;
esac
