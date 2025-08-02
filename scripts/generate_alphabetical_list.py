import os
import re

output_path = os.path.join('recipes', 'appendix', 'alphabetical_list.tex')
entries = []

# Regex patterns
section_re = re.compile(r"\\section\{([^}]*)\}")
label_re = re.compile(r"\\label\{([^}]*)\}")

# descriptors patterns in order of priority
patterns = [
    ("Slow-Cooked ", "Slow-Cooked"),
]

for root, _, files in os.walk('recipes'):
    if 'appendix' in root:
        continue
    for file in files:
        if not file.endswith('.tex'):
            continue
        path = os.path.join(root, file)
        with open(path, 'r') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            sec_match = section_re.search(line)
            if sec_match:
                title = sec_match.group(1).strip()
                rest = line
                label = None
                label_match = label_re.search(rest)
                if label_match:
                    label = label_match.group(1)
                else:
                    # maybe label on next line
                    if i+1 < len(lines):
                        label_match = label_re.search(lines[i+1])
                        if label_match:
                            label = label_match.group(1)
                if not label:
                    continue
                desc = []
                remaining = title
                changed = True
                while changed:
                    changed = False
                    for pat, name in patterns:
                        if remaining.startswith(pat):
                            remaining = remaining[len(pat):]
                            desc.append(name)
                            changed = True
                            break
                if desc:
                    display = f"{remaining}, {' '.join(desc)}"
                else:
                    display = remaining
                sort_key = display.lower()
                entries.append((sort_key, display, label))

entries.sort(key=lambda x: x[0])

with open(output_path, 'w') as out:
    out.write("\\chapter*{Alphabetical List}\n")
    out.write("\\begin{itemize}\n")
    for _, display, label in entries:
        out.write(f"  \\item \\hyperref[{label}]{{{display}}} (page~\\pageref{{{label}}})\n")
    out.write("\\end{itemize}\n")
