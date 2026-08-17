# Environment setup

This repo needs the **Quarto CLI** to render and preview the website in
[`website/`](website/). Two ways to get it, pick one.

> **Network note:** installation downloads packages from PyPI (and, for the pip
> route, a Quarto binary from GitHub). On a network with a corporate proxy, set
> `HTTP_PROXY` / `HTTPS_PROXY` first, or use `pip install --proxy <url> ...`.

## Option A — Python venv (used by this repo)

A virtual environment already exists at `.venv/` (created with the system Python,
3.12.1). It is excluded from git via `.gitignore` — every contributor creates their
own.

**Create it (if it doesn't exist yet):**

```powershell
python -m venv .venv
```

**Activate it:**

```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1

# cmd
.\.venv\Scripts\activate.bat
```

**Install dependencies:**

```powershell
pip install -r requirements.txt
```

This installs [`quarto-cli`](https://pypi.org/project/quarto-cli/), which provides the
`quarto` command. Verify with:

```powershell
quarto --version
```

## Option B — conda env

Conda is not installed on this machine as of this writing. If you have conda
available (Miniconda or Anaconda):

```bash
conda env create -f environment.yml
conda activate benqodhi
```

This installs Quarto directly from the `conda-forge` channel (a different
distribution than the PyPI `quarto-cli` package, but the same tool).

## Using Quarto once installed

All website commands run from the `website/` subfolder:

```powershell
cd website
quarto preview      # live preview at http://localhost:...
quarto render        # build the static site into website/_site/
```

## Uninstall / cleanup

- venv route: delete the `.venv/` folder.
- conda route: `conda env remove -n benqodhi`.
