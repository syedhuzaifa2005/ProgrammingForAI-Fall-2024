import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits

digits = load_digits()
data = digits.data
labels = digits.target

pixels = pd.DataFrame(data, columns=[f'pixel_{i}' for i in range(data.shape[1])])

first_image_row = pixels.iloc[0]
first_image_array = first_image_row.to_numpy()
first_image_reshaped = first_image_array.reshape(8, 8)

plt.imshow(first_image_reshaped, cmap='gray')
plt.title('First Digit Image')
plt.axis('off')
plt.show()

scaler = StandardScaler()
scaled_pixels = scaler.fit_transform(pixels)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_pixels)

explained_variance = pca.explained_variance_ratio_
print(f"Explained variance by the first 2 components: {explained_variance}")

pca_df = pd.DataFrame(pca_result, columns=['PCA1', 'PCA2'])
pca_df['Label'] = labels

plt.figure(figsize=(8, 6))
plt.scatter(pca_df['PCA1'], pca_df['PCA2'], c=pca_df['Label'], cmap='viridis', alpha=0.7)
plt.title('PCA of Handwritten Digits')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Digit Label')
plt.show()
