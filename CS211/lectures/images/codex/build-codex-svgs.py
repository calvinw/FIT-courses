"""Build the step pictures for the Codex-in-a-codespace deck.

Each picture is a 1280x720 SVG: a step header, then a light-theme codespace
window whose terminal shows what Codex prints at that step. The terminal text
follows screenshots taken in a real codespace on BusMgmtBenchmarks.

Run from this folder:  python3 build-codex-svgs.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent
MONO = "Menlo, Consolas, monospace"
TEAL = "#1b7c83"
HILITE = "#f2a900"

# terminal text colors, as Codex shows them in the light theme
INK, DIM, CYAN, GREEN, BROWN, LINK = "#1f2328", "#8c959f", "#0b7fa3", "#1a7f37", "#9a4f00", "#0b7fa3"

FILES = [".devcontainer", ".github", "extract", "mcp", "public", "skills", "src",
         ".gitignore", "CLAUDE.md", "CODESPACES_SETUP.md", "company_to_company.html",
         "components.json", "index.html", "package.json", "README.md"]


def header(step, title, subtitle):
    return f'''  <rect x="40" y="30" width="92" height="34" rx="17" fill="{TEAL}"/>
  <text x="86" y="53" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">Step {step}</text>
  <text x="148" y="58" font-size="34" font-weight="bold" fill="#24292f">{escape(title)}</text>
  <text x="40" y="104" font-size="21" fill="#57606a">{subtitle}</text>'''


def window():
    """Light codespace window: title bar, activity bar, explorer, terminal panel, status bar."""
    o = ['''  <rect x="40" y="128" width="1200" height="572" rx="10" fill="#ffffff" stroke="#d0d7de" stroke-width="2"/>
  <path d="M41 138 a9 9 0 0 1 9 -9 h1180 a9 9 0 0 1 9 9 v24 h-1198 z" fill="#f3f3f3"/>
  <circle cx="62" cy="146" r="6" fill="#ff5f57"/><circle cx="82" cy="146" r="6" fill="#febc2e"/><circle cx="102" cy="146" r="6" fill="#28c840"/>
  <rect x="430" y="135" width="420" height="22" rx="5" fill="#ffffff" stroke="#d0d7de"/>
  <text x="640" y="151" font-size="13" fill="#57606a" text-anchor="middle">BusMgmtBenchmarks [Codespaces: animated sniffle]</text>
  <line x1="41" y1="162" x2="1239" y2="162" stroke="#e1e4e8"/>
  <rect x="41" y="162" width="44" height="512" fill="#f8f8f8"/>
  <g stroke="#6e7781" stroke-width="2" fill="none" stroke-linecap="round">
    <line x1="53" y1="178" x2="73" y2="178"/><line x1="53" y1="185" x2="73" y2="185"/><line x1="53" y1="192" x2="73" y2="192"/>
    <rect x="53" y="208" width="18" height="22" rx="2"/>
    <circle cx="61" cy="252" r="7"/><line x1="66" y1="257" x2="72" y2="263"/>
    <circle cx="57" cy="284" r="3.5"/><circle cx="68" cy="296" r="3.5"/><line x1="57" y1="288" x2="57" y2="302"/>
  </g>
  <rect x="85" y="162" width="220" height="512" fill="#fbfbfb"/>
  <line x1="305" y1="162" x2="305" y2="674" stroke="#e1e4e8"/>
  <text x="100" y="186" font-size="13" font-weight="bold" fill="#1f2328">Explorer</text>
  <text x="100" y="210" font-size="13" font-weight="bold" fill="#1f2328">⌄ BusMgmtBenchmarks</text>''']
    for i, f in enumerate(FILES):
        y = 234 + i * 24
        folder = f in (".devcontainer", ".github", "extract", "mcp", "public", "skills", "src")
        mark = "›" if folder else " "
        o.append(f'  <text x="104" y="{y}" font-size="13" fill="#57606a">{mark}</text>'
                 f'<text x="118" y="{y}" font-size="13" fill="#1f2328">{escape(f)}</text>')
    o.append('''  <g font-size="13" fill="#57606a">
    <text x="322" y="186">Problems</text><text x="396" y="186">Output</text><text x="460" y="186">Debug Console</text>
    <rect x="566" y="170" width="72" height="24" rx="5" fill="#e8eaed"/><text x="578" y="187" fill="#1f2328">Terminal</text>
    <text x="656" y="186">Ports</text><text x="1222" y="186" text-anchor="end">bash  +</text>
  </g>
  <line x1="306" y1="200" x2="1239" y2="200" stroke="#e1e4e8"/>
  <path d="M41 674 h1198 v16 a9 9 0 0 1 -9 9 h-1180 a9 9 0 0 1 -9 -9 z" fill="#f3f3f3"/>
  <rect x="48" y="677" width="200" height="20" rx="3" fill="#0969da"/>
  <text x="58" y="692" font-size="12" fill="#ffffff">⤫ Codespaces: animated sniffle</text>
  <text x="264" y="692" font-size="12" fill="#57606a">⎇ main</text>''')
    return "\n".join(o)


def terminal(lines, hilites=(), y0=232, lh=25):
    """lines: list of lists of (text, color, bold) segments; None is a blank line.
    hilites: list of (first_line, last_line) index ranges to box."""
    o = []
    for a, b in hilites:
        top = y0 + a * lh - 18
        o.append(f'  <rect x="318" y="{top}" width="908" height="{(b - a + 1) * lh + 6}" rx="6" '
                 f'fill="#fff6dd" stroke="{HILITE}" stroke-width="2.5"/>')
    for i, segs in enumerate(lines):
        if not segs:
            continue
        spans = "".join(
            '<tspan fill="%s"%s>%s</tspan>' % (c, ' font-weight="bold"' if bold else "", escape(t))
            for t, c, bold in segs)
        o.append(f'  <text x="330" y="{y0 + i * lh}" font-family="{MONO}" font-size="16" '
                 f'xml:space="preserve">{spans}</text>')
    return "\n".join(o)


def s(t, c=INK, bold=False):
    return (t, c, bold)


def page(name, step, title, subtitle, lines, hilites=(), extra=""):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" font-family="Helvetica, Arial, sans-serif">
  <rect width="1280" height="720" fill="#ffffff"/>
{header(step, title, subtitle)}
{window()}
{terminal(lines, hilites)}
{extra}
</svg>
'''
    (OUT / name).write_text(svg)


WELCOME = [s("Welcome to "), s("Codex", INK, True), s(", OpenAI's command-line coding agent")]

# Step 2: start Codex
page("codex-2-start.svg", 2, "Start Codex in the terminal",
     "Type <tspan font-family=\"Menlo, Consolas, monospace\" fill=\"#24292f\">codex.sh</tspan> at the <tspan font-family=\"Menlo, Consolas, monospace\" fill=\"#24292f\">#</tspan> prompt, then press Enter",
     [[s("# "), s("codex.sh", INK, True), s("▌")]], hilites=[(0, 0)])

# Step 3: choose device-code sign in
page("codex-3-signin.svg", 3, "Choose Sign in with Device Code",
     "Use the arrow keys to move to option 2, then press Enter",
     [WELCOME, None,
      [s("Sign in with ChatGPT to use Codex as part of your paid plan")],
      [s("or connect an API key for usage-based billing")], None,
      [s("  1. Sign in with ChatGPT")],
      [s("     Usage included with Plus, Pro, Business, and Enterprise plans", DIM)], None,
      [s("› 2. Sign in with Device Code", CYAN, True)],
      [s("     Sign in from another device with a one-time code", CYAN)], None,
      [s("  3. Provide your own API key")],
      [s("     Pay for what you use", DIM)], None,
      [s("  Press enter to continue", DIM)]],
     hilites=[(8, 9)])

# Step 4: the device code
page("codex-4-device-code.svg", 4, "Sign in with the one-time code",
     "Open the link in a new tab, sign in with ChatGPT, then type in the code",
     [WELCOME, None,
      [s("Finish signing in via your browser")], None,
      [s("1. Open this link in your browser and sign in")], None,
      [s("https://auth.openai.com/codex/device", LINK, True)], None,
      [s("2. Enter this one-time code after you are signed in (expires in 15 minutes)")], None,
      [s("ABCD-12345", LINK, True), s("      ← your code is different", DIM)], None,
      [s("Continue only if you started this login in Codex. If a website or", DIM)],
      [s("another person gave you this code, cancel.", DIM)], None,
      [s("Press esc to cancel", DIM)]],
     hilites=[(6, 6), (10, 10)])

# Step 5: signed in
page("codex-5-signed-in.svg", 5, "You are signed in",
     "Read the notes, then press Enter to continue",
     [WELCOME, None,
      [s("✓ Signed in with your ChatGPT account", GREEN)], None,
      [s("Before you start:")], None,
      [s("Decide how much autonomy you want to grant Codex")],
      [s("For more details see the Codex docs", DIM)], None,
      [s("Codex can make mistakes")],
      [s("Review the code it writes and commands it runs", DIM)], None,
      [s("Powered by your ChatGPT account")],
      [s("Uses your plan's rate limits and training data preferences", DIM)], None,
      [s("Press enter to continue", CYAN)]],
     hilites=[(2, 2), (15, 15)])

# Step 6: type /model
page("codex-6-slash-model.svg", 6, "Type /model",
     "Commands start with a slash. Start typing and Codex lists the matches.",
     [[s("• You have 3 usage limit resets available. Run /usage to use one.")], None,
      [s("› "), s("/m", INK, True), s("▌")], None,
      [s("/model       ", CYAN, True), s("choose what model and reasoning effort to use", CYAN, True)],
      [s("/memories    "), s("configure memory use and generation", DIM)],
      [s("/mention     "), s("mention a file", DIM)],
      [s("/mcp         "), s("list configured MCP tools; use /mcp verbose for details", DIM)]],
     hilites=[(2, 2), (4, 4)])

# Step 7: pick gpt-6-sol
page("codex-7-pick-model.svg", 7, "Pick gpt-6-sol",
     "Move down to <tspan font-family=\"Menlo, Consolas, monospace\" fill=\"#24292f\">gpt-6-sol</tspan> and press Enter",
     [[s("Select Model and Effort", INK, True)],
      [s("Access legacy models by running codex -m <model_name> or in your config.toml", DIM)], None,
      [s("  1. gpt-6-astra (current)  "), s("Frontier intelligence for the most demanding work.", DIM)],
      [s("› 2. gpt-6-sol              ", CYAN, True), s("Workhorse model for coding and everyday work.", CYAN, True)],
      [s("  3. gpt-6-luna             "), s("Fast and affordable model for easier tasks.", DIM)],
      [s("  4. gpt-5.6-sol            "), s("Older coding model for complex work.", DIM)],
      [s("  5. gpt-5.6-terra          "), s("Older balanced model for straightforward work.", DIM)],
      [s("  6. gpt-5.6-luna           "), s("Older fast and efficient model.", DIM)],
      [s("  7. gpt-5.5                "), s("Legacy coding model.", DIM)], None,
      [s("Press enter to confirm or esc to go back", DIM)]],
     hilites=[(4, 4)])

# Step 8: ask for the change
page("codex-8-ask.svg", 8, "Ask Codex for the change",
     "Describe what you want in plain words, then press Enter",
     [[s("• Model changed to gpt-6-sol medium")], None,
      [s("› "), s("Make the Export to Excel button orange", INK, True), s("▌")], None,
      [s("gpt-6-sol medium", BROWN), s(" · "), s("/workspaces/BusMgmtBenchmarks", GREEN)]],
     hilites=[(0, 0), (2, 2)])


def plain(name, step, title, subtitle, body):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720" font-family="Helvetica, Arial, sans-serif">
  <rect width="1280" height="720" fill="#ffffff"/>
{header(step, title, subtitle)}
{body}
</svg>
"""
    (OUT / name).write_text(svg)


# Step 1: create the codespace from the repo's Code button
REPO_ROWS = [(".devcontainer", "Update postCreateCommand"), (".github/workflows", "Add HTML report generation"),
             ("extract", "Add Resale segment"), ("mcp", "Move install_figma_mcp_claude.sh"),
             ("public", "Restore financial-data"), ("skills", "Add OpenCode skills"),
             ("src", "Change Export to Excel buttons"), ("CLAUDE.md", "Add Resale segment to CLAUDE.md")]
rows = []
for i, (f, msg) in enumerate(REPO_ROWS):
    y = 316 + i * 44
    icon = ('<path d="M%d %d h9 l4 4 h13 v15 h-26 z" fill="#54aeff"/>' % (76, y - 16)) if "." not in f[1:] or "/" in f \
        else ('<path d="M%d %d h11 l5 5 v15 h-16 z" fill="none" stroke="#57606a" stroke-width="1.6"/>' % (80, y - 16))
    rows.append(f'  <line x1="60" y1="{y - 28}" x2="760" y2="{y - 28}" stroke="#d0d7de"/>{icon}'
                f'<text x="114" y="{y}" font-size="16" fill="#1f2328">{f}</text>'
                f'<text x="380" y="{y}" font-size="16" fill="#57606a">{msg}</text>')
plain("codex-1-create-codespace.svg", 1, "Create a codespace on main",
      "On the BusMgmtBenchmarks repo: <tspan font-weight=\"bold\">Code</tspan> → <tspan font-weight=\"bold\">Codespaces</tspan> → <tspan font-weight=\"bold\">Create codespace on main</tspan>",
      """  <text x="40" y="160" font-size="24" font-weight="bold" fill="#1f2328">BusMgmtBenchmarks</text>
  <rect x="310" y="142" width="62" height="24" rx="12" fill="none" stroke="#57606a"/>
  <text x="341" y="159" font-size="13" fill="#57606a" text-anchor="middle">Public</text>
  <rect x="40" y="186" width="104" height="34" rx="6" fill="#f6f8fa" stroke="#d0d7de"/>
  <text x="60" y="209" font-size="16" font-weight="bold" fill="#1f2328">⎇ main ▾</text>
  <rect x="826" y="186" width="116" height="36" rx="6" fill="#1f883d" stroke="#f2a900" stroke-width="3"/>
  <text x="884" y="210" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">&lt;&gt; Code ▾</text>
  <rect x="40" y="236" width="740" height="402" rx="8" fill="#ffffff" stroke="#d0d7de"/>
  <path d="M41 244 a7 7 0 0 1 7 -7 h724 a7 7 0 0 1 7 7 v34 h-738 z" fill="#f6f8fa"/>
  <text x="60" y="264" font-size="15" fill="#1f2328"><tspan font-weight="bold">calvinw</tspan>  Change Export to Excel buttons to blue  <tspan fill="#1a7f37">✓</tspan></text>
""" + "\n".join(rows) + """
  <!-- the Code dropdown -->
  <rect x="610" y="232" width="420" height="330" rx="10" fill="#ffffff" stroke="#d0d7de" stroke-width="1.5"/>
  <text x="636" y="266" font-size="16" fill="#57606a">Local</text>
  <text x="694" y="266" font-size="16" font-weight="bold" fill="#1f2328">Codespaces</text>
  <line x1="690" y1="280" x2="790" y2="280" stroke="#fd8c73" stroke-width="3"/>
  <line x1="610" y1="282" x2="1030" y2="282" stroke="#d0d7de"/>
  <text x="630" y="314" font-size="16" font-weight="bold" fill="#1f2328">Codespaces</text>
  <text x="630" y="336" font-size="14" fill="#57606a">Your workspaces in the cloud</text>
  <line x1="610" y1="354" x2="1030" y2="354" stroke="#d0d7de"/>
  <text x="820" y="390" font-size="18" font-weight="bold" fill="#1f2328" text-anchor="middle">No codespaces</text>
  <text x="820" y="416" font-size="15" fill="#57606a" text-anchor="middle">You don't have any codespaces</text>
  <text x="820" y="436" font-size="15" fill="#57606a" text-anchor="middle">with this repository checked out</text>
  <rect x="712" y="458" width="216" height="40" rx="6" fill="#1f883d" stroke="#f2a900" stroke-width="3"/>
  <text x="820" y="484" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">Create codespace on main</text>
  <text x="820" y="532" font-size="14" fill="#0969da" text-anchor="middle">Learn more about codespaces...</text>
  <!-- what happens next -->
  <text x="1060" y="300" font-size="18" font-weight="bold" fill="#1f2328">Then</text>
  <text x="1060" y="328" font-size="16" fill="#57606a">A new tab opens.</text>
  <text x="1060" y="352" font-size="16" fill="#57606a">GitHub builds the</text>
  <text x="1060" y="376" font-size="16" fill="#57606a">machine. VS Code</text>
  <text x="1060" y="400" font-size="16" fill="#57606a">appears with the</text>
  <text x="1060" y="424" font-size="16" fill="#57606a">terminal open at</text>
  <text x="1060" y="448" font-size="16" fill="#57606a">a <tspan font-family="Menlo, Consolas, monospace" fill="#1f2328">#</tspan> prompt.</text>""")


# Step 9: the change in the app, before and after
def app(x, color, hover_label, label):
    return f"""  <g transform="translate({x},0)">
    <rect x="0" y="176" width="560" height="440" rx="10" fill="#fafafa" stroke="#d0d7de" stroke-width="1.5"/>
    <rect x="0" y="176" width="130" height="440" fill="#ffffff"/>
    <rect x="14" y="192" width="28" height="28" rx="6" fill="#1570ef"/>
    <text x="50" y="211" font-size="12" fill="#1f2328">FIT Retail Index</text>
    <text x="14" y="248" font-size="10" fill="#57606a" letter-spacing="1">PAGES</text>
    <rect x="0" y="258" width="130" height="26" fill="#f0f2f4"/>
    <text x="14" y="276" font-size="11" fill="#1f2328">Company vs Company</text>
    <text x="14" y="302" font-size="11" fill="#57606a">Company vs Segment</text>
    <text x="14" y="326" font-size="11" fill="#57606a">Reports</text>
    <rect x="146" y="192" width="398" height="56" rx="4" fill="#ffffff" stroke="#e1e4e8"/>
    <circle cx="258" cy="220" r="16" fill="#0b57a4"/>
    <text x="258" y="226" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">FIT</text>
    <text x="282" y="228" font-size="20" font-weight="bold" fill="#0b57a4">Retail Index Report</text>
    <rect x="404" y="258" width="140" height="34" rx="8" fill="{color}" stroke="#f2a900" stroke-width="3"/>
    <text x="474" y="280" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">⤓ Export to Excel</text>
    <rect x="146" y="302" width="398" height="296" rx="6" fill="#ffffff" stroke="#e1e4e8"/>
    <text x="160" y="334" font-size="11" fill="#1f2328">Financial Numbers (in thousands)</text>
    <text x="400" y="334" font-size="11" fill="#1f2328">Dillard's</text><text x="480" y="334" font-size="11" fill="#1f2328">Macy's</text>
    <g font-size="11" fill="#1f2328">
      <line x1="146" y1="350" x2="544" y2="350" stroke="#e1e4e8"/>
      <text x="160" y="372">Total Revenue</text><text x="456" y="372" text-anchor="end">$6,563,336</text><text x="536" y="372" text-anchor="end">$22,621,000</text>
      <line x1="146" y1="386" x2="544" y2="386" stroke="#e1e4e8"/>
      <text x="160" y="408">Cost of Goods</text><text x="456" y="408" text-anchor="end">$3,916,862</text><text x="536" y="408" text-anchor="end">$13,497,000</text>
      <line x1="146" y1="422" x2="544" y2="422" stroke="#e1e4e8"/>
      <text x="160" y="444">Gross Margin</text><text x="456" y="444" text-anchor="end">$2,646,474</text><text x="536" y="444" text-anchor="end">$9,124,000</text>
      <line x1="146" y1="458" x2="544" y2="458" stroke="#e1e4e8"/>
      <text x="160" y="480">Operating Profit</text><text x="456" y="480" text-anchor="end">$694,480</text><text x="536" y="480" text-anchor="end">$1,030,000</text>
      <line x1="146" y1="494" x2="544" y2="494" stroke="#e1e4e8"/>
      <text x="160" y="516">Net Profit</text><text x="456" y="516" text-anchor="end">$570,187</text><text x="536" y="516" text-anchor="end">$642,000</text>
    </g>
    <text x="280" y="652" font-size="22" font-weight="bold" fill="{hover_label}" text-anchor="middle">{label}</text>
  </g>"""

plain("codex-9-result.svg", 9, "Codex makes the button orange",
      "It edits the 3 files that draw the button. Check what it changed before you keep it.",
      app(40, "#2563eb", "#57606a", "Before: blue") + app(680, "#f97316", "#c2410c", "After: orange") +
      """  <text x="640" y="410" font-size="44" fill="#57606a" text-anchor="middle">→</text>""")


# Step 10: ask Codex to commit and push
page("codex-10-commit-push.svg", 10, "Ask Codex to commit and push",
     "No git buttons: just tell Codex in plain words, then press Enter",
     [[s("• Made the Export to Excel button orange in 3 files.", DIM)], None,
      [s("› "), s("Commit and push these changes", INK, True), s("▌")], None,
      [s("gpt-6-sol medium", BROWN), s(" · "), s("/workspaces/BusMgmtBenchmarks", GREEN)]],
     hilites=[(2, 2)])
