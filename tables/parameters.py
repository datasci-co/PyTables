########################################################################
#
#       License: BSD
#       Created: February 25, 2005
#       Author:  Ivan Vilata - reverse:net.selidor@ivan
#
#       $Id$
#
########################################################################

"""
Parameters for PyTables.

Misc variables:

`__docformat__`
    The format of documentation strings in this module.
`__version__`
    Repository version of this file.
"""

from tables._parameters_common import _KB, _MB

try:
    from tables._parameters_pro import *
except ImportError:
    pass


__docformat__ = 'reStructuredText'
"""The format of documentation strings in this module."""

__version__ = '$Revision$'
"""Repository version of this file."""


# Mutable parameters
# ==================
# Be careful when touching these!

# Recommended values for maximum number of groups and maximum depth in tree.
# However, these limits are somewhat arbitrary and can be increased.
MAX_TREE_DEPTH = 2048
"""Maximum depth tree allowed in PyTables."""

MAX_GROUP_WIDTH = 4096
"""Maximum allowed number of children hanging from a group."""

MAX_NODE_ATTRS = 4096
"""Maximum allowed number of attributes in a node."""

MAX_UNDO_PATH_LENGTH = 10240
"""Maximum length of paths allowed in undo/redo operations."""

# Size of cache for new metadata cache system in HDF5 1.8.x
METADATA_CACHE_SIZE = 1*_MB  # 1 MB is the default for HDF5
"""Size (in bytes) of the HDF5 metadata cache."""

##########################################################################
# In the next parameters, a value of 0 in XXXX_MAX_SLOTS disables the cache
##########################################################################

# NODE_MAX_SLOTS tells the number of nodes that fits in the cache.
#
# There are several forces driving the election of this number:
# 1.- As more nodes, better chances to re-use nodes
#     --> better performance
# 2.- As more nodes, the re-ordering of the LRU cache takes more time
#     --> less performance
# 3.- As more nodes, the memory needs for PyTables grows, specially for table
#     writings (that could take double of memory than table reads!).
#
# Some experiments has been carried out with an AMD Duron processor with
# 256 KB of secondary cache. For processors with more secondary cache
# this can be bettered. Also, if lrucache could be bettered
# (mainly the comparison code), the CPU consumption would be improved.
#
# The next experiment is for browsing a group with 1000 tables.  Look at
# bench/LRU-experiment*.py for the bench code.  In general, retrieving a
# table from LRU cache is almost 20x times faster than re-loading the
# table from disk (0.4ms vs 7.4ms). For arrays, retrieving from cache is
# 2x faster than re-loading from disk (0.4ms vs 1.0ms). These tests has
# been conducted on a Duron platform, but for faster platforms these
# speed-ups will probably increase.
#
# Warning: This cache size must not be lower than the number of indexes on
# every table that the user is dealing with. So keep this 128 or 256 at very
# least.
#
# The default value here is quite conservative. If you have a system
# with tons of memory, and if you are touching regularly a very large
# number of leaves, try increasing this value and see if it fits better for
# you. Please give us your feedback.
#
# F. Alted 2005-10-31

#NODE_MAX_SLOTS =  1    # 24 MB, 38.6 s
#NODE_MAX_SLOTS =  2    # 24 MB, 38.9 s
#NODE_MAX_SLOTS =  4    # 24 MB, 39.1 s
#NODE_MAX_SLOTS =  8    # 25 MB, 39.2 s
#NODE_MAX_SLOTS = 16    # 26 MB, 39.9 s
#NODE_MAX_SLOTS = 32    # 28 MB, 40.9 s
#NODE_MAX_SLOTS = 64    # 30 MB, 41.1 s
#NODE_MAX_SLOTS = 128   # 35 MB, 41.6 s        , 60 MB for writes (!)
# NODE_MAX_SLOTS = 256   # 42 MB, 42.3s, opt:40.9s , 64 MB for writes
#                         # This is a good compromise between CPU and memory
#                         # consumption.

NODE_MAX_SLOTS = 256
"""Maximum number of unreferenced nodes to be kept in memory.

If positive, this is the number of *unreferenced* nodes to be kept in
the metadata cache. Least recently used nodes are unloaded from memory
when this number of loaded nodes is reached. To load a node again,
simply access it as usual. Nodes referenced by user variables are not
taken into account nor unloaded.

Negative value means that all the touched nodes will be kept in an
internal dictionary.  This is the faster way to load/retrieve nodes.
However, and in order to avoid a large memory comsumption, the user will
be warned when the number of loaded nodes will reach the
``-nodeChacheSize`` value.

A value of zero means that any cache mechanism is disabled.
"""

# *********************** IMPORTANT NOTE ***************************
# There are some situations, like moving indexed tables,
# (test_indexes:BasicReadTestCase.test10[a|b]_moveIndex checks this)
# where a low value of NODE_MAX_SLOTS gives problems.  Although this is
# not grave at all, it should be addressed sooner or later.
# ******************************************************************

#NODE_MAX_SLOTS = 512   # 59 MB, 43.9s, opt: 41.8s
#NODE_MAX_SLOTS = 1024  # 52 MB, 85.1s, opt: 17.0s # everything fits on cache!
#NODE_MAX_SLOTS = 2048  # 52 MB, XXXs, opt: 17.0s # everything fits on cache!
################################################################3
# Experiments with a Pentium IV with 512 KB of secondary cache
#NODE_MAX_SLOTS = 1500  # 30.1 s
#NODE_MAX_SLOTS = 1900  # 30.3 s
#NODE_MAX_SLOTS = 2000  # > 200 s
#NODE_MAX_SLOTS = 2046  # Takes lots of time! > 200 s
#NODE_MAX_SLOTS = MAX_GROUP_WIDTH  # that would be ideal, but takes ages!

# The maximum recommended number of columns in a table.
# However, this limit is somewhat arbitrary and can be increased.
MAX_COLUMNS = 512
"""Maximum number of columns in ``Table`` objects before a
``PerformanceWarning`` is issued.
"""

TABLE_MAX_SIZE = 1*_MB
"""The maximum size for table rows cached during table reads."""

EXPECTED_ROWS_TABLE = 10000
"""Default expected number of rows for ``Table`` objects."""

EXPECTED_ROWS_EARRAY = 1000
"""Default expected number of rows for ``EArray`` objects."""

#CHUNKTIMES = 4  # Makes large seq writings and reads quite fast (4.96 Mrw/s)
CHUNKTIMES = 8   # Makes large seq writings and reads very fast (5.30 Mrw/s)
#CHUNKTIMES = 16   # Makes large seq writings and reads very fast (5.30 Mrw/s)
"""The buffersize/chunksize ratio for chunked datasets."""

BUFFERTIMES = 100
"""The maximum buffersize/rowsize ratio before issuing a PerformanceWarning."""

## Local Variables:
## mode: python
## py-indent-offset: 4
## tab-width: 4
## fill-column: 72
## End:
