@AGENTS.md

# Working on Zen Stafford's portfolio with Claude Code

This is Zen Stafford's personal portfolio site, originally built by Megan McGrath as Zen's technical cofounder and now maintained by Zen.

## About Zen
- Multimedia designer based in Cape Town, looking for jobs and freelance work
- New to coding and the terminal — explain things in plain English
- Define jargon the first time you use it

## About this project
- **Tech stack:** Next.js 16 + React 19 + TypeScript, plain CSS (no Tailwind)
- **Hosted on Vercel** — pushes to `main` auto-deploy in about a minute
- **Live URL:** https://portfolio-hub-zds.vercel.app
- **Repo:** https://github.com/mcgrathcreate-beep/portfolio-hub-zds (public)

## Where things live
- `app/components/PortfolioApp.tsx` — the main React component. Every page section is in here (Home, Web Design, Graphic Design, Social Design, My CV, Contact). Edit page layouts, copy, and JSX here.
- `app/components/data.ts` — the project list (URLs, blurbs, tags, image paths), CV experience entries, sidebar nav items. Edit **content** here.
- `app/components/Icon.tsx` — the sidebar nav icon SVGs.
- `app/globals.css` — every style, color, font, and spacing rule. Variables at the top under `:root` define the system colors.
- `app/layout.tsx` — root HTML and font setup (Geist, Geist Mono, Poppins).
- `public/` — all images: `zen.png` (sidebar avatar), `otters-bend.png` etc. (project screenshots), `social-1.png` through `social-9.png` (social design grid).

## Before doing anything
- Show a brief plan first (numbered steps, 1–2 sentences each)
- Wait for explicit approval before executing
- Explain commands in plain English BEFORE running them
- Flag network operations loudly (pushing to GitHub, deploying to Vercel)

## Running the site locally
```
npm install     # one time only after cloning
npm run dev     # starts the local dev server at http://localhost:3001
```
Edit any file, save, and the change appears instantly in the browser.

## Common edits

**Add a new web project**
Edit `app/components/data.ts`, add a new object to the `WEB_PROJECTS` array (copy an existing entry as a template). Drop the screenshot in `public/` with a clean filename like `new-project.png`. Reference it as `image: "/new-project.png"`.

**Swap a project image**
Just replace the file in `public/` with the new one — same filename, no code change needed.

**Change copy on a page**
Find the text in `app/components/PortfolioApp.tsx` and edit it directly. Each page is a function like `HomePage`, `WebDesignPage`, `CvPage`, `ContactPage`.

**Update CV experience or skills**
Edit the `EXPERIENCE` array in `app/components/data.ts`. The skill chips in the CV page are inside `CvPage` in `PortfolioApp.tsx`.

**Edit colors, fonts, or spacing**
Look in `app/globals.css`. The accent color, background, and surface colors are CSS variables at the top under `:root`. Search for the section comment (e.g. `/* Sidebar */`, `/* Project cards */`) to find the styles for a specific area.

**Add or remove a sidebar nav section**
Edit the `NAV` array in `app/components/data.ts` and the `PAGES` record + matching page component in `PortfolioApp.tsx`.

## Deploying changes
```
git add <the-files-you-changed>
git commit -m "short description of what changed"
git push
```
That's it. Vercel detects the push, builds the site (~30 seconds), and the live URL updates in about a minute. If you don't see the change immediately, hard-refresh the browser with **Cmd + Shift + R**.

## Hard rules
- Never delete files without explicit OK from Zen for that specific file
- Never run global installs (`npm install -g`, `brew install`, `pip install --user`, etc.) without explicit OK
- Never commit `.env*` files or anything with secrets/credentials
- Never force-push to `main`
- If anything is ambiguous, stop and ask before acting

## Communication
- Warm, plain language, no condescension
- Short paragraphs over long ones
- Bullets only for genuine lists, not as a default format
- After finishing something, summarize what changed in 1–2 sentences
- Suggest a quick way to verify the change worked (e.g. "refresh localhost:3001 and click the X tab")

## Verification
- For any non-trivial change, verify locally before committing
- Use the dev server (`npm run dev`) to confirm the page renders without errors before you push
- After pushing, you can confirm Vercel deployed successfully by visiting the live URL and hard-refreshing
