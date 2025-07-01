import csv

def generate_md_table(csv_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames

        # 构造表头
        header_row = "| " + " | ".join(headers) + " |"
        separator_row = "| " + " | ".join(['-' * len(h) for h in headers]) + " |"

        # 构造内容行
        data_rows = []
        for row in reader:
            cells = []
            for h in headers:
                cell = row[h].strip()
                if h.lower() == "title" and "link" in row:
                    # 将 title 和 link 合并为 markdown 链接格式
                    link = row.get("Link", "").strip()
                    if link:
                        cell = f"[{cell}]({link})"
                cells.append(cell)
            data_rows.append("| " + " | ".join(cells) + " |")

        # 输出 Markdown 表格
        output = [header_row, separator_row] + data_rows
        return "\n".join(output)

if __name__ == "__main__":
    md_table = generate_md_table("papers.csv")
    with open("papers_table.md", "w", encoding="utf-8") as f:
        f.write(md_table)
    print("✅ Markdown 表格已生成：papers_table.md")