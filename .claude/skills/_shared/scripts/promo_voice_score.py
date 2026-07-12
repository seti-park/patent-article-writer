#!/usr/bin/env python3
"""Mechanical half of the promo-voice rubric v2 (8 items, deterministic).

Default mode scores a KR long-form promo post (8 items).
Pass --en to score an EN promo thread (6 items; see promo-voice-rubric.md).
"""
import argparse
import re
import sys


def score(name, val, detail):
    print(f"{name} | {val} | {detail}")
    return val


def _score_kr(path):
    kr = open(path, encoding='utf-8').read()
    sents = [s.strip() for s in re.split(r'(?<=[.다요])\s+', kr) if s.strip()]
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


def _split_posts(text):
    """Split EN thread text into post bodies.

    Prefer literal ``[Post N]`` marker lines; fall back to blank-line groups.
    """
    markers = list(re.finditer(r'\[Post \d+\]', text))
    if not markers:
        return [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    posts = []
    for i, m in enumerate(markers):
        start = m.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        posts.append(text[start:end].strip())
    return posts


def _has_status_clause(post):
    """True if post contains at least one status-clause token/pattern (EN-M3/M5)."""
    lower = post.lower()
    if 'pending application' in lower:
        return True
    if 'not yet granted' in lower:
        return True
    if re.search(r'\bfiled\b.*\bpublished\b', post, re.IGNORECASE | re.DOTALL):
        return True
    return False


def _score_en(path):
    text = open(path, encoding='utf-8').read()
    posts = _split_posts(text)
    n = len(posts)
    total = 0.0

    # EN-M1: post count 2–4 → 1; exactly 1 or 5 → 0.5; else → 0
    if 2 <= n <= 4:
        m1 = 1.0
    elif n in (1, 5):
        m1 = 0.5
    else:
        m1 = 0.0
    total += score('EN-M1', m1, f"posts={n}")

    # EN-M2: [ARTICLE-LINK] in final post
    last = posts[-1] if posts else ''
    has_link = '[ARTICLE-LINK]' in last
    total += score('EN-M2', 1.0 if has_link else 0.0, f"final-has-link={has_link}")

    # EN-M3: status-clause discipline — at most one post, and only the final post.
    # Zero posts with a hit → 1.0 (no status upgrade risk; not a discipline violation).
    hit_idxs = [i for i, p in enumerate(posts) if _has_status_clause(p)]
    n_hits = len(hit_idxs)
    if n_hits == 0:
        m3 = 1.0  # zero hits: same bucket as single final-post hit (no upgrade language)
    elif n_hits == 1 and hit_idxs[0] == n - 1:
        m3 = 1.0
    elif n_hits == 1:
        m3 = 0.5
    else:
        m3 = 0.0  # two or more posts with a hit
    total += score('EN-M3', m3, f"status-posts={n_hits}, idxs={[i+1 for i in hit_idxs]}")

    # EN-M4: hygiene — em-dash (U+2014) count and '#' count across whole file
    em = text.count('\u2014')
    hash_n = text.count('#')
    if em == 0 and hash_n == 0:
        m4 = 1.0
    elif em == 0 or hash_n == 0:
        m4 = 0.5
    else:
        m4 = 0.0
    total += score('EN-M4', m4, f"emdash={em}, hash={hash_n}")

    # EN-M5: post 1 clean hook (no status-clause token)
    p1_hit = _has_status_clause(posts[0]) if posts else False
    total += score('EN-M5', 0.0 if p1_hit else 1.0, f"post1-status={p1_hit}")

    # EN-M6: sentence-length variation across whole thread (English terminators)
    thread = ' '.join(posts) if posts else text
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', thread) if s.strip()]
    if sents:
        lens = [len(s) for s in sents]
        mx, mn = max(lens), min(lens)
        if mx >= 100 and mn <= 40:
            m6 = 1.0
        elif mx >= 100:
            m6 = 0.5
        else:
            m6 = 0.0
    else:
        mx, mn, m6 = 0, 0, 0.0
    total += score('EN-M6', m6, f"max={mx}, min={mn}")

    print(f"MECH_SUBTOTAL: {total}/6")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Mechanical promo-voice scorer (KR default; --en for EN thread)."
    )
    parser.add_argument("path", help="Path to promo text file to score")
    parser.add_argument(
        "--en",
        action="store_true",
        default=False,
        help="Score as EN thread (6-item rubric) instead of KR long-form (8-item)",
    )
    args = parser.parse_args(argv)
    if args.en:
        _score_en(args.path)
    else:
        _score_kr(args.path)


if __name__ == "__main__":
    main()
