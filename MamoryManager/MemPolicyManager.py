from typing import Type

from .Policies import *


class MemPolicyManager(FirstFit, BestFit):
    def __init__(self, base: int, bound: int, policy: Type[Policy], full: bool = False):
        super().__init__(base, bound)
        self.NAME = policy.NAME
        self.policy = policy
        self.full = full

    def free(self, mem_block: MemoryBlock) -> MemoryBlock or None:
        return self.policy.free(self, mem_block)

    def alloc(self, mem_size: int) -> MemoryBlock or None:
        return self.policy.alloc(self, mem_size)

    def __str__(self, **kwargs):
        if self.full:
            return self.policy.__str__(self, func=lambda mem_block: mem_block.get_full())
        return self.policy.__str__(self)
