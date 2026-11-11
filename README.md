# you cant cheat me okayy

Run Python commands in PowerShell from `C:\dev\CNCD`. For the Flex/YACC weeks,
run the listed `.exe` from its folder; write the `.l` and `.y` source files in
the exam, not generated `.c`, `.h`, or `.exe` files. Examples show the input
and output.

## Compiler Design (`Cd`)

### Week 1 — Lexical analysis
- **Write:** `Cd/w1/w1-lexical.py`
- **Run:** `py .\Cd\w1\w1-lexical.py`
- **Input:** Enter `int x=10; // comment`, then press **Ctrl+Z** and Enter to finish. Both `// line comments` and `/* block comments */`, spaces, tabs, and newlines are ignored.
- **Output:** `int -> Keyword`, `x -> Identifier`, `= -> Operator`, `10 -> Constant`, `; -> Special Symbol`
- This simplified lexer uses the keywords and tokens listed in its source; the full language token specification was not included in the lab question.

### Week 2 — Lexical analysis with Flex
- **Write:** `Cd/w2/w2-lexer.l`
- **Run:** `.\Cd\w2\w2.exe`
- **Input:** `int x=10; /* comment */`, then press **Ctrl+Z** and Enter to finish input.
- **Output:** `int -> Keyword`, `x -> Identifier`, `= -> Operator`, `10 -> Constant`, `; -> Special Symbol`

### Week 3 — FIRST and FOLLOW
- **Write:** `Cd/w3/w3-first-nd-follow.py`
- **Run:** `py .\Cd\w3\w3-first-nd-follow.py`
- **Input:** None; grammar is in the program.
- **Output:** Prints FIRST and FOLLOW sets. Example: `FIRST( E ) = {'i', '('}`, `FOLLOW( E ) = {')', '$'}`. Set order can vary.

### Week 4 — Predictive parser
- **Write:** `Cd/w4/w4-predictive_parser.py`
- **Run:** `py .\Cd\w4\w4-predictive_parser.py`
- **Input:** `i+i*i`
- **Output:** `Valid String`

### Week 5 — LALR bottom-up parser
- **Write:** `Cd/w5/lalr.y` and `Cd/w5/lalr.l`
- **Run:** `.\Cd\w5\w5-lalr-parser.exe`
- **Grammar:** Arithmetic expressions with identifiers, integers, `+`, `*`, and parentheses. Bison generates an LALR parser from the YACC grammar.
- **Input:** `a+b*c`
- **Output:** `Expression is valid.`
- **Invalid input:** `a+*c` prints a syntax error.
- **Build if needed (from `C:\dev\CNCD\Cd\w5`):** `win_bison -d -o y.tab.c lalr.y`, `win_flex -o lex.yy.c lalr.l`, then `gcc y.tab.c lex.yy.c -o w5-lalr-parser.exe`.

### Week 6.1 — AST using YACC and Flex
- **Write:** `Cd/w6.1/w6.1-bnf-yacc-AST.y` and `Cd/w6.1/bnf-yacc-AST.l`
- **Run:** `.\Cd\w6.1\w6_1.exe`
- **Input:** `a+b*c`
- **Output:**
  ```text
  Abstract Syntax Tree:
  +
    a
    *
      b
      c
  ```

### Week 6.2 — Arithmetic expression syntax check
- **Write:** `Cd/w6.2/w6.2-yacc-arithmetic.y` and `Cd/w6.2/yacc-arithmetic.l`
- **Run:** `.\Cd\w6.2\w6_2.exe`
- **Input:** `a+b*c`
- **Output:** `Valid Expression`

### Week 7 — Arithmetic operations with YACC and Flex
- **Write:** `Cd/w7/w7-arithmetic.y` and `Cd/w7/w7-arithmetic.l`
- **Run:** `.\Cd\w7\w7-arithmetic.exe`
- **Input:** `2+3*(4-1)`
- **Output:** `Result: 11`
- **Build if needed (from `C:\dev\CNCD\Cd\w7`):** `win_bison -d -o y.tab.c w7-arithmetic.y`, `win_flex -o lex.yy.c w7-arithmetic.l`, then `gcc y.tab.c lex.yy.c -o w7-arithmetic.exe`.

### Week 8.1 — Three-address code
- **Write:** `Cd/w8.1/w8.1-three-address-code.py`
- **Run:** `py .\Cd\w8.1\w8.1-three-address-code.py`
- **Input:** `result=(a+b)*(c-d)`
- **Output:**
  ```text
  Three-address code:
  t1 = a + b
  t2 = c - d
  t3 = t1 * t2
  result = t3
  ```
- The code fragment is an example because the actual fragment was not supplied. The program generates three-address code from Python's expression tree.

### Week 8.2 — AST and stack-machine instructions
- **Write:** `Cd/w8.2/w8.2-ast-machine-code.py`
- **Run:** `py .\Cd\w8.2\w8.2-ast-machine-code.py`
- **Input:** `a+b*c`
- **Output:**
  ```text
  Abstract syntax tree:
  Operator: +
    Variable: a
    Operator: *
      Variable: b
      Variable: c

  Stack-machine instructions:
  PUSH a
  PUSH b
  PUSH c
  MUL
  ADD
  ```
- These are educational stack-machine instructions, not machine code for a specified processor.

## Computer Networks (`Cn`)

### Week 9 — Framing and stuffing
- **Write:** `Cn/w9-dll.py`
- **Run:** `py .\Cn\w9-dll.py`
- **Input:** Character data `ABC`, then bit data `11111011111`
- **Output:**
  ```text
  Character Framing: FLAGABCFLAG
  Character Stuffing: FLAGABCFLAG
  Bit Stuffing: 01111110111110011111001111110
  ```

### Week 10 — CRC
- **Write:** `Cn/w10-CRC.py`
- **Run:** `py .\Cn\w10-CRC.py`
- **Input:** `123456789`
- **Output:**
  ```text
  CRC-12 (0x80F): F5B
  CRC-16 (0x8005): FEE8
  CRC-CCITT (0x1021): 31C3
  ```

### Week 11 — Basic networking commands
- **Write:** Commands and descriptions in `Cn/w11-netwk-cmd.txt`
- **Run:** Type each command in PowerShell or Command Prompt: `ipconfig`, `ipconfig /all`, `ping google.com`, `tracert google.com`, `nslookup google.com`, `netstat`, `arp -a`, `hostname`, `getmac`
- **Input:** No program input. `ping`, `tracert`, and `nslookup` use `google.com` as the example host.
- **Output:** Your computer/network details; for example, `ping` reports `Reply from <IP>: bytes=32 time=... TTL=...`. Values depend on your network.

### Week 12 — Connect two computers
- **Write:** Procedure in `Cn/w12-connection.txt`
- **Run:** On each computer, use `ipconfig`, then ping the other computer: `ping <other-computer-IPv4>`
- **Input:** The other computer's actual IPv4 address (the file uses `192.168.1.11` as an example).
- **Output:** `Reply from 192.168.1.11: bytes=32 time<1ms TTL=128` (example; address and timing vary).

### Week 13 — FTP file sharing
- **Write:** Procedure in `Cn/w13-ftp-filesharing.txt`
- **Run:** Set up the IIS FTP site, then connect with `ftp <server-ip>`. At the `ftp>` prompt use `dir`, `get test.txt`, `put filename`, or `bye`.
- **Input:** Server IP, login credentials, and file name.
- **Output:** Example connection messages: `220 Microsoft FTP Service`, `230 User logged in.`; successful transfer: `226 Transfer complete.` The example setup disables SSL, so use only in a trusted lab network.

### Week 14 — Dijkstra shortest paths
- **Write:** `Cn/w14-dijkstra.py`
- **Run:** `py .\Cn\w14-dijkstra.py`
- **Input:**
  ```text
  4
  0 3 0 7
  8 0 2 0
  5 0 0 1
  2 0 0 0
  0
  ```
  Enter these as: vertex count, four cost-matrix rows, then source vertex.
  A matrix `0` between different vertices means no edge. Dijkstra requires
  non-negative weights; vertices with no path are shown as `Unreachable`.
- **Output:**
  ```text
  Shortest distances from vertex 0
  Vertex 0 = 0
  Vertex 1 = 3
  Vertex 2 = 5
  Vertex 3 = 6

  Shortest Paths:
  0 = 0
  0 -> 1 = 3
  0 -> 1 -> 2 = 5
  0 -> 1 -> 2 -> 3 = 6
  ```
