import docx
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


def set_cell_border(cell, **kwargs):
  """Thiết lập viền mảnh cho từng ô bảng."""
  tc = cell._tc
  tcPr = tc.get_or_add_tcPr()
  tcBorders = tcPr.first_child_found_in('w:tcBorders')
  if tcBorders is None:
    tcBorders = OxmlElement('w:tcBorders')
    tcPr.append(tcBorders)
  for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
    edge_data = kwargs.get(edge)
    if edge_data:
      tag = 'w:{}'.format(edge)
      element = tcBorders.find(qn(tag))
      if element is None:
        element = OxmlElement(tag)
        tcBorders.append(element)
      for key in ['val', 'color', 'sz', 'space']:
        if key in edge_data:
          element.set(qn('w:{}'.format(key)), str(edge_data[key]))


# Dữ liệu bảng lần vết Bảng 2.1
data = [
    [
        'Bước',
        'Hàng i',
        'Cột c',
        'Bị ăn?',
        'Việc làm',
        'Trạng thái x = (x1, x2, x3, x4)',
    ],
    ['1', '1', '1', 'Không', 'Đặt quân, gọi DAT-HAU(2)', '(1, 0, 0, 0)'],
    ['2', '2', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(1, 0, 0, 0)'],
    [
        '3',
        '2',
        '2',
        'Có (trùng chéo chính với (1,1))',
        'Bỏ qua',
        '(1, 0, 0, 0)',
    ],
    ['4', '2', '3', 'Không', 'Đặt quân, gọi DAT-HAU(3)', '(1, 3, 0, 0)'],
    ['5', '3', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(1, 3, 0, 0)'],
    ['6', '3', '2', 'Có (trùng chéo phụ với (2,3))', 'Bỏ qua', '(1, 3, 0, 0)'],
    ['7', '3', '3', 'Có (trùng cột 3)', 'Bỏ qua', '(1, 3, 0, 0)'],
    [
        '8',
        '3',
        '4',
        'Có (trùng chéo chính với (2,3))',
        'Bỏ qua; hết cột, quay lui về hàng 2',
        '(1, 3, 0, 0)',
    ],
    ['--', '2', '3', '--', 'Hoàn tác gỡ quân (2,3)', '(1, 0, 0, 0)'],
    ['9', '2', '4', 'Không', 'Đặt quân, gọi DAT-HAU(3)', '(1, 4, 0, 0)'],
    ['10', '3', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(1, 4, 0, 0)'],
    ['11', '3', '2', 'Không', 'Đặt quân, gọi DAT-HAU(4)', '(1, 4, 2, 0)'],
    ['12', '4', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(1, 4, 2, 0)'],
    ['13', '4', '2', 'Có (trùng cột 2)', 'Bỏ qua', '(1, 4, 2, 0)'],
    [
        '14',
        '4',
        '3',
        'Có (trùng chéo chính với (3,2))',
        'Bỏ qua',
        '(1, 4, 2, 0)',
    ],
    [
        '15',
        '4',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 3',
        '(1, 4, 2, 0)',
    ],
    ['--', '3', '2', '--', 'Hoàn tác gỡ quân (3,2)', '(1, 4, 0, 0)'],
    [
        '16',
        '3',
        '3',
        'Có (trùng chéo chính với (1,1))',
        'Bỏ qua',
        '(1, 4, 0, 0)',
    ],
    [
        '17',
        '3',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 2',
        '(1, 4, 0, 0)',
    ],
    [
        '--',
        '2',
        '4',
        '--',
        'Hoàn tác gỡ quân (2,4); hết cột, quay lui về hàng 1',
        '(1, 0, 0, 0)',
    ],
    ['--', '1', '1', '--', 'Hoàn tác gỡ quân (1,1)', '(0, 0, 0, 0)'],
    ['18', '1', '2', 'Không', 'Đặt quân, gọi DAT-HAU(2)', '(2, 0, 0, 0)'],
    [
        '19',
        '2',
        '1',
        'Có (trùng chéo chính với (1,2))',
        'Bỏ qua',
        '(2, 0, 0, 0)',
    ],
    ['20', '2', '2', 'Có (trùng cột 2)', 'Bỏ qua', '(2, 0, 0, 0)'],
    ['21', '2', '3', 'Có (trùng chéo phụ với (1,2))', 'Bỏ qua', '(2, 0, 0, 0)'],
    ['22', '2', '4', 'Không', 'Đặt quân, gọi DAT-HAU(3)', '(2, 4, 0, 0)'],
    ['23', '3', '1', 'Không', 'Đặt quân, gọi DAT-HAU(4)', '(2, 4, 1, 0)'],
    ['24', '4', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(2, 4, 1, 0)'],
    ['25', '4', '2', 'Có (trùng cột 2)', 'Bỏ qua', '(2, 4, 1, 0)'],
    [
        '26',
        '4',
        '3',
        'Không',
        'Đặt quân, gọi DAT-HAU(5) -> LỜI GIẢI 1',
        '(2, 4, 1, 3)',
    ],
    ['--', '4', '3', '--', 'Hoàn tác gỡ quân (4,3)', '(2, 4, 1, 0)'],
    [
        '27',
        '4',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 3',
        '(2, 4, 1, 0)',
    ],
    ['--', '3', '1', '--', 'Hoàn tác gỡ quân (3,1)', '(2, 4, 0, 0)'],
    ['28', '3', '2', 'Có (trùng cột 2)', 'Bỏ qua', '(2, 4, 0, 0)'],
    [
        '29',
        '3',
        '3',
        'Có (trùng chéo chính với (2,4))',
        'Bỏ qua',
        '(2, 4, 0, 0)',
    ],
    [
        '30',
        '3',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 2',
        '(2, 4, 0, 0)',
    ],
    [
        '--',
        '2',
        '4',
        '--',
        'Hoàn tác gỡ quân (2,4); hết cột, quay lui về hàng 1',
        '(2, 0, 0, 0)',
    ],
    ['--', '1', '2', '--', 'Hoàn tác gỡ quân (1,2)', '(0, 0, 0, 0)'],
    ['31', '1', '3', 'Không', 'Đặt quân, gọi DAT-HAU(2)', '(3, 0, 0, 0)'],
    ['32', '2', '1', 'Không', 'Đặt quân, gọi DAT-HAU(3)', '(3, 1, 0, 0)'],
    ['33', '3', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(3, 1, 0, 0)'],
    [
        '34',
        '3',
        '2',
        'Có (trùng chéo chính với (2,1))',
        'Bỏ qua',
        '(3, 1, 0, 0)',
    ],
    ['35', '3', '3', 'Có (trùng cột 3)', 'Bỏ qua', '(3, 1, 0, 0)'],
    ['36', '3', '4', 'Không', 'Đặt quân, gọi DAT-HAU(4)', '(3, 1, 4, 0)'],
    ['37', '4', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(3, 1, 4, 0)'],
    [
        '38',
        '4',
        '2',
        'Không',
        'Đặt quân, gọi DAT-HAU(5) -> LỜI GIẢI 2',
        '(3, 1, 4, 2)',
    ],
    ['--', '4', '2', '--', 'Hoàn tác gỡ quân (4,2)', '(3, 1, 4, 0)'],
    ['39', '4', '3', 'Có (trùng cột 3)', 'Bỏ qua', '(3, 1, 4, 0)'],
    [
        '40',
        '4',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 3',
        '(3, 1, 4, 0)',
    ],
    [
        '--',
        '3',
        '4',
        '--',
        'Hoàn tác gỡ quân (3,4); hết cột, quay lui về hàng 2',
        '(3, 1, 0, 0)',
    ],
    ['--', '2', '1', '--', 'Hoàn tác gỡ quân (2,1)', '(3, 0, 0, 0)'],
    [
        '41',
        '2',
        '2',
        'Có (trùng chéo chính với (1,3))',
        'Bỏ qua',
        '(3, 0, 0, 0)',
    ],
    ['42', '2', '3', 'Có (trùng cột 3)', 'Bỏ qua', '(3, 0, 0, 0)'],
    [
        '43',
        '2',
        '4',
        'Có (trùng chéo phụ với (1,3))',
        'Bỏ qua; hết cột, quay lui về hàng 1',
        '(3, 0, 0, 0)',
    ],
    ['--', '1', '3', '--', 'Hoàn tác gỡ quân (1,3)', '(0, 0, 0, 0)'],
    ['44', '1', '4', 'Không', 'Đặt quân, gọi DAT-HAU(2)', '(4, 0, 0, 0)'],
    ['45', '2', '1', 'Không', 'Đặt quân, gọi DAT-HAU(3)', '(4, 1, 0, 0)'],
    ['46', '3', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(4, 1, 0, 0)'],
    ['47', '3', '2', 'Có (trùng chéo phụ với (1,4))', 'Bỏ qua', '(4, 1, 0, 0)'],
    ['48', '3', '3', 'Không', 'Đặt quân, gọi DAT-HAU(4)', '(4, 1, 3, 0)'],
    ['49', '4', '1', 'Có (trùng cột 1)', 'Bỏ qua', '(4, 1, 3, 0)'],
    ['50', '4', '2', 'Có (trùng chéo phụ với (3,3))', 'Bỏ qua', '(4, 1, 3, 0)'],
    ['51', '4', '3', 'Có (trùng cột 3)', 'Bỏ qua', '(4, 1, 3, 0)'],
    [
        '52',
        '4',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 3',
        '(4, 1, 3, 0)',
    ],
    ['--', '3', '3', '--', 'Hoàn tác gỡ quân (3,3)', '(4, 1, 0, 0)'],
    [
        '53',
        '3',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 2',
        '(4, 1, 0, 0)',
    ],
    ['--', '2', '1', '--', 'Hoàn tác gỡ quân (2,1)', '(4, 0, 0, 0)'],
    ['54', '2', '2', 'Không', 'Đặt quân, gọi DAT-HAU(3)', '(4, 2, 0, 0)'],
    ['55', '3', '1', 'Có (trùng chéo phụ với (2,2))', 'Bỏ qua', '(4, 2, 0, 0)'],
    ['56', '3', '2', 'Có (trùng cột 2)', 'Bỏ qua', '(4, 2, 0, 0)'],
    [
        '57',
        '3',
        '3',
        'Có (trùng chéo chính với (2,2))',
        'Bỏ qua',
        '(4, 2, 0, 0)',
    ],
    [
        '58',
        '3',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 2',
        '(4, 2, 0, 0)',
    ],
    ['--', '2', '2', '--', 'Hoàn tác gỡ quân (2,2)', '(4, 0, 0, 0)'],
    [
        '59',
        '2',
        '3',
        'Có (trùng chéo chính với (1,4))',
        'Bỏ qua',
        '(4, 0, 0, 0)',
    ],
    [
        '60',
        '2',
        '4',
        'Có (trùng cột 4)',
        'Bỏ qua; hết cột, quay lui về hàng 1',
        '(4, 0, 0, 0)',
    ],
    [
        '--',
        '1',
        '4',
        '--',
        'Hoàn tác gỡ quân (1,4); kết thúc toàn bộ duyệt',
        '(0, 0, 0, 0)',
    ],
]

doc = Document()

# Đặt lề trang 2cm
sections = doc.sections
for section in sections:
  section.top_margin = Inches(0.8)
  section.bottom_margin = Inches(0.8)
  section.left_margin = Inches(0.8)
  section.right_margin = Inches(0.8)

# Tiêu đề
title = doc.add_paragraph()
p_run = title.add_run('Bảng 2.1. Lần vết quay lui trên bàn cờ 4 × 4')
p_run.font.name = 'Times New Roman'
p_run.font.size = Pt(13)
p_run.font.bold = True
p_run.font.italic = True
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Tạo bảng
table = doc.add_table(rows=len(data), cols=len(data[0]))
table.alignment = WD_TABLE_ALIGNMENT.CENTER

border_kwargs = {
    'val': 'single',
    'sz': '4',
    'color': 'BFBFBF',
}  # Viền xám mảnh

col_widths = [
    Inches(0.6),
    Inches(0.7),
    Inches(0.6),
    Inches(2.0),
    Inches(1.8),
    Inches(1.3),
]

for row_idx, row_data in enumerate(data):
  row = table.rows[row_idx]
  for col_idx, cell_value in enumerate(row_data):
    cell = row.cells[col_idx]
    cell.width = col_widths[col_idx]
    cell.text = cell_value

    # Định dạng font
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    run = p.runs[0]
    run.font.name = 'Times New Roman'
    run.font.size = Pt(9.5)

    # Tiêu đề cột
    if row_idx == 0:
      run.font.bold = True
      p.alignment = WD_ALIGN_PARAGRAPH.CENTER
      # Đổ màu nền header
      shading_elm = OxmlElement('w:shd')
      shading_elm.set(qn('w:val'), 'clear')
      shading_elm.set(qn('w:color'), 'auto')
      shading_elm.set(qn('w:fill'), 'D9E1F2')
      cell._tc.get_or_add_tcPr().append(shading_elm)
    else:
      if col_idx in [0, 1, 2]:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
      elif col_idx == 5:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
      else:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT

      # Nổi bật 2 dòng ra lời giải
      if 'LỜI GIẢI' in cell_value:
        run.font.bold = True
        run.font.color.rgb = RGBColor(192, 0, 0)

    # Đặt viền
    set_cell_border(
        cell,
        top=border_kwargs,
        bottom=border_kwargs,
        left=border_kwargs,
        right=border_kwargs,
    )

doc.save('Bang_2_1_Lan_Vet_4_Hau.docx')
print('Đã tạo thành công file Bang_2_1_Lan_Vet_4_Hau.docx!')