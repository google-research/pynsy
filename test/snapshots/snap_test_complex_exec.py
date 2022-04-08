# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_nested_iteration (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object myFunc at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object myFunc at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('myFunc')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('myFunc')
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
+            118 LOAD_CONST               4 ('myFunc')
+            120 LOAD_CONST              10 (3)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               8 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 STORE_NAME               2 (myFunc)
  12         134 LOAD_NAME                2 (myFunc)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              11 (101)
+            146 LOAD_CONST               4 ('myFunc')
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

Code Object: myFunc
   3           0 LOAD_CONST               1 (-1)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               2 (100)
+             12 LOAD_CONST               1 (-1)
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              0 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (125)
+             36 LOAD_CONST               7 ('x')
+             38 LOAD_CONST               4 (1)
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               8 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_FAST               0 (x)
   4          52 LOAD_GLOBAL              1 (list)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               9 (116)
+             64 LOAD_CONST              10 ('list')
+             66 LOAD_CONST              11 (2)
+             68 LOAD_CONST               4 (1)
+             70 LOAD_CONST               5 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 LOAD_GLOBAL              2 (range)
+             80 BUILD_LIST               1
+             82 DUP_TOP
+             84 LOAD_GLOBAL              0 (py_instrument_receiver)
+             86 ROT_TWO
+             88 LOAD_CONST               9 (116)
+             90 LOAD_CONST              12 ('range')
+             92 LOAD_CONST              13 (3)
+             94 LOAD_CONST               4 (1)
+             96 LOAD_CONST               5 (True)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
+            102 UNPACK_SEQUENCE          1
             104 LOAD_CONST              14 (5)
+            106 BUILD_LIST               1
+            108 DUP_TOP
+            110 LOAD_GLOBAL              0 (py_instrument_receiver)
+            112 ROT_TWO
+            114 LOAD_CONST               2 (100)
+            116 LOAD_CONST              14 (5)
+            118 LOAD_CONST              15 (4)
+            120 LOAD_CONST               4 (1)
+            122 LOAD_CONST               5 (True)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
+            128 UNPACK_SEQUENCE          1
+            130 BUILD_LIST               2
+            132 DUP_TOP
+            134 LOAD_GLOBAL              0 (py_instrument_receiver)
+            136 ROT_TWO
+            138 LOAD_CONST              16 (131)
+            140 LOAD_CONST               4 (1)
+            142 LOAD_CONST              14 (5)
+            144 LOAD_CONST               4 (1)
+            146 LOAD_CONST               8 (False)
+            148 CALL_FUNCTION            6
+            150 POP_TOP
+            152 LOAD_GLOBAL              3 (reversed)
+            154 ROT_TWO
+            156 CALL_FUNCTION            1
+            158 UNPACK_SEQUENCE          2
             160 CALL_FUNCTION            1
+            162 BUILD_LIST               1
+            164 DUP_TOP
+            166 LOAD_GLOBAL              0 (py_instrument_receiver)
+            168 ROT_TWO
+            170 LOAD_CONST              16 (131)
+            172 LOAD_CONST               4 (1)
+            174 LOAD_CONST              14 (5)
+            176 LOAD_CONST               4 (1)
+            178 LOAD_CONST               5 (True)
+            180 CALL_FUNCTION            6
+            182 POP_TOP
+            184 UNPACK_SEQUENCE          1
+            186 BUILD_LIST               2
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              16 (131)
+            196 LOAD_CONST               4 (1)
+            198 LOAD_CONST              17 (6)
+            200 LOAD_CONST               4 (1)
+            202 LOAD_CONST               8 (False)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 LOAD_GLOBAL              3 (reversed)
+            210 ROT_TWO
+            212 CALL_FUNCTION            1
+            214 UNPACK_SEQUENCE          2
             216 CALL_FUNCTION            1
+            218 BUILD_LIST               1
+            220 DUP_TOP
+            222 LOAD_GLOBAL              0 (py_instrument_receiver)
+            224 ROT_TWO
+            226 LOAD_CONST              16 (131)
+            228 LOAD_CONST               4 (1)
+            230 LOAD_CONST              17 (6)
+            232 LOAD_CONST               4 (1)
+            234 LOAD_CONST               5 (True)
+            236 CALL_FUNCTION            6
+            238 POP_TOP
+            240 UNPACK_SEQUENCE          1
+            242 BUILD_LIST               1
+            244 DUP_TOP
+            246 LOAD_GLOBAL              0 (py_instrument_receiver)
+            248 ROT_TWO
+            250 LOAD_CONST               6 (125)
+            252 LOAD_CONST              18 ('data')
+            254 LOAD_CONST              19 (7)
+            256 LOAD_CONST               4 (1)
+            258 LOAD_CONST               8 (False)
+            260 CALL_FUNCTION            6
+            262 POP_TOP
+            264 UNPACK_SEQUENCE          1
             266 STORE_FAST               1 (data)
+  5         268 LOAD_GLOBAL              0 (py_instrument_receiver)
+            270 BUILD_LIST               0
+            272 LOAD_CONST              20 (120)
+            274 LOAD_CONST              21 ('label')
+            276 LOAD_CONST              22 (43)
+            278 BUILD_MAP                1
+            280 LOAD_CONST              23 (8)
+            282 LOAD_CONST               4 (1)
+            284 LOAD_CONST               8 (False)
+            286 CALL_FUNCTION            6
+            288 POP_TOP
             290 EXTENDED_ARG             3
             292 SETUP_LOOP             782 (to 1076)
+            294 LOAD_FAST                1 (data)
+            296 BUILD_LIST               1
+            298 DUP_TOP
+            300 LOAD_GLOBAL              0 (py_instrument_receiver)
+            302 ROT_TWO
+            304 LOAD_CONST              24 (124)
+            306 LOAD_CONST              18 ('data')
+            308 LOAD_CONST              25 (9)
+            310 LOAD_CONST               4 (1)
+            312 LOAD_CONST               5 (True)
+            314 CALL_FUNCTION            6
+            316 POP_TOP
             318 UNPACK_SEQUENCE          1
+            320 GET_ITER
+        >>  322 LOAD_GLOBAL              0 (py_instrument_receiver)
+            324 BUILD_LIST               0
+            326 LOAD_CONST              26 ('JUMP_TARGET')
+            328 LOAD_CONST              21 ('label')
+            330 LOAD_CONST              27 (12)
+            332 BUILD_MAP                1
+            334 LOAD_CONST              28 (11)
+            336 LOAD_CONST               4 (1)
+            338 LOAD_CONST               8 (False)
+            340 CALL_FUNCTION            6
             342 POP_TOP
+            344 EXTENDED_ARG             2
+            346 FOR_ITER               704 (to 1052)
+            348 BUILD_LIST               1
+            350 DUP_TOP
+            352 LOAD_GLOBAL              0 (py_instrument_receiver)
+            354 ROT_TWO
+            356 LOAD_CONST               6 (125)
+            358 LOAD_CONST              29 ('i')
+            360 LOAD_CONST              30 (13)
+            362 LOAD_CONST               4 (1)
+            364 LOAD_CONST               8 (False)
+            366 CALL_FUNCTION            6
             368 POP_TOP
             370 UNPACK_SEQUENCE          1
+            372 STORE_FAST               2 (i)
+  6         374 LOAD_FAST                2 (i)
+            376 BUILD_LIST               1
+            378 DUP_TOP
+            380 LOAD_GLOBAL              0 (py_instrument_receiver)
+            382 ROT_TWO
+            384 LOAD_CONST              24 (124)
+            386 LOAD_CONST              29 ('i')
+            388 LOAD_CONST              31 (14)
+            390 LOAD_CONST               4 (1)
+            392 LOAD_CONST               5 (True)
+            394 CALL_FUNCTION            6
             396 POP_TOP
+            398 UNPACK_SEQUENCE          1
+            400 LOAD_CONST              13 (3)
+            402 BUILD_LIST               1
+            404 DUP_TOP
+            406 LOAD_GLOBAL              0 (py_instrument_receiver)
+            408 ROT_TWO
+            410 LOAD_CONST               2 (100)
+            412 LOAD_CONST              13 (3)
+            414 LOAD_CONST              32 (15)
+            416 LOAD_CONST               4 (1)
+            418 LOAD_CONST               5 (True)
+            420 CALL_FUNCTION            6
+            422 POP_TOP
+            424 UNPACK_SEQUENCE          1
+            426 BUILD_LIST               2
+            428 DUP_TOP
+            430 LOAD_GLOBAL              0 (py_instrument_receiver)
+            432 ROT_TWO
+            434 LOAD_CONST              33 (107)
+            436 LOAD_CONST              34 (<Compare.EQ: 2>)
+            438 LOAD_CONST              35 (16)
+            440 LOAD_CONST               4 (1)
+            442 LOAD_CONST               8 (False)
+            444 CALL_FUNCTION            6
+            446 POP_TOP
+            448 LOAD_GLOBAL              3 (reversed)
+            450 ROT_TWO
             452 CALL_FUNCTION            1
+            454 UNPACK_SEQUENCE          2
+            456 COMPARE_OP               2 (==)
+            458 BUILD_LIST               1
+            460 DUP_TOP
+            462 LOAD_GLOBAL              0 (py_instrument_receiver)
+            464 ROT_TWO
+            466 LOAD_CONST              33 (107)
+            468 LOAD_CONST              34 (<Compare.EQ: 2>)
+            470 LOAD_CONST              35 (16)
+            472 LOAD_CONST               4 (1)
+            474 LOAD_CONST               5 (True)
+            476 CALL_FUNCTION            6
+            478 POP_TOP
+            480 UNPACK_SEQUENCE          1
+            482 BUILD_LIST               1
+            484 DUP_TOP
+            486 LOAD_GLOBAL              0 (py_instrument_receiver)
+            488 ROT_TWO
+            490 LOAD_CONST              36 (114)
+            492 LOAD_CONST              21 ('label')
+            494 LOAD_CONST              37 (21)
+            496 BUILD_MAP                1
+            498 LOAD_CONST              38 (17)
+            500 LOAD_CONST               4 (1)
+            502 LOAD_CONST               8 (False)
+            504 CALL_FUNCTION            6
             506 POP_TOP
             508 UNPACK_SEQUENCE          1
             510 EXTENDED_ARG             2
+            512 POP_JUMP_IF_FALSE      520
+  7         514 BREAK_LOOP
+            516 EXTENDED_ARG             1
+            518 JUMP_ABSOLUTE          322
+  9     >>  520 LOAD_GLOBAL              0 (py_instrument_receiver)
+            522 BUILD_LIST               0
+            524 LOAD_CONST              26 ('JUMP_TARGET')
+            526 LOAD_CONST              21 ('label')
+            528 LOAD_CONST              37 (21)
+            530 BUILD_MAP                1
+            532 LOAD_CONST              39 (20)
+            534 LOAD_CONST               4 (1)
+            536 LOAD_CONST               8 (False)
+            538 CALL_FUNCTION            6
+            540 POP_TOP
+            542 LOAD_GLOBAL              0 (py_instrument_receiver)
+            544 BUILD_LIST               0
+            546 LOAD_CONST              20 (120)
+            548 LOAD_CONST              21 ('label')
+            550 LOAD_CONST              40 (39)
+            552 BUILD_MAP                1
+            554 LOAD_CONST              37 (21)
             556 LOAD_CONST               4 (1)
+            558 LOAD_CONST               8 (False)
+            560 CALL_FUNCTION            6
+            562 POP_TOP
+            564 EXTENDED_ARG             1
+            566 SETUP_LOOP             458 (to 1026)
+        >>  568 LOAD_GLOBAL              0 (py_instrument_receiver)
+            570 BUILD_LIST               0
+            572 LOAD_CONST              26 ('JUMP_TARGET')
+            574 LOAD_CONST              21 ('label')
+            576 LOAD_CONST              41 (23)
+            578 BUILD_MAP                1
             580 LOAD_CONST              42 (22)
+            582 LOAD_CONST               4 (1)
+            584 LOAD_CONST               8 (False)
+            586 CALL_FUNCTION            6
+            588 POP_TOP
+            590 LOAD_FAST                2 (i)
+            592 BUILD_LIST               1
+            594 DUP_TOP
+            596 LOAD_GLOBAL              0 (py_instrument_receiver)
+            598 ROT_TWO
+            600 LOAD_CONST              24 (124)
+            602 LOAD_CONST              29 ('i')
+            604 LOAD_CONST              41 (23)
             606 LOAD_CONST               4 (1)
+            608 LOAD_CONST               5 (True)
+            610 CALL_FUNCTION            6
+            612 POP_TOP
+            614 UNPACK_SEQUENCE          1
+            616 LOAD_CONST               3 (0)
+            618 BUILD_LIST               1
+            620 DUP_TOP
+            622 LOAD_GLOBAL              0 (py_instrument_receiver)
+            624 ROT_TWO
+            626 LOAD_CONST               2 (100)
+            628 LOAD_CONST               3 (0)
+            630 LOAD_CONST              43 (24)
+            632 LOAD_CONST               4 (1)
+            634 LOAD_CONST               5 (True)
+            636 CALL_FUNCTION            6
+            638 POP_TOP
+            640 UNPACK_SEQUENCE          1
+            642 BUILD_LIST               2
+            644 DUP_TOP
+            646 LOAD_GLOBAL              0 (py_instrument_receiver)
+            648 ROT_TWO
+            650 LOAD_CONST              33 (107)
+            652 LOAD_CONST              44 (<Compare.GT: 4>)
+            654 LOAD_CONST              45 (25)
+            656 LOAD_CONST               4 (1)
+            658 LOAD_CONST               8 (False)
+            660 CALL_FUNCTION            6
             662 POP_TOP
+            664 LOAD_GLOBAL              3 (reversed)
+            666 ROT_TWO
+            668 CALL_FUNCTION            1
+            670 UNPACK_SEQUENCE          2
+            672 COMPARE_OP               4 (>)
+            674 BUILD_LIST               1
+            676 DUP_TOP
+            678 LOAD_GLOBAL              0 (py_instrument_receiver)
+            680 ROT_TWO
+            682 LOAD_CONST              33 (107)
+            684 LOAD_CONST              44 (<Compare.GT: 4>)
+            686 LOAD_CONST              45 (25)
+            688 LOAD_CONST               4 (1)
+            690 LOAD_CONST               5 (True)
+            692 CALL_FUNCTION            6
+            694 POP_TOP
+            696 UNPACK_SEQUENCE          1
+            698 BUILD_LIST               1
+            700 DUP_TOP
+            702 LOAD_GLOBAL              0 (py_instrument_receiver)
+            704 ROT_TWO
+            706 LOAD_CONST              36 (114)
+            708 LOAD_CONST              21 ('label')
+            710 LOAD_CONST              46 (37)
+            712 BUILD_MAP                1
+            714 LOAD_CONST              47 (26)
             716 LOAD_CONST               4 (1)
             718 LOAD_CONST               8 (False)
+            720 CALL_FUNCTION            6
+            722 POP_TOP
+            724 UNPACK_SEQUENCE          1
+            726 EXTENDED_ARG             3
+            728 POP_JUMP_IF_FALSE     1002
+ 10         730 LOAD_FAST                0 (x)
+            732 BUILD_LIST               1
+            734 DUP_TOP
+            736 LOAD_GLOBAL              0 (py_instrument_receiver)
+            738 ROT_TWO
+            740 LOAD_CONST              24 (124)
+            742 LOAD_CONST               7 ('x')
             744 LOAD_CONST              48 (27)
+            746 LOAD_CONST               4 (1)
+            748 LOAD_CONST               5 (True)
+            750 CALL_FUNCTION            6
+            752 POP_TOP
+            754 UNPACK_SEQUENCE          1
+            756 LOAD_FAST                2 (i)
+            758 BUILD_LIST               1
+            760 DUP_TOP
+            762 LOAD_GLOBAL              0 (py_instrument_receiver)
+            764 ROT_TWO
+            766 LOAD_CONST              24 (124)
+            768 LOAD_CONST              29 ('i')
+            770 LOAD_CONST              49 (28)
+            772 LOAD_CONST               4 (1)
+            774 LOAD_CONST               5 (True)
+            776 CALL_FUNCTION            6
+            778 POP_TOP
+            780 UNPACK_SEQUENCE          1
+            782 BUILD_LIST               2
+            784 DUP_TOP
+            786 LOAD_GLOBAL              0 (py_instrument_receiver)
+            788 ROT_TWO
+            790 LOAD_CONST              50 (55)
+            792 LOAD_CONST               0 (None)
+            794 LOAD_CONST              51 (29)
+            796 LOAD_CONST               4 (1)
+            798 LOAD_CONST               8 (False)
             800 CALL_FUNCTION            6
+            802 POP_TOP
+            804 LOAD_GLOBAL              3 (reversed)
+            806 ROT_TWO
+            808 CALL_FUNCTION            1
+            810 UNPACK_SEQUENCE          2
+            812 INPLACE_ADD
+            814 BUILD_LIST               1
+            816 DUP_TOP
+            818 LOAD_GLOBAL              0 (py_instrument_receiver)
+            820 ROT_TWO
+            822 LOAD_CONST              50 (55)
+            824 LOAD_CONST               0 (None)
+            826 LOAD_CONST              51 (29)
+            828 LOAD_CONST               4 (1)
+            830 LOAD_CONST               5 (True)
+            832 CALL_FUNCTION            6
+            834 POP_TOP
+            836 UNPACK_SEQUENCE          1
+            838 BUILD_LIST               1
+            840 DUP_TOP
+            842 LOAD_GLOBAL              0 (py_instrument_receiver)
+            844 ROT_TWO
+            846 LOAD_CONST               6 (125)
+            848 LOAD_CONST               7 ('x')
             850 LOAD_CONST              52 (30)
             852 LOAD_CONST               4 (1)
+            854 LOAD_CONST               8 (False)
+            856 CALL_FUNCTION            6
+            858 POP_TOP
+            860 UNPACK_SEQUENCE          1
+            862 STORE_FAST               0 (x)
+ 11         864 LOAD_FAST                2 (i)
+            866 BUILD_LIST               1
+            868 DUP_TOP
+            870 LOAD_GLOBAL              0 (py_instrument_receiver)
+            872 ROT_TWO
+            874 LOAD_CONST              24 (124)
+            876 LOAD_CONST              29 ('i')
             878 LOAD_CONST              53 (31)
+            880 LOAD_CONST               4 (1)
+            882 LOAD_CONST               5 (True)
+            884 CALL_FUNCTION            6
+            886 POP_TOP
+            888 UNPACK_SEQUENCE          1
+            890 LOAD_CONST               4 (1)
+            892 BUILD_LIST               1
+            894 DUP_TOP
+            896 LOAD_GLOBAL              0 (py_instrument_receiver)
+            898 ROT_TWO
+            900 LOAD_CONST               2 (100)
+            902 LOAD_CONST               4 (1)
+            904 LOAD_CONST              54 (32)
+            906 LOAD_CONST               4 (1)
+            908 LOAD_CONST               5 (True)
+            910 CALL_FUNCTION            6
+            912 POP_TOP
+            914 UNPACK_SEQUENCE          1
+            916 BUILD_LIST               2
+            918 DUP_TOP
+            920 LOAD_GLOBAL              0 (py_instrument_receiver)
+            922 ROT_TWO
+            924 LOAD_CONST              55 (56)
+            926 LOAD_CONST               0 (None)
+            928 LOAD_CONST              56 (33)
+            930 LOAD_CONST               4 (1)
+            932 LOAD_CONST               8 (False)
             934 CALL_FUNCTION            6
+            936 POP_TOP
+            938 LOAD_GLOBAL              3 (reversed)
+            940 ROT_TWO
+            942 CALL_FUNCTION            1
+            944 UNPACK_SEQUENCE          2
+            946 INPLACE_SUBTRACT
+            948 BUILD_LIST               1
+            950 DUP_TOP
+            952 LOAD_GLOBAL              0 (py_instrument_receiver)
+            954 ROT_TWO
+            956 LOAD_CONST              55 (56)
+            958 LOAD_CONST               0 (None)
+            960 LOAD_CONST              56 (33)
+            962 LOAD_CONST               4 (1)
+            964 LOAD_CONST               5 (True)
+            966 CALL_FUNCTION            6
+            968 POP_TOP
+            970 UNPACK_SEQUENCE          1
+            972 BUILD_LIST               1
+            974 DUP_TOP
+            976 LOAD_GLOBAL              0 (py_instrument_receiver)
+            978 ROT_TWO
+            980 LOAD_CONST               6 (125)
+            982 LOAD_CONST              29 ('i')
             984 LOAD_CONST              57 (34)
             986 LOAD_CONST               4 (1)
+            988 LOAD_CONST               8 (False)
+            990 CALL_FUNCTION            6
+            992 POP_TOP
+            994 UNPACK_SEQUENCE          1
+            996 STORE_FAST               2 (i)
+            998 EXTENDED_ARG             2
+           1000 JUMP_ABSOLUTE          568
+        >> 1002 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1004 BUILD_LIST               0
+           1006 LOAD_CONST              26 ('JUMP_TARGET')
+           1008 LOAD_CONST              21 ('label')
            1010 LOAD_CONST              46 (37)
+           1012 BUILD_MAP                1
+           1014 LOAD_CONST              58 (36)
+           1016 LOAD_CONST               4 (1)
+           1018 LOAD_CONST               8 (False)
+           1020 CALL_FUNCTION            6
+           1022 POP_TOP
+           1024 POP_BLOCK
+        >> 1026 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1028 BUILD_LIST               0
+           1030 LOAD_CONST              26 ('JUMP_TARGET')
+           1032 LOAD_CONST              21 ('label')
            1034 LOAD_CONST              40 (39)
+           1036 BUILD_MAP                1
+           1038 LOAD_CONST              59 (38)
+           1040 LOAD_CONST               4 (1)
+           1042 LOAD_CONST               8 (False)
+           1044 CALL_FUNCTION            6
+           1046 POP_TOP
+           1048 EXTENDED_ARG             1
+           1050 JUMP_ABSOLUTE          322
+        >> 1052 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1054 BUILD_LIST               0
+           1056 LOAD_CONST              26 ('JUMP_TARGET')
            1058 LOAD_CONST              21 ('label')
+           1060 LOAD_CONST              60 (41)
+           1062 BUILD_MAP                1
+           1064 LOAD_CONST              61 (40)
+           1066 LOAD_CONST               4 (1)
+           1068 LOAD_CONST               8 (False)
+           1070 CALL_FUNCTION            6
+           1072 POP_TOP
+           1074 POP_BLOCK
+        >> 1076 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1078 BUILD_LIST               0
+           1080 LOAD_CONST              26 ('JUMP_TARGET')
            1082 LOAD_CONST              21 ('label')
+           1084 LOAD_CONST              22 (43)
+           1086 BUILD_MAP                1
+           1088 LOAD_CONST              62 (42)
+           1090 LOAD_CONST               4 (1)
+           1092 LOAD_CONST               8 (False)
+           1094 CALL_FUNCTION            6
+           1096 POP_TOP
+           1098 LOAD_CONST               0 (None)
+           1100 BUILD_LIST               1
+           1102 DUP_TOP
+           1104 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1106 ROT_TWO
+           1108 LOAD_CONST               2 (100)
+           1110 LOAD_CONST               0 (None)
+           1112 LOAD_CONST              22 (43)
+           1114 LOAD_CONST               4 (1)
+           1116 LOAD_CONST               5 (True)
+           1118 CALL_FUNCTION            6
+           1120 POP_TOP
+           1122 UNPACK_SEQUENCE          1
+           1124 BUILD_LIST               1
+           1126 DUP_TOP
+           1128 LOAD_GLOBAL              0 (py_instrument_receiver)
+           1130 ROT_TWO
            1132 LOAD_CONST              63 (83)
'''

snapshots['test_factorial (1, 3, 7)'] = '''
Code Object: <module>
~  2           0 LOAD_CONST               0 (<code object factorial at SOME ADDRESS, file "<string>", line 2>)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (100)
+             12 LOAD_CONST               0 (<code object factorial at SOME ADDRESS, file "<string>", line 2>)
+             14 LOAD_CONST               2 (0)
+             16 LOAD_CONST               2 (0)
+             18 LOAD_CONST               3 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               4 ('factorial')
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 ('factorial')
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
+            118 LOAD_CONST               4 ('factorial')
+            120 LOAD_CONST              10 (3)
+            122 LOAD_CONST               2 (0)
+            124 LOAD_CONST               8 (False)
+            126 CALL_FUNCTION            6
+            128 POP_TOP
+            130 UNPACK_SEQUENCE          1
             132 STORE_NAME               2 (factorial)
   8         134 LOAD_NAME                2 (factorial)
+            136 BUILD_LIST               1
+            138 DUP_TOP
+            140 LOAD_GLOBAL              0 (py_instrument_receiver)
+            142 ROT_TWO
+            144 LOAD_CONST              11 (101)
+            146 LOAD_CONST               4 ('factorial')
+            148 LOAD_CONST              12 (4)
+            150 LOAD_CONST               2 (0)
+            152 LOAD_CONST               3 (True)
+            154 CALL_FUNCTION            6
+            156 POP_TOP
+            158 UNPACK_SEQUENCE          1
             160 LOAD_CONST              13 (5)
+            162 BUILD_LIST               1
+            164 DUP_TOP
+            166 LOAD_GLOBAL              0 (py_instrument_receiver)
+            168 ROT_TWO
+            170 LOAD_CONST               1 (100)
+            172 LOAD_CONST              13 (5)
+            174 LOAD_CONST              13 (5)
+            176 LOAD_CONST               2 (0)
+            178 LOAD_CONST               3 (True)
+            180 CALL_FUNCTION            6
+            182 POP_TOP
+            184 UNPACK_SEQUENCE          1
+            186 BUILD_LIST               2
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              14 (131)
+            196 LOAD_CONST               5 (1)
+            198 LOAD_CONST              15 (6)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               8 (False)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 LOAD_GLOBAL              1 (reversed)
+            210 ROT_TWO
+            212 CALL_FUNCTION            1
+            214 UNPACK_SEQUENCE          2
             216 CALL_FUNCTION            1
+            218 BUILD_LIST               1
+            220 DUP_TOP
+            222 LOAD_GLOBAL              0 (py_instrument_receiver)
+            224 ROT_TWO
+            226 LOAD_CONST              14 (131)
+            228 LOAD_CONST               5 (1)
+            230 LOAD_CONST              15 (6)
+            232 LOAD_CONST               2 (0)
+            234 LOAD_CONST               3 (True)
+            236 CALL_FUNCTION            6
+            238 POP_TOP
+            240 UNPACK_SEQUENCE          1
+            242 BUILD_LIST               1
+            244 DUP_TOP
+            246 LOAD_GLOBAL              0 (py_instrument_receiver)
+            248 ROT_TWO
+            250 LOAD_CONST               5 (1)
+            252 LOAD_CONST              16 (None)
+            254 LOAD_CONST              17 (7)
+            256 LOAD_CONST               2 (0)
+            258 LOAD_CONST               8 (False)
+            260 CALL_FUNCTION            6
+            262 POP_TOP
+            264 UNPACK_SEQUENCE          1
             266 POP_TOP
             268 LOAD_CONST              16 (None)
+            270 BUILD_LIST               1
+            272 DUP_TOP
+            274 LOAD_GLOBAL              0 (py_instrument_receiver)
+            276 ROT_TWO
+            278 LOAD_CONST               1 (100)
+            280 LOAD_CONST              16 (None)
+            282 LOAD_CONST              18 (8)
+            284 LOAD_CONST               2 (0)
+            286 LOAD_CONST               3 (True)
+            288 CALL_FUNCTION            6
+            290 POP_TOP
+            292 UNPACK_SEQUENCE          1
+            294 BUILD_LIST               1
+            296 DUP_TOP
+            298 LOAD_GLOBAL              0 (py_instrument_receiver)
+            300 ROT_TWO
+            302 LOAD_CONST              19 (83)
+            304 LOAD_CONST              16 (None)
+            306 LOAD_CONST              20 (9)
+            308 LOAD_CONST               2 (0)
+            310 LOAD_CONST               8 (False)
+            312 CALL_FUNCTION            6
+            314 POP_TOP
+            316 UNPACK_SEQUENCE          1
             318 RETURN_VALUE

Code Object: factorial
   3           0 LOAD_FAST                0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (124)
+             12 LOAD_CONST               2 ('i')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
              26 LOAD_CONST               3 (0)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               6 (100)
+             38 LOAD_CONST               3 (0)
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
+             60 LOAD_CONST               7 (107)
+             62 LOAD_CONST               8 (<Compare.EQ: 2>)
+             64 LOAD_CONST               9 (2)
+             66 LOAD_CONST               4 (1)
+             68 LOAD_CONST              10 (False)
+             70 CALL_FUNCTION            6
+             72 POP_TOP
+             74 LOAD_GLOBAL              1 (reversed)
+             76 ROT_TWO
+             78 CALL_FUNCTION            1
+             80 UNPACK_SEQUENCE          2
              82 COMPARE_OP               2 (==)
+             84 BUILD_LIST               1
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST               7 (107)
+             94 LOAD_CONST               8 (<Compare.EQ: 2>)
+             96 LOAD_CONST               9 (2)
+             98 LOAD_CONST               4 (1)
+            100 LOAD_CONST               5 (True)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 UNPACK_SEQUENCE          1
+            108 BUILD_LIST               1
+            110 DUP_TOP
+            112 LOAD_GLOBAL              0 (py_instrument_receiver)
+            114 ROT_TWO
+            116 LOAD_CONST              11 (114)
+            118 LOAD_CONST              12 ('label')
+            120 LOAD_CONST              13 (7)
+            122 BUILD_MAP                1
+            124 LOAD_CONST              14 (3)
+            126 LOAD_CONST               4 (1)
+            128 LOAD_CONST              10 (False)
+            130 CALL_FUNCTION            6
+            132 POP_TOP
+            134 UNPACK_SEQUENCE          1
             136 POP_JUMP_IF_FALSE      190
   4         138 LOAD_CONST               4 (1)
+            140 BUILD_LIST               1
+            142 DUP_TOP
+            144 LOAD_GLOBAL              0 (py_instrument_receiver)
+            146 ROT_TWO
+            148 LOAD_CONST               6 (100)
+            150 LOAD_CONST               4 (1)
+            152 LOAD_CONST              15 (4)
+            154 LOAD_CONST               4 (1)
+            156 LOAD_CONST               5 (True)
+            158 CALL_FUNCTION            6
+            160 POP_TOP
+            162 UNPACK_SEQUENCE          1
+            164 BUILD_LIST               1
+            166 DUP_TOP
+            168 LOAD_GLOBAL              0 (py_instrument_receiver)
+            170 ROT_TWO
+            172 LOAD_CONST              16 (83)
+            174 LOAD_CONST               0 (None)
+            176 LOAD_CONST              17 (5)
+            178 LOAD_CONST               4 (1)
+            180 LOAD_CONST              10 (False)
+            182 CALL_FUNCTION            6
+            184 POP_TOP
+            186 UNPACK_SEQUENCE          1
             188 RETURN_VALUE
+  6     >>  190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 BUILD_LIST               0
+            194 LOAD_CONST              18 ('JUMP_TARGET')
+            196 LOAD_CONST              12 ('label')
+            198 LOAD_CONST              13 (7)
+            200 BUILD_MAP                1
+            202 LOAD_CONST              19 (6)
+            204 LOAD_CONST               4 (1)
+            206 LOAD_CONST              10 (False)
+            208 CALL_FUNCTION            6
+            210 POP_TOP
             212 LOAD_FAST                0 (i)
+            214 BUILD_LIST               1
+            216 DUP_TOP
+            218 LOAD_GLOBAL              0 (py_instrument_receiver)
+            220 ROT_TWO
+            222 LOAD_CONST               1 (124)
+            224 LOAD_CONST               2 ('i')
+            226 LOAD_CONST              13 (7)
+            228 LOAD_CONST               4 (1)
+            230 LOAD_CONST               5 (True)
+            232 CALL_FUNCTION            6
+            234 POP_TOP
+            236 UNPACK_SEQUENCE          1
             238 LOAD_GLOBAL              2 (factorial)
+            240 BUILD_LIST               1
+            242 DUP_TOP
+            244 LOAD_GLOBAL              0 (py_instrument_receiver)
+            246 ROT_TWO
+            248 LOAD_CONST              20 (116)
+            250 LOAD_CONST              21 ('factorial')
+            252 LOAD_CONST              22 (8)
+            254 LOAD_CONST               4 (1)
+            256 LOAD_CONST               5 (True)
+            258 CALL_FUNCTION            6
+            260 POP_TOP
+            262 UNPACK_SEQUENCE          1
             264 LOAD_FAST                0 (i)
+            266 BUILD_LIST               1
+            268 DUP_TOP
+            270 LOAD_GLOBAL              0 (py_instrument_receiver)
+            272 ROT_TWO
+            274 LOAD_CONST               1 (124)
+            276 LOAD_CONST               2 ('i')
+            278 LOAD_CONST              23 (9)
+            280 LOAD_CONST               4 (1)
+            282 LOAD_CONST               5 (True)
+            284 CALL_FUNCTION            6
+            286 POP_TOP
+            288 UNPACK_SEQUENCE          1
             290 LOAD_CONST               4 (1)
+            292 BUILD_LIST               1
+            294 DUP_TOP
+            296 LOAD_GLOBAL              0 (py_instrument_receiver)
+            298 ROT_TWO
+            300 LOAD_CONST               6 (100)
+            302 LOAD_CONST               4 (1)
+            304 LOAD_CONST              24 (10)
+            306 LOAD_CONST               4 (1)
+            308 LOAD_CONST               5 (True)
+            310 CALL_FUNCTION            6
+            312 POP_TOP
+            314 UNPACK_SEQUENCE          1
+            316 BUILD_LIST               2
+            318 DUP_TOP
+            320 LOAD_GLOBAL              0 (py_instrument_receiver)
+            322 ROT_TWO
+            324 LOAD_CONST              25 (24)
+            326 LOAD_CONST               0 (None)
+            328 LOAD_CONST              26 (11)
+            330 LOAD_CONST               4 (1)
+            332 LOAD_CONST              10 (False)
+            334 CALL_FUNCTION            6
+            336 POP_TOP
+            338 LOAD_GLOBAL              1 (reversed)
+            340 ROT_TWO
+            342 CALL_FUNCTION            1
+            344 UNPACK_SEQUENCE          2
             346 BINARY_SUBTRACT
+            348 BUILD_LIST               1
+            350 DUP_TOP
+            352 LOAD_GLOBAL              0 (py_instrument_receiver)
+            354 ROT_TWO
+            356 LOAD_CONST              25 (24)
+            358 LOAD_CONST               0 (None)
+            360 LOAD_CONST              26 (11)
+            362 LOAD_CONST               4 (1)
+            364 LOAD_CONST               5 (True)
+            366 CALL_FUNCTION            6
+            368 POP_TOP
+            370 UNPACK_SEQUENCE          1
+            372 BUILD_LIST               2
+            374 DUP_TOP
+            376 LOAD_GLOBAL              0 (py_instrument_receiver)
+            378 ROT_TWO
+            380 LOAD_CONST              27 (131)
+            382 LOAD_CONST               4 (1)
+            384 LOAD_CONST              28 (12)
+            386 LOAD_CONST               4 (1)
+            388 LOAD_CONST              10 (False)
+            390 CALL_FUNCTION            6
+            392 POP_TOP
+            394 LOAD_GLOBAL              1 (reversed)
+            396 ROT_TWO
+            398 CALL_FUNCTION            1
+            400 UNPACK_SEQUENCE          2
             402 CALL_FUNCTION            1
+            404 BUILD_LIST               1
+            406 DUP_TOP
+            408 LOAD_GLOBAL              0 (py_instrument_receiver)
+            410 ROT_TWO
+            412 LOAD_CONST              27 (131)
+            414 LOAD_CONST               4 (1)
+            416 LOAD_CONST              28 (12)
+            418 LOAD_CONST               4 (1)
+            420 LOAD_CONST               5 (True)
+            422 CALL_FUNCTION            6
+            424 POP_TOP
+            426 UNPACK_SEQUENCE          1
+            428 BUILD_LIST               2
+            430 DUP_TOP
+            432 LOAD_GLOBAL              0 (py_instrument_receiver)
+            434 ROT_TWO
+            436 LOAD_CONST              29 (20)
+            438 LOAD_CONST               0 (None)
+            440 LOAD_CONST              30 (13)
+            442 LOAD_CONST               4 (1)
+            444 LOAD_CONST              10 (False)
+            446 CALL_FUNCTION            6
+            448 POP_TOP
+            450 LOAD_GLOBAL              1 (reversed)
+            452 ROT_TWO
+            454 CALL_FUNCTION            1
+            456 UNPACK_SEQUENCE          2
             458 BINARY_MULTIPLY
+            460 BUILD_LIST               1
+            462 DUP_TOP
+            464 LOAD_GLOBAL              0 (py_instrument_receiver)
+            466 ROT_TWO
+            468 LOAD_CONST              29 (20)
+            470 LOAD_CONST               0 (None)
+            472 LOAD_CONST              30 (13)
+            474 LOAD_CONST               4 (1)
+            476 LOAD_CONST               5 (True)
+            478 CALL_FUNCTION            6
+            480 POP_TOP
+            482 UNPACK_SEQUENCE          1
+            484 BUILD_LIST               1
+            486 DUP_TOP
+            488 LOAD_GLOBAL              0 (py_instrument_receiver)
+            490 ROT_TWO
+            492 LOAD_CONST              16 (83)
+            494 LOAD_CONST               0 (None)
+            496 LOAD_CONST              31 (14)
+            498 LOAD_CONST               4 (1)
+            500 LOAD_CONST              10 (False)
+            502 CALL_FUNCTION            6
+            504 POP_TOP
+            506 UNPACK_SEQUENCE          1
             508 RETURN_VALUE
             510 LOAD_CONST               0 (None)
+            512 BUILD_LIST               1
+            514 DUP_TOP
+            516 LOAD_GLOBAL              0 (py_instrument_receiver)
+            518 ROT_TWO
+            520 LOAD_CONST               6 (100)
+            522 LOAD_CONST               0 (None)
+            524 LOAD_CONST              32 (15)
+            526 LOAD_CONST               4 (1)
+            528 LOAD_CONST               5 (True)
+            530 CALL_FUNCTION            6
+            532 POP_TOP
+            534 UNPACK_SEQUENCE          1
+            536 BUILD_LIST               1
+            538 DUP_TOP
+            540 LOAD_GLOBAL              0 (py_instrument_receiver)
+            542 ROT_TWO
+            544 LOAD_CONST              16 (83)
+            546 LOAD_CONST               0 (None)
+            548 LOAD_CONST              33 (16)
+            550 LOAD_CONST               4 (1)
+            552 LOAD_CONST              10 (False)
+            554 CALL_FUNCTION            6
+            556 POP_TOP
+            558 UNPACK_SEQUENCE          1
             560 RETURN_VALUE
'''

snapshots['test_list_map (1, 3, 7)'] = '''
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
              26 LOAD_CONST               4 (2)
+             28 BUILD_LIST               1
+             30 DUP_TOP
+             32 LOAD_GLOBAL              0 (py_instrument_receiver)
+             34 ROT_TWO
+             36 LOAD_CONST               1 (100)
+             38 LOAD_CONST               4 (2)
+             40 LOAD_CONST               0 (1)
+             42 LOAD_CONST               2 (0)
+             44 LOAD_CONST               3 (True)
+             46 CALL_FUNCTION            6
+             48 POP_TOP
+             50 UNPACK_SEQUENCE          1
              52 LOAD_CONST               5 (3)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               5 (3)
+             66 LOAD_CONST               4 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
              78 BUILD_LIST               3
+             80 BUILD_LIST               1
+             82 DUP_TOP
+             84 LOAD_GLOBAL              0 (py_instrument_receiver)
+             86 ROT_TWO
+             88 LOAD_CONST               6 (90)
+             90 LOAD_CONST               7 ('my_arr')
+             92 LOAD_CONST               8 (4)
+             94 LOAD_CONST               2 (0)
+             96 LOAD_CONST               9 (False)
+             98 CALL_FUNCTION            6
+            100 POP_TOP
+            102 UNPACK_SEQUENCE          1
             104 STORE_NAME               1 (my_arr)
+  3         106 LOAD_GLOBAL              0 (py_instrument_receiver)
+            108 BUILD_LIST               0
+            110 LOAD_CONST              10 (120)
+            112 LOAD_CONST              11 ('label')
+            114 LOAD_CONST              12 (26)
+            116 BUILD_MAP                1
+            118 LOAD_CONST              13 (5)
+            120 LOAD_CONST               2 (0)
+            122 LOAD_CONST               9 (False)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
             128 EXTENDED_ARG             1
             130 SETUP_LOOP             490 (to 622)
+            132 LOAD_NAME                2 (range)
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              0 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST              14 (101)
+            144 LOAD_CONST              15 ('range')
+            146 LOAD_CONST              16 (6)
+            148 LOAD_CONST               2 (0)
+            150 LOAD_CONST               3 (True)
+            152 CALL_FUNCTION            6
+            154 POP_TOP
             156 UNPACK_SEQUENCE          1
+            158 LOAD_CONST               2 (0)
+            160 BUILD_LIST               1
+            162 DUP_TOP
+            164 LOAD_GLOBAL              0 (py_instrument_receiver)
+            166 ROT_TWO
+            168 LOAD_CONST               1 (100)
+            170 LOAD_CONST               2 (0)
+            172 LOAD_CONST              17 (7)
+            174 LOAD_CONST               2 (0)
+            176 LOAD_CONST               3 (True)
+            178 CALL_FUNCTION            6
+            180 POP_TOP
             182 UNPACK_SEQUENCE          1
+            184 LOAD_CONST               5 (3)
+            186 BUILD_LIST               1
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST               1 (100)
+            196 LOAD_CONST               5 (3)
+            198 LOAD_CONST              18 (8)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               3 (True)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 UNPACK_SEQUENCE          1
+            210 BUILD_LIST               3
+            212 DUP_TOP
+            214 LOAD_GLOBAL              0 (py_instrument_receiver)
+            216 ROT_TWO
+            218 LOAD_CONST              19 (131)
+            220 LOAD_CONST               4 (2)
+            222 LOAD_CONST              20 (9)
+            224 LOAD_CONST               2 (0)
+            226 LOAD_CONST               9 (False)
+            228 CALL_FUNCTION            6
+            230 POP_TOP
+            232 LOAD_GLOBAL              3 (reversed)
+            234 ROT_TWO
+            236 CALL_FUNCTION            1
             238 UNPACK_SEQUENCE          3
+            240 CALL_FUNCTION            2
+            242 BUILD_LIST               1
+            244 DUP_TOP
+            246 LOAD_GLOBAL              0 (py_instrument_receiver)
+            248 ROT_TWO
+            250 LOAD_CONST              19 (131)
+            252 LOAD_CONST               4 (2)
+            254 LOAD_CONST              20 (9)
+            256 LOAD_CONST               2 (0)
+            258 LOAD_CONST               3 (True)
+            260 CALL_FUNCTION            6
+            262 POP_TOP
             264 UNPACK_SEQUENCE          1
+            266 GET_ITER
+        >>  268 LOAD_GLOBAL              0 (py_instrument_receiver)
+            270 BUILD_LIST               0
+            272 LOAD_CONST              21 ('JUMP_TARGET')
+            274 LOAD_CONST              11 ('label')
+            276 LOAD_CONST              22 (12)
+            278 BUILD_MAP                1
+            280 LOAD_CONST              23 (11)
+            282 LOAD_CONST               2 (0)
+            284 LOAD_CONST               9 (False)
+            286 CALL_FUNCTION            6
             288 POP_TOP
+            290 EXTENDED_ARG             1
+            292 FOR_ITER               304 (to 598)
+            294 BUILD_LIST               1
+            296 DUP_TOP
+            298 LOAD_GLOBAL              0 (py_instrument_receiver)
+            300 ROT_TWO
+            302 LOAD_CONST               6 (90)
+            304 LOAD_CONST              24 ('i')
+            306 LOAD_CONST              25 (13)
+            308 LOAD_CONST               2 (0)
+            310 LOAD_CONST               9 (False)
+            312 CALL_FUNCTION            6
             314 POP_TOP
             316 UNPACK_SEQUENCE          1
+            318 STORE_NAME               4 (i)
+  4         320 LOAD_NAME                1 (my_arr)
+            322 BUILD_LIST               1
+            324 DUP_TOP
+            326 LOAD_GLOBAL              0 (py_instrument_receiver)
+            328 ROT_TWO
+            330 LOAD_CONST              14 (101)
+            332 LOAD_CONST               7 ('my_arr')
+            334 LOAD_CONST              26 (14)
+            336 LOAD_CONST               2 (0)
+            338 LOAD_CONST               3 (True)
+            340 CALL_FUNCTION            6
             342 POP_TOP
+            344 UNPACK_SEQUENCE          1
+            346 LOAD_NAME                4 (i)
+            348 BUILD_LIST               1
+            350 DUP_TOP
+            352 LOAD_GLOBAL              0 (py_instrument_receiver)
+            354 ROT_TWO
+            356 LOAD_CONST              14 (101)
+            358 LOAD_CONST              24 ('i')
+            360 LOAD_CONST              27 (15)
+            362 LOAD_CONST               2 (0)
+            364 LOAD_CONST               3 (True)
+            366 CALL_FUNCTION            6
+            368 POP_TOP
+            370 UNPACK_SEQUENCE          1
+            372 BUILD_LIST               2
+            374 DUP_TOP
+            376 LOAD_GLOBAL              0 (py_instrument_receiver)
+            378 ROT_TWO
+            380 LOAD_CONST              28 (25)
+            382 LOAD_CONST              29 (None)
+            384 LOAD_CONST              30 (16)
+            386 LOAD_CONST               2 (0)
+            388 LOAD_CONST               9 (False)
+            390 CALL_FUNCTION            6
+            392 POP_TOP
+            394 LOAD_GLOBAL              3 (reversed)
+            396 ROT_TWO
             398 CALL_FUNCTION            1
+            400 UNPACK_SEQUENCE          2
+            402 BINARY_SUBSCR
+            404 BUILD_LIST               1
+            406 DUP_TOP
+            408 LOAD_GLOBAL              0 (py_instrument_receiver)
+            410 ROT_TWO
+            412 LOAD_CONST              28 (25)
+            414 LOAD_CONST              29 (None)
+            416 LOAD_CONST              30 (16)
+            418 LOAD_CONST               2 (0)
+            420 LOAD_CONST               3 (True)
+            422 CALL_FUNCTION            6
             424 POP_TOP
+            426 UNPACK_SEQUENCE          1
+            428 LOAD_CONST               0 (1)
+            430 BUILD_LIST               1
+            432 DUP_TOP
+            434 LOAD_GLOBAL              0 (py_instrument_receiver)
+            436 ROT_TWO
+            438 LOAD_CONST               1 (100)
+            440 LOAD_CONST               0 (1)
+            442 LOAD_CONST              31 (17)
+            444 LOAD_CONST               2 (0)
+            446 LOAD_CONST               3 (True)
+            448 CALL_FUNCTION            6
+            450 POP_TOP
+            452 UNPACK_SEQUENCE          1
+            454 BUILD_LIST               2
+            456 DUP_TOP
+            458 LOAD_GLOBAL              0 (py_instrument_receiver)
+            460 ROT_TWO
+            462 LOAD_CONST              32 (23)
+            464 LOAD_CONST              29 (None)
+            466 LOAD_CONST              33 (18)
+            468 LOAD_CONST               2 (0)
+            470 LOAD_CONST               9 (False)
+            472 CALL_FUNCTION            6
+            474 POP_TOP
+            476 LOAD_GLOBAL              3 (reversed)
+            478 ROT_TWO
             480 CALL_FUNCTION            1
+            482 UNPACK_SEQUENCE          2
+            484 BINARY_ADD
+            486 BUILD_LIST               1
+            488 DUP_TOP
+            490 LOAD_GLOBAL              0 (py_instrument_receiver)
+            492 ROT_TWO
+            494 LOAD_CONST              32 (23)
+            496 LOAD_CONST              29 (None)
+            498 LOAD_CONST              33 (18)
+            500 LOAD_CONST               2 (0)
+            502 LOAD_CONST               3 (True)
+            504 CALL_FUNCTION            6
             506 POP_TOP
+            508 UNPACK_SEQUENCE          1
+            510 LOAD_NAME                1 (my_arr)
+            512 BUILD_LIST               1
+            514 DUP_TOP
+            516 LOAD_GLOBAL              0 (py_instrument_receiver)
+            518 ROT_TWO
+            520 LOAD_CONST              14 (101)
+            522 LOAD_CONST               7 ('my_arr')
+            524 LOAD_CONST              34 (19)
+            526 LOAD_CONST               2 (0)
+            528 LOAD_CONST               3 (True)
+            530 CALL_FUNCTION            6
             532 POP_TOP
+            534 UNPACK_SEQUENCE          1
+            536 LOAD_NAME                4 (i)
+            538 BUILD_LIST               1
+            540 DUP_TOP
+            542 LOAD_GLOBAL              0 (py_instrument_receiver)
+            544 ROT_TWO
+            546 LOAD_CONST              14 (101)
+            548 LOAD_CONST              24 ('i')
+            550 LOAD_CONST              35 (20)
+            552 LOAD_CONST               2 (0)
+            554 LOAD_CONST               3 (True)
+            556 CALL_FUNCTION            6
+            558 POP_TOP
+            560 UNPACK_SEQUENCE          1
+            562 BUILD_LIST               3
+            564 DUP_TOP
+            566 LOAD_GLOBAL              0 (py_instrument_receiver)
+            568 ROT_TWO
+            570 LOAD_CONST              36 (60)
+            572 LOAD_CONST              29 (None)
+            574 LOAD_CONST              37 (21)
+            576 LOAD_CONST               2 (0)
+            578 LOAD_CONST               9 (False)
+            580 CALL_FUNCTION            6
+            582 POP_TOP
+            584 LOAD_GLOBAL              3 (reversed)
+            586 ROT_TWO
             588 CALL_FUNCTION            1
             590 UNPACK_SEQUENCE          3
+            592 STORE_SUBSCR
+            594 EXTENDED_ARG             1
+            596 JUMP_ABSOLUTE          268
+        >>  598 LOAD_GLOBAL              0 (py_instrument_receiver)
+            600 BUILD_LIST               0
+            602 LOAD_CONST              21 ('JUMP_TARGET')
+            604 LOAD_CONST              11 ('label')
+            606 LOAD_CONST              38 (24)
+            608 BUILD_MAP                1
+            610 LOAD_CONST              32 (23)
+            612 LOAD_CONST               2 (0)
             614 LOAD_CONST               9 (False)
+            616 CALL_FUNCTION            6
+            618 POP_TOP
+            620 POP_BLOCK
+        >>  622 LOAD_GLOBAL              0 (py_instrument_receiver)
+            624 BUILD_LIST               0
+            626 LOAD_CONST              21 ('JUMP_TARGET')
+            628 LOAD_CONST              11 ('label')
+            630 LOAD_CONST              12 (26)
+            632 BUILD_MAP                1
+            634 LOAD_CONST              28 (25)
+            636 LOAD_CONST               2 (0)
             638 LOAD_CONST               9 (False)
+            640 CALL_FUNCTION            6
+            642 POP_TOP
+            644 LOAD_CONST              29 (None)
+            646 BUILD_LIST               1
+            648 DUP_TOP
+            650 LOAD_GLOBAL              0 (py_instrument_receiver)
+            652 ROT_TWO
+            654 LOAD_CONST               1 (100)
+            656 LOAD_CONST              29 (None)
+            658 LOAD_CONST              12 (26)
+            660 LOAD_CONST               2 (0)
+            662 LOAD_CONST               3 (True)
+            664 CALL_FUNCTION            6
+            666 POP_TOP
+            668 UNPACK_SEQUENCE          1
+            670 BUILD_LIST               1
+            672 DUP_TOP
+            674 LOAD_GLOBAL              0 (py_instrument_receiver)
+            676 ROT_TWO
+            678 LOAD_CONST              39 (83)
+            680 LOAD_CONST              29 (None)
+            682 LOAD_CONST              40 (27)
+            684 LOAD_CONST               2 (0)
+            686 LOAD_CONST               9 (False)
             688 CALL_FUNCTION            6
'''

snapshots['test_list_map (2, 3, 7)'] = [
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            3
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 104,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': {
            'label': 638
        },
        'code': '<module>',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 128,
        'stack': [
        ]
    },
    {
        'arg': 'range',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 130,
        'stack': [
            GenericRepr("<class 'range'>")
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 156,
        'stack': [
            0
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 182,
        'stack': [
            3
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 238,
        'stack': [
            GenericRepr("<class 'range'>"),
            0,
            3
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 238,
        'stack': [
            GenericRepr('range(0, 3)')
        ]
    },
    {
        'arrive_at': 288
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 314,
        'stack': [
            0
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 316,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 342,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
        'stack': [
            [
                2,
                3,
                4
            ],
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 424,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            2
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 506,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 532,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 588,
        'stack': [
            2,
            [
                2,
                3,
                4
            ],
            0
        ]
    },
    {
        'arrive_at': 288
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 314,
        'stack': [
            1
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 316,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 342,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
        'stack': [
            [
                2,
                3,
                4
            ],
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 424,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            3
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 506,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 532,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 588,
        'stack': [
            3,
            [
                2,
                3,
                4
            ],
            1
        ]
    },
    {
        'arrive_at': 288
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 314,
        'stack': [
            2
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 316,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 342,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
        'stack': [
            [
                2,
                3,
                4
            ],
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_SUBSCR',
        'orig_op': 398,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 424,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            3,
            1
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'BINARY_ADD',
        'orig_op': 480,
        'stack': [
            4
        ]
    },
    {
        'arg': 'my_arr',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 506,
        'stack': [
            [
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'i',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 532,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_SUBSCR',
        'orig_op': 588,
        'stack': [
            4,
            [
                2,
                3,
                4
            ],
            2
        ]
    },
    {
        'arrive_at': 288
    },
    {
        'arrive_at': 614
    },
    {
        'arrive_at': 638
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 638,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 688,
        'stack': [
            None
        ]
    }
]

snapshots['test_nonlocal_load (1, 3, 7)'] = '''
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
   7         134 LOAD_NAME                2 (f)
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
             160 LOAD_CONST               2 (0)
+            162 BUILD_LIST               1
+            164 DUP_TOP
+            166 LOAD_GLOBAL              0 (py_instrument_receiver)
+            168 ROT_TWO
+            170 LOAD_CONST               1 (100)
+            172 LOAD_CONST               2 (0)
+            174 LOAD_CONST              13 (5)
+            176 LOAD_CONST               2 (0)
+            178 LOAD_CONST               3 (True)
+            180 CALL_FUNCTION            6
+            182 POP_TOP
+            184 UNPACK_SEQUENCE          1
+            186 BUILD_LIST               2
+            188 DUP_TOP
+            190 LOAD_GLOBAL              0 (py_instrument_receiver)
+            192 ROT_TWO
+            194 LOAD_CONST              14 (131)
+            196 LOAD_CONST               5 (1)
+            198 LOAD_CONST              15 (6)
+            200 LOAD_CONST               2 (0)
+            202 LOAD_CONST               8 (False)
+            204 CALL_FUNCTION            6
+            206 POP_TOP
+            208 LOAD_GLOBAL              1 (reversed)
+            210 ROT_TWO
+            212 CALL_FUNCTION            1
+            214 UNPACK_SEQUENCE          2
             216 CALL_FUNCTION            1
+            218 BUILD_LIST               1
+            220 DUP_TOP
+            222 LOAD_GLOBAL              0 (py_instrument_receiver)
+            224 ROT_TWO
+            226 LOAD_CONST              14 (131)
+            228 LOAD_CONST               5 (1)
+            230 LOAD_CONST              15 (6)
+            232 LOAD_CONST               2 (0)
+            234 LOAD_CONST               3 (True)
+            236 CALL_FUNCTION            6
+            238 POP_TOP
+            240 UNPACK_SEQUENCE          1
+            242 BUILD_LIST               1
+            244 DUP_TOP
+            246 LOAD_GLOBAL              0 (py_instrument_receiver)
+            248 ROT_TWO
+            250 LOAD_CONST               5 (1)
+            252 LOAD_CONST              16 (None)
+            254 LOAD_CONST              17 (7)
+            256 LOAD_CONST               2 (0)
+            258 LOAD_CONST               8 (False)
+            260 CALL_FUNCTION            6
+            262 POP_TOP
+            264 UNPACK_SEQUENCE          1
             266 POP_TOP
   8         268 LOAD_NAME                2 (f)
+            270 BUILD_LIST               1
+            272 DUP_TOP
+            274 LOAD_GLOBAL              0 (py_instrument_receiver)
+            276 ROT_TWO
+            278 LOAD_CONST              11 (101)
+            280 LOAD_CONST               4 ('f')
+            282 LOAD_CONST              18 (8)
+            284 LOAD_CONST               2 (0)
+            286 LOAD_CONST               3 (True)
+            288 CALL_FUNCTION            6
+            290 POP_TOP
+            292 UNPACK_SEQUENCE          1
             294 LOAD_CONST               5 (1)
+            296 BUILD_LIST               1
+            298 DUP_TOP
+            300 LOAD_GLOBAL              0 (py_instrument_receiver)
+            302 ROT_TWO
+            304 LOAD_CONST               1 (100)
+            306 LOAD_CONST               5 (1)
+            308 LOAD_CONST              19 (9)
+            310 LOAD_CONST               2 (0)
+            312 LOAD_CONST               3 (True)
+            314 CALL_FUNCTION            6
+            316 POP_TOP
+            318 UNPACK_SEQUENCE          1
+            320 BUILD_LIST               2
+            322 DUP_TOP
+            324 LOAD_GLOBAL              0 (py_instrument_receiver)
+            326 ROT_TWO
+            328 LOAD_CONST              14 (131)
+            330 LOAD_CONST               5 (1)
+            332 LOAD_CONST              20 (10)
+            334 LOAD_CONST               2 (0)
+            336 LOAD_CONST               8 (False)
+            338 CALL_FUNCTION            6
+            340 POP_TOP
+            342 LOAD_GLOBAL              1 (reversed)
+            344 ROT_TWO
+            346 CALL_FUNCTION            1
+            348 UNPACK_SEQUENCE          2
             350 CALL_FUNCTION            1
+            352 BUILD_LIST               1
+            354 DUP_TOP
+            356 LOAD_GLOBAL              0 (py_instrument_receiver)
+            358 ROT_TWO
+            360 LOAD_CONST              14 (131)
+            362 LOAD_CONST               5 (1)
+            364 LOAD_CONST              20 (10)
+            366 LOAD_CONST               2 (0)
+            368 LOAD_CONST               3 (True)
+            370 CALL_FUNCTION            6
+            372 POP_TOP
+            374 UNPACK_SEQUENCE          1
+            376 BUILD_LIST               1
+            378 DUP_TOP
+            380 LOAD_GLOBAL              0 (py_instrument_receiver)
+            382 ROT_TWO
+            384 LOAD_CONST               5 (1)
+            386 LOAD_CONST              16 (None)
+            388 LOAD_CONST              21 (11)
+            390 LOAD_CONST               2 (0)
+            392 LOAD_CONST               8 (False)
+            394 CALL_FUNCTION            6
+            396 POP_TOP
+            398 UNPACK_SEQUENCE          1
             400 POP_TOP
             402 LOAD_CONST              16 (None)
+            404 BUILD_LIST               1
+            406 DUP_TOP
+            408 LOAD_GLOBAL              0 (py_instrument_receiver)
+            410 ROT_TWO
+            412 LOAD_CONST               1 (100)
+            414 LOAD_CONST              16 (None)
+            416 LOAD_CONST              22 (12)
+            418 LOAD_CONST               2 (0)
+            420 LOAD_CONST               3 (True)
+            422 CALL_FUNCTION            6
+            424 POP_TOP
+            426 UNPACK_SEQUENCE          1
+            428 BUILD_LIST               1
+            430 DUP_TOP
+            432 LOAD_GLOBAL              0 (py_instrument_receiver)
+            434 ROT_TWO
+            436 LOAD_CONST              23 (83)
+            438 LOAD_CONST              16 (None)
+            440 LOAD_CONST              24 (13)
+            442 LOAD_CONST               2 (0)
+            444 LOAD_CONST               8 (False)
+            446 CALL_FUNCTION            6
+            448 POP_TOP
+            450 UNPACK_SEQUENCE          1
             452 RETURN_VALUE

Code Object: f
   3           0 LOAD_CLOSURE             0 (i)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              0 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (135)
+             12 LOAD_CONST               2 ('cell')
+             14 LOAD_CONST               3 ('i')
+             16 BUILD_MAP                1
+             18 LOAD_CONST               4 (0)
+             20 LOAD_CONST               5 (1)
+             22 LOAD_CONST               6 (True)
+             24 CALL_FUNCTION            6
+             26 POP_TOP
+             28 UNPACK_SEQUENCE          1
              30 BUILD_TUPLE              1
~             32 LOAD_CONST               7 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+             34 BUILD_LIST               1
+             36 DUP_TOP
+             38 LOAD_GLOBAL              0 (py_instrument_receiver)
+             40 ROT_TWO
+             42 LOAD_CONST               8 (100)
+             44 LOAD_CONST               7 (<code object g at SOME ADDRESS, file "<string>", line 3>)
+             46 LOAD_CONST               9 (2)
+             48 LOAD_CONST               5 (1)
+             50 LOAD_CONST               6 (True)
+             52 CALL_FUNCTION            6
+             54 POP_TOP
+             56 UNPACK_SEQUENCE          1
              58 LOAD_CONST              10 ('f.<locals>.g')
+             60 BUILD_LIST               1
+             62 DUP_TOP
+             64 LOAD_GLOBAL              0 (py_instrument_receiver)
+             66 ROT_TWO
+             68 LOAD_CONST               8 (100)
+             70 LOAD_CONST              10 ('f.<locals>.g')
+             72 LOAD_CONST              11 (3)
+             74 LOAD_CONST               5 (1)
+             76 LOAD_CONST               6 (True)
+             78 CALL_FUNCTION            6
+             80 POP_TOP
+             82 UNPACK_SEQUENCE          1
+             84 BUILD_LIST               2
+             86 DUP_TOP
+             88 LOAD_GLOBAL              0 (py_instrument_receiver)
+             90 ROT_TWO
+             92 LOAD_CONST              12 (132)
+             94 LOAD_CONST              13 (8)
+             96 LOAD_CONST              14 (4)
+             98 LOAD_CONST               5 (1)
+            100 LOAD_CONST              15 (False)
+            102 CALL_FUNCTION            6
+            104 POP_TOP
+            106 LOAD_GLOBAL              1 (reversed)
+            108 ROT_TWO
+            110 CALL_FUNCTION            1
+            112 UNPACK_SEQUENCE          2
             114 MAKE_FUNCTION            8
+            116 BUILD_LIST               1
+            118 DUP_TOP
+            120 LOAD_GLOBAL              0 (py_instrument_receiver)
+            122 ROT_TWO
+            124 LOAD_CONST              12 (132)
+            126 LOAD_CONST              13 (8)
+            128 LOAD_CONST              14 (4)
+            130 LOAD_CONST               5 (1)
+            132 LOAD_CONST               6 (True)
+            134 CALL_FUNCTION            6
+            136 POP_TOP
+            138 UNPACK_SEQUENCE          1
+            140 BUILD_LIST               1
+            142 DUP_TOP
+            144 LOAD_GLOBAL              0 (py_instrument_receiver)
+            146 ROT_TWO
+            148 LOAD_CONST              16 (125)
+            150 LOAD_CONST              17 ('g')
+            152 LOAD_CONST              18 (5)
+            154 LOAD_CONST               5 (1)
+            156 LOAD_CONST              15 (False)
+            158 CALL_FUNCTION            6
+            160 POP_TOP
+            162 UNPACK_SEQUENCE          1
             164 STORE_FAST               1 (g)
   6         166 LOAD_FAST                1 (g)
+            168 BUILD_LIST               1
+            170 DUP_TOP
+            172 LOAD_GLOBAL              0 (py_instrument_receiver)
+            174 ROT_TWO
+            176 LOAD_CONST              19 (124)
+            178 LOAD_CONST              17 ('g')
+            180 LOAD_CONST              20 (6)
+            182 LOAD_CONST               5 (1)
+            184 LOAD_CONST               6 (True)
+            186 CALL_FUNCTION            6
+            188 POP_TOP
+            190 UNPACK_SEQUENCE          1
+            192 BUILD_LIST               1
+            194 DUP_TOP
+            196 LOAD_GLOBAL              0 (py_instrument_receiver)
+            198 ROT_TWO
+            200 LOAD_CONST              21 (131)
+            202 LOAD_CONST               4 (0)
+            204 LOAD_CONST              22 (7)
+            206 LOAD_CONST               5 (1)
+            208 LOAD_CONST              15 (False)
+            210 CALL_FUNCTION            6
+            212 POP_TOP
+            214 UNPACK_SEQUENCE          1
             216 CALL_FUNCTION            0
+            218 BUILD_LIST               1
+            220 DUP_TOP
+            222 LOAD_GLOBAL              0 (py_instrument_receiver)
+            224 ROT_TWO
+            226 LOAD_CONST              21 (131)
+            228 LOAD_CONST               4 (0)
+            230 LOAD_CONST              22 (7)
+            232 LOAD_CONST               5 (1)
+            234 LOAD_CONST               6 (True)
+            236 CALL_FUNCTION            6
+            238 POP_TOP
+            240 UNPACK_SEQUENCE          1
+            242 BUILD_LIST               1
+            244 DUP_TOP
+            246 LOAD_GLOBAL              0 (py_instrument_receiver)
+            248 ROT_TWO
+            250 LOAD_CONST               5 (1)
+            252 LOAD_CONST               0 (None)
+            254 LOAD_CONST              13 (8)
+            256 LOAD_CONST               5 (1)
+            258 LOAD_CONST              15 (False)
+            260 CALL_FUNCTION            6
+            262 POP_TOP
+            264 UNPACK_SEQUENCE          1
             266 POP_TOP
             268 LOAD_CONST               0 (None)
+            270 BUILD_LIST               1
+            272 DUP_TOP
+            274 LOAD_GLOBAL              0 (py_instrument_receiver)
+            276 ROT_TWO
+            278 LOAD_CONST               8 (100)
+            280 LOAD_CONST               0 (None)
+            282 LOAD_CONST              23 (9)
+            284 LOAD_CONST               5 (1)
+            286 LOAD_CONST               6 (True)
+            288 CALL_FUNCTION            6
+            290 POP_TOP
+            292 UNPACK_SEQUENCE          1
+            294 BUILD_LIST               1
+            296 DUP_TOP
+            298 LOAD_GLOBAL              0 (py_instrument_receiver)
+            300 ROT_TWO
+            302 LOAD_CONST              24 (83)
+            304 LOAD_CONST               0 (None)
+            306 LOAD_CONST              25 (10)
+            308 LOAD_CONST               5 (1)
+            310 LOAD_CONST              15 (False)
+            312 CALL_FUNCTION            6
+            314 POP_TOP
+            316 UNPACK_SEQUENCE          1
             318 RETURN_VALUE

Code Object: g
   5           0 LOAD_DEREF               0 (i)
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

snapshots['test_scope_forwarding_loads (1, 3, 7)'] = '''
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
   3          52 LOAD_CONST               7 (2)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              0 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST               1 (100)
+             64 LOAD_CONST               7 (2)
+             66 LOAD_CONST               7 (2)
+             68 LOAD_CONST               2 (0)
+             70 LOAD_CONST               3 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               1
+             80 DUP_TOP
+             82 LOAD_GLOBAL              0 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST               4 (90)
+             88 LOAD_CONST               8 ('y')
+             90 LOAD_CONST               9 (3)
+             92 LOAD_CONST               2 (0)
+             94 LOAD_CONST               6 (False)
+             96 CALL_FUNCTION            6
+             98 POP_TOP
+            100 UNPACK_SEQUENCE          1
             102 STORE_NAME               2 (y)
   4         104 LOAD_CONST               9 (3)
+            106 BUILD_LIST               1
+            108 DUP_TOP
+            110 LOAD_GLOBAL              0 (py_instrument_receiver)
+            112 ROT_TWO
+            114 LOAD_CONST               1 (100)
+            116 LOAD_CONST               9 (3)
+            118 LOAD_CONST              10 (4)
+            120 LOAD_CONST               2 (0)
+            122 LOAD_CONST               3 (True)
+            124 CALL_FUNCTION            6
+            126 POP_TOP
+            128 UNPACK_SEQUENCE          1
+            130 BUILD_LIST               1
+            132 DUP_TOP
+            134 LOAD_GLOBAL              0 (py_instrument_receiver)
+            136 ROT_TWO
+            138 LOAD_CONST               4 (90)
+            140 LOAD_CONST              11 ('z')
+            142 LOAD_CONST              12 (5)
+            144 LOAD_CONST               2 (0)
+            146 LOAD_CONST               6 (False)
+            148 CALL_FUNCTION            6
+            150 POP_TOP
+            152 UNPACK_SEQUENCE          1
             154 STORE_NAME               3 (z)
~  5         156 LOAD_CONST              13 (<code object f1 at SOME ADDRESS, file "<string>", line 5>)
+            158 BUILD_LIST               1
+            160 DUP_TOP
+            162 LOAD_GLOBAL              0 (py_instrument_receiver)
+            164 ROT_TWO
+            166 LOAD_CONST               1 (100)
+            168 LOAD_CONST              13 (<code object f1 at SOME ADDRESS, file "<string>", line 5>)
+            170 LOAD_CONST              14 (6)
+            172 LOAD_CONST               2 (0)
+            174 LOAD_CONST               3 (True)
+            176 CALL_FUNCTION            6
+            178 POP_TOP
+            180 UNPACK_SEQUENCE          1
             182 LOAD_CONST              15 ('f1')
+            184 BUILD_LIST               1
+            186 DUP_TOP
+            188 LOAD_GLOBAL              0 (py_instrument_receiver)
+            190 ROT_TWO
+            192 LOAD_CONST               1 (100)
+            194 LOAD_CONST              15 ('f1')
+            196 LOAD_CONST              16 (7)
+            198 LOAD_CONST               2 (0)
+            200 LOAD_CONST               3 (True)
+            202 CALL_FUNCTION            6
+            204 POP_TOP
+            206 UNPACK_SEQUENCE          1
+            208 BUILD_LIST               2
+            210 DUP_TOP
+            212 LOAD_GLOBAL              0 (py_instrument_receiver)
+            214 ROT_TWO
+            216 LOAD_CONST              17 (132)
+            218 LOAD_CONST               2 (0)
+            220 LOAD_CONST              18 (8)
+            222 LOAD_CONST               2 (0)
+            224 LOAD_CONST               6 (False)
+            226 CALL_FUNCTION            6
+            228 POP_TOP
+            230 LOAD_GLOBAL              4 (reversed)
+            232 ROT_TWO
+            234 CALL_FUNCTION            1
+            236 UNPACK_SEQUENCE          2
             238 MAKE_FUNCTION            0
+            240 BUILD_LIST               1
+            242 DUP_TOP
+            244 LOAD_GLOBAL              0 (py_instrument_receiver)
+            246 ROT_TWO
+            248 LOAD_CONST              17 (132)
+            250 LOAD_CONST               2 (0)
+            252 LOAD_CONST              18 (8)
+            254 LOAD_CONST               2 (0)
+            256 LOAD_CONST               3 (True)
+            258 CALL_FUNCTION            6
+            260 POP_TOP
+            262 UNPACK_SEQUENCE          1
+            264 BUILD_LIST               1
+            266 DUP_TOP
+            268 LOAD_GLOBAL              0 (py_instrument_receiver)
+            270 ROT_TWO
+            272 LOAD_CONST               4 (90)
+            274 LOAD_CONST              15 ('f1')
+            276 LOAD_CONST              19 (9)
+            278 LOAD_CONST               2 (0)
+            280 LOAD_CONST               6 (False)
+            282 CALL_FUNCTION            6
+            284 POP_TOP
+            286 UNPACK_SEQUENCE          1
             288 STORE_NAME               5 (f1)
  19         290 LOAD_NAME                5 (f1)
+            292 BUILD_LIST               1
+            294 DUP_TOP
+            296 LOAD_GLOBAL              0 (py_instrument_receiver)
+            298 ROT_TWO
+            300 LOAD_CONST              20 (101)
+            302 LOAD_CONST              15 ('f1')
+            304 LOAD_CONST              21 (10)
+            306 LOAD_CONST               2 (0)
+            308 LOAD_CONST               3 (True)
+            310 CALL_FUNCTION            6
+            312 POP_TOP
+            314 UNPACK_SEQUENCE          1
+            316 BUILD_LIST               1
+            318 DUP_TOP
+            320 LOAD_GLOBAL              0 (py_instrument_receiver)
+            322 ROT_TWO
+            324 LOAD_CONST              22 (131)
+            326 LOAD_CONST               2 (0)
+            328 LOAD_CONST              23 (11)
+            330 LOAD_CONST               2 (0)
+            332 LOAD_CONST               6 (False)
+            334 CALL_FUNCTION            6
+            336 POP_TOP
+            338 UNPACK_SEQUENCE          1
             340 CALL_FUNCTION            0
+            342 BUILD_LIST               1
+            344 DUP_TOP
+            346 LOAD_GLOBAL              0 (py_instrument_receiver)
+            348 ROT_TWO
+            350 LOAD_CONST              22 (131)
+            352 LOAD_CONST               2 (0)
+            354 LOAD_CONST              23 (11)
+            356 LOAD_CONST               2 (0)
+            358 LOAD_CONST               3 (True)
+            360 CALL_FUNCTION            6
+            362 POP_TOP
+            364 UNPACK_SEQUENCE          1
+            366 BUILD_LIST               1
+            368 DUP_TOP
+            370 LOAD_GLOBAL              0 (py_instrument_receiver)
+            372 ROT_TWO
+            374 LOAD_CONST               0 (1)
+            376 LOAD_CONST              24 (None)
+            378 LOAD_CONST              25 (12)
+            380 LOAD_CONST               2 (0)
+            382 LOAD_CONST               6 (False)
+            384 CALL_FUNCTION            6
+            386 POP_TOP
+            388 UNPACK_SEQUENCE          1
             390 POP_TOP
             392 LOAD_CONST              24 (None)
+            394 BUILD_LIST               1
+            396 DUP_TOP
+            398 LOAD_GLOBAL              0 (py_instrument_receiver)
+            400 ROT_TWO
+            402 LOAD_CONST               1 (100)
+            404 LOAD_CONST              24 (None)
+            406 LOAD_CONST              26 (13)
+            408 LOAD_CONST               2 (0)
+            410 LOAD_CONST               3 (True)
+            412 CALL_FUNCTION            6
+            414 POP_TOP
+            416 UNPACK_SEQUENCE          1
+            418 BUILD_LIST               1
+            420 DUP_TOP
+            422 LOAD_GLOBAL              0 (py_instrument_receiver)
+            424 ROT_TWO
+            426 LOAD_CONST              27 (83)
+            428 LOAD_CONST              24 (None)
+            430 LOAD_CONST              28 (14)
+            432 LOAD_CONST               2 (0)
+            434 LOAD_CONST               6 (False)
+            436 CALL_FUNCTION            6
+            438 POP_TOP
+            440 UNPACK_SEQUENCE          1
             442 RETURN_VALUE

Code Object: f1
   6           0 LOAD_GLOBAL              0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (116)
+             12 LOAD_CONST               2 ('x')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (1)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              1 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (125)
+             36 LOAD_CONST               7 ('test1')
+             38 LOAD_CONST               4 (1)
+             40 LOAD_CONST               4 (1)
+             42 LOAD_CONST               8 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_FAST               0 (test1)
   7          52 LOAD_CONST               9 (4)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST              10 (100)
+             64 LOAD_CONST               9 (4)
+             66 LOAD_CONST              11 (2)
+             68 LOAD_CONST               4 (1)
+             70 LOAD_CONST               5 (True)
+             72 CALL_FUNCTION            6
+             74 POP_TOP
+             76 UNPACK_SEQUENCE          1
+             78 BUILD_LIST               1
+             80 DUP_TOP
+             82 LOAD_GLOBAL              1 (py_instrument_receiver)
+             84 ROT_TWO
+             86 LOAD_CONST              12 (137)
+             88 LOAD_CONST              13 ('cell')
+             90 LOAD_CONST              14 ('w')
+             92 BUILD_MAP                1
+             94 LOAD_CONST              15 (3)
+             96 LOAD_CONST               4 (1)
+             98 LOAD_CONST               8 (False)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
             106 STORE_DEREF              0 (w)
   8         108 LOAD_CONST              16 (5)
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              1 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST              10 (100)
+            120 LOAD_CONST              16 (5)
+            122 LOAD_CONST               9 (4)
+            124 LOAD_CONST               4 (1)
+            126 LOAD_CONST               5 (True)
+            128 CALL_FUNCTION            6
+            130 POP_TOP
+            132 UNPACK_SEQUENCE          1
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              1 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST               6 (125)
+            144 LOAD_CONST              17 ('u')
+            146 LOAD_CONST              16 (5)
+            148 LOAD_CONST               4 (1)
+            150 LOAD_CONST               8 (False)
+            152 CALL_FUNCTION            6
+            154 POP_TOP
+            156 UNPACK_SEQUENCE          1
             158 STORE_FAST               1 (u)
   9         160 LOAD_CLOSURE             0 (w)
+            162 BUILD_LIST               1
+            164 DUP_TOP
+            166 LOAD_GLOBAL              1 (py_instrument_receiver)
+            168 ROT_TWO
+            170 LOAD_CONST              18 (135)
+            172 LOAD_CONST              13 ('cell')
+            174 LOAD_CONST              14 ('w')
+            176 BUILD_MAP                1
+            178 LOAD_CONST              19 (6)
+            180 LOAD_CONST               4 (1)
+            182 LOAD_CONST               5 (True)
+            184 CALL_FUNCTION            6
+            186 POP_TOP
+            188 UNPACK_SEQUENCE          1
             190 BUILD_TUPLE              1
~            192 LOAD_CONST              20 (<code object f2 at SOME ADDRESS, file "<string>", line 9>)
+            194 BUILD_LIST               1
+            196 DUP_TOP
+            198 LOAD_GLOBAL              1 (py_instrument_receiver)
+            200 ROT_TWO
+            202 LOAD_CONST              10 (100)
+            204 LOAD_CONST              20 (<code object f2 at SOME ADDRESS, file "<string>", line 9>)
+            206 LOAD_CONST              21 (8)
+            208 LOAD_CONST               4 (1)
+            210 LOAD_CONST               5 (True)
+            212 CALL_FUNCTION            6
+            214 POP_TOP
+            216 UNPACK_SEQUENCE          1
             218 LOAD_CONST              22 ('f1.<locals>.f2')
+            220 BUILD_LIST               1
+            222 DUP_TOP
+            224 LOAD_GLOBAL              1 (py_instrument_receiver)
+            226 ROT_TWO
+            228 LOAD_CONST              10 (100)
+            230 LOAD_CONST              22 ('f1.<locals>.f2')
+            232 LOAD_CONST              23 (9)
+            234 LOAD_CONST               4 (1)
+            236 LOAD_CONST               5 (True)
+            238 CALL_FUNCTION            6
+            240 POP_TOP
+            242 UNPACK_SEQUENCE          1
+            244 BUILD_LIST               2
+            246 DUP_TOP
+            248 LOAD_GLOBAL              1 (py_instrument_receiver)
+            250 ROT_TWO
+            252 LOAD_CONST              24 (132)
+            254 LOAD_CONST              21 (8)
+            256 LOAD_CONST              25 (10)
+            258 LOAD_CONST               4 (1)
+            260 LOAD_CONST               8 (False)
+            262 CALL_FUNCTION            6
+            264 POP_TOP
+            266 LOAD_GLOBAL              2 (reversed)
+            268 ROT_TWO
+            270 CALL_FUNCTION            1
+            272 UNPACK_SEQUENCE          2
             274 MAKE_FUNCTION            8
+            276 BUILD_LIST               1
+            278 DUP_TOP
+            280 LOAD_GLOBAL              1 (py_instrument_receiver)
+            282 ROT_TWO
+            284 LOAD_CONST              24 (132)
+            286 LOAD_CONST              21 (8)
+            288 LOAD_CONST              25 (10)
+            290 LOAD_CONST               4 (1)
+            292 LOAD_CONST               5 (True)
+            294 CALL_FUNCTION            6
+            296 POP_TOP
+            298 UNPACK_SEQUENCE          1
+            300 BUILD_LIST               1
+            302 DUP_TOP
+            304 LOAD_GLOBAL              1 (py_instrument_receiver)
+            306 ROT_TWO
+            308 LOAD_CONST               6 (125)
+            310 LOAD_CONST              26 ('f2')
+            312 LOAD_CONST              27 (11)
+            314 LOAD_CONST               4 (1)
+            316 LOAD_CONST               8 (False)
+            318 CALL_FUNCTION            6
+            320 POP_TOP
+            322 UNPACK_SEQUENCE          1
             324 STORE_FAST               2 (f2)
  18         326 LOAD_FAST                2 (f2)
+            328 BUILD_LIST               1
+            330 DUP_TOP
+            332 LOAD_GLOBAL              1 (py_instrument_receiver)
+            334 ROT_TWO
+            336 LOAD_CONST              28 (124)
+            338 LOAD_CONST              26 ('f2')
+            340 LOAD_CONST              29 (12)
+            342 LOAD_CONST               4 (1)
+            344 LOAD_CONST               5 (True)
+            346 CALL_FUNCTION            6
+            348 POP_TOP
+            350 UNPACK_SEQUENCE          1
+            352 BUILD_LIST               1
+            354 DUP_TOP
+            356 LOAD_GLOBAL              1 (py_instrument_receiver)
+            358 ROT_TWO
+            360 LOAD_CONST              30 (131)
+            362 LOAD_CONST               3 (0)
+            364 LOAD_CONST              31 (13)
+            366 LOAD_CONST               4 (1)
+            368 LOAD_CONST               8 (False)
+            370 CALL_FUNCTION            6
+            372 POP_TOP
+            374 UNPACK_SEQUENCE          1
             376 CALL_FUNCTION            0
+            378 BUILD_LIST               1
+            380 DUP_TOP
+            382 LOAD_GLOBAL              1 (py_instrument_receiver)
+            384 ROT_TWO
+            386 LOAD_CONST              30 (131)
+            388 LOAD_CONST               3 (0)
+            390 LOAD_CONST              31 (13)
+            392 LOAD_CONST               4 (1)
+            394 LOAD_CONST               5 (True)
+            396 CALL_FUNCTION            6
+            398 POP_TOP
+            400 UNPACK_SEQUENCE          1
+            402 BUILD_LIST               1
+            404 DUP_TOP
+            406 LOAD_GLOBAL              1 (py_instrument_receiver)
+            408 ROT_TWO
+            410 LOAD_CONST               4 (1)
+            412 LOAD_CONST               0 (None)
+            414 LOAD_CONST              32 (14)
+            416 LOAD_CONST               4 (1)
+            418 LOAD_CONST               8 (False)
+            420 CALL_FUNCTION            6
+            422 POP_TOP
+            424 UNPACK_SEQUENCE          1
             426 POP_TOP
             428 LOAD_CONST               0 (None)
+            430 BUILD_LIST               1
+            432 DUP_TOP
+            434 LOAD_GLOBAL              1 (py_instrument_receiver)
+            436 ROT_TWO
+            438 LOAD_CONST              10 (100)
+            440 LOAD_CONST               0 (None)
+            442 LOAD_CONST              33 (15)
+            444 LOAD_CONST               4 (1)
+            446 LOAD_CONST               5 (True)
+            448 CALL_FUNCTION            6
+            450 POP_TOP
+            452 UNPACK_SEQUENCE          1
+            454 BUILD_LIST               1
+            456 DUP_TOP
+            458 LOAD_GLOBAL              1 (py_instrument_receiver)
+            460 ROT_TWO
+            462 LOAD_CONST              34 (83)
+            464 LOAD_CONST               0 (None)
+            466 LOAD_CONST              35 (16)
+            468 LOAD_CONST               4 (1)
+            470 LOAD_CONST               8 (False)
+            472 CALL_FUNCTION            6
+            474 POP_TOP
+            476 UNPACK_SEQUENCE          1
             478 RETURN_VALUE

Code Object: f2
  10           0 LOAD_GLOBAL              0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (116)
+             12 LOAD_CONST               2 ('x')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (2)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              1 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (125)
+             36 LOAD_CONST               7 ('test2')
+             38 LOAD_CONST               8 (1)
+             40 LOAD_CONST               4 (2)
+             42 LOAD_CONST               9 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_FAST               0 (test2)
  11          52 LOAD_DEREF               1 (w)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST              10 (136)
+             64 LOAD_CONST              11 ('free')
+             66 LOAD_CONST              12 ('w')
+             68 BUILD_MAP                1
+             70 LOAD_CONST               4 (2)
+             72 LOAD_CONST               4 (2)
+             74 LOAD_CONST               5 (True)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              1 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               6 (125)
+             92 LOAD_CONST              13 ('test3')
+             94 LOAD_CONST              14 (3)
+             96 LOAD_CONST               4 (2)
+             98 LOAD_CONST               9 (False)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
             106 STORE_FAST               1 (test3)
  12         108 LOAD_CONST              15 (6)
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              1 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST              16 (100)
+            120 LOAD_CONST              15 (6)
+            122 LOAD_CONST              17 (4)
+            124 LOAD_CONST               4 (2)
+            126 LOAD_CONST               5 (True)
+            128 CALL_FUNCTION            6
+            130 POP_TOP
+            132 UNPACK_SEQUENCE          1
+            134 BUILD_LIST               1
+            136 DUP_TOP
+            138 LOAD_GLOBAL              1 (py_instrument_receiver)
+            140 ROT_TWO
+            142 LOAD_CONST              18 (137)
+            144 LOAD_CONST              19 ('cell')
+            146 LOAD_CONST              20 ('u')
+            148 BUILD_MAP                1
+            150 LOAD_CONST              21 (5)
+            152 LOAD_CONST               4 (2)
+            154 LOAD_CONST               9 (False)
+            156 CALL_FUNCTION            6
+            158 POP_TOP
+            160 UNPACK_SEQUENCE          1
             162 STORE_DEREF              0 (u)
  13         164 LOAD_CLOSURE             0 (u)
+            166 BUILD_LIST               1
+            168 DUP_TOP
+            170 LOAD_GLOBAL              1 (py_instrument_receiver)
+            172 ROT_TWO
+            174 LOAD_CONST              22 (135)
+            176 LOAD_CONST              19 ('cell')
+            178 LOAD_CONST              20 ('u')
+            180 BUILD_MAP                1
+            182 LOAD_CONST              15 (6)
+            184 LOAD_CONST               4 (2)
+            186 LOAD_CONST               5 (True)
+            188 CALL_FUNCTION            6
+            190 POP_TOP
+            192 UNPACK_SEQUENCE          1
             194 LOAD_CLOSURE             1 (w)
+            196 BUILD_LIST               1
+            198 DUP_TOP
+            200 LOAD_GLOBAL              1 (py_instrument_receiver)
+            202 ROT_TWO
+            204 LOAD_CONST              22 (135)
+            206 LOAD_CONST              11 ('free')
+            208 LOAD_CONST              12 ('w')
+            210 BUILD_MAP                1
+            212 LOAD_CONST              23 (7)
+            214 LOAD_CONST               4 (2)
+            216 LOAD_CONST               5 (True)
+            218 CALL_FUNCTION            6
+            220 POP_TOP
+            222 UNPACK_SEQUENCE          1
             224 BUILD_TUPLE              2
~            226 LOAD_CONST              24 (<code object f3 at SOME ADDRESS, file "<string>", line 13>)
+            228 BUILD_LIST               1
+            230 DUP_TOP
+            232 LOAD_GLOBAL              1 (py_instrument_receiver)
+            234 ROT_TWO
+            236 LOAD_CONST              16 (100)
+            238 LOAD_CONST              24 (<code object f3 at SOME ADDRESS, file "<string>", line 13>)
+            240 LOAD_CONST              25 (9)
+            242 LOAD_CONST               4 (2)
+            244 LOAD_CONST               5 (True)
+            246 CALL_FUNCTION            6
+            248 POP_TOP
+            250 UNPACK_SEQUENCE          1
             252 LOAD_CONST              26 ('f1.<locals>.f2.<locals>.f3')
+            254 BUILD_LIST               1
+            256 DUP_TOP
+            258 LOAD_GLOBAL              1 (py_instrument_receiver)
+            260 ROT_TWO
+            262 LOAD_CONST              16 (100)
+            264 LOAD_CONST              26 ('f1.<locals>.f2.<locals>.f3')
+            266 LOAD_CONST              27 (10)
+            268 LOAD_CONST               4 (2)
+            270 LOAD_CONST               5 (True)
+            272 CALL_FUNCTION            6
+            274 POP_TOP
+            276 UNPACK_SEQUENCE          1
+            278 BUILD_LIST               2
+            280 DUP_TOP
+            282 LOAD_GLOBAL              1 (py_instrument_receiver)
+            284 ROT_TWO
+            286 LOAD_CONST              28 (132)
+            288 LOAD_CONST              29 (8)
+            290 LOAD_CONST              30 (11)
+            292 LOAD_CONST               4 (2)
+            294 LOAD_CONST               9 (False)
+            296 CALL_FUNCTION            6
+            298 POP_TOP
+            300 LOAD_GLOBAL              2 (reversed)
+            302 ROT_TWO
+            304 CALL_FUNCTION            1
+            306 UNPACK_SEQUENCE          2
             308 MAKE_FUNCTION            8
+            310 BUILD_LIST               1
+            312 DUP_TOP
+            314 LOAD_GLOBAL              1 (py_instrument_receiver)
+            316 ROT_TWO
+            318 LOAD_CONST              28 (132)
+            320 LOAD_CONST              29 (8)
+            322 LOAD_CONST              30 (11)
+            324 LOAD_CONST               4 (2)
+            326 LOAD_CONST               5 (True)
+            328 CALL_FUNCTION            6
+            330 POP_TOP
+            332 UNPACK_SEQUENCE          1
+            334 BUILD_LIST               1
+            336 DUP_TOP
+            338 LOAD_GLOBAL              1 (py_instrument_receiver)
+            340 ROT_TWO
+            342 LOAD_CONST               6 (125)
+            344 LOAD_CONST              31 ('f3')
+            346 LOAD_CONST              32 (12)
+            348 LOAD_CONST               4 (2)
+            350 LOAD_CONST               9 (False)
+            352 CALL_FUNCTION            6
+            354 POP_TOP
+            356 UNPACK_SEQUENCE          1
             358 STORE_FAST               2 (f3)
  17         360 LOAD_FAST                2 (f3)
+            362 BUILD_LIST               1
+            364 DUP_TOP
+            366 LOAD_GLOBAL              1 (py_instrument_receiver)
+            368 ROT_TWO
+            370 LOAD_CONST              33 (124)
+            372 LOAD_CONST              31 ('f3')
+            374 LOAD_CONST              34 (13)
+            376 LOAD_CONST               4 (2)
+            378 LOAD_CONST               5 (True)
+            380 CALL_FUNCTION            6
+            382 POP_TOP
+            384 UNPACK_SEQUENCE          1
+            386 BUILD_LIST               1
+            388 DUP_TOP
+            390 LOAD_GLOBAL              1 (py_instrument_receiver)
+            392 ROT_TWO
+            394 LOAD_CONST              35 (131)
+            396 LOAD_CONST               3 (0)
+            398 LOAD_CONST              36 (14)
+            400 LOAD_CONST               4 (2)
+            402 LOAD_CONST               9 (False)
+            404 CALL_FUNCTION            6
+            406 POP_TOP
+            408 UNPACK_SEQUENCE          1
             410 CALL_FUNCTION            0
+            412 BUILD_LIST               1
+            414 DUP_TOP
+            416 LOAD_GLOBAL              1 (py_instrument_receiver)
+            418 ROT_TWO
+            420 LOAD_CONST              35 (131)
+            422 LOAD_CONST               3 (0)
+            424 LOAD_CONST              36 (14)
+            426 LOAD_CONST               4 (2)
+            428 LOAD_CONST               5 (True)
+            430 CALL_FUNCTION            6
+            432 POP_TOP
+            434 UNPACK_SEQUENCE          1
+            436 BUILD_LIST               1
+            438 DUP_TOP
+            440 LOAD_GLOBAL              1 (py_instrument_receiver)
+            442 ROT_TWO
+            444 LOAD_CONST               8 (1)
+            446 LOAD_CONST               0 (None)
+            448 LOAD_CONST              37 (15)
+            450 LOAD_CONST               4 (2)
+            452 LOAD_CONST               9 (False)
+            454 CALL_FUNCTION            6
+            456 POP_TOP
+            458 UNPACK_SEQUENCE          1
             460 POP_TOP
             462 LOAD_CONST               0 (None)
+            464 BUILD_LIST               1
+            466 DUP_TOP
+            468 LOAD_GLOBAL              1 (py_instrument_receiver)
+            470 ROT_TWO
+            472 LOAD_CONST              16 (100)
+            474 LOAD_CONST               0 (None)
+            476 LOAD_CONST              38 (16)
+            478 LOAD_CONST               4 (2)
+            480 LOAD_CONST               5 (True)
+            482 CALL_FUNCTION            6
+            484 POP_TOP
+            486 UNPACK_SEQUENCE          1
+            488 BUILD_LIST               1
+            490 DUP_TOP
+            492 LOAD_GLOBAL              1 (py_instrument_receiver)
+            494 ROT_TWO
+            496 LOAD_CONST              39 (83)
+            498 LOAD_CONST               0 (None)
+            500 LOAD_CONST              40 (17)
+            502 LOAD_CONST               4 (2)
+            504 LOAD_CONST               9 (False)
+            506 CALL_FUNCTION            6
+            508 POP_TOP
+            510 UNPACK_SEQUENCE          1
             512 RETURN_VALUE

Code Object: f3
  14           0 LOAD_GLOBAL              0 (x)
+              2 BUILD_LIST               1
+              4 DUP_TOP
+              6 LOAD_GLOBAL              1 (py_instrument_receiver)
+              8 ROT_TWO
+             10 LOAD_CONST               1 (116)
+             12 LOAD_CONST               2 ('x')
+             14 LOAD_CONST               3 (0)
+             16 LOAD_CONST               4 (3)
+             18 LOAD_CONST               5 (True)
+             20 CALL_FUNCTION            6
+             22 POP_TOP
+             24 UNPACK_SEQUENCE          1
+             26 BUILD_LIST               1
+             28 DUP_TOP
+             30 LOAD_GLOBAL              1 (py_instrument_receiver)
+             32 ROT_TWO
+             34 LOAD_CONST               6 (125)
+             36 LOAD_CONST               7 ('test4')
+             38 LOAD_CONST               8 (1)
+             40 LOAD_CONST               4 (3)
+             42 LOAD_CONST               9 (False)
+             44 CALL_FUNCTION            6
+             46 POP_TOP
+             48 UNPACK_SEQUENCE          1
              50 STORE_FAST               0 (test4)
  15          52 LOAD_DEREF               1 (w)
+             54 BUILD_LIST               1
+             56 DUP_TOP
+             58 LOAD_GLOBAL              1 (py_instrument_receiver)
+             60 ROT_TWO
+             62 LOAD_CONST              10 (136)
+             64 LOAD_CONST              11 ('free')
+             66 LOAD_CONST              12 ('w')
+             68 BUILD_MAP                1
+             70 LOAD_CONST              13 (2)
+             72 LOAD_CONST               4 (3)
+             74 LOAD_CONST               5 (True)
+             76 CALL_FUNCTION            6
+             78 POP_TOP
+             80 UNPACK_SEQUENCE          1
+             82 BUILD_LIST               1
+             84 DUP_TOP
+             86 LOAD_GLOBAL              1 (py_instrument_receiver)
+             88 ROT_TWO
+             90 LOAD_CONST               6 (125)
+             92 LOAD_CONST              14 ('test5')
+             94 LOAD_CONST               4 (3)
+             96 LOAD_CONST               4 (3)
+             98 LOAD_CONST               9 (False)
+            100 CALL_FUNCTION            6
+            102 POP_TOP
+            104 UNPACK_SEQUENCE          1
             106 STORE_FAST               1 (test5)
  16         108 LOAD_DEREF               0 (u)
+            110 BUILD_LIST               1
+            112 DUP_TOP
+            114 LOAD_GLOBAL              1 (py_instrument_receiver)
+            116 ROT_TWO
+            118 LOAD_CONST              10 (136)
+            120 LOAD_CONST              11 ('free')
+            122 LOAD_CONST              15 ('u')
+            124 BUILD_MAP                1
+            126 LOAD_CONST              16 (4)
+            128 LOAD_CONST               4 (3)
+            130 LOAD_CONST               5 (True)
+            132 CALL_FUNCTION            6
+            134 POP_TOP
+            136 UNPACK_SEQUENCE          1
+            138 BUILD_LIST               1
+            140 DUP_TOP
+            142 LOAD_GLOBAL              1 (py_instrument_receiver)
+            144 ROT_TWO
+            146 LOAD_CONST               6 (125)
+            148 LOAD_CONST              17 ('test6')
+            150 LOAD_CONST              18 (5)
+            152 LOAD_CONST               4 (3)
+            154 LOAD_CONST               9 (False)
+            156 CALL_FUNCTION            6
+            158 POP_TOP
+            160 UNPACK_SEQUENCE          1
             162 STORE_FAST               2 (test6)
             164 LOAD_CONST               0 (None)
+            166 BUILD_LIST               1
+            168 DUP_TOP
+            170 LOAD_GLOBAL              1 (py_instrument_receiver)
+            172 ROT_TWO
+            174 LOAD_CONST              19 (100)
+            176 LOAD_CONST               0 (None)
+            178 LOAD_CONST              20 (6)
+            180 LOAD_CONST               4 (3)
+            182 LOAD_CONST               5 (True)
+            184 CALL_FUNCTION            6
+            186 POP_TOP
+            188 UNPACK_SEQUENCE          1
+            190 BUILD_LIST               1
+            192 DUP_TOP
+            194 LOAD_GLOBAL              1 (py_instrument_receiver)
+            196 ROT_TWO
+            198 LOAD_CONST              21 (83)
+            200 LOAD_CONST               0 (None)
+            202 LOAD_CONST              22 (7)
+            204 LOAD_CONST               4 (3)
+            206 LOAD_CONST               9 (False)
+            208 CALL_FUNCTION            6
+            210 POP_TOP
+            212 UNPACK_SEQUENCE          1
             214 RETURN_VALUE
'''

snapshots['test_nested_iteration (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object myFunc at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object myFunc at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'myFunc'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 82,
        'stack': [
            GenericRepr('<code object myFunc at 0x100000000, file "<string>", line 2>'),
            'myFunc'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 82,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 132,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'myFunc',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 134,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 184,
        'stack': [
            '<function myFunc at SOME ADDRESS>'
        ]
    },
    {
        'arg': -1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            -1
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 50,
        'stack': [
            -1
        ]
    },
    {
        'arg': 'list',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 52,
        'stack': [
            GenericRepr("<class 'list'>")
        ]
    },
    {
        'arg': 'range',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 78,
        'stack': [
            GenericRepr("<class 'range'>")
        ]
    },
    {
        'arg': 5,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 104,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 160,
        'stack': [
            GenericRepr("<class 'range'>"),
            5
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 160,
        'stack': [
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            GenericRepr("<class 'list'>"),
            GenericRepr('range(0, 5)')
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            [
                0,
                1,
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': 'data',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 266,
        'stack': [
            [
                0,
                1,
                2,
                3,
                4
            ]
        ]
    },
    {
        'arg': {
            'label': 1082
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 290,
        'stack': [
        ]
    },
    {
        'arg': 'data',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 292,
        'stack': [
            [
                0,
                1,
                2,
                3,
                4
            ]
        ]
    },
    {
        'arrive_at': 342
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 368,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 370,
        'stack': [
            0
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 396,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            0,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 556
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 506,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 556
    },
    {
        'arg': {
            'label': 1034
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 556,
        'stack': [
        ]
    },
    {
        'arrive_at': 580
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 580,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 606,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 1010
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 716,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 1010
    },
    {
        'arrive_at': 1034
    },
    {
        'arrive_at': 342
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 368,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 370,
        'stack': [
            1
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 396,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            1,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 556
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 506,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 556
    },
    {
        'arg': {
            'label': 1034
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 556,
        'stack': [
        ]
    },
    {
        'arrive_at': 580
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 580,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 606,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            1,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 1010
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 716,
        'stack': [
            True
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 718,
        'stack': [
            -1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 744,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_ADD',
        'orig_op': 800,
        'stack': [
            -1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_ADD',
        'orig_op': 800,
        'stack': [
            0
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 850,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 852,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 878,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 934,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 934,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 984,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 580
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 580,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 606,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 1010
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 716,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 1010
    },
    {
        'arrive_at': 1034
    },
    {
        'arrive_at': 342
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 368,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 370,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 396,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            2,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 556
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 506,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 556
    },
    {
        'arg': {
            'label': 1034
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'SETUP_LOOP',
        'orig_op': 556,
        'stack': [
        ]
    },
    {
        'arrive_at': 580
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 580,
        'stack': [
            2
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 606,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            2,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 1010
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 716,
        'stack': [
            True
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 718,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 744,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_ADD',
        'orig_op': 800,
        'stack': [
            0,
            2
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_ADD',
        'orig_op': 800,
        'stack': [
            2
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 850,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 852,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 878,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 934,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 934,
        'stack': [
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 984,
        'stack': [
            1
        ]
    },
    {
        'arrive_at': 580
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 580,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 606,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            1,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 1010
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 716,
        'stack': [
            True
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 718,
        'stack': [
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 744,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_ADD',
        'orig_op': 800,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_ADD',
        'orig_op': 800,
        'stack': [
            3
        ]
    },
    {
        'arg': 'x',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 850,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 852,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 878,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 934,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'INPLACE_SUBTRACT',
        'orig_op': 934,
        'stack': [
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 984,
        'stack': [
            0
        ]
    },
    {
        'arrive_at': 580
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 580,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 606,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.GT'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 662,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 1010
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 716,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 1010
    },
    {
        'arrive_at': 1034
    },
    {
        'arrive_at': 342
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 368,
        'stack': [
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 370,
        'stack': [
            3
        ]
    },
    {
        'arg': 3,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 396,
        'stack': [
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            3,
            3
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 452,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 556
        },
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 506,
        'stack': [
            True
        ]
    },
    {
        'arrive_at': 1082
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 1082,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'myFunc',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 1132,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 184,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 234,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 236,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 286,
        'stack': [
            None
        ]
    }
]

snapshots['test_factorial (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object factorial at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object factorial at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'factorial'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 82,
        'stack': [
            GenericRepr('<code object factorial at 0x100000000, file "<string>", line 2>'),
            'factorial'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 82,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 132,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'factorial',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 134,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 5,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 160,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            5
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            5
        ]
    },
    {
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            5,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 212
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 212
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 212,
        'stack': [
            5
        ]
    },
    {
        'arg': 'factorial',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 238,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 264,
        'stack': [
            5
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 290,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            5,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            4
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            4
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            4
        ]
    },
    {
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            4,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 212
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 212
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 212,
        'stack': [
            4
        ]
    },
    {
        'arg': 'factorial',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 238,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 264,
        'stack': [
            4
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 290,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            4,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            3
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            3
        ]
    },
    {
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            3,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 212
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 212
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 212,
        'stack': [
            3
        ]
    },
    {
        'arg': 'factorial',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 238,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 264,
        'stack': [
            3
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 290,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            3,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            2
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            2
        ]
    },
    {
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            2,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 212
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 212
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 212,
        'stack': [
            2
        ]
    },
    {
        'arg': 'factorial',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 238,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 264,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 290,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            1
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            1,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            False
        ]
    },
    {
        'arg': {
            'label': 212
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            False
        ]
    },
    {
        'arrive_at': 212
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 212,
        'stack': [
            1
        ]
    },
    {
        'arg': 'factorial',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 238,
        'stack': [
            '<function factorial at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 264,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 290,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_SUBTRACT',
        'orig_op': 346,
        'stack': [
            0
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            '<function factorial at SOME ADDRESS>',
            0
        ]
    },
    {
        'arg': 'i',
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 0,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            0,
            0
        ]
    },
    {
        'arg': {
            'cmp': 'Compare.EQ'
        },
        'code': 'factorial',
        'is_post': True,
        'opcode': 'COMPARE_OP',
        'orig_op': 82,
        'stack': [
            True
        ]
    },
    {
        'arg': {
            'label': 212
        },
        'code': 'factorial',
        'is_post': False,
        'opcode': 'POP_JUMP_IF_FALSE',
        'orig_op': 136,
        'stack': [
            True
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 138,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 188,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            1,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 508,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            2,
            1
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 508,
        'stack': [
            2
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            2
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            3,
            2
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            6
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 508,
        'stack': [
            6
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            6
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            4,
            6
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            24
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 508,
        'stack': [
            24
        ]
    },
    {
        'arg': 1,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 402,
        'stack': [
            24
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            5,
            24
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': True,
        'opcode': 'BINARY_MULTIPLY',
        'orig_op': 458,
        'stack': [
            120
        ]
    },
    {
        'arg': None,
        'code': 'factorial',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 508,
        'stack': [
            120
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            120
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 266,
        'stack': [
            120
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 268,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 318,
        'stack': [
            None
        ]
    }
]

snapshots['test_nonlocal_load (2, 3, 7)'] = [
    {
        'arg': GenericRepr('<code object f at 0x100000000, file "<string>", line 2>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            GenericRepr('<code object f at 0x100000000, file "<string>", line 2>')
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 26,
        'stack': [
            'f'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 82,
        'stack': [
            GenericRepr('<code object f at 0x100000000, file "<string>", line 2>'),
            'f'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 82,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 132,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 134,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 160,
        'stack': [
            0
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            '<function f at SOME ADDRESS>',
            0
        ]
    },
    {
        'arg': {
            'cell': 'i'
        },
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 0,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object g at 0x100000000, file "<string>", line 3>'),
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 32,
        'stack': [
            GenericRepr('<code object g at 0x100000000, file "<string>", line 3>')
        ]
    },
    {
        'arg': 'f.<locals>.g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 58,
        'stack': [
            'f.<locals>.g'
        ]
    },
    {
        'arg': 8,
        'code': 'f',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 114,
        'stack': [
            GenericRepr('<code object g at 0x100000000, file "<string>", line 3>'),
            'f.<locals>.g'
        ]
    },
    {
        'arg': 8,
        'code': 'f',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 114,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 164,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 166,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': {
            'free': 'i'
        },
        'code': 'g',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 0,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': 'g',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 54,
        'stack': [
            0
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 266,
        'stack': [
            0
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 268,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 318,
        'stack': [
            None
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 266,
        'stack': [
            None
        ]
    },
    {
        'arg': 'f',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 268,
        'stack': [
            '<function f at SOME ADDRESS>'
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 294,
        'stack': [
            1
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 350,
        'stack': [
            '<function f at SOME ADDRESS>',
            1
        ]
    },
    {
        'arg': {
            'cell': 'i'
        },
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 0,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object g at 0x100000000, file "<string>", line 3>'),
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 32,
        'stack': [
            GenericRepr('<code object g at 0x100000000, file "<string>", line 3>')
        ]
    },
    {
        'arg': 'f.<locals>.g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 58,
        'stack': [
            'f.<locals>.g'
        ]
    },
    {
        'arg': 8,
        'code': 'f',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 114,
        'stack': [
            GenericRepr('<code object g at 0x100000000, file "<string>", line 3>'),
            'f.<locals>.g'
        ]
    },
    {
        'arg': 8,
        'code': 'f',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 114,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 164,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'g',
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 166,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            '<function f.<locals>.g at SOME ADDRESS>'
        ]
    },
    {
        'arg': {
            'free': 'i'
        },
        'code': 'g',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'g',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 54,
        'stack': [
            1
        ]
    },
    {
        'arg': 0,
        'code': 'f',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 216,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 266,
        'stack': [
            1
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 268,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 318,
        'stack': [
            None
        ]
    },
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 350,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 400,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 402,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 452,
        'stack': [
            None
        ]
    }
]

snapshots['test_scope_forwarding_loads (2, 3, 7)'] = [
    {
        'arg': 1,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 'x',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 50,
        'stack': [
            1
        ]
    },
    {
        'arg': 2,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            2
        ]
    },
    {
        'arg': 'y',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 102,
        'stack': [
            2
        ]
    },
    {
        'arg': 3,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 104,
        'stack': [
            3
        ]
    },
    {
        'arg': 'z',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 154,
        'stack': [
            3
        ]
    },
    {
        'arg': GenericRepr('<code object f1 at 0x100000000, file "<string>", line 5>'),
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 156,
        'stack': [
            GenericRepr('<code object f1 at 0x100000000, file "<string>", line 5>')
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 182,
        'stack': [
            'f1'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 238,
        'stack': [
            GenericRepr('<code object f1 at 0x100000000, file "<string>", line 5>'),
            'f1'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 238,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': False,
        'opcode': 'STORE_NAME',
        'orig_op': 288,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f1',
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_NAME',
        'orig_op': 290,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 340,
        'stack': [
            '<function f1 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'x',
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 'test1',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 50,
        'stack': [
            1
        ]
    },
    {
        'arg': 4,
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 52,
        'stack': [
            4
        ]
    },
    {
        'arg': {
            'cell': 'w'
        },
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_DEREF',
        'orig_op': 106,
        'stack': [
            4
        ]
    },
    {
        'arg': 5,
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 108,
        'stack': [
            5
        ]
    },
    {
        'arg': 'u',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 158,
        'stack': [
            5
        ]
    },
    {
        'arg': {
            'cell': 'w'
        },
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 160,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object f2 at 0x100000000, file "<string>", line 9>'),
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 192,
        'stack': [
            GenericRepr('<code object f2 at 0x100000000, file "<string>", line 9>')
        ]
    },
    {
        'arg': 'f1.<locals>.f2',
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 218,
        'stack': [
            'f1.<locals>.f2'
        ]
    },
    {
        'arg': 8,
        'code': 'f1',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 274,
        'stack': [
            GenericRepr('<code object f2 at 0x100000000, file "<string>", line 9>'),
            'f1.<locals>.f2'
        ]
    },
    {
        'arg': 8,
        'code': 'f1',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 274,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f2',
        'code': 'f1',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 324,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f2',
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 326,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f1',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 376,
        'stack': [
            '<function f1.<locals>.f2 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'x',
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 'test2',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 50,
        'stack': [
            1
        ]
    },
    {
        'arg': {
            'free': 'w'
        },
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 52,
        'stack': [
            4
        ]
    },
    {
        'arg': 'test3',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 106,
        'stack': [
            4
        ]
    },
    {
        'arg': 6,
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 108,
        'stack': [
            6
        ]
    },
    {
        'arg': {
            'cell': 'u'
        },
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_DEREF',
        'orig_op': 162,
        'stack': [
            6
        ]
    },
    {
        'arg': {
            'cell': 'u'
        },
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 164,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': {
            'free': 'w'
        },
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CLOSURE',
        'orig_op': 194,
        'stack': [
            '<cell at SOME ADDRESS: int object at SOME ADDRESS>'
        ]
    },
    {
        'arg': GenericRepr('<code object f3 at 0x100000000, file "<string>", line 13>'),
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 226,
        'stack': [
            GenericRepr('<code object f3 at 0x100000000, file "<string>", line 13>')
        ]
    },
    {
        'arg': 'f1.<locals>.f2.<locals>.f3',
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 252,
        'stack': [
            'f1.<locals>.f2.<locals>.f3'
        ]
    },
    {
        'arg': 8,
        'code': 'f2',
        'is_post': False,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 308,
        'stack': [
            GenericRepr('<code object f3 at 0x100000000, file "<string>", line 13>'),
            'f1.<locals>.f2.<locals>.f3'
        ]
    },
    {
        'arg': 8,
        'code': 'f2',
        'is_post': True,
        'opcode': 'MAKE_FUNCTION',
        'orig_op': 308,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f3',
        'code': 'f2',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 358,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'f3',
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_FAST',
        'orig_op': 360,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 0,
        'code': 'f2',
        'is_post': False,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 410,
        'stack': [
            '<function f1.<locals>.f2.<locals>.f3 at SOME ADDRESS>'
        ]
    },
    {
        'arg': 'x',
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_GLOBAL',
        'orig_op': 0,
        'stack': [
            1
        ]
    },
    {
        'arg': 'test4',
        'code': 'f3',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 50,
        'stack': [
            1
        ]
    },
    {
        'arg': {
            'free': 'w'
        },
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 52,
        'stack': [
            4
        ]
    },
    {
        'arg': 'test5',
        'code': 'f3',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 106,
        'stack': [
            4
        ]
    },
    {
        'arg': {
            'free': 'u'
        },
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_DEREF',
        'orig_op': 108,
        'stack': [
            6
        ]
    },
    {
        'arg': 'test6',
        'code': 'f3',
        'is_post': False,
        'opcode': 'STORE_FAST',
        'orig_op': 162,
        'stack': [
            6
        ]
    },
    {
        'arg': None,
        'code': 'f3',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 164,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f3',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 214,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': 'f2',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 410,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f2',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 460,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f2',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 462,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f2',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 512,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': 'f1',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 376,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f1',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 426,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f1',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 428,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': 'f1',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 478,
        'stack': [
            None
        ]
    },
    {
        'arg': 0,
        'code': '<module>',
        'is_post': True,
        'opcode': 'CALL_FUNCTION',
        'orig_op': 340,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'POP_TOP',
        'orig_op': 390,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': True,
        'opcode': 'LOAD_CONST',
        'orig_op': 392,
        'stack': [
            None
        ]
    },
    {
        'arg': None,
        'code': '<module>',
        'is_post': False,
        'opcode': 'RETURN_VALUE',
        'orig_op': 442,
        'stack': [
            None
        ]
    }
]
