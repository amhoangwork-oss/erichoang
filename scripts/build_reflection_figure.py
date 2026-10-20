"""Draw the reflection's figure from the archived NeurIPS language analysis.

Source: legacy/neurips-2026/project/analysis/cluster_language_results.md,
Table B. These are later project results, not the first discovery log and
not results from the current ACL manuscript. Each row uses a different
selected cluster. Counts are retained here to make the figure reproducible.
"""
from pathlib import Path

from reportlab.graphics import renderSVG
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib import colors


ROOT = Path(__file__).resolve().parents[1]
ROWS = [('Python', 805, 38270), ('Swift', 785, 4497),
        ('Shell (Bash)', 1341, 4728)]
BLUE = colors.HexColor('#176B93')
GRAY = colors.HexColor('#E4E9ED')
INK = colors.HexColor('#172A38')

d = Drawing(860, 330)
d.add(Rect(0, 0, 860, 330, fillColor=colors.white, strokeColor=None))
d.add(String(28, 289, 'A cluster captured only part of each language',
             fontName='Helvetica-Bold', fontSize=21, fillColor=INK))
d.add(String(28, 263, "Share of each language's requests inside its selected cluster",
             fontName='Helvetica', fontSize=13, fillColor=INK))

chart = HorizontalBarChart()
chart.x, chart.y, chart.width, chart.height = 155, 82, 470, 162
shares = [100 * selected / total for _, selected, total in ROWS]
chart.data = [shares, [100 - share for share in shares]]
chart.categoryAxis.categoryNames = [row[0] for row in ROWS]
chart.categoryAxis.style = 'stacked'
chart.categoryAxis.labels.fontName = 'Helvetica'
chart.categoryAxis.labels.fontSize = 13
chart.categoryAxis.labels.fillColor = INK
chart.categoryAxis.visibleAxis = False
chart.categoryAxis.visibleTicks = False
chart.valueAxis.valueMin, chart.valueAxis.valueMax = 0, 100
chart.valueAxis.visible = False
chart.bars[0].fillColor = BLUE
chart.bars[1].fillColor = GRAY
chart.bars.strokeColor = None
chart.barWidth = 24
d.add(chart)

for i, (_, selected, total) in enumerate(ROWS):
    d.add(String(647, chart.y + (i + .5) * chart.height / len(ROWS) - 4,
                 f'{100 * selected / total:.1f}%  ({selected:,} / {total:,})',
                 fontName='Helvetica', fontSize=13, fillColor=INK))

for x, fill, label in [(155, BLUE, 'Inside selected cluster'),
                       (375, GRAY, 'In other clusters')]:
    d.add(Rect(x, 37, 13, 13, fillColor=fill, strokeColor=None))
    d.add(String(x + 20, 39, label, fontName='Helvetica', fontSize=12,
                 fillColor=INK))

output = ROOT / 'images/research/neurips-cluster-coverage.svg'
renderSVG.drawToFile(d, str(output))
svg = output.read_text(encoding='utf-8')
# SVG viewers need web font families rather than PDF's Helvetica-Bold name.
svg = svg.replace('font-family: Helvetica-Bold;',
                  'font-family: Arial, Helvetica, sans-serif; font-weight: 700;')
svg = svg.replace('font-family: Helvetica;',
                  'font-family: Arial, Helvetica, sans-serif;')
svg = svg.replace('<title>...</title>',
                  '<title>Language coverage of selected clusters</title>')
svg = svg.replace('<desc>...</desc>',
                  '<desc>Archived NeurIPS-era analysis. Selected clusters contained '
                  '28.4 percent of Shell requests, 17.5 percent of Swift requests, '
                  'and 2.1 percent of Python requests. Each row uses a different '
                  'selected cluster.</desc>')
output.write_text(svg, encoding='utf-8')
print('Created NeurIPS reflection figure from archived counts.')
