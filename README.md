# PDF 파일 분할 및 병합 도구

이 프로젝트는 PDF 파일을 페이지 단위로 분할하고 다시 병합할 수 있는 Python 기반 도구입니다.

## 주요 기능

1. PDF 파일 분할
   - 지정된 페이지 범위에 따라 PDF 파일을 여러 개의 작은 PDF 파일로 분할
   - 페이지 범위는 `page.txt` 파일에서 정의

2. PDF 파일 병합
   - 분할된 PDF 파일들을 지정된 순서대로 하나의 PDF 파일로 병합
   - 병합할 파일 목록은 `merge.txt` 파일에서 정의

## 필요 조건

- Python 3.x
- PyMuPDF (fitz)

## 설치 방법

```bash
pip install PyMuPDF
```

## 사용 방법

1. 프로젝트 구조:
   ```
   data/
   ├── product.pdf      # 원본 PDF 파일
   ├── page.txt         # 분할할 페이지 범위 정보
   ├── merge.txt        # 병합할 파일 목록
   └── split_files/     # 분할된 파일들이 저장되는 폴더
   ```

2. `page.txt` 파일 형식:
   ```
   1-3    # 1페이지부터 3페이지까지
   4-6    # 4페이지부터 6페이지까지
   ```

3. `merge.txt` 파일 형식:
   ```
   split_1.pdf
   split_2.pdf
   ```

4. 실행:
   ```bash
   python split_file.py
   ```

## 주의사항

- 입력 PDF 파일은 `data` 폴더 내에 위치해야 합니다.
- 페이지 범위는 1부터 시작하며, 하이픈(-)으로 구분합니다.
- 병합 시에는 `split_files` 폴더 내의 파일들만 사용 가능합니다.
