def apply_kmeans(filename: str, num_clusters: int):
    from imgutils import load_image
    img = load_image(filename)

    from kmeans import kmeans
    img_quantized = kmeans(img, num_clusters)

    import matplotlib.pyplot as plt
    fix, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].set_title("Original")
    axes[0].imshow(img)
    axes[1].set_title("Quantisiert")
    axes[1].imshow(img_quantized)

fp = "rrze.png"
num_clusters = 5
apply_kmeans(fp, num_clusters)