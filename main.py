from MamoryManager import *

mem_manager = MemPolicyManager(1000, 100, BestFit)
inputParser = TextInputParser(mem_manager)
inputParser.execute("input.txt")


# print(mem_manager, "\n ------- \n")
# p0 = mem_manager.alloc(1)
# print(mem_manager.get_free_mem_blocks())
# mem_manager.free(p0)
# print(mem_manager.get_free_mem_blocks())
# p1 = mem_manager.alloc(7)
# print(mem_manager.get_free_mem_blocks())
# mem_manager.free(p1)
# print(mem_manager.get_free_mem_blocks())
# p2 = mem_manager.alloc(5)
# print(mem_manager.get_free_mem_blocks())
# p3 = mem_manager.alloc(8)
# print(mem_manager.get_free_mem_blocks())
# mem_manager.free(p3)
# print(mem_manager.get_free_mem_blocks())
# mem_manager.free(p2)
# print(mem_manager.get_free_mem_blocks())
# p4 = mem_manager.alloc(1)
# print(mem_manager.get_free_mem_blocks())
# p5 = mem_manager.alloc(5)
# print(mem_manager.get_free_mem_blocks())

