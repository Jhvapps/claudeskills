#!/usr/bin/env bash
# Pull latest skills from all three repos (gstack, marketingskills, claudeskills).
# All 93 skills are symlinked to these repos, so a `git pull` here = instant update.

set -e

GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
DIM='\033[0;90m'
NC='\033[0m'

pull_repo() {
  local name=$1
  local path=$2
  local remote=${3:-origin}
  local branch=${4:-main}

  if [ ! -d "$path" ]; then
    echo -e "${YELLOW}⚠ $name: not cloned at $path — skipping${NC}"
    return
  fi

  echo -e "${BLUE}→ $name${NC} ${DIM}($path, $remote/$branch)${NC}"
  cd "$path"
  local before=$(git rev-parse HEAD)
  if ! git fetch "$remote" "$branch" --quiet 2>&1; then
    echo -e "${YELLOW}  ⚠ fetch failed — skipping${NC}"
    return
  fi
  local behind=$(git rev-list --count HEAD.."$remote/$branch" 2>/dev/null || echo 0)
  if [ "$behind" -eq 0 ]; then
    echo -e "${DIM}  already up to date${NC}"
    return
  fi
  echo -e "${GREEN}  $behind new commit(s) — pulling${NC}"
  git pull "$remote" "$branch" --quiet
  local after=$(git rev-parse HEAD)
  if [ "$before" != "$after" ]; then
    git log --oneline "$before..$after" | sed 's/^/    /'
  fi
}

echo -e "${BLUE}Updating skill repos…${NC}"
echo ""

# gstack: pull from upstream (Garry Tan's repo) for latest releases
pull_repo "gstack          " "$HOME/repos/gstack" "upstream" "main"
echo ""

# marketingskills: pull from upstream (Corey Haines' repo)
pull_repo "marketingskills " "$HOME/repos/marketingskills" "upstream" "main"
echo ""

# claudeskills: your own repo — pull from origin
pull_repo "claudeskills    " "$HOME/repos/claudeskills" "origin" "main"
echo ""

# Sanity check: any broken skill symlinks?
broken=0
for f in "$HOME"/.claude/skills/*; do
  [ -e "$f" ] || { echo -e "${YELLOW}⚠ broken symlink: $(basename "$f")${NC}"; broken=$((broken + 1)); }
done

if [ "$broken" -eq 0 ]; then
  total=$(ls "$HOME/.claude/skills/" | wc -l | tr -d ' ')
  echo -e "${GREEN}✓ All $total skills resolved cleanly${NC}"
else
  echo -e "${YELLOW}⚠ $broken broken symlinks — investigate${NC}"
fi
