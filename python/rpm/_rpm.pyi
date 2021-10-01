from __future__ import annotations
from collections.abc import Callable, Iterator
from typing import (
    Any, AnyStr, Dict, Final, List, Literal, NewType, Optional, overload,
    Protocol, Tuple, Type, Union
)

## Enumerated types.  We use subtypes of int where possible.  Those that are
## plain int are bitwise types.

rpmTag = NewType('rpmTag', int)
rpmRC = NewType('rpmRC', int)
rpmfileState = NewType('rpmfileState', int)
rpmProblemType = NewType('rpmProblemType', int)
rpmMireMode = NewType('rpmMireMode', int)
rpmDbiTag = NewType('rpmDbiTag', int)
headerConvOps = NewType('headerConvOps', int)

RPMTAG_NOT_FOUND: Final[rpmTag]
RPMTAG_HEADERIMAGE: Final[rpmTag]
RPMTAG_HEADERSIGNATURES: Final[rpmTag]
RPMTAG_HEADERIMMUTABLE: Final[rpmTag]
RPMTAG_HEADERREGIONS: Final[rpmTag]
RPMTAG_HEADERI18NTABLE: Final[rpmTag]
RPMTAG_SIGSIZE: Final[rpmTag]
RPMTAG_SIGPGP: Final[rpmTag]
RPMTAG_SIGMD5: Final[rpmTag]
RPMTAG_PKGID: Final[rpmTag]
RPMTAG_SIGGPG: Final[rpmTag]
RPMTAG_PUBKEYS: Final[rpmTag]
RPMTAG_DSAHEADER: Final[rpmTag]
RPMTAG_RSAHEADER: Final[rpmTag]
RPMTAG_SHA1HEADER: Final[rpmTag]
RPMTAG_HDRID: Final[rpmTag]
RPMTAG_LONGSIGSIZE: Final[rpmTag]
RPMTAG_LONGARCHIVESIZE: Final[rpmTag]
RPMTAG_SHA256HEADER: Final[rpmTag]
RPMTAG_NAME: Final[rpmTag]
RPMTAG_N: Final[rpmTag]
RPMTAG_VERSION: Final[rpmTag]
RPMTAG_V: Final[rpmTag]
RPMTAG_RELEASE: Final[rpmTag]
RPMTAG_R: Final[rpmTag]
RPMTAG_EPOCH: Final[rpmTag]
RPMTAG_E: Final[rpmTag]
RPMTAG_SUMMARY: Final[rpmTag]
RPMTAG_DESCRIPTION: Final[rpmTag]
RPMTAG_BUILDTIME: Final[rpmTag]
RPMTAG_BUILDHOST: Final[rpmTag]
RPMTAG_INSTALLTIME: Final[rpmTag]
RPMTAG_SIZE: Final[rpmTag]
RPMTAG_DISTRIBUTION: Final[rpmTag]
RPMTAG_VENDOR: Final[rpmTag]
RPMTAG_GIF: Final[rpmTag]
RPMTAG_XPM: Final[rpmTag]
RPMTAG_LICENSE: Final[rpmTag]
RPMTAG_PACKAGER: Final[rpmTag]
RPMTAG_GROUP: Final[rpmTag]
RPMTAG_SOURCE: Final[rpmTag]
RPMTAG_PATCH: Final[rpmTag]
RPMTAG_URL: Final[rpmTag]
RPMTAG_OS: Final[rpmTag]
RPMTAG_ARCH: Final[rpmTag]
RPMTAG_PREIN: Final[rpmTag]
RPMTAG_POSTIN: Final[rpmTag]
RPMTAG_PREUN: Final[rpmTag]
RPMTAG_POSTUN: Final[rpmTag]
RPMTAG_OLDFILENAMES: Final[rpmTag]
RPMTAG_FILESIZES: Final[rpmTag]
RPMTAG_FILESTATES: Final[rpmTag]
RPMTAG_FILEMODES: Final[rpmTag]
RPMTAG_FILERDEVS: Final[rpmTag]
RPMTAG_FILEMTIMES: Final[rpmTag]
RPMTAG_FILEDIGESTS: Final[rpmTag]
RPMTAG_FILEMD5S: Final[rpmTag]
RPMTAG_FILELINKTOS: Final[rpmTag]
RPMTAG_FILEFLAGS: Final[rpmTag]
RPMTAG_FILEUSERNAME: Final[rpmTag]
RPMTAG_FILEGROUPNAME: Final[rpmTag]
RPMTAG_ICON: Final[rpmTag]
RPMTAG_SOURCERPM: Final[rpmTag]
RPMTAG_FILEVERIFYFLAGS: Final[rpmTag]
RPMTAG_ARCHIVESIZE: Final[rpmTag]
RPMTAG_PROVIDENAME: Final[rpmTag]
RPMTAG_PROVIDES: Final[rpmTag]
RPMTAG_P: Final[rpmTag]
RPMTAG_REQUIREFLAGS: Final[rpmTag]
RPMTAG_REQUIRENAME: Final[rpmTag]
RPMTAG_REQUIRES: Final[rpmTag]
RPMTAG_REQUIREVERSION: Final[rpmTag]
RPMTAG_NOSOURCE: Final[rpmTag]
RPMTAG_NOPATCH: Final[rpmTag]
RPMTAG_CONFLICTFLAGS: Final[rpmTag]
RPMTAG_CONFLICTNAME: Final[rpmTag]
RPMTAG_CONFLICTS: Final[rpmTag]
RPMTAG_C: Final[rpmTag]
RPMTAG_CONFLICTVERSION: Final[rpmTag]
RPMTAG_EXCLUDEARCH: Final[rpmTag]
RPMTAG_EXCLUDEOS: Final[rpmTag]
RPMTAG_EXCLUSIVEARCH: Final[rpmTag]
RPMTAG_EXCLUSIVEOS: Final[rpmTag]
RPMTAG_RPMVERSION: Final[rpmTag]
RPMTAG_TRIGGERSCRIPTS: Final[rpmTag]
RPMTAG_TRIGGERNAME: Final[rpmTag]
RPMTAG_TRIGGERVERSION: Final[rpmTag]
RPMTAG_TRIGGERFLAGS: Final[rpmTag]
RPMTAG_TRIGGERINDEX: Final[rpmTag]
RPMTAG_VERIFYSCRIPT: Final[rpmTag]
RPMTAG_CHANGELOGTIME: Final[rpmTag]
RPMTAG_CHANGELOGNAME: Final[rpmTag]
RPMTAG_CHANGELOGTEXT: Final[rpmTag]
RPMTAG_PREINPROG: Final[rpmTag]
RPMTAG_POSTINPROG: Final[rpmTag]
RPMTAG_PREUNPROG: Final[rpmTag]
RPMTAG_POSTUNPROG: Final[rpmTag]
RPMTAG_BUILDARCHS: Final[rpmTag]
RPMTAG_OBSOLETENAME: Final[rpmTag]
RPMTAG_OBSOLETES: Final[rpmTag]
RPMTAG_O: Final[rpmTag]
RPMTAG_VERIFYSCRIPTPROG: Final[rpmTag]
RPMTAG_TRIGGERSCRIPTPROG: Final[rpmTag]
RPMTAG_COOKIE: Final[rpmTag]
RPMTAG_FILEDEVICES: Final[rpmTag]
RPMTAG_FILEINODES: Final[rpmTag]
RPMTAG_FILELANGS: Final[rpmTag]
RPMTAG_PREFIXES: Final[rpmTag]
RPMTAG_INSTPREFIXES: Final[rpmTag]
RPMTAG_SOURCEPACKAGE: Final[rpmTag]
RPMTAG_PROVIDEFLAGS: Final[rpmTag]
RPMTAG_PROVIDEVERSION: Final[rpmTag]
RPMTAG_OBSOLETEFLAGS: Final[rpmTag]
RPMTAG_OBSOLETEVERSION: Final[rpmTag]
RPMTAG_DIRINDEXES: Final[rpmTag]
RPMTAG_BASENAMES: Final[rpmTag]
RPMTAG_DIRNAMES: Final[rpmTag]
RPMTAG_ORIGDIRINDEXES: Final[rpmTag]
RPMTAG_ORIGBASENAMES: Final[rpmTag]
RPMTAG_ORIGDIRNAMES: Final[rpmTag]
RPMTAG_OPTFLAGS: Final[rpmTag]
RPMTAG_DISTURL: Final[rpmTag]
RPMTAG_PAYLOADFORMAT: Final[rpmTag]
RPMTAG_PAYLOADCOMPRESSOR: Final[rpmTag]
RPMTAG_PAYLOADFLAGS: Final[rpmTag]
RPMTAG_INSTALLCOLOR: Final[rpmTag]
RPMTAG_INSTALLTID: Final[rpmTag]
RPMTAG_REMOVETID: Final[rpmTag]
RPMTAG_PLATFORM: Final[rpmTag]
RPMTAG_PATCHESNAME: Final[rpmTag]
RPMTAG_PATCHESFLAGS: Final[rpmTag]
RPMTAG_PATCHESVERSION: Final[rpmTag]
RPMTAG_FILECOLORS: Final[rpmTag]
RPMTAG_FILECLASS: Final[rpmTag]
RPMTAG_CLASSDICT: Final[rpmTag]
RPMTAG_FILEDEPENDSX: Final[rpmTag]
RPMTAG_FILEDEPENDSN: Final[rpmTag]
RPMTAG_DEPENDSDICT: Final[rpmTag]
RPMTAG_SOURCEPKGID: Final[rpmTag]
RPMTAG_FILECONTEXTS: Final[rpmTag]
RPMTAG_FSCONTEXTS: Final[rpmTag]
RPMTAG_RECONTEXTS: Final[rpmTag]
RPMTAG_POLICIES: Final[rpmTag]
RPMTAG_PRETRANS: Final[rpmTag]
RPMTAG_POSTTRANS: Final[rpmTag]
RPMTAG_PRETRANSPROG: Final[rpmTag]
RPMTAG_POSTTRANSPROG: Final[rpmTag]
RPMTAG_DISTTAG: Final[rpmTag]
RPMTAG_OLDSUGGESTSNAME: Final[rpmTag]
RPMTAG_OLDSUGGESTS: Final[rpmTag]
RPMTAG_OLDSUGGESTSVERSION: Final[rpmTag]
RPMTAG_OLDSUGGESTSFLAGS: Final[rpmTag]
RPMTAG_OLDENHANCESNAME: Final[rpmTag]
RPMTAG_OLDENHANCES: Final[rpmTag]
RPMTAG_OLDENHANCESVERSION: Final[rpmTag]
RPMTAG_OLDENHANCESFLAGS: Final[rpmTag]
RPMTAG_DBINSTANCE: Final[rpmTag]
RPMTAG_NVRA: Final[rpmTag]
RPMTAG_FILENAMES: Final[rpmTag]
RPMTAG_FILEPROVIDE: Final[rpmTag]
RPMTAG_FILEREQUIRE: Final[rpmTag]
RPMTAG_TRIGGERCONDS: Final[rpmTag]
RPMTAG_TRIGGERTYPE: Final[rpmTag]
RPMTAG_ORIGFILENAMES: Final[rpmTag]
RPMTAG_LONGFILESIZES: Final[rpmTag]
RPMTAG_LONGSIZE: Final[rpmTag]
RPMTAG_FILECAPS: Final[rpmTag]
RPMTAG_FILEDIGESTALGO: Final[rpmTag]
RPMTAG_BUGURL: Final[rpmTag]
RPMTAG_EVR: Final[rpmTag]
RPMTAG_NVR: Final[rpmTag]
RPMTAG_NEVR: Final[rpmTag]
RPMTAG_NEVRA: Final[rpmTag]
RPMTAG_HEADERCOLOR: Final[rpmTag]
RPMTAG_VERBOSE: Final[rpmTag]
RPMTAG_EPOCHNUM: Final[rpmTag]
RPMTAG_PREINFLAGS: Final[rpmTag]
RPMTAG_POSTINFLAGS: Final[rpmTag]
RPMTAG_PREUNFLAGS: Final[rpmTag]
RPMTAG_POSTUNFLAGS: Final[rpmTag]
RPMTAG_PRETRANSFLAGS: Final[rpmTag]
RPMTAG_POSTTRANSFLAGS: Final[rpmTag]
RPMTAG_VERIFYSCRIPTFLAGS: Final[rpmTag]
RPMTAG_TRIGGERSCRIPTFLAGS: Final[rpmTag]
RPMTAG_POLICYNAMES: Final[rpmTag]
RPMTAG_POLICYTYPES: Final[rpmTag]
RPMTAG_POLICYTYPESINDEXES: Final[rpmTag]
RPMTAG_POLICYFLAGS: Final[rpmTag]
RPMTAG_VCS: Final[rpmTag]
RPMTAG_ORDERNAME: Final[rpmTag]
RPMTAG_ORDERVERSION: Final[rpmTag]
RPMTAG_ORDERFLAGS: Final[rpmTag]
RPMTAG_INSTFILENAMES: Final[rpmTag]
RPMTAG_REQUIRENEVRS: Final[rpmTag]
RPMTAG_PROVIDENEVRS: Final[rpmTag]
RPMTAG_OBSOLETENEVRS: Final[rpmTag]
RPMTAG_CONFLICTNEVRS: Final[rpmTag]
RPMTAG_FILENLINKS: Final[rpmTag]
RPMTAG_RECOMMENDNAME: Final[rpmTag]
RPMTAG_RECOMMENDS: Final[rpmTag]
RPMTAG_RECOMMENDVERSION: Final[rpmTag]
RPMTAG_RECOMMENDFLAGS: Final[rpmTag]
RPMTAG_SUGGESTNAME: Final[rpmTag]
RPMTAG_SUGGESTS: Final[rpmTag]
RPMTAG_SUGGESTVERSION: Final[rpmTag]
RPMTAG_SUGGESTFLAGS: Final[rpmTag]
RPMTAG_SUPPLEMENTNAME: Final[rpmTag]
RPMTAG_SUPPLEMENTS: Final[rpmTag]
RPMTAG_SUPPLEMENTVERSION: Final[rpmTag]
RPMTAG_SUPPLEMENTFLAGS: Final[rpmTag]
RPMTAG_ENHANCENAME: Final[rpmTag]
RPMTAG_ENHANCES: Final[rpmTag]
RPMTAG_ENHANCEVERSION: Final[rpmTag]
RPMTAG_ENHANCEFLAGS: Final[rpmTag]
RPMTAG_RECOMMENDNEVRS: Final[rpmTag]
RPMTAG_SUGGESTNEVRS: Final[rpmTag]
RPMTAG_SUPPLEMENTNEVRS: Final[rpmTag]
RPMTAG_ENHANCENEVRS: Final[rpmTag]
RPMTAG_ENCODING: Final[rpmTag]
RPMTAG_FILETRIGGERSCRIPTS: Final[rpmTag]
RPMTAG_FILETRIGGERSCRIPTPROG: Final[rpmTag]
RPMTAG_FILETRIGGERSCRIPTFLAGS: Final[rpmTag]
RPMTAG_FILETRIGGERNAME: Final[rpmTag]
RPMTAG_FILETRIGGERINDEX: Final[rpmTag]
RPMTAG_FILETRIGGERVERSION: Final[rpmTag]
RPMTAG_FILETRIGGERFLAGS: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERSCRIPTS: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERSCRIPTPROG: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERSCRIPTFLAGS: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERNAME: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERINDEX: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERVERSION: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERFLAGS: Final[rpmTag]
RPMTAG_FILETRIGGERPRIORITIES: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERPRIORITIES: Final[rpmTag]
RPMTAG_FILETRIGGERCONDS: Final[rpmTag]
RPMTAG_FILETRIGGERTYPE: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERCONDS: Final[rpmTag]
RPMTAG_TRANSFILETRIGGERTYPE: Final[rpmTag]
RPMTAG_FILESIGNATURES: Final[rpmTag]
RPMTAG_FILESIGNATURELENGTH: Final[rpmTag]
RPMTAG_PAYLOADDIGEST: Final[rpmTag]
RPMTAG_PAYLOADDIGESTALGO: Final[rpmTag]
RPMTAG_MODULARITYLABEL: Final[rpmTag]
RPMTAG_PAYLOADDIGESTALT: Final[rpmTag]

RPMRC_OK: Final[rpmRC]
RPMRC_NOTFOUND: Final[rpmRC]
RPMRC_FAIL: Final[rpmRC]
RPMRC_NOTTRUSTED: Final[rpmRC]
RPMRC_NOKEY: Final[rpmRC]

RPMFILE_STATE_NORMAL: Final[rpmfileState]
RPMFILE_STATE_REPLACED: Final[rpmfileState]
RPMFILE_STATE_NOTINSTALLED: Final[rpmfileState]
RPMFILE_STATE_NETSHARED: Final[rpmfileState]
RPMFILE_STATE_WRONGCOLOR: Final[rpmfileState]

# rpmfileAttrs
RPMFILE_CONFIG: Final[int]
RPMFILE_DOC: Final[int]
RPMFILE_ICON: Final[int]
RPMFILE_MISSINGOK: Final[int]
RPMFILE_NOREPLACE: Final[int]
RPMFILE_SPECFILE: Final[int]
RPMFILE_GHOST: Final[int]
RPMFILE_LICENSE: Final[int]
RPMFILE_README: Final[int]
RPMFILE_PUBKEY: Final[int]
RPMFILE_ARTIFACT: Final[int]

RPMDEP_SENSE_REQUIRES: Final[int]
RPMDEP_SENSE_CONFLICTS: Final[int]

# rpmsenseFlags
RPMSENSE_ANY: Final[int]
RPMSENSE_GREATER: Final[int]
RPMSENSE_LESS: Final[int]
RPMSENSE_EQUAL: Final[int]
RPMSENSE_POSTTRANS: Final[int]
RPMSENSE_PREREQ: Final[int]
RPMSENSE_PRETRANS: Final[int]
RPMSENSE_INTERP: Final[int]
RPMSENSE_SCRIPT_PRE: Final[int]
RPMSENSE_SCRIPT_POST: Final[int]
RPMSENSE_SCRIPT_PREUN: Final[int]
RPMSENSE_SCRIPT_POSTUN: Final[int]
RPMSENSE_SCRIPT_VERIFY: Final[int]
RPMSENSE_FIND_REQUIRES: Final[int]
RPMSENSE_FIND_PROVIDES: Final[int]
RPMSENSE_TRIGGERIN: Final[int]
RPMSENSE_TRIGGERUN: Final[int]
RPMSENSE_TRIGGERPOSTUN: Final[int]
RPMSENSE_MISSINGOK: Final[int]
RPMSENSE_RPMLIB: Final[int]
RPMSENSE_TRIGGERPREIN: Final[int]
RPMSENSE_KEYRING: Final[int]
RPMSENSE_CONFIG: Final[int]

# rpmtransFlags
RPMTRANS_FLAG_TEST: Final[int]
RPMTRANS_FLAG_BUILD_PROBS: Final[int]
RPMTRANS_FLAG_NOSCRIPTS: Final[int]
RPMTRANS_FLAG_JUSTDB: Final[int]
RPMTRANS_FLAG_NOTRIGGERS: Final[int]
RPMTRANS_FLAG_NODOCS: Final[int]
RPMTRANS_FLAG_ALLFILES: Final[int]
RPMTRANS_FLAG_NOPLUGINS: Final[int]
RPMTRANS_FLAG_NOCONTEXTS: Final[int]
RPMTRANS_FLAG_NOCAPS: Final[int]
RPMTRANS_FLAG_NOTRIGGERPREIN: Final[int]
RPMTRANS_FLAG_NOPRE: Final[int]
RPMTRANS_FLAG_NOPOST: Final[int]
RPMTRANS_FLAG_NOTRIGGERIN: Final[int]
RPMTRANS_FLAG_NOTRIGGERUN: Final[int]
RPMTRANS_FLAG_NOPREUN: Final[int]
RPMTRANS_FLAG_NOPOSTUN: Final[int]
RPMTRANS_FLAG_NOTRIGGERPOSTUN: Final[int]
RPMTRANS_FLAG_NOPRETRANS: Final[int]
RPMTRANS_FLAG_NOPOSTTRANS: Final[int]
RPMTRANS_FLAG_NOMD5: Final[int]
RPMTRANS_FLAG_NOFILEDIGEST: Final[int]
RPMTRANS_FLAG_NOARTIFACTS: Final[int]
RPMTRANS_FLAG_NOCONFIGS: Final[int]
RPMTRANS_FLAG_DEPLOOPS: Final[int]
RPMTRANS_FLAG_KEEPOBSOLETE: Final[int]
RPMTRANS_FLAG_REPACKAGE: Final[int]
RPMTRANS_FLAG_REVERSE: Final[int]
RPMTRANS_FLAG_NOSUGGEST: Final[int]
RPMTRANS_FLAG_ADDINDEPS: Final[int]

# rpmprobFilterFlags
RPMPROB_FILTER_IGNOREOS: Final[int]
RPMPROB_FILTER_IGNOREARCH: Final[int]
RPMPROB_FILTER_REPLACEPKG: Final[int]
RPMPROB_FILTER_FORCERELOCATE: Final[int]
RPMPROB_FILTER_REPLACENEWFILES: Final[int]
RPMPROB_FILTER_REPLACEOLDFILES: Final[int]
RPMPROB_FILTER_OLDPACKAGE: Final[int]
RPMPROB_FILTER_DISKSPACE: Final[int]
RPMPROB_FILTER_DISKNODES: Final[int]
RPMPROB_FILTER_VERIFY: Final[int]

# rpmCallbackType
RPMCALLBACK_UNKNOWN: Final[int]
RPMCALLBACK_INST_PROGRESS: Final[int]
RPMCALLBACK_INST_START: Final[int]
RPMCALLBACK_INST_OPEN_FILE: Final[int]
RPMCALLBACK_INST_CLOSE_FILE: Final[int]
RPMCALLBACK_TRANS_PROGRESS: Final[int]
RPMCALLBACK_TRANS_START: Final[int]
RPMCALLBACK_TRANS_STOP: Final[int]
RPMCALLBACK_UNINST_PROGRESS: Final[int]
RPMCALLBACK_UNINST_START: Final[int]
RPMCALLBACK_UNINST_STOP: Final[int]
RPMCALLBACK_REPACKAGE_PROGRESS: Final[int]
RPMCALLBACK_REPACKAGE_START: Final[int]
RPMCALLBACK_REPACKAGE_STOP: Final[int]
RPMCALLBACK_UNPACK_ERROR: Final[int]
RPMCALLBACK_CPIO_ERROR: Final[int]
RPMCALLBACK_SCRIPT_ERROR: Final[int]
RPMCALLBACK_SCRIPT_START: Final[int]
RPMCALLBACK_SCRIPT_STOP: Final[int]
RPMCALLBACK_INST_STOP: Final[int]
RPMCALLBACK_ELEM_PROGRESS: Final[int]
RPMCALLBACK_VERIFY_PROGRESS: Final[int]
RPMCALLBACK_VERIFY_START: Final[int]
RPMCALLBACK_VERIFY_STOP: Final[int]

RPMPROB_BADARCH: Final[rpmProblemType]
RPMPROB_BADOS: Final[rpmProblemType]
RPMPROB_PKG_INSTALLED: Final[rpmProblemType]
RPMPROB_BADRELOCATE: Final[rpmProblemType]
RPMPROB_REQUIRES: Final[rpmProblemType]
RPMPROB_CONFLICT: Final[rpmProblemType]
RPMPROB_NEW_FILE_CONFLICT: Final[rpmProblemType]
RPMPROB_FILE_CONFLICT: Final[rpmProblemType]
RPMPROB_OLDPACKAGE: Final[rpmProblemType]
RPMPROB_DISKSPACE: Final[rpmProblemType]
RPMPROB_DISKNODES: Final[rpmProblemType]
RPMPROB_OBSOLETES: Final[rpmProblemType]
RPMPROB_VERIFY: Final[rpmProblemType]

# rpmlogLvl: should be bitwise ORd with a log facility, but the facility
# constants are not exposed to python
RPMLOG_EMERG: Final[int]
RPMLOG_ALERT: Final[int]
RPMLOG_CRIT: Final[int]
RPMLOG_ERR: Final[int]
RPMLOG_WARNING: Final[int]
RPMLOG_NOTICE: Final[int]
RPMLOG_INFO: Final[int]
RPMLOG_DEBUG: Final[int]

RPMMIRE_DEFAULT: Final[rpmMireMode]
RPMMIRE_STRCMP: Final[rpmMireMode]
RPMMIRE_REGEX: Final[rpmMireMode]
RPMMIRE_GLOB: Final[rpmMireMode]

# rpmVSFlags
RPMVSF_DEFAULT: Final[int]
RPMVSF_NOHDRCHK: Final[int]
RPMVSF_NEEDPAYLOAD: Final[int]
RPMVSF_NOSHA1HEADER: Final[int]
RPMVSF_NOSHA256HEADER: Final[int]
RPMVSF_NODSAHEADER: Final[int]
RPMVSF_NORSAHEADER: Final[int]
RPMVSF_NOPAYLOAD: Final[int]
RPMVSF_NOMD5: Final[int]
RPMVSF_NODSA: Final[int]
RPMVSF_NORSA: Final[int]
RPMVSF_MASK_NODIGESTS: Final[int]
_RPMVSF_NODIGESTS: Final[int]
RPMVSF_MASK_NOSIGNATURES: Final[int]
_RPMVSF_NOSIGNATURES: Final[int]
RPMVSF_MASK_NOHEADER: Final[int]
_RPMVSF_NOHEADER: Final[int]
RPMVSF_MASK_NOPAYLOAD: Final[int]
_RPMVSF_NOPAYLOAD: Final[int]

RPMSIG_NONE_TYPE: Final[int]
RPMSIG_DIGEST_TYPE: Final[int]
RPMSIG_SIGNATURE_TYPE: Final[int]
RPMSIG_VERIFIABLE_TYPE: Final[int]
RPMSIG_UNVERIFIED_TYPE: Final[int]

# rpmElementType
TR_ADDED: Final[int]
TR_REMOVED: Final[int]
TR_RPMDB: Final[int]

RPMDBI_PACKAGES: Final[rpmDbiTag]
RPMDBI_LABEL: Final[rpmDbiTag]
RPMDBI_NAME: Final[rpmDbiTag]
RPMDBI_BASENAMES: Final[rpmDbiTag]
RPMDBI_GROUP: Final[rpmDbiTag]
RPMDBI_REQUIRENAME: Final[rpmDbiTag]
RPMDBI_PROVIDENAME: Final[rpmDbiTag]
RPMDBI_CONFLICTNAME: Final[rpmDbiTag]
RPMDBI_OBSOLETENAME: Final[rpmDbiTag]
RPMDBI_TRIGGERNAME: Final[rpmDbiTag]
RPMDBI_DIRNAMES: Final[rpmDbiTag]
RPMDBI_INSTALLTID: Final[rpmDbiTag]
RPMDBI_SIGMD5: Final[rpmDbiTag]
RPMDBI_SHA1HEADER: Final[rpmDbiTag]
RPMDBI_INSTFILENAMES: Final[rpmDbiTag]

HEADERCONV_EXPANDFILELIST: Final[headerConvOps]
HEADERCONV_COMPRESSFILELIST: Final[headerConvOps]
HEADERCONV_RETROFIT_V3: Final[headerConvOps]

# rpmVerifyAttrs
RPMVERIFY_NONE: Final[int]
RPMVERIFY_FILEDIGEST: Final[int]
RPMVERIFY_FILESIZE: Final[int]
RPMVERIFY_LINKTO: Final[int]
RPMVERIFY_USER: Final[int]
RPMVERIFY_GROUP: Final[int]
RPMVERIFY_MTIME: Final[int]
RPMVERIFY_MODE: Final[int]
RPMVERIFY_RDEV: Final[int]
RPMVERIFY_CAPS: Final[int]
RPMVERIFY_READLINKFAIL: Final[int]
RPMVERIFY_READFAIL: Final[int]
RPMVERIFY_LSTATFAIL: Final[int]

# rpmSourceFlags
RPMBUILD_ISSOURCE: Final[int]
RPMBUILD_ISPATCH: Final[int]
RPMBUILD_ISICON: Final[int]
RPMBUILD_ISNO: Final[int]

# rpmBuildFlags
RPMBUILD_NONE: Final[int]
RPMBUILD_PREP: Final[int]
RPMBUILD_BUILD: Final[int]
RPMBUILD_INSTALL: Final[int]
RPMBUILD_CHECK: Final[int]
RPMBUILD_CLEAN: Final[int]
RPMBUILD_FILECHECK: Final[int]
RPMBUILD_PACKAGESOURCE: Final[int]
RPMBUILD_PACKAGEBINARY: Final[int]
RPMBUILD_RMSOURCE: Final[int]
RPMBUILD_RMBUILD: Final[int]
RPMBUILD_RMSPEC: Final[int]

# rpmBuildPkgFlags
RPMBUILD_PKG_NONE: Final[int]
RPMBUILD_PKG_NODIRTOKENS: Final[int]

# rpmSpecFlags
RPMSPEC_NONE: Final[int]
RPMSPEC_ANYARCH: Final[int]
RPMSPEC_FORCE: Final[int]
RPMSPEC_NOLANG: Final[int]

## Classes
class error(Exception): ...

AnyVer = Union[str, Tuple[Optional[str], str, Optional[str]]]

class ver:
    def __init__(self, evr: AnyVer) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

    e: Final[Optional[str]] = ...
    v: Final[str] = ...
    r: Final[Optional[str]] = ...
    evr: Final[str] = ...

class strpool:
    def __init__(self) -> None: ...
    def __getitem__(self, index: int) -> str: ...
    def __len__(self) -> int: ...
    def str2id(self, str: str, create: bool = ...) -> int: ...
    def id2str(self, id: int) -> str: ...
    def freeze(self, keephash: bool = ...) -> None: ...
    def unfreeze(self) -> None: ...

class _HasFileno(Protocol):
    def fileno(self) -> int: ...

_FileObject = Union[int, _HasFileno]
AnyFD = Union[_FileObject, AnyStr]

class fd:
    @classmethod
    def open(self, obj: AnyFD, mode: str = ..., flags: str = ...) -> fd: ...

    def __init__(self, obj: AnyFD, mode: str = ...,
                 flags: str = ...) -> None: ...
    def close(self) -> None: ...
    def fileno(self) -> int: ...
    def flush(self) -> None: ...
    def isatty(self) -> bool: ...
    def seek(self, offset: int, whence: int = ...) -> None: ...
    def tell(self) -> int: ...
    def read(self, size: int = ...) -> bytes: ...
    def write(self, buffer: AnyStr) -> int: ...

    closed: bool = ...
    name: Final[str] = ...
    mode: Final[str] = ...
    flags: Final[str] = ...

AnyTag = Union[rpmTag, AnyStr]
AnyFDOrHdr = Union[AnyFD, hdr, None]

class hdr:
    def __init__(self, obj: AnyFDOrHdr = ...) -> None: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[rpmTag]: ...
    def __next__(self) -> rpmTag: ...
    def __contains__(self, tag: AnyTag) -> bool: ...
    def __getitem__(self, tag: AnyTag) -> Any: ...
    def __setitem__(self, tag: AnyTag, value: Any) -> None: ...
    def __delitem__(self, tag: AnyTag) -> None: ...
    def __reduce__(self) -> Tuple[Type[hdr], bytes]: ...
    @overload
    def __getattr__(self, attr: Union[rpmTag, bytes]) -> Union[int, AnyStr]: ...
    @overload
    def __getattr__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, value: Any) -> Any: ...
    def __delattr__(self, attr: str) -> None: ...
    def keys(self) -> List[rpmTag]: ...
    def unload(self) -> bytes: ...
    def expandFilelist(self) -> None: ...
    def compressFilelist(self) -> None: ...
    def fullFilelist(self) -> None: ...
    def format(self, format: str) -> str: ...
    def sprintf(self, format: str) -> str: ...
    def isSource(self) -> bool: ...
    def convert(self, op: headerConvOps = ...) -> bool: ...
    def write(self, file: AnyFD, magic: bool = ...) -> None: ...
    def fiFromHeader(self) -> "fi": ...
    def dsFromHeader(self, to: AnyTag = ..., flags: int = ...) -> "ds": ...
    def dsOfHeader(self) -> "ds": ...

class file:
    def matches(self, other: file) -> bool: ...
    def verify(self, omitMask: int = ...) -> int: ...

    fx: Final[int] = ...
    dx: Final[int] = ...
    name: Final[str] = ...
    basename: Final[Optional[str]] = ...
    dirname: Final[Optional[str]] = ...
    orig_name: Final[str] = ...
    orig_basename: Final[Optional[str]] = ...
    orig_dirname: Final[Optional[str]] = ...
    mode: Final[int] = ...
    size: Final[int] = ...
    mtime: Final[int] = ...
    rdev: Final[int] = ...
    inode: Final[int] = ...
    nlink: Final[int] = ...
    linkto: Final[Optional[str]] = ...
    user: Final[Optional[str]] = ...
    group: Final[Optional[str]] = ...
    fflags: Final[int] = ...
    vflags: Final[int] = ...
    color: Final[int] = ...
    state: Final[rpmfileState] = ...
    digest: Final[Optional[str]] = ...
    # mypy does not like this field.
    # If the name is class, it says: "error: invalid syntax".
    # If the name is "class", it says: "error: illegal target for annotation".
    # class: Final[str] = ...
    caps: Final[Optional[str]] = ...
    langs: Final[Optional[str]] = ...
    links: Final[Optional[Tuple[file, ...]]] = ...

class archive:
    def __iter__(self) -> Iterator[file]: ...
    def __next__(self) -> file: ...
    def tell(self) -> int: ...
    def close(self) -> None: ...
    def hascontent(self) -> Literal[0, 1]: ...
    def read(self, size: int = ...) -> bytes: ...
    def write(self, buffer: AnyStr) -> int: ...
    def readto(self, fd: AnyFD, nodigest: bool = ...) -> None: ...
    def writeto(self, fd: AnyFD) -> None: ...

class files:
    def __init__(self, header: hdr, tag: Any = ..., flags: int = ...,
                 pool: strpool = ...) -> None: ...
    def __contains__(self, fil: str) -> bool: ...
    @overload
    def __getitem__(self, index: Union[int, AnyStr]) -> file: ...
    @overload
    def __getitem__(self, index: slice) -> Tuple[file]: ...
    def __len__(self) -> int: ...
    def find(self, filename: str, orig: bool = ...) -> Optional[file]: ...
    def archive(self, fd: AnyFD, write: bool = ...) -> archive: ...

FileTuple = Tuple[Optional[str], int, int, int, int, int, int, int, int, int,
                  Optional[str], Optional[str], Optional[str]]

class fi:
    def __init__(self, header: hdr, tag: Any = ..., flags: int = ...,
                 pool: strpool = ...) -> None: ...
    def __iter__(self) -> Iterator[FileTuple]: ...
    def __next__(self) -> FileTuple: ...
    def __getitem__(self, index: int) -> Optional[str]: ...
    def __len__(self) -> int: ...
    def FC(self) -> int: ...
    def FX(self) -> int: ...
    def DC(self) -> int: ...
    def DX(self) -> int: ...
    def BN(self) -> Optional[str]: ...
    def DN(self) -> Optional[str]: ...
    def FN(self) -> Optional[str]: ...
    def FindFN(self, filename: bytes) -> int: ...
    def FFlags(self) -> int: ...
    def VFlags(self) -> int: ...
    def FMode(self) -> int: ...
    def FState(self) -> rpmfileState: ...
    def Digest(self) -> Optional[str]: ...
    def MD5(self) -> Optional[str]: ...
    def FLink(self) -> Optional[str]: ...
    def FSize(self) -> int: ...
    def FRdev(self) -> int: ...
    def FMtime(self) -> int: ...
    def FUser(self) -> Optional[str]: ...
    def FGroup(self) -> Optional[str]: ...
    def FColor(self) -> int: ...
    def FClass(self) -> str: ...
    def FLinks(self) -> Tuple[int, ...]: ...

class ds:
    def __init__(self, obj: Union[hdr, Tuple[str], Tuple[str, int, str]],
                 tag: AnyTag, pool: strpool = ...) -> None: ...
    def __iter__(self) -> Iterator[ds]: ...
    def __next__(self) -> ds: ...
    def __getitem__(self, index: int) -> Optional[str]: ...
    def __len__(self) -> int: ...
    def Count(self) -> int: ...
    def Ix(self) -> int: ...
    def DNEVR(self) -> str: ...
    def N(self) -> Optional[str]: ...
    def EVR(self) -> Optional[str]: ...
    def Flags(self) -> int: ...
    def TagN(self) -> rpmTag: ...
    def Color(self) -> int: ...
    def IsWeak(self) -> bool: ...
    def IsRich(self) -> bool: ...
    def IsReverse(self) -> bool: ...
    def SetNoPromote(self, noPromote: int) -> int: ...
    def Sort(self) -> None: ...
    def Find(self, ods: ds) -> int: ...
    def Merge(self, ods: ds) -> int: ...
    def Search(self, ods: ds) -> int: ...
    def Compare(self, ods: ds) -> bool: ...
    def Instance(self) -> int: ...
    def Rpmlib(self, pool: strpool = ...) -> ds: ...

class pubkey:
    def __init__(self, key: bytes) -> None: ...
    def base64(self) -> str: ...

class keyring:
    def __init__(self) -> None: ...
    def addKey(self, key: pubkey) -> Literal[-1, 0]: ...

class ii:
    def __iter__(self) -> Iterator[Union[int, AnyStr]]: ...
    def __next__(self) -> Union[int, AnyStr]: ...
    def __bool__(self) -> bool: ...
    def instances(self) -> List[Tuple[int, int]]: ...

class mi:
    def __iter__(self) -> Iterator[hdr]: ...
    def __next__(self) -> hdr: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def instance(self) -> int: ...
    def count(self) -> int: ...
    def pattern(self, TagN: AnyTag, mire_type: rpmMireMode,
                pattern: str) -> None: ...

class prob:
    type: Final[rpmProblemType] = ...
    pkgNEVR: Final[Optional[str]] = ...
    altNEVR: Final[Optional[str]] = ...
    key: Final[Any] = ...
    _str: Final[str] = ...
    _num: Final[int] = ...

class te:
    def Type(self) -> int: ...
    def N(self) -> str: ...
    def E(self) -> Optional[str]: ...
    def V(self) -> str: ...
    def R(self) -> str: ...
    def A(self) -> Optional[str]: ...
    def O(self) -> Optional[str]: ...
    def NEVR(self) -> Optional[str]: ...
    def NEVRA(self) -> Optional[str]: ...
    def Color(self) -> int: ...
    def PkgFileSize(self) -> int: ...
    def Parent(self) -> Optional[te]: ...
    def Failed(self) -> int: ...
    def Problems(self) -> List[prob]: ...
    def DBOffset(self) -> int: ...
    def Key(self) -> Any: ...
    def SetUserdata(self, data: Any) -> None: ...
    def Userdata(self) -> Any: ...
    def DS(self, tag: AnyTag) -> ds: ...
    def FI(self) -> Optional[fi]: ...
    def Files(self) -> Optional[files]: ...
    def Verified(self) -> int: ...

tsCheckCb = Callable[[ts, rpmTag, str, str, int], int]
tsRunCb = Union[Callable[[int, int, int, Optional[str], Any], int],
                Callable[[te, int, int, int, Any], int]]

class ts:
    def __init__(self, rootdir: str = ..., vsflags: int = ...) -> None: ...
    def __iter__(self) -> Iterator[te]: ...
    def __next__(self) -> te: ...
    def addInstall(self, hdr: hdr, data: Any, mode: int) -> bool: ...
    def addReinstall(self, hdr: hdr, data: Any) -> bool: ...
    def addErase(self, hdr: hdr) -> bool: ...
    def check(self, callback: tsCheckCb) -> bool: ...
    def order(self) -> int: ...
    def clean(self) -> None: ...
    def clear(self) -> None: ...
    def openDB(self) -> int: ...
    def closeDB(self) -> int: ...
    def initDB(self) -> int: ...
    def rebuildDB(self) -> int: ...
    def verifyDB(self) -> int: ...
    def dbCookie(self) -> str: ...
    def hdrFromFdno(self, fdno: AnyFD) -> Tuple[rpmRC, hdr]: ...
    def hdrCheck(self, hdrblob: bytes) -> Tuple[rpmRC, Optional[str]]: ...
    def pgpPrtPkts(self, octets: bytes) -> int: ...
    def pgpImportPubkey(self, pubkey: bytes) -> int: ...
    def setKeyring(self, keyring: Optional[keyring]) -> bool: ...
    def getKeyring(self, autoload: bool = ...) -> Optional[keyring]: ...
    def problems(self) -> List[prob]: ...
    def run(self, callback: tsRunCb, data: Any, ignoreSet: int) -> int: ...
    def dbMatch(self, tagNumber: rpmDbiTag = ..., key: Union[int, AnyStr] = ...) -> mi: ...
    def dbIndex(self, tag: Union[rpmDbiTag, AnyTag]) -> ii: ...

    cbStyle: int = ...
    scriptFd: Optional[AnyFD] = ...
    tid: Final[int] = ...
    rootDir: Final[Optional[str]] = ...
    _color: int = ...
    _prefcolor: int = ...
    _flags: int = ...
    _vsflags: int = ...
    _vfyflags: int = ...
    _vfylevel: int = ...

class specPkg:
    header: Final[hdr] = ...
    fileFile: Final[Optional[str]] = ...
    fileList: Final[Optional[str]] = ...
    policyList: Final[Optional[str]] = ...

class spec:
    def __init__(self, specfile: str, flags: int = ...) -> None: ...
    def _doBuild(self, ts: ts, buildAmount: int, pkgFlags: int = ...) -> bool: ...

    sources: Final[List[Tuple[Optional[str], int, int]]] = ...
    parsed: Final[Optional[str]] = ...
    prep: Final[Optional[str]] = ...
    build: Final[Optional[str]] = ...
    install: Final[Optional[str]] = ...
    check: Final[Optional[str]] = ...
    clean: Final[Optional[str]] = ...
    packages: Final[List[specPkg]] = ...
    sourceHeader: Final[hdr] = ...

## Functions

def addMacro(name: str, value: str) -> None: ...
def delMacro(name: str) -> None: ...
def expandMacro(macro: str, numeric: int = ...) -> Union[int, str, None]: ...
def archscore(archname: str) -> int: ...
def signalCaught(signo: int) -> bool: ...
def checkSignals() -> int: ...
def blockSignals(block: bool) -> int: ...
def mergeHeaderListFromFD(list: List[hdr], fd: int, matchTag: rpmTag) -> None: ...
def log(code: int, msg: str) -> None: ...
def setLogFile(file: Optional[_FileObject]) -> None: ...
def versionCompare(version0: hdr, version1: hdr) -> Literal[-1, 0, 1]: ...
def labelCompare(version0: AnyVer, version1: AnyVer) -> Literal[-1, 0, 1]: ...
def setVerbosity(level: int) -> None: ...
def setStats(stats: int) -> None: ...
def reloadConfig(target: str = ...) -> bool: ...
def setInterruptSafety(on: Any = ...) -> None: ...
def addSign(path: str, keyid: str = ..., hashalgo: int = ...) -> bool: ...
def delSign(path: str, keyid: str = ..., hashalgo: int = ...) -> bool: ...

## Global variables
__version__: Final[str]
tagnames: Final[Dict[rpmTag, str]]
header_magic: Final[bytes]