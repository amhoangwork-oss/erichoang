"""Regenerate the website's editable and PDF CVs from _data/cv.json.

Dependencies: python-docx, reportlab. Run from any directory with Python 3.
The DOCX reuses Harvard MCS's official bullet-point template. The PDF follows
its centered headings and plain single-column structure with the same content.
Content covers recent research, education, selected honors, and language qualifications.
"""
import json
from html import escape
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.text.paragraph import Paragraph as WordParagraph
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from copy import deepcopy
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Flowable

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / '_data/cv.json').read_text(encoding='utf-8-sig'))
OUT = ROOT / 'files'
OUT.mkdir(exist_ok=True)


def cv_blocks():
    c = DATA
    yield 'title', c['basics']['name']
    yield 'contact', c['basics']['email'] + '  |  ' + c['basics']['location'] + '  |  ' + c['basics']['website'].removeprefix('https://')
    yield 'body', c['basics']['summary']
    yield 'heading', 'Current Research'
    for project in c['current_research']:
        yield 'item', project['title'] + ' | ' + project['status']
        for bullet in project['bullets']:
            yield 'bullet', bullet
    yield 'heading', 'Research Manuscripts'
    for paper in c['publications']:
        yield 'item', paper['title']
        yield 'meta', paper['authors'] + ' | ' + paper['year'] + ' | ' + paper['status']
        for bullet in paper['bullets']:
            yield 'bullet', bullet
    yield 'heading', 'Research Experience'
    for role in c['experience']:
        yield 'item', role['organization']
        yield 'role', role['role'] + '\t' + role['dates']
        for bullet in role['bullets']:
            yield 'bullet', bullet
    yield 'heading', 'Education'
    yield 'item', c['education']['institution']
    yield 'body', c['education']['degree'] + ', ' + c['education']['status'].lower() + ' | ' + c['education']['location']
    yield 'heading', 'Selected Honors'
    for award in c['awards']:
        yield 'body', award['year'] + ' | ' + award['text']
    yield 'heading', 'Skills'
    for label, skills in c['skills'].items():
        yield 'body', label + ': ' + skills


def build_docx():
    # Reuse Harvard MCS's official Word template and its paragraph/numbering styles.
    template = ROOT / 'local/harvard-resume-template.docx'
    doc = Document(template)
    if 'Title' not in doc.styles:
        doc.styles.add_style('Title', 1)
    prototypes = {kind: deepcopy(doc.paragraphs[index]._p) for kind, index in
                  {'title':1, 'contact':6, 'heading':8, 'item':9,
                   'body':10, 'meta':10, 'role':23, 'bullet':24}.items()}
    body = doc._element.body
    for element in list(body):
        if element.tag != qn('w:sectPr'):
            body.remove(element)
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin = sec.bottom_margin = Inches(.6)
    sec.left_margin = sec.right_margin = Inches(.65)
    for s in doc.styles:
        if s.type == 1:
            s.font.color.rgb = RGBColor(0, 0, 0)
    for kind, text in cv_blocks():
        if kind == 'pagebreak':
            doc.add_page_break()
            continue
        element = deepcopy(prototypes[kind])
        body.insert(len(body)-1, element)
        p = WordParagraph(element, doc._body)
        p.clear()
        pf = p.paragraph_format
        pf.left_indent = Inches(0)
        pf.right_indent = Inches(0)
        pf.first_line_indent = Inches(0)
        pf.space_before = Pt(0)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.0
        pf.widow_control = True
        pf.keep_with_next = kind in ('title','contact','heading','item','meta','role')
        pf.keep_together = True
        pf.tab_stops.clear_all()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if kind in ('title','contact','heading'):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if kind == 'title':
            p.style = doc.styles['Title']
            pf.space_after = Pt(5)
        if kind == 'heading':
            pf.space_before = Pt(6)
            pf.space_after = Pt(4)
        if kind == 'item':
            pf.space_before = Pt(5)
            pf.space_after = Pt(2)
        if kind == 'role':
            pf.tab_stops.add_tab_stop(Inches(7.2), WD_TAB_ALIGNMENT.RIGHT)
        if kind == 'bullet':
            pf.left_indent = Inches(.15)
            pf.first_line_indent = Inches(-.12)
        website_label = DATA['basics']['website'].removeprefix('https://')
        if kind == 'contact' and website_label in text:
            prefix = p.add_run(text.split(website_label)[0])
            prefix.font.name = 'Times New Roman'
            prefix.font.size = Pt(11)
            link = OxmlElement('w:hyperlink')
            link.set(qn('r:id'), p.part.relate_to(DATA['basics']['website'], RT.HYPERLINK, is_external=True))
            link_run = OxmlElement('w:r')
            props = OxmlElement('w:rPr')
            fonts = OxmlElement('w:rFonts')
            fonts.set(qn('w:ascii'), 'Times New Roman')
            fonts.set(qn('w:hAnsi'), 'Times New Roman')
            props.append(fonts)
            size = OxmlElement('w:sz')
            size.set(qn('w:val'), '22')
            props.append(size)
            link_run.append(props)
            value = OxmlElement('w:t')
            value.text = website_label
            link_run.append(value)
            link.append(link_run)
            p._p.append(link)
            continue
        run = p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(19 if kind == 'title' else 10.5 if kind == 'meta' else 11)
        run.font.color.rgb = RGBColor(0,0,0)
        run.bold = kind in ('title','heading','item')
        run.italic = kind == 'role'
    doc.core_properties.title = 'Anh Minh Hoang Curriculum Vitae'
    doc.core_properties.author = DATA['basics']['name']
    doc.core_properties.subject = 'Research CV in Harvard MCS bullet point template'
    doc.core_properties.comments = ''
    doc.save(OUT / 'anh-minh-hoang-cv.docx')


def build_pdf():
    # Embed an installed font when available, falling back to PDF core fonts.
    candidates = [Path('C:/Windows/Fonts/times.ttf'), Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')]
    regular = next((p for p in candidates if p.exists()), None)
    font, bold, italic = 'Helvetica', 'Helvetica-Bold', 'Helvetica-Oblique'
    if regular:
        pdfmetrics.registerFont(TTFont('CV', str(regular)))
        bold_path = regular.with_name('timesbd.ttf' if regular.name == 'times.ttf' else 'DejaVuSans-Bold.ttf')
        pdfmetrics.registerFont(TTFont('CV-Bold', str(bold_path)))
        font, bold = 'CV', 'CV-Bold'
        italic_path = regular.with_name('timesi.ttf' if regular.name == 'times.ttf' else 'DejaVuSans-Oblique.ttf')
        if italic_path.exists():
            pdfmetrics.registerFont(TTFont('CV-Italic', str(italic_path)))
            italic = 'CV-Italic'
    class RoleLine(Flowable):
        def __init__(self, text):
            Flowable.__init__(self)
            self.left, self.right = text.split('\t', 1)
            self.height = 16
            self.keepWithNext = True
        def wrap(self, available_width, available_height):
            self.width = available_width
            return self.width, self.height
        def draw(self):
            self.canv.setFont(italic, 11)
            self.canv.drawString(0, 4, self.left)
            self.canv.drawRightString(self.width, 4, self.right)
    base = dict(fontName=font, fontSize=11, leading=12, spaceAfter=3, textColor=colors.black, alignment=TA_LEFT)
    styles = {'body': ParagraphStyle('body', **base)}
    for kind, override in {
        'title':dict(fontName=bold,fontSize=19,leading=23,spaceAfter=5,alignment=TA_CENTER),
        'subtitle':dict(fontSize=12,leading=15,spaceAfter=4),
        'contact':dict(fontSize=11,leading=12,spaceAfter=9,alignment=TA_CENTER),
        'heading':dict(fontName=bold,fontSize=11,leading=13,spaceBefore=6,spaceAfter=4,keepWithNext=True,alignment=TA_CENTER),
        'item':dict(fontName=bold,fontSize=11,leading=13,spaceBefore=5,spaceAfter=2,keepWithNext=True),
        'meta':dict(fontSize=10.5,leading=12,spaceAfter=4,keepWithNext=True),
        'role':dict(fontSize=11,leading=12,spaceAfter=4,keepWithNext=True),
        'bullet':dict(leftIndent=11,firstLineIndent=-8,spaceAfter=3)
    }.items():
        styles[kind] = ParagraphStyle(kind, **(base | override))
    flow = []
    for kind, text in cv_blocks():
        if kind == 'pagebreak':
            flow.append(PageBreak())
        elif kind == 'role':
            flow.append(RoleLine(text))
        else:
            safe = escape(text).replace('\t', ' &nbsp; | &nbsp; ')
            if kind == 'role': safe = '<i>'+safe+'</i>'
            if kind == 'bullet': safe = '&#8226; ' + safe
            if kind == 'contact':
                safe = safe.replace(DATA['basics']['email'], f'<link href="mailto:{DATA["basics"]["email"]}">{DATA["basics"]["email"]}</link>')
                website = DATA['basics']['website']
                label = website.removeprefix('https://')
                safe = safe.replace(label, f'<link href="{website}">{label}</link>')
            flow.append(Paragraph(safe, styles[kind]))
    SimpleDocTemplate(str(OUT/'anh-minh-hoang-cv.pdf'), pagesize=letter,
                      leftMargin=46.8,rightMargin=46.8,topMargin=43.2,bottomMargin=43.2,
                      title='Anh Minh Hoang Curriculum Vitae',author=DATA['basics']['name']).build(flow)


if __name__ == '__main__':
    build_docx()
    build_pdf()
    print('Created editable and PDF CVs in files/.')
