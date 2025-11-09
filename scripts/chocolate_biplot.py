import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression

def plot_pls_biplot(X, y, n_components=2, top_consumers=30):
    """
    X: DataFrame of product descriptors (rows=products, cols=descriptors)
    y: DataFrame of consumer liking (rows=products, cols=consumers)
    """
    pls = PLSRegression(n_components=n_components)
    pls.fit(X, y)

    # Scores and loadings
    x_scores = pls.x_scores_
    x_loadings = pls.x_loadings_
    y_loadings = pls.y_loadings_

    scores_df = pd.DataFrame(x_scores, index=X.index, columns=[f'PLS{i+1}' for i in range(n_components)])
    x_load_df = pd.DataFrame(x_loadings, index=X.columns, columns=[f'PLS{i+1}' for i in range(n_components)])
    y_load_df = pd.DataFrame(y_loadings, index=y.columns, columns=[f'PLS{i+1}' for i in range(n_components)])

    # Plot biplot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axhline(0, color='lightgray', linewidth=0.8)
    ax.axvline(0, color='lightgray', linewidth=0.8)

    # Products
    ax.scatter(scores_df['PLS1'], scores_df['PLS2'], s=120, marker='o', edgecolor='k', label='Products')
    for txt, (x_val, y_val) in scores_df[['PLS1','PLS2']].iterrows():
        ax.annotate(txt, (x_val, y_val), fontsize=10, ha='center', va='center', weight='bold')

    # Descriptor arrows
    score_range = max(np.abs(scores_df.values).max(), 1e-6)
    arrow_scale = score_range * 0.9
    for name, (lx, ly) in x_load_df[['PLS1','PLS2']].iterrows():
        ax.arrow(0, 0, lx*arrow_scale, ly*arrow_scale,
                 head_width=0.03*arrow_scale, head_length=0.03*arrow_scale,
                 fc='red', ec='red', length_includes_head=True)
        ax.text(lx*arrow_scale*1.12, ly*arrow_scale*1.12, name, color='red', fontsize=10, weight='semibold')

    # Consumer arrows (top-N)
    y_lengths = np.sqrt((y_load_df**2).sum(axis=1))
    topn = min(top_consumers, len(y_lengths))
    top_ids = y_lengths.sort_values(ascending=False).index[:topn]
    for cid in top_ids:
        lx, ly = y_load_df.loc[cid, ['PLS1','PLS2']]
        ax.arrow(0, 0, lx*arrow_scale*0.6, ly*arrow_scale*0.6,
                 head_width=0.02*arrow_scale, head_length=0.02*arrow_scale,
                 fc='gray', ec='gray', alpha=0.6)
    for cid in top_ids[:10]:
        lx, ly = y_load_df.loc[cid, ['PLS1','PLS2']]
        ax.text(lx*arrow_scale*0.7, ly*arrow_scale*0.7, str(cid), fontsize=8, alpha=0.7)

    ax.set_xlabel('PLS1')
    ax.set_ylabel('PLS2')
    ax.set_title('PLS Biplot — Products (points), Descriptors (red vectors), Consumers (grey vectors)')
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()
