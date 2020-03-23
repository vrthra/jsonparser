import fuzzingbook.Parser as P

import gjson as gj
print(gj.json_grammar)

myjp = P.IterativeEarleyParser(gj.json_grammar, canonical=True)
print(1)
res = myjp.parse_on('{"a": []}', start_symbol='<start>')
print(2)
for t in res:
    print(t)
