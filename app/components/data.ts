import type { IconName } from "./Icon";

export type NavItem = {
  id: string;
  label: string;
  icon: IconName;
};

export const NAV: NavItem[] = [
  { id: "home", label: "Home", icon: "home" },
  { id: "web", label: "Web Design", icon: "web" },
  { id: "graphic", label: "Graphic Design", icon: "graphic" },
  { id: "social", label: "Social Design", icon: "social" },
  { id: "cv", label: "My CV", icon: "cv" },
  { id: "contact", label: "Contact", icon: "contact" },
];

export type WebProject = {
  id: string;
  title: string;
  url: string;
  href: string;
  blurb: string;
  tags: string[];
  image?: string;
};

export const WEB_PROJECTS: WebProject[] = [
  {
    id: "otters-bend",
    title: "Otter's Bend Lodge",
    url: "ottersbendlodge.co.za",
    href: "https://ottersbendlodge.co.za/",
    blurb: "Riverside Lodge & Campsite in Franschhoek",
    tags: ["Accommodation", "Tourism"],
    image: "/otters-bend.png",
  },
  {
    id: "olive-bean",
    title: "Olive Bean Leather",
    url: "olivebeanleather.co.za",
    href: "https://olivebeanleather.co.za/",
    blurb: "Artisanal Local Leather Products",
    tags: ["E-commerce", "D2C"],
    image: "/olive-bean.png",
  },
  {
    id: "stiint-it",
    title: "Stiint It",
    url: "stiint-it.com",
    href: "https://stiint-it.com/",
    blurb: "Connecting Verified Talent to Opportunities",
    tags: ["Marketplace", "Recruitment"],
    image: "/stiint-it.png",
  },
  {
    id: "bestbuds",
    title: "Best Buds",
    url: "bestbuds420.co.za",
    href: "https://bestbuds420.co.za/",
    blurb: "Bud Buying Built for Members",
    tags: ["E-commerce", "Membership"],
    image: "/best-buds.png",
  },
  {
    id: "wip-africa",
    title: "WIP Africa",
    url: "worldinstituteofpainafrica.org",
    href: "https://worldinstituteofpainafrica.org/",
    blurb: "Regional Leaders in Pain Management and Education",
    tags: ["Healthcare", "Education"],
  },
  {
    id: "drcaryn",
    title: "Dr Caryn April Inc",
    url: "drcarynapril.com",
    href: "https://drcarynapril.com/",
    blurb: "Medical Physician",
    tags: ["Professional Services", "Personal Brand"],
  },
  {
    id: "pomerol",
    title: "Pomerol",
    url: "pomerolpartners.com",
    href: "https://pomerolpartners.com/netsuite-operational-rescue/",
    blurb: "Data analytics consultancy",
    tags: ["SaaS", "Analytics"],
    image: "/pomerol.png",
  },
  {
    id: "steelorex",
    title: "Steelorex",
    url: "steelorex.co.za",
    href: "https://steelorex.co.za/",
    blurb: "Commercial manufacturer and online retailer",
    tags: ["E-commerce", "Manufacturing"],
    image: "/steelorex.png",
  },
];

export type Experience = {
  mark: string;
  title: string;
  body: string;
  when: string;
  where: string;
  current?: boolean;
};

export const EXPERIENCE: Experience[] = [
  {
    mark: "ZDS",
    title: "ZDS Designs — Freelance Website & Design",
    body: "I don't just make websites look good, I make sure they're easy to use, fast, and ready to grow with your business. From mapping user journeys in Figma to building custom WordPress sites and creating on-brand social media designs in Canva or Figma, I handle the full process from first idea to final launch.",
    when: "Present",
    where: "Tamboerskloof, Cape Town",
    current: true,
  },
  {
    mark: "TML",
    title: "Tomorrow Labs — Lead of Digital Design & Web Development",
    body: "Led the agency's web and digital delivery across fintech, e-commerce, and creative clients. Owned UI/UX design, technical strategy, and project execution — translating Figma designs into high-performing WordPress builds. Oversaw infrastructure, hosting, and integrations to ensure reliable launches and scalable digital platforms aligned with brand and marketing goals.",
    when: "Sep 2024 — Oct 2025",
    where: "De Waterkant, Cape Town",
  },
  {
    mark: "MC",
    title: "MC Agency — Head of Digital Design & Web Development",
    body: "Directed end-to-end web design and development projects, combining design leadership with hands-on technical execution. Worked closely with clients to turn creative concepts into functional, polished websites while improving delivery workflows, QA processes, and post-launch reliability through proper hosting and system management.",
    when: "Jun 2022 — Jul 2024",
    where: "Vredehoek, Cape Town",
  },
  {
    mark: "RuZ",
    title: "RuZen — Founder & Lead Web & Graphic Designer",
    body: "Founded and operated an independent digital studio delivering custom websites and branding solutions. Managed the full project lifecycle from client consultation to launch — providing UX design, front-end development, and graphic design. Built a strong reputation for creative problem-solving and high-quality digital craftsmanship.",
    when: "Oct 2020 — Aug 2022",
    where: "Kommetjie, Western Cape",
  },
  {
    mark: "GBT",
    title: "Gordons Bay Tourism — Marketing & Design Lead",
    body: "Led marketing, design, and sales initiatives for a tourism business managing 40+ properties. Oversaw team operations, client relationships, and business development while creating digital, print, and branding assets. Implemented strategic marketing campaigns that increased bookings and strengthened local and international visibility.",
    when: "Jan 2018 — Sep 2020",
    where: "Gordons Bay, Western Cape",
  },
];

export const GFX_TILES = [
  { id: "gfx-1", cls: "wide landscape", cap: "Digital Designs" },
  { id: "gfx-2", cls: "square", cap: "Branding" },
  { id: "gfx-3", cls: "portrait", cap: "Poster" },
  { id: "gfx-4", cls: "square", cap: "Email Signature" },
  { id: "gfx-5", cls: "square", cap: "Banner" },
  { id: "gfx-6", cls: "wide landscape", cap: "Brand System" },
  { id: "gfx-7", cls: "square", cap: "Poster" },
  { id: "gfx-8", cls: "square", cap: "Identity" },
];
