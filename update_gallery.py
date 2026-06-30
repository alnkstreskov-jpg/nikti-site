import os
import re

ph_dir = 'ph'
files = [f for f in os.listdir(ph_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))]
files.sort()

def gen_item(filename, index):
    bg_colors = ['bg-y2k-yellow', 'bg-y2k-magenta', 'bg-y2k-blue']
    rotates = ['hover:rotate-2', 'hover:-rotate-1', 'hover:rotate-1', 'hover:-rotate-2']
    
    bg_color = bg_colors[index % len(bg_colors)]
    rotate = rotates[index % len(rotates)]
    
    return f"""                    <div
                        class="bg-white p-2 border-4 border-black shadow-brutal transform {rotate} transition-transform">
                        <div
                            class="aspect-square {bg_color} flex items-center justify-center overflow-hidden border-2 border-black">
                            <img src="ph/{filename}" alt="Nail Art {index + 1}" class="w-full h-full object-cover"
                                loading="lazy">
                        </div>
                    </div>"""

first_6 = files[:6]
rest = files[6:]

first_6_html = "\n".join([gen_item(f, i) for i, f in enumerate(first_6)])
rest_html = "\n".join([gen_item(f, i + 6) for i, f in enumerate(rest)])

replacement = f"""<!-- Masonry-ish Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
{first_6_html}
                </div>

                <!-- Hidden Gallery Items -->
                <div id="more-gallery" class="hidden mt-6">
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
{rest_html}
                    </div>
                </div>"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find start and end indices
start_marker = "<!-- Masonry-ish Grid -->"
end_marker = "<!-- Gallery Controls -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # We replace from start_idx up to end_idx (we'll just append end_marker back or replace the space before it)
    # Actually end_idx points to the start of "<!-- Gallery Controls -->"
    # Let's see the space before end_marker.
    
    new_content = content[:start_idx] + replacement + "\n\n                " + content[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Gallery updated successfully.")
else:
    print("Could not find markers.")
