# Figure Attachment Policy: Promo 첨부 도면 선택

X promo 첨부 도면은 essay 의 5:2 wide header composite 가 아니다. 명세서 원본 sheet (Layer 1 cleaned, 직사각형 portrait/landscape) 가 default.

## 선택 절차

### 1. Default = 1 figure (명세서 원본 sheet)

`patent-figure` skill 의 Layer 1 cleanup 결과 사용 (header band 제거 + tight crop, 4-panel grid 등 원본 layout 보존). X timeline preview 에서 *full visible* + 각 panel detail *최대화* + patent attorney 격 *authority signal*.

### 2. Essay header composite (5:2) 첨부 회피

X timeline preview 의 세로 압축 (50-60% only) 으로 detail 손실. 가공된 composite 가 명세서 원본 그대로 격보다 authority signal 약함. Header composite 는 essay article 의 visual header 전용.

### 3. Multi-figure (2-3 figures) 시점

- Header 의 thesis carry 부족 (예: non-visual essay, 분산된 evidence) → §3/§4 mechanism figure 추가
- 도면들 모두 원본 sheet form (직사각형 portrait/landscape) 우선. Wide composite 아님
- 최대 3 figures (X 플랫폼 1-post limit 4 이지만 Digest 격은 단순함 우선)

### 4. X 플랫폼 image aspect ratio 권장

- **최적**: 16:9 (1.78:1) horizontal 또는 4:5 (0.80) portrait. Timeline preview full visible
- **수용 가능**: 1:1 ~ 1.91:1 (X 의 timeline preview 영역 내)
- **회피**: aspect > 2.1 (wide composite, 세로 압축으로 detail 손실)
- **회피**: aspect < 0.5 (very tall, preview 잘림)

### 5. Layer 1 cleanup 만 적용

`patent-figure` skill 의 `crop.py` 1-step 적용으로 충분. 5:2 composite 단계 (Layer 2) 는 essay header 전용, promo 에는 불필요.

## Validation

**050 Tesla CAM promo (2026-05)**: Essay header composite (3890×1556, aspect 2.5) 대신 명세서 원본 FIG. 5 sheet (2271×2042, aspect 1.11) 첨부. 각 panel 크기 ~2 배, X timeline 에서 4 panels 모두 visible, patent document 원본 격.
