# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_load_name (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (xx)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (101)
+             12 LOAD_CONST               2 ('xx')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               3 (0)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              1 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               5 (1)
+             36 LOAD_CONST               0 (None)
+             38 LOAD_CONST               5 (1)
+             40 LOAD_CONST               3 (0)
+             42 LOAD_CONST               6 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 POP_TOP
              52 LOAD_CONST               0 (None)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               7 (100)
+             64 LOAD_CONST               0 (None)
+             66 LOAD_CONST               8 (2)
+             68 LOAD_CONST               3 (0)
+             70 LOAD_CONST               4 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               1
+             80 DUP_TOP
+             82 LOAD_GLOBAL              1 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST               9 (83)
+             88 LOAD_CONST               0 (None)
+             90 LOAD_CONST              10 (3)
+             92 LOAD_CONST               3 (0)
+             94 LOAD_CONST               6 (False)
+             96 CALL_FUNCTION            6
+             98 POP_TOP
+            100 UNPACK_SEQUENCE          1
             102 RETURN_VALUE
'''

snapshots['test_store_name (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               4 (90)
+             36 LOAD_CONST               5 ('x')
+             38 LOAD_CONST               0 (1)
+             40 LOAD_CONST               2 (0)
+             42 LOAD_CONST               6 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_NAME               1 (x)
              52 LOAD_CONST               7 (None)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               7 (None)
+             66 LOAD_CONST               8 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               1
+             80 DUP_TOP
+             82 LOAD_GLOBAL              0 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST               9 (83)
+             88 LOAD_CONST               7 (None)
+             90 LOAD_CONST              10 (3)
+             92 LOAD_CONST               2 (0)
+             94 LOAD_CONST               6 (False)
+             96 CALL_FUNCTION            6
+             98 POP_TOP
+            100 UNPACK_SEQUENCE          1
             102 RETURN_VALUE
'''

snapshots['test_load_attr (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (101)
+             12 LOAD_CONST               2 ('x')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               3 (0)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              1 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               5 (106)
+             36 LOAD_CONST               6 ('a')
+             38 LOAD_CONST               7 (1)
+             40 LOAD_CONST               3 (0)
+             42 LOAD_CONST               8 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 LOAD_ATTR                2 (a)
+             52 BUILD_LIST               1
+             54 DUP_TOP
+             56 LOAD_GLOBAL              1 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               5 (106)
+             62 LOAD_CONST               6 ('a')
+             64 LOAD_CONST               7 (1)
+             66 LOAD_CONST               3 (0)
+             68 LOAD_CONST               4 (True)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 UNPACK_SEQUENCE          1
+             76 BUILD_LIST               1
+             78 DUP_TOP
+             80 LOAD_GLOBAL              1 (py_instrument_receiver)
+             82 ROT_TWO
+             84 LOAD_CONST               7 (1)
+             86 LOAD_CONST               0 (None)
+             88 LOAD_CONST               9 (2)
+             90 LOAD_CONST               3 (0)
+             92 LOAD_CONST               8 (False)
+             94 CALL_FUNCTION            6
+             96 POP_TOP
+             98 UNPACK_SEQUENCE          1
             100 POP_TOP
             102 LOAD_CONST               0 (None)
+            104 BUILD_LIST               1
+            106 DUP_TOP
+            108 LOAD_GLOBAL              1 (py_instrument_receiver)
+            110 ROT_TWO
+            112 LOAD_CONST              10 (100)
+            114 LOAD_CONST               0 (None)
+            116 LOAD_CONST              11 (3)
+            118 LOAD_CONST               3 (0)
+            120 LOAD_CONST               4 (True)
+            122 CALL_FUNCTION            6
+            124 POP_TOP
+            126 UNPACK_SEQUENCE          1
+            128 BUILD_LIST               1
+            130 DUP_TOP
+            132 LOAD_GLOBAL              1 (py_instrument_receiver)
+            134 ROT_TWO
+            136 LOAD_CONST              12 (83)
+            138 LOAD_CONST               0 (None)
+            140 LOAD_CONST              13 (4)
+            142 LOAD_CONST               3 (0)
+            144 LOAD_CONST               8 (False)
+            146 CALL_FUNCTION            6
+            148 POP_TOP
+            150 UNPACK_SEQUENCE          1
             152 RETURN_VALUE
'''

snapshots['test_store_attr (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_NAME                1 (x)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               4 (101)
+             38 LOAD_CONST               5 ('x')
+             40 LOAD_CONST               0 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               6 (95)
+             62 LOAD_CONST               7 ('a')
+             64 LOAD_CONST               8 (2)
+             66 LOAD_CONST               2 (0)
+             68 LOAD_CONST               9 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              2 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 STORE_ATTR               3 (a)
              84 LOAD_CONST              10 (None)
+             86 BUILD_LIST               1
+             88 DUP_TOP
+             90 LOAD_GLOBAL              0 (py_instrument_receiver)
+             92 ROT_TWO
+             94 LOAD_CONST               1 (100)
+             96 LOAD_CONST              10 (None)
+             98 LOAD_CONST              11 (3)
+            100 LOAD_CONST               2 (0)
+            102 LOAD_CONST               3 (True)
+            104 CALL_FUNCTION            6
+            106 POP_TOP
+            108 UNPACK_SEQUENCE          1
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              0 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST              12 (83)
+            120 LOAD_CONST              10 (None)
+            122 LOAD_CONST              13 (4)
+            124 LOAD_CONST               2 (0)
+            126 LOAD_CONST               9 (False)
+            128 CALL_FUNCTION            6
+            130 POP_TOP
+            132 UNPACK_SEQUENCE          1
             134 RETURN_VALUE
'''

snapshots['test_list_load (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_NAME                0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               0 (101)
+             12 LOAD_CONST               1 ('x')
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 (1)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              1 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               5 (100)
+             38 LOAD_CONST               4 (1)
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              1 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               6 (25)
+             62 LOAD_CONST               7 (None)
+             64 LOAD_CONST               8 (2)
+             66 LOAD_CONST               2 (0)
+             68 LOAD_CONST               9 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              2 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 BINARY_SUBSCR
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              1 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               6 (25)
+             94 LOAD_CONST               7 (None)
+             96 LOAD_CONST               8 (2)
+             98 LOAD_CONST               2 (0)
+            100 LOAD_CONST               3 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              1 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               4 (1)
+            118 LOAD_CONST               7 (None)
+            120 LOAD_CONST              10 (3)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               9 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 POP_TOP
             134 LOAD_CONST               7 (None)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              1 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST               5 (100)
+            146 LOAD_CONST               7 (None)
+            148 LOAD_CONST              11 (4)
+            150 LOAD_CONST               2 (0)
+            152 LOAD_CONST               3 (True)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              1 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST              12 (83)
+            170 LOAD_CONST               7 (None)
+            172 LOAD_CONST              13 (5)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               9 (False)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
+            182 UNPACK_SEQUENCE          1
             184 RETURN_VALUE
'''

snapshots['test_list_store (1, 3, 7)'] = '''
Code Object: <module>
   2           0 LOAD_CONST               0 (1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (1)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_NAME                1 (x)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               4 (101)
+             38 LOAD_CONST               5 ('x')
+             40 LOAD_CONST               0 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 LOAD_CONST               0 (1)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               0 (1)
+             66 LOAD_CONST               6 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               3
+             80 DUP_TOP
+             82 LOAD_GLOBAL              0 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST               7 (60)
+             88 LOAD_CONST               8 (None)
+             90 LOAD_CONST               9 (3)
+             92 LOAD_CONST               2 (0)
+             94 LOAD_CONST              10 (False)
+             96 CALL_FUNCTION            6
+             98 POP_TOP
+            100 LOAD_GLOBAL              2 (reversed)
+            102 ROT_TWO
+            104 CALL_FUNCTION            1
+            106 UNPACK_SEQUENCE          3
             108 STORE_SUBSCR
             110 LOAD_CONST               8 (None)
+            112 BUILD_LIST               1
+            114 DUP_TOP
+            116 LOAD_GLOBAL              0 (py_instrument_receiver)
+            118 ROT_TWO
+            120 LOAD_CONST               1 (100)
+            122 LOAD_CONST               8 (None)
+            124 LOAD_CONST              11 (4)
+            126 LOAD_CONST               2 (0)
+            128 LOAD_CONST               3 (True)
+            130 CALL_FUNCTION            6
+            132 POP_TOP
+            134 UNPACK_SEQUENCE          1
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              12 (83)
+            146 LOAD_CONST               8 (None)
+            148 LOAD_CONST              13 (5)
+            150 LOAD_CONST               2 (0)
+            152 LOAD_CONST              10 (False)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
             160 RETURN_VALUE
'''

snapshots['test_for_loop (1, 3, 7)'] = '''
Code Object: <module>
+  2           0 LOAD_GLOBAL              0 (py_instrument_receiver)
+              2 BUILD_LIST               0
+              4 LOAD_CONST               1 (120)
+              6 LOAD_CONST               2 ('label')
+              8 LOAD_CONST               3 (10)
+             10 BUILD_MAP                1
+             12 LOAD_CONST               4 (0)
+             14 LOAD_CONST               4 (0)
+             16 LOAD_CONST               5 (False)
+             18 CALL_FUNCTION            6
+             20 POP_TOP
              22 SETUP_LOOP             104 (to 128)
              24 LOAD_CONST               0 (None)
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (100)
+             36 LOAD_CONST               0 (None)
+             38 LOAD_CONST               7 (1)
+             40 LOAD_CONST               4 (0)
+             42 LOAD_CONST               8 (True)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 GET_ITER
+        >>   52 LOAD_GLOBAL              0 (py_instrument_receiver)
+             54 BUILD_LIST               0
+             56 LOAD_CONST               9 ('JUMP_TARGET')
+             58 LOAD_CONST               2 ('label')
+             60 LOAD_CONST              10 (4)
+             62 BUILD_MAP                1
+             64 LOAD_CONST              11 (3)
+             66 LOAD_CONST               4 (0)
+             68 LOAD_CONST               5 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
              74 FOR_ITER                28 (to 104)
+             76 BUILD_LIST               1
+             78 DUP_TOP
+             80 LOAD_GLOBAL              0 (py_instrument_receiver)
+             82 ROT_TWO
+             84 LOAD_CONST              12 (90)
+             86 LOAD_CONST              13 ('i')
+             88 LOAD_CONST              14 (5)
+             90 LOAD_CONST               4 (0)
+             92 LOAD_CONST               5 (False)
+             94 CALL_FUNCTION            6
+             96 POP_TOP
+             98 UNPACK_SEQUENCE          1
             100 STORE_NAME               1 (i)
   3         102 JUMP_ABSOLUTE           52
+        >>  104 LOAD_GLOBAL              0 (py_instrument_receiver)
+            106 BUILD_LIST               0
+            108 LOAD_CONST               9 ('JUMP_TARGET')
+            110 LOAD_CONST               2 ('label')
+            112 LOAD_CONST              15 (8)
+            114 BUILD_MAP                1
+            116 LOAD_CONST              16 (7)
+            118 LOAD_CONST               4 (0)
+            120 LOAD_CONST               5 (False)
+            122 CALL_FUNCTION            6
+            124 POP_TOP
             126 POP_BLOCK
+        >>  128 LOAD_GLOBAL              0 (py_instrument_receiver)
+            130 BUILD_LIST               0
+            132 LOAD_CONST               9 ('JUMP_TARGET')
+            134 LOAD_CONST               2 ('label')
+            136 LOAD_CONST               3 (10)
+            138 BUILD_MAP                1
+            140 LOAD_CONST              17 (9)
+            142 LOAD_CONST               4 (0)
+            144 LOAD_CONST               5 (False)
+            146 CALL_FUNCTION            6
+            148 POP_TOP
             150 LOAD_CONST               0 (None)
+            152 BUILD_LIST               1
+            154 DUP_TOP
+            156 LOAD_GLOBAL              0 (py_instrument_receiver)
+            158 ROT_TWO
+            160 LOAD_CONST               6 (100)
+            162 LOAD_CONST               0 (None)
+            164 LOAD_CONST               3 (10)
+            166 LOAD_CONST               4 (0)
+            168 LOAD_CONST               8 (True)
+            170 CALL_FUNCTION            6
+            172 POP_TOP
+            174 UNPACK_SEQUENCE          1
+            176 BUILD_LIST               1
+            178 DUP_TOP
+            180 LOAD_GLOBAL              0 (py_instrument_receiver)
+            182 ROT_TWO
+            184 LOAD_CONST              18 (83)
+            186 LOAD_CONST               0 (None)
+            188 LOAD_CONST              19 (11)
+            190 LOAD_CONST               4 (0)
+            192 LOAD_CONST               5 (False)
+            194 CALL_FUNCTION            6
+            196 POP_TOP
+            198 UNPACK_SEQUENCE          1
             200 RETURN_VALUE
'''

snapshots['test_while_loop (1, 3, 7)'] = '''
Code Object: <module>
+  2           0 LOAD_GLOBAL              0 (py_instrument_receiver)
+              2 BUILD_LIST               0
+              4 LOAD_CONST               1 (120)
+              6 LOAD_CONST               2 ('label')
+              8 LOAD_CONST               3 (5)
+             10 BUILD_MAP                1
+             12 LOAD_CONST               4 (0)
+             14 LOAD_CONST               4 (0)
+             16 LOAD_CONST               5 (False)
+             18 CALL_FUNCTION            6
+             20 POP_TOP
              22 SETUP_LOOP              26 (to 50)
+  3     >>   24 LOAD_GLOBAL              0 (py_instrument_receiver)
+             26 BUILD_LIST               0
+             28 LOAD_CONST               6 ('JUMP_TARGET')
+             30 LOAD_CONST               2 ('label')
+             32 LOAD_CONST               7 (2)
+             34 BUILD_MAP                1
+             36 LOAD_CONST               8 (1)
+             38 LOAD_CONST               4 (0)
+             40 LOAD_CONST               5 (False)
+             42 CALL_FUNCTION            6
+             44 POP_TOP
              46 JUMP_ABSOLUTE           24
              48 POP_BLOCK
+        >>   50 LOAD_GLOBAL              0 (py_instrument_receiver)
+             52 BUILD_LIST               0
+             54 LOAD_CONST               6 ('JUMP_TARGET')
+             56 LOAD_CONST               2 ('label')
+             58 LOAD_CONST               3 (5)
+             60 BUILD_MAP                1
+             62 LOAD_CONST               9 (4)
+             64 LOAD_CONST               4 (0)
+             66 LOAD_CONST               5 (False)
+             68 CALL_FUNCTION            6
+             70 POP_TOP
              72 LOAD_CONST               0 (None)
+             74 BUILD_LIST               1
+             76 DUP_TOP
+             78 LOAD_GLOBAL              0 (py_instrument_receiver)
+             80 ROT_TWO
+             82 LOAD_CONST              10 (100)
+             84 LOAD_CONST               0 (None)
+             86 LOAD_CONST               3 (5)
+             88 LOAD_CONST               4 (0)
+             90 LOAD_CONST              11 (True)
+             92 CALL_FUNCTION            6
+             94 POP_TOP
+             96 UNPACK_SEQUENCE          1
+             98 BUILD_LIST               1
+            100 DUP_TOP
+            102 LOAD_GLOBAL              0 (py_instrument_receiver)
+            104 ROT_TWO
+            106 LOAD_CONST              12 (83)
+            108 LOAD_CONST               0 (None)
+            110 LOAD_CONST              13 (6)
+            112 LOAD_CONST               4 (0)
+            114 LOAD_CONST               5 (False)
+            116 CALL_FUNCTION            6
+            118 POP_TOP
+            120 UNPACK_SEQUENCE          1
             122 RETURN_VALUE
'''

snapshots['test_function_definition (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               6 (132)
+             62 LOAD_CONST               2 (0)
+             64 LOAD_CONST               7 (2)
+             66 LOAD_CONST               2 (0)
+             68 LOAD_CONST               8 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              1 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 MAKE_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               6 (132)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               7 (2)
+             98 LOAD_CONST               2 (0)
+            100 LOAD_CONST               3 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               9 (90)
+            118 LOAD_CONST               4 ('f')
+            120 LOAD_CONST              10 (3)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               8 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 STORE_NAME               2 (f)
   4         134 LOAD_NAME                2 (f)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              11 (101)
+            146 LOAD_CONST               4 ('f')
+            148 LOAD_CONST              12 (4)
+            150 LOAD_CONST               2 (0)
+            152 LOAD_CONST               3 (True)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST              13 (131)
+            170 LOAD_CONST               2 (0)
+            172 LOAD_CONST              14 (5)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               8 (False)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
+            182 UNPACK_SEQUENCE          1
             184 CALL_FUNCTION            0
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              13 (131)
+            196 LOAD_CONST               2 (0)
+            198 LOAD_CONST              14 (5)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               5 (1)
+            220 LOAD_CONST              15 (None)
+            222 LOAD_CONST              16 (6)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               8 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 POP_TOP
             236 LOAD_CONST              15 (None)
+            238 BUILD_LIST               1
+            240 DUP_TOP
+            242 LOAD_GLOBAL              0 (py_instrument_receiver)
+            244 ROT_TWO
+            246 LOAD_CONST               1 (100)
+            248 LOAD_CONST              15 (None)
+            250 LOAD_CONST              17 (7)
+            252 LOAD_CONST               2 (0)
+            254 LOAD_CONST               3 (True)
+            256 CALL_FUNCTION            6
+            258 POP_TOP
+            260 UNPACK_SEQUENCE          1
+            262 BUILD_LIST               1
+            264 DUP_TOP
+            266 LOAD_GLOBAL              0 (py_instrument_receiver)
+            268 ROT_TWO
+            270 LOAD_CONST              18 (83)
+            272 LOAD_CONST              15 (None)
+            274 LOAD_CONST              19 (8)
+            276 LOAD_CONST               2 (0)
+            278 LOAD_CONST               8 (False)
+            280 CALL_FUNCTION            6
+            282 POP_TOP
+            284 UNPACK_SEQUENCE          1
             286 RETURN_VALUE

Code Object: f
   3           0 LOAD_CONST               0 (None)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (None)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               3 (1)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               5 (83)
+             36 LOAD_CONST               0 (None)
+             38 LOAD_CONST               3 (1)
+             40 LOAD_CONST               3 (1)
+             42 LOAD_CONST               6 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 RETURN_VALUE
'''

snapshots['test_inner_function (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               6 (132)
+             62 LOAD_CONST               2 (0)
+             64 LOAD_CONST               7 (2)
+             66 LOAD_CONST               2 (0)
+             68 LOAD_CONST               8 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              1 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 MAKE_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               6 (132)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               7 (2)
+             98 LOAD_CONST               2 (0)
+            100 LOAD_CONST               3 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               9 (90)
+            118 LOAD_CONST               4 ('f')
+            120 LOAD_CONST              10 (3)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               8 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 STORE_NAME               2 (f)
   6         134 LOAD_NAME                2 (f)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              11 (101)
+            146 LOAD_CONST               4 ('f')
+            148 LOAD_CONST              12 (4)
+            150 LOAD_CONST               2 (0)
+            152 LOAD_CONST               3 (True)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST              13 (131)
+            170 LOAD_CONST               2 (0)
+            172 LOAD_CONST              14 (5)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               8 (False)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
+            182 UNPACK_SEQUENCE          1
             184 CALL_FUNCTION            0
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              13 (131)
+            196 LOAD_CONST               2 (0)
+            198 LOAD_CONST              14 (5)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               5 (1)
+            220 LOAD_CONST              15 (None)
+            222 LOAD_CONST              16 (6)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               8 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 POP_TOP
             236 LOAD_CONST              15 (None)
+            238 BUILD_LIST               1
+            240 DUP_TOP
+            242 LOAD_GLOBAL              0 (py_instrument_receiver)
+            244 ROT_TWO
+            246 LOAD_CONST               1 (100)
+            248 LOAD_CONST              15 (None)
+            250 LOAD_CONST              17 (7)
+            252 LOAD_CONST               2 (0)
+            254 LOAD_CONST               3 (True)
+            256 CALL_FUNCTION            6
+            258 POP_TOP
+            260 UNPACK_SEQUENCE          1
+            262 BUILD_LIST               1
+            264 DUP_TOP
+            266 LOAD_GLOBAL              0 (py_instrument_receiver)
+            268 ROT_TWO
+            270 LOAD_CONST              18 (83)
+            272 LOAD_CONST              15 (None)
+            274 LOAD_CONST              19 (8)
+            276 LOAD_CONST               2 (0)
+            278 LOAD_CONST               8 (False)
+            280 CALL_FUNCTION            6
+            282 POP_TOP
+            284 UNPACK_SEQUENCE          1
             286 RETURN_VALUE

Code Object: f
~  3           0 LOAD_CONST               1 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               2 (100)
+             12 LOAD_CONST               1 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               6 ('f.<locals>.g')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               2 (100)
+             38 LOAD_CONST               6 ('f.<locals>.g')
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               4 (1)
+             44 LOAD_CONST               5 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               7 (132)
+             62 LOAD_CONST               3 (0)
+             64 LOAD_CONST               8 (2)
+             66 LOAD_CONST               4 (1)
+             68 LOAD_CONST               9 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              1 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 MAKE_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               7 (132)
+             94 LOAD_CONST               3 (0)
+             96 LOAD_CONST               8 (2)
+             98 LOAD_CONST               4 (1)
+            100 LOAD_CONST               5 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST              10 (125)
+            118 LOAD_CONST              11 ('g')
+            120 LOAD_CONST              12 (3)
+            122 LOAD_CONST               4 (1)
+            124 LOAD_CONST               9 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 STORE_FAST               0 (g)
   5         134 LOAD_FAST                0 (g)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              13 (124)
+            146 LOAD_CONST              11 ('g')
+            148 LOAD_CONST              14 (4)
+            150 LOAD_CONST               4 (1)
+            152 LOAD_CONST               5 (True)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST              15 (131)
+            170 LOAD_CONST               3 (0)
+            172 LOAD_CONST              16 (5)
+            174 LOAD_CONST               4 (1)
+            176 LOAD_CONST               9 (False)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
+            182 UNPACK_SEQUENCE          1
             184 CALL_FUNCTION            0
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              15 (131)
+            196 LOAD_CONST               3 (0)
+            198 LOAD_CONST              16 (5)
+            200 LOAD_CONST               4 (1)
+            202 LOAD_CONST               5 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               4 (1)
+            220 LOAD_CONST               0 (None)
+            222 LOAD_CONST              17 (6)
+            224 LOAD_CONST               4 (1)
+            226 LOAD_CONST               9 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 POP_TOP
             236 LOAD_CONST               0 (None)
+            238 BUILD_LIST               1
+            240 DUP_TOP
+            242 LOAD_GLOBAL              0 (py_instrument_receiver)
+            244 ROT_TWO
+            246 LOAD_CONST               2 (100)
+            248 LOAD_CONST               0 (None)
+            250 LOAD_CONST              18 (7)
+            252 LOAD_CONST               4 (1)
+            254 LOAD_CONST               5 (True)
+            256 CALL_FUNCTION            6
+            258 POP_TOP
+            260 UNPACK_SEQUENCE          1
+            262 BUILD_LIST               1
+            264 DUP_TOP
+            266 LOAD_GLOBAL              0 (py_instrument_receiver)
+            268 ROT_TWO
+            270 LOAD_CONST              19 (83)
+            272 LOAD_CONST               0 (None)
+            274 LOAD_CONST              20 (8)
+            276 LOAD_CONST               4 (1)
+            278 LOAD_CONST               9 (False)
+            280 CALL_FUNCTION            6
+            282 POP_TOP
+            284 UNPACK_SEQUENCE          1
             286 RETURN_VALUE

Code Object: g
   4           0 LOAD_CONST               0 (None)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (None)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               3 (2)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               5 (83)
+             36 LOAD_CONST               0 (None)
+             38 LOAD_CONST               6 (1)
+             40 LOAD_CONST               3 (2)
+             42 LOAD_CONST               7 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 RETURN_VALUE
'''

snapshots['test_nonlocal_ref (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object f at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('f')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('f')
+             40 LOAD_CONST               5 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
+             52 BUILD_LIST               2
+             54 DUP_TOP
+             56 LOAD_GLOBAL              0 (py_instrument_receiver)
+             58 ROT_TWO
+             60 LOAD_CONST               6 (132)
+             62 LOAD_CONST               2 (0)
+             64 LOAD_CONST               7 (2)
+             66 LOAD_CONST               2 (0)
+             68 LOAD_CONST               8 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              1 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 MAKE_FUNCTION            0
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               6 (132)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               7 (2)
+             98 LOAD_CONST               2 (0)
+            100 LOAD_CONST               3 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST               9 (90)
+            118 LOAD_CONST               4 ('f')
+            120 LOAD_CONST              10 (3)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               8 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 STORE_NAME               2 (f)
   8         134 LOAD_NAME                2 (f)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              11 (101)
+            146 LOAD_CONST               4 ('f')
+            148 LOAD_CONST              12 (4)
+            150 LOAD_CONST               2 (0)
+            152 LOAD_CONST               3 (True)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST              13 (131)
+            170 LOAD_CONST               2 (0)
+            172 LOAD_CONST              14 (5)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               8 (False)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
+            182 UNPACK_SEQUENCE          1
             184 CALL_FUNCTION            0
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              13 (131)
+            196 LOAD_CONST               2 (0)
+            198 LOAD_CONST              14 (5)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
+            210 BUILD_LIST               1
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST               5 (1)
+            220 LOAD_CONST              15 (None)
+            222 LOAD_CONST              16 (6)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               8 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 UNPACK_SEQUENCE          1
             234 POP_TOP
             236 LOAD_CONST              15 (None)
+            238 BUILD_LIST               1
+            240 DUP_TOP
+            242 LOAD_GLOBAL              0 (py_instrument_receiver)
+            244 ROT_TWO
+            246 LOAD_CONST               1 (100)
+            248 LOAD_CONST              15 (None)
+            250 LOAD_CONST              17 (7)
+            252 LOAD_CONST               2 (0)
+            254 LOAD_CONST               3 (True)
+            256 CALL_FUNCTION            6
+            258 POP_TOP
+            260 UNPACK_SEQUENCE          1
+            262 BUILD_LIST               1
+            264 DUP_TOP
+            266 LOAD_GLOBAL              0 (py_instrument_receiver)
+            268 ROT_TWO
+            270 LOAD_CONST              18 (83)
+            272 LOAD_CONST              15 (None)
+            274 LOAD_CONST              19 (8)
+            276 LOAD_CONST               2 (0)
+            278 LOAD_CONST               8 (False)
+            280 CALL_FUNCTION            6
+            282 POP_TOP
+            284 UNPACK_SEQUENCE          1
             286 RETURN_VALUE

Code Object: f
   3           0 LOAD_CONST               1 (0)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               2 (100)
+             12 LOAD_CONST               1 (0)
+             14 LOAD_CONST               1 (0)
+             16 LOAD_CONST               3 (1)
+             18 LOAD_CONST               4 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               5 (137)
+             36 LOAD_CONST               6 ('cell')
+             38 LOAD_CONST               7 ('i')
+             40 BUILD_MAP                1
+             42 LOAD_CONST               3 (1)
+             44 LOAD_CONST               3 (1)
+             46 LOAD_CONST               8 (False)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 UNPACK_SEQUENCE          1
              54 STORE_DEREF              0 (i)
   4          56 LOAD_CLOSURE             0 (i)
+             58 BUILD_LIST               1
+             60 DUP_TOP
+             62 LOAD_GLOBAL              0 (py_instrument_receiver)
+             64 ROT_TWO
+             66 LOAD_CONST               9 (135)
+             68 LOAD_CONST               6 ('cell')
+             70 LOAD_CONST               7 ('i')
+             72 BUILD_MAP                1
+             74 LOAD_CONST              10 (2)
+             76 LOAD_CONST               3 (1)
+             78 LOAD_CONST               4 (True)
+             80 CALL_FUNCTION            6
+             82 POP_TOP
+             84 UNPACK_SEQUENCE          1
              86 BUILD_TUPLE              1
~             88 LOAD_CONST              11 (<code object g at SOME ADDRESS, file "<string>", line 4>)
+             90 BUILD_LIST               1
+             92 DUP_TOP
+             94 LOAD_GLOBAL              0 (py_instrument_receiver)
+             96 ROT_TWO
+             98 LOAD_CONST               2 (100)
+            100 LOAD_CONST              11 (<code object g at SOME ADDRESS, file "<string>", line 4>)
+            102 LOAD_CONST              12 (4)
+            104 LOAD_CONST               3 (1)
+            106 LOAD_CONST               4 (True)
+            108 CALL_FUNCTION            6
+            110 POP_TOP
+            112 UNPACK_SEQUENCE          1
             114 LOAD_CONST              13 ('f.<locals>.g')
+            116 BUILD_LIST               1
+            118 DUP_TOP
+            120 LOAD_GLOBAL              0 (py_instrument_receiver)
+            122 ROT_TWO
+            124 LOAD_CONST               2 (100)
+            126 LOAD_CONST              13 ('f.<locals>.g')
+            128 LOAD_CONST              14 (5)
+            130 LOAD_CONST               3 (1)
+            132 LOAD_CONST               4 (True)
+            134 CALL_FUNCTION            6
+            136 POP_TOP
+            138 UNPACK_SEQUENCE          1
+            140 BUILD_LIST               2
+            142 DUP_TOP
+            144 LOAD_GLOBAL              0 (py_instrument_receiver)
+            146 ROT_TWO
+            148 LOAD_CONST              15 (132)
+            150 LOAD_CONST              16 (8)
+            152 LOAD_CONST              17 (6)
+            154 LOAD_CONST               3 (1)
+            156 LOAD_CONST               8 (False)
+            158 CALL_FUNCTION            6
+            160 POP_TOP
+            162 LOAD_GLOBAL              1 (reversed)
+            164 ROT_TWO
+            166 CALL_FUNCTION            1
+            168 UNPACK_SEQUENCE          2
             170 MAKE_FUNCTION            8
+            172 BUILD_LIST               1
+            174 DUP_TOP
+            176 LOAD_GLOBAL              0 (py_instrument_receiver)
+            178 ROT_TWO
+            180 LOAD_CONST              15 (132)
+            182 LOAD_CONST              16 (8)
+            184 LOAD_CONST              17 (6)
+            186 LOAD_CONST               3 (1)
+            188 LOAD_CONST               4 (True)
+            190 CALL_FUNCTION            6
+            192 POP_TOP
+            194 UNPACK_SEQUENCE          1
+            196 BUILD_LIST               1
+            198 DUP_TOP
+            200 LOAD_GLOBAL              0 (py_instrument_receiver)
+            202 ROT_TWO
+            204 LOAD_CONST              18 (125)
+            206 LOAD_CONST              19 ('g')
+            208 LOAD_CONST              20 (7)
+            210 LOAD_CONST               3 (1)
+            212 LOAD_CONST               8 (False)
+            214 CALL_FUNCTION            6
+            216 POP_TOP
+            218 UNPACK_SEQUENCE          1
             220 STORE_FAST               0 (g)
   7         222 LOAD_FAST                0 (g)
+            224 BUILD_LIST               1
+            226 DUP_TOP
+            228 LOAD_GLOBAL              0 (py_instrument_receiver)
+            230 ROT_TWO
+            232 LOAD_CONST              21 (124)
+            234 LOAD_CONST              19 ('g')
+            236 LOAD_CONST              16 (8)
+            238 LOAD_CONST               3 (1)
+            240 LOAD_CONST               4 (True)
+            242 CALL_FUNCTION            6
+            244 POP_TOP
+            246 UNPACK_SEQUENCE          1
+            248 BUILD_LIST               1
+            250 DUP_TOP
+            252 LOAD_GLOBAL              0 (py_instrument_receiver)
+            254 ROT_TWO
+            256 LOAD_CONST              22 (131)
+            258 LOAD_CONST               1 (0)
+            260 LOAD_CONST              23 (9)
+            262 LOAD_CONST               3 (1)
+            264 LOAD_CONST               8 (False)
+            266 CALL_FUNCTION            6
+            268 POP_TOP
+            270 UNPACK_SEQUENCE          1
             272 CALL_FUNCTION            0
+            274 BUILD_LIST               1
+            276 DUP_TOP
+            278 LOAD_GLOBAL              0 (py_instrument_receiver)
+            280 ROT_TWO
+            282 LOAD_CONST              22 (131)
+            284 LOAD_CONST               1 (0)
+            286 LOAD_CONST              23 (9)
+            288 LOAD_CONST               3 (1)
+            290 LOAD_CONST               4 (True)
+            292 CALL_FUNCTION            6
+            294 POP_TOP
+            296 UNPACK_SEQUENCE          1
+            298 BUILD_LIST               1
+            300 DUP_TOP
+            302 LOAD_GLOBAL              0 (py_instrument_receiver)
+            304 ROT_TWO
+            306 LOAD_CONST               3 (1)
+            308 LOAD_CONST               0 (None)
+            310 LOAD_CONST              24 (10)
+            312 LOAD_CONST               3 (1)
+            314 LOAD_CONST               8 (False)
+            316 CALL_FUNCTION            6
+            318 POP_TOP
+            320 UNPACK_SEQUENCE          1
             322 POP_TOP
             324 LOAD_CONST               0 (None)
+            326 BUILD_LIST               1
+            328 DUP_TOP
+            330 LOAD_GLOBAL              0 (py_instrument_receiver)
+            332 ROT_TWO
+            334 LOAD_CONST               2 (100)
+            336 LOAD_CONST               0 (None)
+            338 LOAD_CONST              25 (11)
+            340 LOAD_CONST               3 (1)
+            342 LOAD_CONST               4 (True)
+            344 CALL_FUNCTION            6
+            346 POP_TOP
+            348 UNPACK_SEQUENCE          1
+            350 BUILD_LIST               1
+            352 DUP_TOP
+            354 LOAD_GLOBAL              0 (py_instrument_receiver)
+            356 ROT_TWO
+            358 LOAD_CONST              26 (83)
+            360 LOAD_CONST               0 (None)
+            362 LOAD_CONST              27 (12)
+            364 LOAD_CONST               3 (1)
+            366 LOAD_CONST               8 (False)
+            368 CALL_FUNCTION            6
+            370 POP_TOP
+            372 UNPACK_SEQUENCE          1
             374 RETURN_VALUE

Code Object: g
   6           0 LOAD_DEREF               0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (136)
+             12 LOAD_CONST               2 ('free')
+             14 LOAD_CONST               3 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               4 (0)
+             20 LOAD_CONST               5 (2)
+             22 LOAD_CONST               6 (True)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
+             30 BUILD_LIST               1
+             32 DUP_TOP
+             34 LOAD_GLOBAL              0 (py_instrument_receiver)
+             36 ROT_TWO
+             38 LOAD_CONST               7 (83)
+             40 LOAD_CONST               0 (None)
+             42 LOAD_CONST               8 (1)
+             44 LOAD_CONST               5 (2)
+             46 LOAD_CONST               9 (False)
+             48 CALL_FUNCTION            6
+             50 POP_TOP
+             52 UNPACK_SEQUENCE          1
              54 RETURN_VALUE
'''
