import os
from PIL import Image, ImageOps

SRC_DIR = r"C:\Users\peteg\OneDrive - CAP Strategy Partners\Desktop\Springfield Training Center Pics"
ASSETS_DIR = r"C:\Users\peteg\Documents\springfield-training-center-theme\assets"
SCRATCH = r"C:\Users\peteg\AppData\Local\Temp\claude\C--Users-peteg--claude-sessions\0cdf4fdf-0b2d-44c1-af68-4096f29c28d3\scratchpad"

# slug -> (source filename, max_dim)
PHOTOS = {
    "stc-hero": ("1000016668.jpg", 1800),
    "stc-gym-1": ("1000016661.jpg", 1400),
    "stc-gym-2": ("1000016631.jpg", 1000),
    "stc-gym-3": ("1000016656.jpg", 1000),
    "stc-gym-4": ("1000016666.jpg", 1000),
    "stc-gym-5": ("1000016664.jpg", 1000),
    "stc-coach": ("1000016663.jpg", 1400),
    "stc-training-coach": ("1000016654.jpg", 1400),
    "stc-who-woman": ("1000016665.jpg", 1000),
    "stc-who-man": ("1000016630.jpg", 1000),
    "stc-who-student": ("1000016633.jpg", 1000),
    "stc-who-group": ("1000016659.jpg", 1000),
    "stc-freeweek": ("1000016658.jpg", 1400),
    "stc-location": ("1000016667.jpg", 1400),
}

os.makedirs(ASSETS_DIR, exist_ok=True)

for slug, (fname, max_dim) in PHOTOS.items():
    im = Image.open(os.path.join(SRC_DIR, fname))
    im = ImageOps.exif_transpose(im).convert("RGB")
    w, h = im.size
    scale = max_dim / max(w, h)
    if scale < 1:
        im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    out_path = os.path.join(ASSETS_DIR, slug + ".jpg")
    im.save(out_path, format="JPEG", quality=82, optimize=True)
    print(slug, im.size, f"{os.path.getsize(out_path)/1024:.0f} KB")

# copy logo variants already prepared in scratchpad
LOGOS = ["logo_small_light.png", "logo_small_dark.png", "logo_circular_light.png",
         "logo_primary_light.png", "logo_primary_dark.png"]
for name in LOGOS:
    src = os.path.join(SCRATCH, name)
    if os.path.exists(src):
        dst = os.path.join(ASSETS_DIR, "stc-" + name.replace("_", "-"))
        with open(src, "rb") as f_in, open(dst, "wb") as f_out:
            f_out.write(f_in.read())
        print("copied", dst)
    else:
        print("MISSING", src)
