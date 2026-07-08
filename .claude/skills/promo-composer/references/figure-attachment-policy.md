# Figure attachment policy (promo pack)

첨부 이미지의 source of truth 는 `essays/<id>/publication-package/` 다: `cover-5x2.png`
(있으면 `cover-letterbox.png` 도), 원본 sheet `fig-NN.png` 들, 그리고 alt text 가 실린
`posting-checklist.md`. `input/figures/` 나 `handoff/` 의 사본은 쓰지 않는다:
publication-package 의 이미지와 alt text 가 loop 를 통과한 게시본이고, 이전 단계 사본은
다를 수 있다.

## Defaults

- **Default 첨부 = `publication-package/cover-5x2.png`** (아티클 자신의 커버). Promo 와
  아티클이 하나의 시각 아이덴티티로 이어진다. KR post 와 thread tweet 1 의 기본값.
- **Deliverable 당 1-2 figures max.** Digest 격은 단순함 우선; 세 번째 이미지가 필요해
  보이면 보통 글이 일을 안 하고 있는 것이다.
- 팩 안에서 첨부는 **metadata line 으로만** 적는다 (`attach:` + `alt:`). Paste block
  본문에 inline markdown 이미지 금지 (paste surface 는 텍스트다).
- **Alt-text line 필수.** `posting-checklist.md` 의 cover alt / body figure alt 를
  verbatim 재사용한다. 없는 도면이면 essay 의 해당 캡션 문구로 만든다 (새 주장 금지).
  Alt 는 1-2 문장, 구체적으로, reference numeral 나열 금지 (SURF-003 의 정신을 피드
  이미지에도 적용).

## When to swap the default (v1 aspect 지침, carried)

v1 은 원본 sheet 를 default 로 했다: X timeline preview 가 wide composite 를 세로
압축 (50-60% 노출) 해서 detail 이 죽고, 명세서 원본 격의 authority signal 이 더 강하기
때문이다. 검증 사례 (050 Tesla CAM promo, 2026-05): aspect 2.5 composite 대신 aspect
1.11 원본 FIG. 5 sheet 를 첨부, 각 panel ~2 배 크기로 timeline 에서 4 panels 모두
visible.

v2 는 hook 자리 (KR post, tweet 1) 의 default 를 아티클 커버 (`cover-5x2.png`) 로
바꾼다: 링크할 아티클과 같은 얼굴이 신뢰 신호이기 때문이다. v1 지침은 swap 기준으로
살아 있다:

- **Mechanism beat (thread tweet 2)** 처럼 panel detail 이 논점을 실어 나를 때는 원본
  sheet `fig-NN.png` 를 첨부한다.
- Aspect 권장: 최적 16:9 (1.78) horizontal 또는 4:5 (0.80) portrait; 수용 1:1 ~ 1.91:1;
  회피 aspect > 2.1 (세로 압축) 및 < 0.5 (preview 잘림). `cover-5x2.png` 는 aspect 2.5
  로 회피 구간이지만 커버 아이덴티티 목적이 detail 목적보다 앞설 때만 default 로 쓴다.
  detail 이 목적이면 sheet 로 swap 하고 metadata line 에 이유를 한 줄 적는다.

## Link-card interplay

미디어를 첨부한 포스트는 아티클 링크의 card preview 를 밀어낸다 (미디어가 이긴다).
커버 첨부 + 링크 = 커버가 미디어로 한 번 노출. 링크 card 렌더를 원하면 게시 시점에
attachment line 을 버리면 된다: 팩은 default 를 적고, 최종 선택은 게시하는 사람의
몫이다.

## Rules

- 이미지 편집/재크롭 없음. `publication-package/` 파일을 as-is 로 지정한다 (이미지
  가공이 필요하면 그것은 pipeline 단계의 일이지 promo 의 일이 아니다).
- Essay 본문 스크린샷 첨부 금지 (텍스트는 텍스트로).
- 존재 확인: `attach:` 에 적는 모든 경로는 실제 파일이어야 한다 (`ls` 로 확인). 팩이
  없는 파일을 가리키면 posting 단계에서 깨진다.
