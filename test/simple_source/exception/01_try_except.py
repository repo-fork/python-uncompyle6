# Tests:
#   trystmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK
#               try_middle COME_FROM
#   except_stmt ::= except

try:
    x = 1
except:
    pass

# Tests:
#   trystmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK
#               try_middle COME_FROM
#   except_stmt ::= except_cond1 except_suite
#   except_suite ::= ...

try:
    x = 1
except ImportError:
    pass

try:
    x = 2
except ImportError:
    x = 3
finally:
    x = 4

try:
    x = 1
except ImportError as e:
    x = 2
