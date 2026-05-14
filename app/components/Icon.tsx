type IconName =
  | "home"
  | "web"
  | "ai"
  | "graphic"
  | "social"
  | "cv"
  | "contact"
  | "arrow-out"
  | "pin"
  | "mail"
  | "phone"
  | "linkedin"
  | "design"
  | "code";

export function Icon({ name, size = 18 }: { name: IconName; size?: number }) {
  const props = {
    width: size,
    height: size,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.6,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
  };
  switch (name) {
    case "home":
      return (
        <svg {...props}>
          <path d="M4 11.5L12 5l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5h-3.2v-5.3h-6.6v5.3H5.5A1.5 1.5 0 0 1 4 19v-7.5Z" />
        </svg>
      );
    case "web":
      return (
        <svg {...props}>
          <rect x="3" y="4.5" width="18" height="14" rx="2.5" />
          <path d="M3 8.5h18" />
          <circle cx="6" cy="6.5" r=".5" fill="currentColor" />
          <circle cx="8" cy="6.5" r=".5" fill="currentColor" />
        </svg>
      );
    case "ai":
      return (
        <svg {...props}>
          <path d="M12 3.5l1.6 4.4 4.4 1.6-4.4 1.6L12 15.5l-1.6-4.4-4.4-1.6 4.4-1.6L12 3.5Z" />
          <path d="M18.5 16l.7 1.8 1.8.7-1.8.7-.7 1.8-.7-1.8-1.8-.7 1.8-.7.7-1.8Z" />
        </svg>
      );
    case "graphic":
      return (
        <svg {...props}>
          <path d="M12 3.5a8.5 8.5 0 1 0 0 17h1.5a2 2 0 0 0 1.5-3.3l-.5-.6a1.5 1.5 0 0 1 1.1-2.5h1.7a2.5 2.5 0 0 0 2.5-2.5C19.8 7 16.4 3.5 12 3.5Z" />
          <circle cx="7.5" cy="11" r="1" fill="currentColor" />
          <circle cx="11" cy="7.5" r="1" fill="currentColor" />
          <circle cx="15" cy="8" r="1" fill="currentColor" />
        </svg>
      );
    case "social":
      return (
        <svg {...props}>
          <rect x="3.5" y="3.5" width="17" height="17" rx="4" />
          <circle cx="12" cy="12" r="3.5" />
          <circle cx="16.8" cy="7.2" r=".8" fill="currentColor" />
        </svg>
      );
    case "cv":
      return (
        <svg {...props}>
          <path d="M6.5 3.5h8L19 8v11a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 5 19V5a1.5 1.5 0 0 1 1.5-1.5Z" />
          <path d="M14 3.5V8h5" />
          <path d="M8.5 12.5h7M8.5 16h5" />
        </svg>
      );
    case "contact":
      return (
        <svg {...props}>
          <rect x="3" y="5.5" width="18" height="13" rx="2.5" />
          <path d="M3.5 7L12 13l8.5-6" />
        </svg>
      );
    case "arrow-out":
      return (
        <svg {...props}>
          <path d="M7 17L17 7M9 7h8v8" />
        </svg>
      );
    case "pin":
      return (
        <svg {...props}>
          <path d="M12 21s-6-5.5-6-11a6 6 0 1 1 12 0c0 5.5-6 11-6 11Z" />
          <circle cx="12" cy="10" r="2.2" />
        </svg>
      );
    case "mail":
      return (
        <svg {...props}>
          <rect x="3" y="5.5" width="18" height="13" rx="2.5" />
          <path d="M3.5 7L12 13l8.5-6" />
        </svg>
      );
    case "phone":
      return (
        <svg {...props}>
          <path d="M5 4.5h3l1.6 4-2.2 1.4a11 11 0 0 0 6.7 6.7l1.4-2.2 4 1.6v3a2 2 0 0 1-2 2A14 14 0 0 1 3 6.5a2 2 0 0 1 2-2Z" />
        </svg>
      );
    case "linkedin":
      return (
        <svg {...props}>
          <rect x="3.5" y="3.5" width="17" height="17" rx="2.5" />
          <path d="M8 10.5v6M8 7.5v.01M12 16.5v-6M12 13c0-1.5 1-2.5 2.3-2.5S16.5 11.5 16.5 13v3.5" />
        </svg>
      );
    case "design":
      return (
        <svg {...props}>
          <circle cx="12" cy="12" r="8.5" />
          <path d="M8 12l3 3 5-6" />
        </svg>
      );
    case "code":
      return (
        <svg {...props}>
          <path d="M9 8l-4 4 4 4M15 8l4 4-4 4" />
        </svg>
      );
    default:
      return null;
  }
}

export type { IconName };
