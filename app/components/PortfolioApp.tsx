"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import { Icon } from "./Icon";
import {
  NAV,
  WEB_PROJECTS,
  EXPERIENCE,
  GFX_TILES,
  type WebProject,
} from "./data";

function PageHead({
  kicker,
  title,
  sub,
}: {
  kicker?: string;
  title: React.ReactNode;
  sub?: string;
}) {
  return (
    <header className="page-head">
      {kicker && <div className="kicker">{kicker}</div>}
      <h1>{title}</h1>
      {sub && <div className="sub">{sub}</div>}
    </header>
  );
}

function ProjectCard({
  p,
  featured,
}: {
  p: WebProject;
  featured?: boolean;
}) {
  return (
    <a
      className={"project-card" + (featured ? " featured" : "")}
      href={p.href}
      target="_blank"
      rel="noopener noreferrer"
    >
      <div className="media">
        <span className="slot-placeholder">{p.title} screenshot</span>
      </div>
      <div className="meta">
        <div className="meta-top">
          <div className="title">{p.title}</div>
          <span className="url">
            {p.url}
            <Icon name="arrow-out" size={12} />
          </span>
        </div>
        <div className="blurb">{p.blurb}</div>
        <div className="tags">
          {p.tags.map((t) => (
            <span className="tag" key={t}>
              {t}
            </span>
          ))}
        </div>
      </div>
    </a>
  );
}

function HomePage() {
  const featured = WEB_PROJECTS[0];
  const rest = WEB_PROJECTS.slice(1, 5);
  return (
    <div className="page">
      <section className="home-hero">
        <div>
          <div className="eyebrow">Multimedia Designer · Cape Town</div>
          <h1>
            Designing <em>thoughtful</em>
            <br />
            digital products & brand systems.
          </h1>
          <p>
            I build websites, digital products, and AI-powered systems for
            businesses that care about thoughtful execution and long-term
            quality. My work sits between design, development, and strategy.
          </p>
        </div>
        <div className="quick-stats">
          <div className="stat">
            <span className="num">8+</span>Years designing
          </div>
          <div className="stat">
            <span className="num">40+</span>Projects shipped
          </div>
          <div className="stat">
            <span className="num">06</span>Live websites
          </div>
        </div>
      </section>

      <PageHead
        title="Recent Projects"
        sub="A closer look at recent web work — where creativity meets precision."
      />

      <div className="project-stack">
        <ProjectCard p={featured} featured />
        <div className="project-grid">
          {rest.map((p) => (
            <ProjectCard key={p.id} p={p} />
          ))}
        </div>
      </div>
    </div>
  );
}

function WebDesignPage() {
  return (
    <div className="page">
      <PageHead
        kicker="Web Design — Selected Work"
        title="Websites built to last."
        sub="WordPress, custom builds, and end-to-end delivery — from user journeys to hosting."
      />
      <div className="project-grid">
        {WEB_PROJECTS.map((p) => (
          <ProjectCard key={p.id} p={p} />
        ))}
      </div>
    </div>
  );
}

function AiWorksPage() {
  return (
    <div className="page">
      <PageHead
        kicker="AI Works"
        title="Building with AI, in public."
        sub="Experiments with generative imagery, prompt-driven workflows, and AI-augmented design systems. New work landing soon — drop me a line if you want to collaborate."
      />
      <div className="coming">
        <div className="coming-card">
          <div className="sub">Slot 01</div>
          <div className="ttl">Generative brand visuals</div>
        </div>
        <div className="coming-card">
          <div className="sub">Slot 02</div>
          <div className="ttl">AI-powered design systems</div>
        </div>
        <div className="coming-card">
          <div className="sub">Slot 03</div>
          <div className="ttl">Prompt → product workflows</div>
        </div>
        <div className="coming-card">
          <div className="sub">Slot 04</div>
          <div className="ttl">Editorial AI imagery</div>
        </div>
      </div>
    </div>
  );
}

function GraphicDesignPage() {
  return (
    <div className="page">
      <PageHead
        kicker="Graphic Design"
        title="Identity, print & the everyday."
        sub="Digital designs, posters, banners, and branding work — email signatures, social assets, and pitch decks."
      />
      <div className="gfx-grid">
        {GFX_TILES.map((t) => (
          <div className={"tile " + t.cls} key={t.id}>
            <span className="slot-placeholder">{t.cap}</span>
            <div className="cap">{t.cap}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SocialDesignPage() {
  return (
    <div className="page">
      <PageHead
        kicker="Social Design"
        title="Designed for the feed."
        sub="Mockups, story templates, and content systems — drop in your campaign artwork."
      />
      <div className="social-grid">
        {Array.from({ length: 8 }).map((_, i) => (
          <div className="tile" key={i}>
            <span className="slot-placeholder">{`Mockup ${i + 1}`}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function CvPage() {
  return (
    <div className="page">
      <PageHead
        kicker="Curriculum Vitae"
        title="Experience & craft."
        sub="Eight years across agency, in-house, and independent work — building digital products and brands across Cape Town and beyond."
      />

      <section className="section">
        <h2 className="section-title">Experience</h2>
        <div className="exp-list">
          {EXPERIENCE.map((e, i) => (
            <div className={"exp-row" + (e.current ? " current" : "")} key={i}>
              <div className="exp-mark">{e.mark}</div>
              <div className="exp-body">
                <h3>{e.title}</h3>
                <p>{e.body}</p>
              </div>
              <div className="exp-side">
                <div className="when">{e.when}</div>
                <div className="where">
                  <Icon name="pin" size={13} />
                  {e.where}
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="section">
        <h2 className="section-title">Skills</h2>
        <div className="skills-grid">
          <div className="skill-row">
            <div className="skill-label">
              <span className="ico">
                <Icon name="design" size={16} />
              </span>
              Design
            </div>
            <div className="skill-chunks">
              <div className="skill-chunk split">
                <span>Web Design</span>
                <span className="vr"></span>
                <span>Mobile Design</span>
              </div>
              <div className="skill-chunk">User Experience</div>
              <div className="skill-chunk">
                <div className="lst">
                  <div className="li">Wireframing</div>
                  <div className="li">Prototyping</div>
                  <div className="li">Testing</div>
                </div>
              </div>
              <div className="skill-chunk">Design System</div>
            </div>
          </div>
          <div className="skill-row">
            <div className="skill-label">
              <span className="ico">
                <Icon name="code" size={16} />
              </span>
              Development
            </div>
            <div className="skill-chunks">
              <div className="skill-chunk">WordPress</div>
              <div className="skill-chunk">
                <div className="lst">
                  <div className="li">Divi</div>
                  <div className="li">Elementor</div>
                  <div className="li">Breakdance Builder</div>
                </div>
              </div>
              <div className="skill-chunk split">
                <span>Figma</span>
                <span className="vr"></span>
                <span>Canva</span>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

function ContactPage() {
  return (
    <div className="page">
      <PageHead
        kicker="Contact"
        title="Let's make something."
        sub="Available for freelance projects, contract roles, and full-time opportunities."
      />
      <div className="contact-grid">
        <div className="contact-card big">
          <h2>
            Open to new
            <br />
            opportunities.
          </h2>
          <p>
            Whether it&apos;s a website, a brand refresh, or a product team that
            needs a multimedia designer who can ship — I&apos;d love to hear
            from you.
          </p>
          <p className="contact-meta">Based in Cape Town · Remote-friendly</p>
        </div>
        <div className="contact-card">
          <div className="contact-list">
            <a className="row" href="mailto:staffyzen@gmail.com">
              <span className="ico">
                <Icon name="mail" size={18} />
              </span>
              <div>
                <div className="lbl">Email</div>
                <div className="val">staffyzen@gmail.com</div>
              </div>
              <span className="arr">
                <Icon name="arrow-out" size={14} />
              </span>
            </a>
            <a className="row" href="tel:+27742131531">
              <span className="ico">
                <Icon name="phone" size={18} />
              </span>
              <div>
                <div className="lbl">Phone</div>
                <div className="val">+27 74 213 1531</div>
              </div>
              <span className="arr">
                <Icon name="arrow-out" size={14} />
              </span>
            </a>
            <a
              className="row"
              href="https://www.linkedin.com/in/zen-stafford-52a043183/"
              target="_blank"
              rel="noopener noreferrer"
            >
              <span className="ico">
                <Icon name="linkedin" size={18} />
              </span>
              <div>
                <div className="lbl">LinkedIn</div>
                <div className="val">zen-stafford</div>
              </div>
              <span className="arr">
                <Icon name="arrow-out" size={14} />
              </span>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

const PAGES: Record<string, () => React.JSX.Element> = {
  home: HomePage,
  web: WebDesignPage,
  ai: AiWorksPage,
  graphic: GraphicDesignPage,
  social: SocialDesignPage,
  cv: CvPage,
  contact: ContactPage,
};

export default function PortfolioApp() {
  const [active, setActive] = useState<string>("home");

  useEffect(() => {
    const sync = () => {
      const h = (window.location.hash || "").replace("#", "");
      if (h && PAGES[h]) setActive(h);
      else setActive("home");
    };
    sync();
    window.addEventListener("hashchange", sync);
    return () => window.removeEventListener("hashchange", sync);
  }, []);

  const go = (id: string) => {
    setActive(id);
    history.replaceState(null, "", "#" + id);
    window.scrollTo({ top: 0, behavior: "instant" });
  };

  const CurrentPage = PAGES[active] ?? HomePage;

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="profile">
          <div className="avatar" aria-label="Zen Stafford">
            <Image
              src="/zen.png"
              alt="Zen Stafford"
              width={112}
              height={112}
              priority
            />
          </div>
          <div className="who">
            <div className="name">Zen Stafford</div>
            <div className="role">Multimedia Designer</div>
          </div>
        </div>

        <nav className="nav">
          {NAV.map((n) => (
            <button
              key={n.id}
              className={"nav-item" + (active === n.id ? " active" : "")}
              onClick={() => go(n.id)}
            >
              <span className="ico">
                <Icon name={n.icon} size={18} />
              </span>
              <span className="label">{n.label}</span>
            </button>
          ))}
        </nav>

        <div className="spacer"></div>

        <div className="status">
          <span className="dot"></span>
          <span className="lbl">Available Now</span>
        </div>
        <button className="hire-btn" onClick={() => go("contact")}>
          <span className="lbl">Hire Me</span>
          <Icon name="arrow-out" size={14} />
        </button>
      </aside>

      <main className="main">
        <CurrentPage />
      </main>
    </div>
  );
}
