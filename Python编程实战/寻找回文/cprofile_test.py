"""用cProfile模块分析程序性能"""
import cProfile
import palingrams
cProfile.run('palingrams_optimized.find_palingrams()')
