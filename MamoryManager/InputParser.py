from MamoryManager import MemPolicyManager
import re


class InputParser:
    ALLOC_PATTERN = None
    FREE_PATTERN = None

    def __init__(self, mem_manager: MemPolicyManager):
        self.mem_manager = mem_manager

    def execute(self, path: str, silent: bool = False) -> None:
        pass

    def exec_line(self, line) -> None:
        pass

    def make_alloc(self, var_name: str, mem_size: str) -> None:
        pass

    def make_free(self, var_name: str) -> None:
        pass


class TextInputParser(InputParser):
    ALLOC_PATTERN = r"(.*) = Alloc\((.*)\)"
    FREE_PATTERN = r"Free\((.*)\)"

    def __init__(self, mem_manager: MemPolicyManager):
        super().__init__(mem_manager)
        self.init_mem_blocks = {}

    def execute(self, path: str, silent: bool = False) -> None:
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            self.exec_line(line)
            if not silent:
                print(f"{line.strip():<15} -> {self.mem_manager.get_free_mem_blocks()}")

    def exec_line(self, line) -> None:
        for alloc_setting in re.findall(TextInputParser.ALLOC_PATTERN, line):
            self.make_alloc(*alloc_setting)
        for free_setting in re.findall(TextInputParser.FREE_PATTERN, line):
            self.make_free(free_setting)

    def make_alloc(self, var_name: str, mem_size: str) -> None:
        self.init_mem_blocks[var_name] = self.mem_manager.alloc(int(mem_size))

    def make_free(self, var_name: str) -> None:
        self.init_mem_blocks[var_name] = self.mem_manager.free(self.init_mem_blocks[var_name])
