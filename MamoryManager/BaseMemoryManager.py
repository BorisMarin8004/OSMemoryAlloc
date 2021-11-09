from .MemoryBlock import MemoryBlock


class BaseMemoryManager:
    def __init__(self, base: int, bound: int, mem_arr=None):
        self.base = base
        self.bound = bound
        if mem_arr is None:
            mem_block = MemoryBlock(base, bound, True)
            mem_arr = [mem_block]
        self.mem_arr = mem_arr

    def free(self, mem_block: MemoryBlock) -> MemoryBlock or None:
        pass

    def alloc(self, mem_size: int) -> int or None:
        pass

    def get_free_mem_blocks(self) -> list[MemoryBlock]:
        return [mem_block for mem_block in self.mem_arr if mem_block.free]

    def insert(self, index: int, mem_block: MemoryBlock, mem_size: int) -> None:
        self.mem_arr.insert(index, mem_block.split_mem_block(mem_size))
        for mem_block in self.mem_arr[:]:
            if mem_block.bound == 0:
                self.mem_arr.remove(mem_block)

    def __str__(self, **kwargs):
        if "func" not in kwargs:
            kwargs["func"] = lambda mem_block: mem_block
        return "\n".join((
            "Base - Bound: " + str((self.base, self.bound)),
            "Memory array: " + str(list(map(kwargs["func"], self.mem_arr))),
        ))
