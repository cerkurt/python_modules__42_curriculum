#!/usr/bin/env python3


"""Capability abstract classes used by special creatures in ex1."""


from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for creatures that can heal."""
    @abstractmethod
    def heal(self) -> str:
        """Return the healing action of the creature."""
        pass


class TransformCapability(ABC):
    """Abstract capability for creatures that can transform."""
    @abstractmethod
    def transform(self) -> str:
        """Enable the transformed state of the creature."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Return the creature to its normal state."""
        pass
