#!/usr/bin/env python3
"""Mechanical half of the promo-voice rubric v2 (8 items, deterministic)."""
import re, sys
kr = open(sys.argv[1], encoding='utf-8').read()
sents = [s.strip() for s in re.split(r'(?<=[.다요])\s+', kr) if s.strip()]
def score(name, val, detail):
    print(f"{name} | {val} | {detail}")
    return val
total = 0.0
# A4p: enumeration announcements + article pointer at end
enum = len(re.findall(r'(두|세|네) 가지', kr))
ptr = '[ARTICLE-LINK]' in kr.split('\n\n')[-1] or 'ARTICLE-LINK' in kr[-160:]
total += score('A4p', 1.0 if (enum>=1 and ptr) else 0.5 if (enum>=1 or ptr) else 0.0, f"enum={enum}, end-pointer={ptr}")
# B2: sentence length variation (>=1 sentence >=50 chars AND >=1 <=25 chars)
lens = [len(s) for s in sents]
total += score('B2', 1.0 if (max(lens)>=50 and min(lens)<=25) else 0.5 if max(lens)>=50 else 0.0, f"max={max(lens)}, min={min(lens)}")
# B3: discourse markers 2..5
mk = sum(kr.count(m) for m in ['흥미롭게도','또한','먼저','두 번째로','세 번째로','우선','나아가'])
total += score('B3', 1.0 if 2<=mk<=5 else 0.5 if mk in (1,6) else 0.0, f"markers={mk}")
# B4: rhetorical questions 0 AND short punches <=1
q = kr.count('?')
punch = sum(1 for s in sents if len(s)<=12)
total += score('B4', 1.0 if (q==0 and punch<=1) else 0.5 if (q==0 or punch<=1) else 0.0, f"q={q}, punch={punch}")
# C1: distinct tech terms >=4
terms = [t for t in ['적층체','최외각부','집전','분리막','컬렉터','포일','전극 필름','양극','음극','단자'] if t in kr]
total += score('C1', 1.0 if len(terms)>=4 else 0.5 if len(terms)==3 else 0.0, f"terms={terms}")
# C2: hangul(english) glosses >=3
gloss = re.findall(r'[가-힣][가-힣 ]*\([A-Za-z][A-Za-z .\-]{1,30}\)', kr)
total += score('C2', 1.0 if len(gloss)>=3 else 0.5 if len(gloss)==2 else 0.0, f"gloss={len(gloss)}: {[g[:20] for g in gloss[:5]]}")
# C4: patent number exact
total += score('C4', 1.0 if 'US 2026/0196678 A1' in kr else 0.0, 'exact match' if 'US 2026/0196678 A1' in kr else 'missing/wrong')
# E1: modality on effects — count of '수 있' >= 3
mod = kr.count('수 있')
total += score('E1', 1.0 if mod>=3 else 0.5 if mod==2 else 0.0, f"수있={mod}")
print(f"MECH_SUBTOTAL: {total}/8")
