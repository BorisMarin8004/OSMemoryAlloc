from .MemoryBlock import MemoryBlock
from .BaseMemoryManager import BaseMemoryManager


class Policy(BaseMemoryManager):
    NAME = None

    def get_possible_blocks(self, mem_size: int) -> list[MemoryBlock]:
        return [mem_block for i, mem_block in enumerate(self.mem_arr) if mem_block.has_space(mem_size)]

    def free(self, mem_block: MemoryBlock) -> MemoryBlock or None:
        if mem_block in self.mem_arr:
            mem_block.free = True
            return mem_block
        return None

    def __str__(self, **kwargs):
        return "\n".join((
            "Policy: " + self.NAME,
            super().__str__(**kwargs)
        ))


class BestFit(Policy):
    NAME = "BestFit"

    def alloc(self, mem_size: int) -> MemoryBlock or None:
        possible_blocks = self.get_possible_blocks(mem_size)
        if len(possible_blocks) == 0:
            return None
        best_fit_mem_block = 0, possible_blocks[0], possible_blocks[0].bound
        for i, mem_block in enumerate(self.mem_arr):
            if mem_block in possible_blocks and mem_block.bound <= best_fit_mem_block[2]:
                best_fit_mem_block = i, mem_block, mem_block.bound
        self.insert(*best_fit_mem_block[:-1], mem_size=mem_size)
        return self.mem_arr[best_fit_mem_block[0]]


class FirstFit(Policy):
    NAME = "FirstFit"

    def alloc(self, mem_size: int) -> MemoryBlock or None:
        for i, mem_block in enumerate(self.mem_arr):
            if mem_block.has_space(mem_size):
                self.insert(i, mem_block, mem_size)
                return self.mem_arr[i]
        return None


class WorstFit(Policy):
    NAME = "WorstFit"

    def alloc(self, mem_size: int) -> int or None:
        possible_blocks = self.get_possible_blocks(mem_size)
        if len(possible_blocks) == 0:
            return None
        worst_fit_mem_block = 0, possible_blocks[0], possible_blocks[0].bound
        for i, mem_block in enumerate(self.mem_arr):
            if mem_block in possible_blocks and mem_block.bound >= worst_fit_mem_block[2]:
                worst_fit_mem_block = i, mem_block, mem_block.bound
        self.insert(*worst_fit_mem_block[:-1], mem_size=mem_size)
        return self.mem_arr[worst_fit_mem_block[0]]
