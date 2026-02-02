# SAFE Package Migration Guide - Minimal Version

## Overview

Modified the original SAFE package to make transformer training capabilities optional. The main utility of this package is SMILES to SAFE string conversion with updated package compatibility.

## Major Changes

### 1. Dependencies

#### Previous Installation Requirements
- `torch>=2.0` (~2GB)
- `transformers` (~500MB)
- `datasets`, `tokenizers`, `accelerate`, `evaluate`
- `wandb`, `huggingface-hub`
- `tqdm`, `typer`, `universal_pathlib`
- Plus core: `rdkit`, `datamol`, `numpy`, `loguru`

#### Current Installation Requirements
Only requires:
- `rdkit` - Chemistry toolkit
- `datamol` - RDKit wrapper
- `numpy` - Numerical operations
- `loguru` - Logging


### 3. Python Version Support

Added support for Python 3.12 and 3.13:
- **Before:** Python 3.9 - 3.11
- **After:** Python 3.9 - 3.13

### 4. Installation Options

```bash
# Core version
pip install -e .

# With visualization utilities
pip install -e ".[viz]"

# With training capabilities
pip install -e ".[training]"

# Full installation
pip install -e ".[training,viz]"
```

Or using requirements files:
```bash
# Minimal
pip install -r requirements-minimal.txt

# Full
pip install -r requirements-full.txt
```

## Usage Examples

### Basic Usage (Minimal Installation)

```python
import safe

# Encode SMILES to SAFE
smiles = "CC(C)Cc1ccc(cc1)C(C)C(=O)O"
safe_str = safe.encode(smiles)
print(safe_str)
# Output: c12ccc3cc1.C3(C)C(=O)O.CC(C)C2

# Decode back to SMILES
decoded = safe.decode(safe_str, canonical=True)
print(decoded)
# Output: CC(C)Cc1ccc(C(C)C(=O)O)cc1
```

### Different Fragmentation Algorithms

```python
import safe

smiles = "CC(C)Cc1ccc(cc1)C(C)C(=O)O"

# Try different slicers
for slicer in ["brics", "recap", "hr", "mmpa"]:
    try:
        result = safe.encode(smiles, slicer=slicer)
        print(f"{slicer:8s}: {result}")
    except safe.SAFEFragmentationError:
        print(f"{slicer:8s}: No fragmentable bonds")
```

### Advanced: Custom Converter Settings

```python
from safe import SAFEConverter

converter = SAFEConverter(
    slicer="brics",
    ignore_stereo=False,
    require_hs=False
)

smiles = "c1ccccc1CCO"
safe_str = converter.encoder(smiles, canonical=True)
decoded = converter.decoder(safe_str, canonical=True)
```

## Fragmentation Algorithms

The core converter supports multiple bond-breaking strategies:

| Algorithm | Description | SMARTS Pattern |
|-----------|-------------|----------------|
| `brics` | RDKit's BRICS (default) | Built-in RDKit algorithm |
| `recap` | Retrosynthetic Combinatorial Analysis | 11 different patterns |
| `hr` | Hussain-Rea (non-ring single bonds) | `[*]!@-[*]` |
| `mmpa` | Matched Molecular Pair Analysis | `[#6+0;!$(*=,#[!#6])]!@!=!#[*]` |
| `attach` | Any attachment point | `[*]!@[*]` |
| `rotatable` | Rotatable bonds | `[!$(*#*)&!D1]-&!@[!$(*#*)&!D1]` |
| Custom | User-defined callable | Your function returning bond IDs |

