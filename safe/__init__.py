# Core SMILES to SAFE conversion functionality
from ._exception import SAFEDecodeError, SAFEEncodeError, SAFEFragmentationError
from .converter import SAFEConverter, decode, encode

# Optional imports for advanced utility features (require networkx)
# Install with: pip install safe-mol[viz]
try:
    from . import utils
except ImportError:
    utils = None

# Training and generation features (require transformers)
# Install with: pip install safe-mol[training]
try:
    from .sample import SAFEDesign
    from .tokenizer import SAFETokenizer, split
    from . import trainer
except ImportError:
    SAFEDesign = None
    SAFETokenizer = None
    split = None
    trainer = None

# Visualization features (require networkx)
# Install with: pip install safe-mol[viz]
try:
    from .viz import to_image
except ImportError:
    to_image = None

# W&B integration (requires wandb)
try:
    from .io import upload_to_wandb
except ImportError:
    upload_to_wandb = None

# Public API for core functionality
__all__ = [
    # Core conversion
    "encode",
    "decode",
    "SAFEConverter",
    # Exceptions
    "SAFEDecodeError",
    "SAFEEncodeError",
    "SAFEFragmentationError",
    # Optional features (may be None if dependencies not installed)
    "utils",
    "SAFEDesign",
    "SAFETokenizer",
    "split",
    "to_image",
    "upload_to_wandb",
    "trainer",
]
