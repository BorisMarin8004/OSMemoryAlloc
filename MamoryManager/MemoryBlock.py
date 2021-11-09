class MemoryBlock:
    def __init__(self, base: int, bound: int, free: bool = False):
        self.base = base
        self.bound = bound
        self.free = free

    def has_space(self, mem_size: int) -> bool:
        if not self.free:
            return False
        return self.bound >= mem_size

    def split_mem_block(self, mem_size: int):
        new_mem_block = MemoryBlock(self.base, mem_size)
        self.base += mem_size
        self.bound -= mem_size
        return new_mem_block

    def get_upper_bound(self) -> int:
        return self.base + self.bound

    def get_full(self) -> tuple:
        return self.base, self.bound, self.free

    def __eq__(self, other):
        if isinstance(other, MemoryBlock):
            return self.base == other.base and self.bound == other.bound
        return False

    def __str__(self):
        return str((self.base, self.bound))

    def __repr__(self):
        return self.__str__()
