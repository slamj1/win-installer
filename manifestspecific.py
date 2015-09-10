# Copyright (c) Citrix Systems Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided
# that the following conditions are met:
#
# *   Redistributions of source code must retain the above
#     copyright notice, this list of conditions and the
#     following disclaimer.
# *   Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the
#     following disclaimer in the documentation and/or other
#     materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

secureserver = r'\\10.80.13.10\distfiles\distfiles\WindowsBuilds'
localserver = r'\\camos.uk.xensource.com\build\windowsbuilds\WindowsBuilds'

build_tar_source_files = {
       "xenbus" : r'xenbus-patchq.git\41\xenbus.tar',
       "xenvif" : r'xenvif-patchq.git\34\xenvif.tar',
       "xennet" : r'xennet-patchq.git\19\xennet.tar',
       "xeniface" : r'xeniface-patchq.git\10\xeniface.tar',
       "xenvbd" : r'xenvbd-patchq.git\107\xenvbd.tar',
       "xenguestagent" : r'xenguestagent.git\141\xenguestagent.tar',
       "xenvss" : r'standard-lcm\16\xenvss-7.tar',
}

all_drivers_signed = False
