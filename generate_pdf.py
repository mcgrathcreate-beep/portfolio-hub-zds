#!/usr/bin/env python3
"""
Generates zen-stafford-portfolio.pdf — a clickable PDF that mirrors the website.
Run with: python3 generate_pdf.py
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase.pdfmetrics import stringWidth
import os

W, H = A4  # 595.27 x 841.89

# ── Colors (matching globals.css) ─────────────────────────────────────────────
BG           = HexColor('#f6f4ef')
SURFACE      = HexColor('#ffffff')
ACCENT       = HexColor('#0682D4')
ACCENT_SOFT  = HexColor('#deeefa')
ACCENT_DARK  = HexColor('#055fa0')
INK          = HexColor('#14151a')
INK_2        = HexColor('#4a4d5a')
INK_3        = HexColor('#8a8d99')
LINE         = HexColor('#e3e1dc')
LINE_2       = HexColor('#eceae5')
GREEN        = HexColor('#22c55e')
CARD_SHADOW  = HexColor('#dedad4')

# ── Layout ────────────────────────────────────────────────────────────────────
SB_W    = 155          # sidebar width
CX      = SB_W + 1     # content x
CW      = W - CX - 22  # content width
PAD     = 18
TOP     = H - 26       # top y of content
BOTTOM  = 22

PUBLIC  = os.path.join(os.path.dirname(__file__), 'public')
OUT     = os.path.join(os.path.dirname(__file__), 'zen-stafford-portfolio.pdf')

NAV = [
    ('home',    'Home'),
    ('web',     'Web Design'),
    ('social',  'Social Design'),
    ('cv',      'My CV'),
    ('contact', 'Contact'),
]

WEB_PROJECTS = [
    {'id':'otters-bend',      'title':"Otter's Bend Lodge",     'url':'ottersbendlodge.co.za',           'href':'https://ottersbendlodge.co.za/',                         'blurb':'Riverside Lodge & Campsite in Franschhoek',                    'tags':['Accommodation','Tourism'],             'image':'web-design-otters-bend-lodge.png'},
    {'id':'olive-bean',       'title':'Olive Bean Leather',      'url':'olivebeanleather.co.za',          'href':'https://olivebeanleather.co.za/',                        'blurb':'Artisanal Local Leather Products',                             'tags':['E-commerce','D2C'],                    'image':'web-design-olive-bean-leather.png'},
    {'id':'stiint-it',        'title':'Stiint It',               'url':'stiint-it.com',                   'href':'https://stiint-it.com/',                                 'blurb':'Connecting Verified Talent to Opportunities',                  'tags':['Marketplace','Recruitment'],           'image':'web-design-stiint-it.png'},
    {'id':'bestbuds',         'title':'Best Buds',               'url':'bestbuds420.co.za',               'href':'https://bestbuds420.co.za/',                             'blurb':'Bud Buying Built for Members',                                 'tags':['E-commerce','Membership'],             'image':'web-design-best-buds-420.png'},
    {'id':'wip-africa',       'title':'WIP Africa',              'url':'worldinstituteofpainafrica.org',  'href':'https://worldinstituteofpainafrica.org/',                 'blurb':'Regional Leaders in Pain Management and Education',            'tags':['Healthcare','Education'],              'image':'web-design-wip-africa.png'},
    {'id':'drcaryn',          'title':'Dr Caryn April Inc',      'url':'drcarynapril.com',                'href':'https://drcarynapril.com/',                              'blurb':'Medical Physician',                                           'tags':['Professional Services','Personal Brand'],'image':'web-design-dr-caryn-april.png'},
    {'id':'pomerol',          'title':'Pomerol',                 'url':'pomerolpartners.com',             'href':'https://pomerolpartners.com/netsuite-operational-rescue/','blurb':'Data analytics consultancy',                                  'tags':['SaaS','Analytics'],                    'image':'web-design-pomerol-partners.png'},
    {'id':'steelorex',        'title':'Steelorex',               'url':'steelorex.co.za',                 'href':'https://steelorex.co.za/',                               'blurb':'Commercial manufacturer and online retailer',                  'tags':['E-commerce','Manufacturing'],          'image':'web-design-steelorex.png'},
    {'id':'leopard-tours',    'title':'Leopard Tours',           'url':'leopard.voyage',                  'href':'https://leopard.voyage/',                                'blurb':'Curated travel experiences',                                   'tags':['Tourism','Travel'],                    'image':'web-design-leopard-tours.png'},
    {'id':'matriarch-africa', 'title':'Matriarch Africa',        'url':'matriarch.africa',                'href':'https://matriarch.africa/',                              'blurb':'Energy & utilities management for property portfolios',         'tags':['Energy','Property'],                   'image':'web-design-matriarch-africa.png'},
]

EXPERIENCE = [
    {'mark':'ZDS','title':'ZDS Designs — Freelance Website & Design',                    'body':"I don't just make websites look good, I make sure they're easy to use, fast, and ready to grow with your business. From mapping user journeys in Figma to building custom WordPress sites and creating on-brand social media designs in Canva or Figma, I handle the full process from first idea to final launch.",                                                                                                                                                            'when':'Present',            'where':'Tamboerskloof, Cape Town','current':True},
    {'mark':'TML','title':'Tomorrow Labs — Lead of Digital Design & Web Development',     'body':"Led the agency's web and digital delivery across fintech, e-commerce, and creative clients. Owned UI/UX design, technical strategy, and project execution — translating Figma designs into high-performing WordPress builds. Oversaw infrastructure, hosting, and integrations to ensure reliable launches and scalable digital platforms aligned with brand and marketing goals.",                                                                                          'when':'Sep 2024 — Oct 2025','where':'De Waterkant, Cape Town'},
    {'mark':'MC', 'title':'MC Agency — Head of Digital Design & Web Development',         'body':'Directed end-to-end web design and development projects, combining design leadership with hands-on technical execution. Worked closely with clients to turn creative concepts into functional, polished websites while improving delivery workflows, QA processes, and post-launch reliability through proper hosting and system management.',                                                                                                                               'when':'Jun 2022 — Jul 2024','where':'Vredehoek, Cape Town'},
    {'mark':'RuZ','title':'RuZen — Founder & Lead Web & Graphic Designer',                'body':'Founded and operated an independent digital studio delivering custom websites and branding solutions. Managed the full project lifecycle from client consultation to launch — providing UX design, front-end development, and graphic design. Built a strong reputation for creative problem-solving and high-quality digital craftsmanship.',                                                                                                                               'when':'Oct 2020 — Aug 2022','where':'Kommetjie, Western Cape'},
    {'mark':'GBT','title':'Gordons Bay Tourism — Marketing & Design Lead',                'body':'Led marketing, design, and sales initiatives for a tourism business managing 40+ properties. Oversaw team operations, client relationships, and business development while creating digital, print, and branding assets. Implemented strategic marketing campaigns that increased bookings and strengthened local and international visibility.',                                                                                                                            'when':'Jan 2018 — Sep 2020','where':'Gordons Bay, Western Cape'},
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def wrap(text, max_w, font, size, max_lines=99):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        test = (cur + ' ' + w).strip()
        if stringWidth(test, font, size) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
                if len(lines) >= max_lines:
                    return lines
            cur = w
    if cur:
        lines.append(cur)
    return lines[:max_lines]


def draw_chip(c, x, y, text, font_size=7.5, bg=None, fg=None, border=None):
    bg     = bg     or HexColor('#eceae5')
    fg     = fg     or INK_2
    border = border or LINE
    pw = stringWidth(text, 'Helvetica', font_size) + 12
    ph = font_size + 6
    c.setFillColor(bg)
    c.setStrokeColor(border)
    c.setLineWidth(0.4)
    c.roundRect(x, y - 2, pw, ph, 4, fill=1, stroke=1)
    c.setFillColor(fg)
    c.setFont('Helvetica', font_size)
    c.drawString(x + 6, y + 2, text)
    return pw + 4


def draw_sidebar(c, active_id):
    # Background
    c.setFillColor(SURFACE)
    c.rect(0, 0, SB_W, H, fill=1, stroke=0)
    # Right border
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(SB_W, 0, SB_W, H)

    # Avatar
    ava = 42
    ax  = (SB_W - ava) / 2
    ay  = H - 28 - ava
    c.setFillColor(ACCENT_SOFT)
    c.circle(ax + ava/2, ay + ava/2, ava/2 + 2, fill=1, stroke=0)
    img_path = os.path.join(PUBLIC, 'zen.png')
    if os.path.exists(img_path):
        try:
            c.drawImage(img_path, ax, ay, ava, ava, mask='auto')
        except Exception:
            pass

    # Name + role
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 10.5)
    c.drawCentredString(SB_W / 2, ay - 13, 'Zen Stafford')
    c.setFillColor(INK_3)
    c.setFont('Helvetica', 8)
    c.drawCentredString(SB_W / 2, ay - 24, 'Multimedia Designer')

    # Nav
    ny = ay - 48
    for nav_id, label in NAV:
        active = nav_id == active_id
        if active:
            c.setFillColor(ACCENT_SOFT)
            c.roundRect(8, ny - 5, SB_W - 16, 20, 7, fill=1, stroke=0)
            c.setFillColor(ACCENT)
            c.setFont('Helvetica-Bold', 9)
        else:
            c.setFillColor(INK_2)
            c.setFont('Helvetica', 9)
        c.drawString(PAD, ny + 3, label)
        # Internal link
        c.linkAbsolute('', f'sec_{nav_id}', (8, ny - 5, SB_W - 8, ny + 15))
        ny -= 26

    # Available Now
    c.setFillColor(GREEN)
    c.circle(PAD + 4, 50, 3, fill=1, stroke=0)
    c.setFillColor(INK_2)
    c.setFont('Helvetica', 8)
    c.drawString(PAD + 12, 47, 'Available Now')

    # Hire Me button
    bw = SB_W - PAD * 2
    c.setFillColor(INK)
    c.roundRect(PAD, 26, bw, 18, 9, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 8.5)
    c.drawCentredString(PAD + bw / 2, 31, 'Hire Me')
    c.linkAbsolute('', 'sec_contact', (PAD, 26, PAD + bw, 44))


def page_head(c, y, kicker, title, sub):
    c.setFillColor(ACCENT)
    c.setFont('Helvetica', 7.5)
    c.drawString(CX + PAD, y, kicker.upper())
    y -= 17

    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 20)
    c.drawString(CX + PAD, y, title)
    y -= 14

    c.setFillColor(INK_2)
    c.setFont('Helvetica', 9)
    for ln in wrap(sub, CW - PAD, 'Helvetica', 9):
        c.drawString(CX + PAD, y, ln)
        y -= 11
    return y - 10


def draw_project_card(c, proj, x, y, cw, ch):
    # Shadow
    c.setFillColor(CARD_SHADOW)
    c.roundRect(x + 2, y - 2, cw, ch, 11, fill=1, stroke=0)
    # Card
    c.setFillColor(SURFACE)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, cw, ch, 11, fill=1, stroke=1)

    img_h = round(ch * 0.52)
    img_y = y + ch - img_h

    # Image area
    c.saveState()
    path = c.beginPath()
    path.roundRect(x + 0.5, img_y, cw - 1, img_h, 11)
    c.clipPath(path, stroke=0)
    c.setFillColor(LINE_2)
    c.rect(x, img_y, cw, img_h, fill=1, stroke=0)
    if proj.get('image'):
        ip = os.path.join(PUBLIC, proj['image'])
        if os.path.exists(ip):
            try:
                c.drawImage(ip, x, img_y, cw, img_h,
                            preserveAspectRatio=False, mask='auto')
            except Exception:
                pass
    c.restoreState()

    # Divider between image and meta
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(x, img_y, x + cw, img_y)

    # Meta
    mp  = 10
    ty  = img_y - 13

    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 9)
    for ln in wrap(proj['title'], cw - mp * 2, 'Helvetica-Bold', 9, max_lines=1):
        c.drawString(x + mp, ty, ln)
        ty -= 11

    c.setFillColor(INK_3)
    c.setFont('Helvetica', 7)
    c.drawString(x + mp, ty, proj['url'])
    ty -= 11

    c.setFillColor(INK_2)
    c.setFont('Helvetica', 8)
    for ln in wrap(proj['blurb'], cw - mp * 2, 'Helvetica', 8, max_lines=2):
        c.drawString(x + mp, ty, ln)
        ty -= 10

    ty -= 3
    tx = x + mp
    for tag in proj['tags']:
        tw = draw_chip(c, tx, ty, tag, 7, ACCENT_SOFT, ACCENT, HexColor('#b8d8f0'))
        tx += tw

    # Clickable whole card
    c.linkURL(proj['href'], (x, y, x + cw, y + ch))


# ── Canvas ────────────────────────────────────────────────────────────────────
c = rl_canvas.Canvas(OUT, pagesize=A4)
c.setTitle('Zen Stafford — Multimedia Designer Portfolio')
c.setAuthor('Zen Stafford')
c.setSubject('Portfolio — Cape Town')

card_w   = (CW - PAD - 10) / 2
card_h   = 180
card_gap = 10


def new_section_page(section_id, mark_bookmark=True):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_sidebar(c, section_id)
    if mark_bookmark:
        c.bookmarkPage(f'sec_{section_id}', fit='XYZ', left=0, top=H)


def continuation_page(section_id):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_sidebar(c, section_id)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 — HOME
# ─────────────────────────────────────────────────────────────────────────────
new_section_page('home')

y = TOP

# Hero block
hx, hw, hh = CX + PAD, CW - PAD, 168
c.setFillColor(SURFACE)
c.setStrokeColor(LINE)
c.setLineWidth(0.5)
c.roundRect(hx, y - hh, hw, hh, 13, fill=1, stroke=0)
# Top + right border only (matching website)
c.setStrokeColor(LINE)
c.setLineWidth(0.5)
c.line(hx + 13, y, hx + hw, y)           # top
c.line(hx + hw, y, hx + hw, y - hh + 13) # right

# Eyebrow
c.setFillColor(ACCENT)
c.setFont('Helvetica', 7)
c.drawString(hx + 18, y - 16, '—  MULTIMEDIA DESIGNER  ·  CAPE TOWN')

# Headline
c.setFillColor(INK)
c.setFont('Helvetica-Bold', 24)
c.drawString(hx + 18, y - 38, 'Designing thoughtful')
c.drawString(hx + 18, y - 62, 'digital products &')
c.drawString(hx + 18, y - 86, 'brand systems.')

# Sub
c.setFillColor(INK_2)
c.setFont('Helvetica', 8.5)
sub_lines = wrap(
    'I build websites, digital products, and AI-powered systems for businesses that care about '
    'thoughtful execution and long-term quality. My work sits between design, development, and strategy.',
    hw - 110, 'Helvetica', 8.5
)
sy = y - 104
for ln in sub_lines:
    c.drawString(hx + 18, sy, ln)
    sy -= 11

# Stats
sx = hx + hw - 86
c.setFillColor(INK)
c.setFont('Helvetica-Bold', 18)
c.drawString(sx, y - 44, '8+')
c.setFillColor(INK_3)
c.setFont('Helvetica', 6.5)
c.drawString(sx, y - 55, 'YEARS DESIGNING')
c.setFillColor(INK)
c.setFont('Helvetica-Bold', 18)
c.drawString(sx, y - 78, '40+')
c.setFillColor(INK_3)
c.setFont('Helvetica', 6.5)
c.drawString(sx, y - 89, 'PROJECTS SHIPPED')

y -= hh + 22

# Section heading
c.setFillColor(INK)
c.setFont('Helvetica-Bold', 14)
c.drawString(CX + PAD, y, 'Recent Projects')
y -= 12
c.setFillColor(INK_2)
c.setFont('Helvetica', 8.5)
c.drawString(CX + PAD, y, 'A closer look at recent web work — where creativity meets precision.')
y -= 18

# 4 project cards 2×2
home_ids  = ['wip-africa', 'bestbuds', 'steelorex', 'leopard-tours']
home_proj = [p for p in WEB_PROJECTS if p['id'] in home_ids]

for i, proj in enumerate(home_proj):
    col = i % 2
    row = i // 2
    px  = CX + PAD + col * (card_w + card_gap)
    py  = y - card_h - row * (card_h + card_gap)
    draw_project_card(c, proj, px, py, card_w, card_h)

c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGES — WEB DESIGN  (10 projects, 4 per page = 3 pages)
# ─────────────────────────────────────────────────────────────────────────────
new_section_page('web')
y = page_head(c, TOP, 'Web Design', 'Built for the real world.',
              'Every site is designed to reflect the brand and built to perform — clean, fast, and made to grow.')

for i, proj in enumerate(WEB_PROJECTS):
    if i > 0 and i % 4 == 0:
        c.showPage()
        continuation_page('web')
        y = TOP - 8

    col = i % 2
    row = (i % 4) // 2
    px  = CX + PAD + col * (card_w + card_gap)
    py  = y - card_h - row * (card_h + card_gap)
    draw_project_card(c, proj, px, py, card_w, card_h)

c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGES — SOCIAL DESIGN  (8 images, square tiles, 2 per row, 4 per page)
# ─────────────────────────────────────────────────────────────────────────────
new_section_page('social')
y = page_head(c, TOP, 'Social Design', 'Designed for the feed.',
              'Mockups, story templates, and content systems.')

tile_w   = (CW - PAD - 10) / 2
tile_h   = tile_w  # square
tile_gap = 10

for i in range(8):
    if i > 0 and i % 4 == 0:
        c.showPage()
        continuation_page('social')
        y = TOP - 8

    col = i % 2
    row = (i % 4) // 2
    tx  = CX + PAD + col * (tile_w + tile_gap)
    ty  = y - tile_h - row * (tile_h + tile_gap)

    c.setFillColor(SURFACE)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.roundRect(tx, ty, tile_w, tile_h, 10, fill=1, stroke=1)

    img_path = os.path.join(PUBLIC, f'social-design-{i+1}.jpg')
    if os.path.exists(img_path):
        try:
            c.saveState()
            clip = c.beginPath()
            clip.roundRect(tx + 0.5, ty + 0.5, tile_w - 1, tile_h - 1, 10)
            c.clipPath(clip, stroke=0)
            c.drawImage(img_path, tx, ty, tile_w, tile_h,
                        preserveAspectRatio=False, mask='auto')
            c.restoreState()
        except Exception:
            pass

c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGES — MY CV
# ─────────────────────────────────────────────────────────────────────────────
new_section_page('cv')
y = page_head(c, TOP, 'Curriculum Vitae', 'Experience & craft.',
              'Eight years across agency, in-house, and independent work — building digital products and brands across Cape Town and beyond.')

c.setFillColor(INK)
c.setFont('Helvetica-Bold', 11)
c.drawString(CX + PAD, y, 'Experience')
y -= 14

for exp in EXPERIENCE:
    body_lines = wrap(exp['body'], CW - PAD - 46 - 82, 'Helvetica', 7.5, max_lines=4)
    row_h = max(58, 28 + len(body_lines) * 9 + 10)

    if y - row_h < BOTTOM + 10:
        c.showPage()
        continuation_page('cv')
        y = TOP - 8

    current = exp.get('current', False)
    rx, rw  = CX + PAD, CW - PAD

    # Row bg
    c.setFillColor(ACCENT_SOFT if current else SURFACE)
    c.setStrokeColor(HexColor('#b8d8f0') if current else LINE)
    c.setLineWidth(0.5)
    c.roundRect(rx, y - row_h, rw, row_h, 9, fill=1, stroke=1)

    # Badge
    bs = 30
    bx = rx + 10
    by = y - row_h / 2 - bs / 2
    c.setFillColor(ACCENT if current else HexColor('#e8e5e0'))
    c.roundRect(bx, by, bs, bs, 7, fill=1, stroke=0)
    c.setFillColor(white if current else INK_3)
    c.setFont('Helvetica-Bold', 6.5)
    c.drawCentredString(bx + bs / 2, by + bs / 2 - 3, exp['mark'])

    # Title
    tx_  = rx + 10 + bs + 10
    tw_  = rw - bs - 20 - 84
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 8.5)
    title_lines = wrap(exp['title'], tw_, 'Helvetica-Bold', 8.5, max_lines=2)
    ty_ = y - 12
    for tl in title_lines:
        c.drawString(tx_, ty_, tl)
        ty_ -= 10

    # Body
    c.setFillColor(INK_2)
    c.setFont('Helvetica', 7.5)
    for bl in body_lines:
        c.drawString(tx_, ty_ - 2, bl)
        ty_ -= 9

    # When / Where
    wx = rx + rw - 82
    c.setFillColor(INK_3)
    c.setFont('Helvetica', 7.5)
    c.drawRightString(wx + 80, y - 12, exp['when'])
    c.setFont('Helvetica', 7)
    c.drawRightString(wx + 80, y - 22, exp['where'])

    y -= row_h + 7

# Skills
if y < 160:
    c.showPage()
    continuation_page('cv')
    y = TOP - 8

y -= 8
c.setFillColor(INK)
c.setFont('Helvetica-Bold', 11)
c.drawString(CX + PAD, y, 'Skills')
y -= 14

skills = {
    'Design': {
        'chips': ['Web Design','Mobile Design','User Experience','Wireframing','Prototyping','Testing','Design System'],
        'subs': {'Tools': ['Figma','Canva','Adobe Suite']},
    },
    'Development': {
        'chips': [],
        'subs': {
            'WordPress': ['Breakdance Builder','Elementor','Divi'],
            'AI': ['Build with Claude Code'],
            'Hosting': ['Xneelo','GoDaddy DNS pointing','Domain purchasing','Email & site hosting'],
        },
    },
}

for group, data in skills.items():
    c.setFillColor(INK)
    c.setFont('Helvetica-Bold', 9.5)
    c.drawString(CX + PAD, y, group)
    y -= 13

    def draw_chips(chips, y):
        cx_ = CX + PAD
        for ch in chips:
            pw = stringWidth(ch, 'Helvetica', 7.5) + 12
            if cx_ + pw > CX + CW - PAD:
                cx_ = CX + PAD
                y -= 17
            draw_chip(c, cx_, y, ch, 7.5)
            cx_ += pw + 4
        return y - 17

    if data['chips']:
        y = draw_chips(data['chips'], y)

    for sub_label, sub_chips in data['subs'].items():
        c.setFillColor(INK_3)
        c.setFont('Helvetica', 8)
        c.drawString(CX + PAD, y, sub_label)
        y -= 12
        y = draw_chips(sub_chips, y)

    y -= 8

c.showPage()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE — CONTACT
# ─────────────────────────────────────────────────────────────────────────────
new_section_page('contact')
y = page_head(c, TOP, 'Contact', "Let's make something.",
              'Available for freelance projects, contract roles, and full-time opportunities.')

gap   = 12
big_w = CW * 0.54 - gap / 2 - PAD / 2
sml_w = CW - PAD - big_w - gap
ch_   = 195
bx_   = CX + PAD
sx_   = bx_ + big_w + gap
cy_   = y - ch_

# Dark card
c.setFillColor(INK)
c.roundRect(bx_, cy_, big_w, ch_, 13, fill=1, stroke=0)

c.setFillColor(white)
c.setFont('Helvetica-Bold', 17)
c.drawString(bx_ + 18, cy_ + ch_ - 32, 'Open to new')
c.drawString(bx_ + 18, cy_ + ch_ - 50, 'opportunities.')

c.setFillColor(HexColor('#9ba8bb'))
c.setFont('Helvetica', 8.5)
body = wrap(
    "Whether it's a website, a brand refresh, or a product team that needs a multimedia "
    "designer who can ship — I'd love to hear from you.",
    big_w - 36, 'Helvetica', 8.5
)
by_ = cy_ + ch_ - 70
for bl in body:
    c.drawString(bx_ + 18, by_, bl)
    by_ -= 11

c.setFillColor(HexColor('#6b7280'))
c.setFont('Helvetica', 7.5)
c.drawString(bx_ + 18, cy_ + 16, 'Based in Cape Town · Remote-friendly')

# Contact card
c.setFillColor(SURFACE)
c.setStrokeColor(LINE)
c.setLineWidth(0.5)
c.roundRect(sx_, cy_, sml_w, ch_, 13, fill=1, stroke=1)

contacts = [
    ('Email',    'staffyzen@gmail.com',  'mailto:staffyzen@gmail.com'),
    ('Phone',    '+27 74 213 1531',      'tel:+27742131531'),
    ('LinkedIn', 'linkedin.com/in/zen-stafford', 'https://www.linkedin.com/in/zen-stafford-52a043183/'),
]
row_h_ = ch_ / len(contacts)

for i, (lbl, val, href) in enumerate(contacts):
    ry_ = cy_ + ch_ - (i + 1) * row_h_
    mid = ry_ + row_h_ / 2

    if i > 0:
        c.setStrokeColor(LINE)
        c.setLineWidth(0.5)
        c.line(sx_ + 14, ry_ + row_h_, sx_ + sml_w - 14, ry_ + row_h_)

    c.setFillColor(INK_3)
    c.setFont('Helvetica', 7.5)
    c.drawString(sx_ + 16, mid + 5, lbl)
    c.setFillColor(ACCENT)
    c.setFont('Helvetica-Bold', 8.5)
    c.drawString(sx_ + 16, mid - 5, val)
    c.linkURL(href, (sx_, ry_, sx_ + sml_w, ry_ + row_h_))


# ─────────────────────────────────────────────────────────────────────────────
c.save()
print(f'✓ PDF saved → {OUT}')
