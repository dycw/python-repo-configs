import hypothesis
import typed_settings
from hypothesis import Verbosity
from typed_settings import load


@typed_settings.settings(frozen=True)  # type: ignore
class _Config:
    """A collection of test configurations."""

    max_examples: int = 100
    verbosity: Verbosity = Verbosity.normal


HYPOTHESIS_CONFIG = load(_Config, "hypothesis")


hypothesis.settings.register_profile("default")
