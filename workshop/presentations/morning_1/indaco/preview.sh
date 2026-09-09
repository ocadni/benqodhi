#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="${CONDA_ENV_NAME:-benqodhi}"
HOST="${HOST:-127.0.0.1}"
PORT="${PORT:-4242}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/../../../.." && pwd)"
CACHE_DIR="${QUARTO_CACHE_HOME:-${ROOT_DIR}/.quarto-cache}"

if ! command -v conda >/dev/null 2>&1; then
  echo "ERROR: conda was not found on PATH." >&2
  echo "Open a shell where conda is initialized, then retry." >&2
  exit 1
fi

CONDA_BASE="$(conda info --base)"
# shellcheck source=/dev/null
source "${CONDA_BASE}/etc/profile.d/conda.sh"
conda activate "${ENV_NAME}"

mkdir -p "${CACHE_DIR}"
export XDG_CACHE_HOME="${CACHE_DIR}"

cd "${SCRIPT_DIR}"

cat <<MSG
Starting BENQODHI intro slide preview

Remote URL: http://${HOST}:${PORT}/

If you are in VS Code Remote SSH:
  1. Open the Ports tab
  2. Forward port ${PORT} if VS Code does not do it automatically
  3. Open http://localhost:${PORT}/ in your local browser

Press Ctrl+C in this terminal to stop the preview.

MSG

exec quarto preview intro.qmd --host "${HOST}" --port "${PORT}" --no-browser
