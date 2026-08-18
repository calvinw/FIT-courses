#!/bin/bash
# Regenerate index.html from the course list in courses.txt.
# Only the syllabuses listed there appear; anything else stays in the repo
# but is left off the page.
set -euo pipefail
cd "$(dirname "$0")/.."

cat <<'HEAD'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>FIT Courses</title>
<style>
  body { font-family: Arial, sans-serif; line-height: 1.6; color: #333;
         max-width: 800px; margin: 0 auto; padding: 20px; }
  h1 { color: #2c3e50; }
  h2 { color: #2c3e50; margin-top: 1.5em; border-bottom: 1px solid #eee; }
  ul { list-style-type: none; padding-left: 0; }
  li { margin-bottom: 8px; }
  a { color: #3498db; text-decoration: none; margin-right: 10px; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>FIT Courses</h1>
HEAD

# Path (without extension) of a syllabus, in whichever course folder holds it
find_base() {
  local name=$1 dir
  for dir in */; do
    [ -e "$dir$name.md" ] && { echo "${dir}$name"; return 0; }
  done
  return 1
}

# One row of links: HTML, PDF, Markdown, and the Google Site if there is one
syllabus_row() {
  local base=$1 url=$2
  printf '  <li>%s: ' "$(basename "$base")"
  [ -e "$base.html" ] && printf '<a href="%s.html">HTML</a>' "$base"
  [ -e "$base.pdf" ]  && printf '<a href="%s.pdf">PDF</a>' "$base"
  printf '<a href="%s.md">Markdown</a>' "$base"
  [ -n "$url" ] && printf '<a href="%s">Course Site</a>' "$url"
  printf '</li>\n'
}

echo "<h2>Courses</h2>"
echo "<ul>"
listed_dirs=""
while read -r name url _rest || [ -n "$name" ]; do
  case "$name" in ''|\#*) continue ;; esac
  if base=$(find_base "$name"); then
    syllabus_row "$base" "${url:-}"
    listed_dirs="$listed_dirs $(dirname "$base")"
  else
    echo "  <!-- $name listed in courses.txt but no .md found -->"
  fi
done < courses.txt
echo "</ul>"

# Lecture decks belonging to the courses listed above
decks=""
for dir in $(echo "$listed_dirs" | tr ' ' '\n' | sort -u); do
  [ -n "$dir" ] || continue
  for qmd in "$dir"/lectures/*.qmd; do
    [ -e "$qmd" ] || continue
    decks="$decks ${qmd%.qmd}"
  done
done
if [ -n "$decks" ]; then
  echo "<h2>Lectures</h2>"
  echo "<ul>"
  for base in $decks; do
    printf '  <li>%s: <a href="%s.html">HTML</a></li>\n' "$(basename "$base")" "$base"
  done
  echo "</ul>"
fi

if [ -d shared ]; then
  echo "<h2>Shared</h2>"
  echo "<ul>"
  for md in shared/*.md; do
    [ -e "$md" ] || continue
    syllabus_row "${md%.md}" ""
  done
  echo "</ul>"
fi

cat <<'FOOT'
<footer>
<p>Last updated: <script>document.write(new Date().toDateString())</script></p>
</footer>
</body>
</html>
FOOT
