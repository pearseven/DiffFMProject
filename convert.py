from pdf2image import convert_from_path

images = convert_from_path("./static/pdfs/Teaser_new.pdf", dpi=600)  # dpi 越高越清晰
for i, img in enumerate(images):
    img.save(f"page_{i+1}.png", "PNG")