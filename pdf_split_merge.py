import fitz
import os


def split_pdf_by_pages(pdf_path, page_info_path, output_folder):
    # PDF 열기
    doc = fitz.open(pdf_path)

    # 출력 폴더 생성
    os.makedirs(output_folder, exist_ok=True)

    # page.txt 파일 읽기
    with open(page_info_path, 'r') as f:
        lines = f.readlines()

    # 페이지 분할 및 저장
    for idx, line in enumerate(lines):
        parts = line.strip().split('-')
        if len(parts) != 2:
            print(f"Invalid format in line {idx + 1}: {line}")
            continue

        try:
            from_page = int(parts[0]) - 1  # PyMuPDF는 0-based index
            to_page = int(parts[1])

            if from_page >= to_page or from_page < 0 or to_page > len(doc):
                print(f"Invalid page range in line {idx + 1}: {line}")
                continue

            new_doc = fitz.open()
            for page_num in range(from_page, to_page):
                new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)

            output_path = os.path.join(output_folder, f"split_{idx + 1}.pdf")
            # 압축 적용
            new_doc.save(output_path, garbage=4, deflate=True)
            # new_doc.save(output_path)
            new_doc.close()
            print(f"Saved: {output_path}")
        except ValueError:
            print(f"Invalid number in line {idx + 1}: {line}")

    doc.close()


def merge_pdfs(merge_list_path, input_folder, output_pdf):
    if not os.path.exists(merge_list_path):
        print(f"Error: Merge list file not found at {merge_list_path}")
        return

    with open(merge_list_path, 'r') as f:
        files_to_merge = [line.strip() for line in f.readlines() if line.strip()]

    merged_pdf = fitz.open()

    for file_name in files_to_merge:
        file_path = os.path.join(input_folder, file_name)
        if not os.path.exists(file_path):
            print(f"Warning: File {file_name} not found, skipping.")
            continue

        doc = fitz.open(file_path)
        for page in doc:
            merged_pdf.insert_pdf(doc, from_page=page.number, to_page=page.number)  # 메타데이터 최소화
        doc.close()

    merged_pdf.save(output_pdf, garbage=4, deflate=True)  # 압축 적용
    merged_pdf.close()
    print(f"Merged PDF saved as {output_pdf}")


# 파일 경로 설정
pdf_path = "data/product.pdf"
page_info_path = "data/page.txt"
output_folder = "data/split_files"
merge_list_path = "data/merge.txt"
output_pdf = "data/merged_result.pdf"

# 실행
split_pdf_by_pages(pdf_path, page_info_path, output_folder)
merge_pdfs(merge_list_path, output_folder, output_pdf)
