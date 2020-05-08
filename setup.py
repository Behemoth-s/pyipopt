# Originally contributed by Lorne McIntosh.
# Previous modification by Eric Xu
# Modified by Kai Liu
# Further modification by random internet people.

# You will probably have to edit this file in unpredictable ways
# if you want pyipopt to work for you, sorry.

# 该版本为了适配windows 系统和msvc编译器而作修改
# Ipopt二进制文件基于mumps和mkl 使用coinbrew脚本和msvc编译器生成。
# 安装脚本会将ipopt所有二进制文件复制到pyipopt根目录下，因为不这样做即使加到系统目录，
# pyipoptcore仍然找不到dll，作者还没有找到解决方法
# 默认Ipopt文件位置
IPOPT_DIR = 'Ipopt'

import os
# from distutils.core import setup
# from distutils.extension import Extension
from setuptools import Extension
from setuptools import setup
# NumPy is much easier to install than pyipopt,
# and is a pyipopt dependency, so require it here.
# We need it to tell us where the numpy header files are.
import numpy

numpy_include = numpy.get_include()


# I personally do not need support for lib64 but I'm keeping it in the code.
def get_ipopt_lib():
    for lib_suffix in ('lib', 'lib64'):
        d = os.path.join(IPOPT_DIR, lib_suffix)
        if os.path.isdir(d):
            return d


def get_ipopt_inc():
    for inc_suffix in ('coin', 'coin-or'):
        d = os.path.join(IPOPT_DIR, 'include', inc_suffix)
        if os.path.isdir(d):
            return d


IPOPT_LIB = get_ipopt_lib()
if IPOPT_LIB is None:
    raise Exception('failed to find ipopt lib')

IPOPT_INC = get_ipopt_inc()
if IPOPT_INC is None:
    raise Exception('failed to find ipopt include')

IPOPT_BIN = os.path.join(IPOPT_DIR, 'bin')
data_files = []
for file in os.listdir(IPOPT_BIN):
    if file.endswith('dll'):
        data_files.append(os.path.join(IPOPT_BIN, file))


FILES = ['src/callback.c', 'src/pyipoptcoremodule.c']

# The extra_link_args is commented out here;
# that line was causing my pyipopt install to not work.
# Also I am using coinmumps instead of coinhsl.
pyipopt_extension = Extension(
    'pyipoptcore',
    FILES,
    # extra_link_args=['-Wl,--rpath','-Wl,'+ IPOPT_LIB],
    library_dirs=[IPOPT_LIB],
    # libraries=[
    #     'ipopt', 'coinblas',
    #     # 'coinhsl',
    #     'coinmumps',
    #     'coinmetis',
    #     'coinlapack', 'dl', 'm',
    # ],
    libraries=[
        'ipopt.dll',
        "ipoptamplinterface.dll",
        "coinasl.dll"
        # 'coinhsl',
        # 'coinmumps.dll',
        # 'coinmetis.dll',
        # "mkl_intel_lp64_dll",
        # "mkl_core_dll",
        # "mkl_sequential_dll"
    ],
    include_dirs=[numpy_include, IPOPT_INC],
    language="c++"
)

setup(
    name="pyipopt",
    version="0.81",
    description="An IPOPT connector for Python Windows version",
    author="Kai Liu",
    author_email="liukaiv5@gmail.com",
    url="https://github.com/Behemoth-s/pyipopt",
    packages=['pyipopt'],
    package_dir={'pyipopt': 'pyipoptpackage'},
    # package_data={'':data_files},
    ext_package='pyipopt',
    ext_modules=[pyipopt_extension],
    data_files=[('pyipopt',data_files)]
)
