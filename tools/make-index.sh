#!/bin/bash
# Regenerate index.html by walking <Course>/<Semester>/ and shared/.
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
  h3 { color: #555; font-size: 1.05em; margin-bottom: .3em; }
  ul { list-style-type: none; padding-left: 1em; }
  li { margin-bottom: 8px; }
  a { color: #3498db; text-decoration: none; margin-right: 10px; }
  a:hover { text-decoration: underline; }
</style>
</head>
<body>
<h1>FIT Courses</h1>
HEAD

# Newest semesters first: sort by year descending, then Fall, Summer, Spring, Winter
semester_key() {
  case "$1" in
    Fall*)   echo "${1#Fall}4"   ;;
    Summer*) echo "${1#Summer}3" ;;
    Spring*) echo "${1#Spring}2" ;;
    Winter*) echo "${1#Winter}1" ;;
    *)       echo "000"          ;;
  esac
}

for course in */; do
  course=${course%/}
  case "$course" in shared|tools) continue ;; esac
  echo "<h2>$course</h2>"
  for sem in $(for s in "$course"/*/; do s=${s%/}; s=${s#*/}; echo "$(semester_key "$s") $s"; done | sort -rn | awk '{print $2}'); do
    echo "<h3>$sem</h3>"
    echo "<ul>"
    for md in "$course/$sem"/*.md; do
      [ -e "$md" ] || continue
      base=${md%.md}
      name=$(basename "$base")
      printf '  <li>%s: ' "$name"
      [ -e "$base.html" ] && printf '<a href="%s.html">HTML</a>' "$base"
      [ -e "$base.pdf" ]  && printf '<a href="%s.pdf">PDF</a>' "$base"
      printf '<a href="%s.md">Markdown</a></li>\n' "$base"
    done
    for qmd in "$course/$sem"/lectures/*.qmd; do
      [ -e "$qmd" ] || continue
      base=${qmd%.qmd}
      printf '  <li>%s (slides): ' "$(basename "$base")"
      printf '<a href="%s.html">HTML</a></li>\n' "$base"
    done
    echo "</ul>"
  done
done

if [ -d shared ]; then
  echo "<h2>Shared</h2>"
  echo "<ul>"
  for md in shared/*.md; do
    [ -e "$md" ] || continue
    base=${md%.md}
    printf '  <li>%s: ' "$(basename "$base")"
    [ -e "$base.html" ] && printf '<a href="%s.html">HTML</a>' "$base"
    [ -e "$base.pdf" ]  && printf '<a href="%s.pdf">PDF</a>' "$base"
    printf '<a href="%s.md">Markdown</a></li>\n' "$base"
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
