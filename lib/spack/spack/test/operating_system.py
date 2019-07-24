# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import spack.operating_systems.cnl as cnl


def test_read_cle_release_file(tmpdir, monkeypatch):
    """test reading the Cray cle-release file"""
    cle_release_path = tmpdir.join('cle-release')
    with cle_release_path.open('w') as f:
        f.write("""\
RELEASE=6.0.UP07
BUILD=6.0.7424
DATE=20190611
ARCH=noarch
NETWORK=ari
PATCHSET=35-201906112304
DUMMY=foo=bar
""")

    monkeypatch.setattr(cnl, '_cle_release_file', str(cle_release_path))
    attrs = cnl.read_cle_release_file()

    assert attrs['RELEASE'] == '6.0.UP07'
    assert attrs['BUILD'] == '6.0.7424'
    assert attrs['DATE'] == '20190611'
    assert attrs['ARCH'] == 'noarch'
    assert attrs['NETWORK'] == 'ari'
    assert attrs['PATCHSET'] == '35-201906112304'
    assert attrs['DUMMY'] == 'foo=bar'

    assert cnl.Cnl._detect_crayos_version() == 6
