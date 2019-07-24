# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMdanalysis(PythonPackage):
    """MDAnalysis is a Python toolkit to analyze molecular dynamics
    trajectories generated by a wide range of popular simulation
    packages including DL_Poly, CHARMM, Amber, NAMD, LAMMPS, and
    Gromacs. (See the lists of supported trajectory formats and
    topology formats.)"""

    homepage = "http://www.mdanalysis.org"
    url      = "https://pypi.io/packages/source/M/MDAnalysis/MDAnalysis-0.19.2.tar.gz"

    version('0.19.2', sha256='c5395bbafa5efca2e1aee4715d26129844140c47cb8301da0293106cb969de7d')
    version('0.19.1', sha256='ff1d694f8598c0833ec340de6a6adb3b5e62b92d0fa94ee6401718ba972db3cc')
    version('0.19.0', sha256='248e3b37fc6150e31c609cc18a3927c32aee37b76d29cbfedf635e7e1aa982cf')
    version('0.18.0', sha256='a08acea1755112411e7db55e3f282e164b47a59e15794b38744cce6c596f252a')
    version('0.17.0', sha256='9bd61760334698cc7b8a57ad26456451e926e9c9e66722594ad8816561348cde')
    version('0.16.2', sha256='407d9a9ff1ab8a5e47973714d06fabff220f8d08a28792dee93e88e70e995b0a')
    version('0.16.1', sha256='3dc8f5d639ab3a0d152cbd7259ae9372ec8a9bac0f8cb7d3b80ce5adc1e3ee57')
    version('0.16.0', sha256='c4824fa1fddd336daa39371436187ebb023366885fb250c2827ed7fce2546bd4')
    version('0.15.0', '19e5a8e6c2bfe85f6209d1d7a36e4f20')

    variant('analysis', default=True, 
            description='Enable analysis packages: matplotlib, scipy, seaborn')
    variant('amber', default=False,
            description='Support AMBER netcdf format.')

    depends_on('python@2.7:')
    depends_on('py-setuptools', type='build')
    depends_on('py-cython@0.16:', type='build')
    depends_on('py-numpy@1.5.0:', type=('build', 'run'))
    depends_on('py-six@1.4.0:', type=('build', 'run'))
    depends_on('py-biopython@1.59:', type=('build', 'run'))
    depends_on('py-networkx@1.0:', type=('build', 'run'))
    depends_on('py-griddataformats@0.3.2:', type=('build', 'run'))

    depends_on('py-matplotlib', when='+analysis', type=('build', 'run'))
    depends_on('py-scipy', when='+analysis', type=('build', 'run'))
    depends_on('py-seaborn', when='+analysis', type=('build', 'run'))

    depends_on('py-netcdf4@1.0:', when='+amber', type=('build', 'run'))
    depends_on('hdf5', when='+amber', type=('run'))
